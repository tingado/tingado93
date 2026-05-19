// =====================================================
// POLLA MUNDIALERA 2026 — Google Apps Script Backend
// =====================================================

const SHEET_NAME_JUGADORES   = "Jugadores";
const SHEET_NAME_PRONOSTICOS = "Pronosticos";
const SHEET_NAME_RESULTADOS  = "Resultados";

// ── Entrada principal ──────────────────────────────
// Apps Script publicado como "Cualquier persona" responde
// a GET y POST. Usamos GET con parámetro action + data (JSON)
// para evitar problemas CORS con preflight OPTIONS.

function doGet(e) {
  return handleRequest(e);
}

function doPost(e) {
  return handleRequest(e);
}

function handleRequest(e) {
  const lock = LockService.getScriptLock();
  lock.tryLock(10000);

  try {
    // Soporta tanto GET (?action=X&data={...}) como POST (body JSON)
    const params = e.parameter || {};
    let body = {};

    if (e.postData && e.postData.contents) {
      try { body = JSON.parse(e.postData.contents); } catch(ex) {}
    }

    // También soporta data como parámetro GET
    if (params.data) {
      try { body = JSON.parse(decodeURIComponent(params.data)); } catch(ex) {}
    }

    const action = params.action || body.action;
    let result;

    switch (action) {
      case "getAll":             result = getAll();                  break;
      case "inscribir":          result = inscribir(body);           break;
      case "guardarPron":        result = guardarPronostico(body);   break;
      case "guardarResultados":  result = guardarResultados(body);   break;
      case "eliminarJugador":    result = eliminarJugador(body);     break;
      case "resetear":           result = resetear();                break;
      case "fetchResultadosAPI": result = fetchResultadosAPI(body);  break;
      case "ping":               result = { ok: true, ts: new Date().toISOString() }; break;
      default: result = { error: "Acción no reconocida: " + (action || "ninguna") };
    }

    // Soporte JSONP — si viene parámetro callback, envolver respuesta
    const callback = (e.parameter || {}).callback;
    if (callback) {
      return ContentService
        .createTextOutput(callback + '(' + JSON.stringify(result) + ')')
        .setMimeType(ContentService.MimeType.JAVASCRIPT);
    }
    return ContentService
      .createTextOutput(JSON.stringify(result))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    const callback = (e.parameter || {}).callback;
    const errObj = JSON.stringify({ error: err.message });
    if (callback) {
      return ContentService
        .createTextOutput(callback + '(' + errObj + ')')
        .setMimeType(ContentService.MimeType.JAVASCRIPT);
    }
    return ContentService
      .createTextOutput(errObj)
      .setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

// ── Helpers de Sheet ───────────────────────────────
function getOrCreateSheet(name) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sh = ss.getSheetByName(name);
  if (!sh) {
    sh = ss.insertSheet(name);
    if (name === SHEET_NAME_JUGADORES) {
      sh.appendRow(["nombre", "monto", "fecha"]);
    } else if (name === SHEET_NAME_PRONOSTICOS) {
      sh.appendRow(["nombre", "json"]);
    } else if (name === SHEET_NAME_RESULTADOS) {
      sh.appendRow(["clave", "valor"]);
    }
  }
  return sh;
}

function sheetToArray(sh) {
  const data = sh.getDataRange().getValues();
  if (data.length <= 1) return [];
  const headers = data[0];
  return data.slice(1).map(row => {
    const obj = {};
    headers.forEach((h, i) => { obj[h] = row[i]; });
    return obj;
  });
}

// ── GET ALL ────────────────────────────────────────
function getAll() {
  const shJ = getOrCreateSheet(SHEET_NAME_JUGADORES);
  const shP = getOrCreateSheet(SHEET_NAME_PRONOSTICOS);
  const shR = getOrCreateSheet(SHEET_NAME_RESULTADOS);

  const jugadores  = sheetToArray(shJ);
  const pronRows   = sheetToArray(shP);
  const resultRows = sheetToArray(shR);

  const pronosticos = {};
  pronRows.forEach(r => {
    try { pronosticos[r.nombre] = JSON.parse(r.json); } catch(e) {}
  });

  const resultados = {};
  resultRows.forEach(r => { resultados[r.clave] = r.valor; });

  return { jugadores, pronosticos, resultados };
}

// ── INSCRIBIR ──────────────────────────────────────
function inscribir(body) {
  const sh    = getOrCreateSheet(SHEET_NAME_JUGADORES);
  const rows  = sheetToArray(sh);
  const nombre = (body.nombre || "").trim();
  if (!nombre) return { error: "Nombre vacío" };
  if (rows.find(r => r.nombre.toLowerCase() === nombre.toLowerCase())) {
    return { error: "Ya existe un participante con ese nombre" };
  }
  const monto = parseFloat(body.monto) || 0;
  const fecha = new Date().toLocaleDateString("es-CL");
  sh.appendRow([nombre, monto, fecha]);
  return { ok: true };
}

// ── GUARDAR PRONÓSTICO ─────────────────────────────
function guardarPronostico(body) {
  const sh     = getOrCreateSheet(SHEET_NAME_PRONOSTICOS);
  const nombre = (body.nombre || "").trim();
  const json   = JSON.stringify(body.pronostico || {});

  const data = sh.getDataRange().getValues();
  for (let i = 1; i < data.length; i++) {
    if (data[i][0] && data[i][0].toLowerCase() === nombre.toLowerCase()) {
      sh.getRange(i + 1, 2).setValue(json);
      return { ok: true, updated: true };
    }
  }
  sh.appendRow([nombre, json]);
  return { ok: true, created: true };
}

// ── GUARDAR RESULTADOS ─────────────────────────────
function guardarResultados(body) {
  const sh  = getOrCreateSheet(SHEET_NAME_RESULTADOS);
  sh.clearContents();
  sh.appendRow(["clave", "valor"]);
  const res = body.resultados || {};
  Object.entries(res).forEach(([k, v]) => {
    sh.appendRow([k, typeof v === "object" ? JSON.stringify(v) : v]);
  });
  return { ok: true };
}

// ── ELIMINAR JUGADOR ───────────────────────────────
function eliminarJugador(body) {
  const nombre = (body.nombre || "").trim().toLowerCase();
  [SHEET_NAME_JUGADORES, SHEET_NAME_PRONOSTICOS].forEach(shName => {
    const sh   = getOrCreateSheet(shName);
    const data = sh.getDataRange().getValues();
    for (let i = data.length - 1; i >= 1; i--) {
      if (data[i][0] && data[i][0].toLowerCase() === nombre) {
        sh.deleteRow(i + 1);
      }
    }
  });
  return { ok: true };
}

// ── RESETEAR TODO ──────────────────────────────────
function resetear() {
  [SHEET_NAME_JUGADORES, SHEET_NAME_PRONOSTICOS, SHEET_NAME_RESULTADOS].forEach(name => {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const sh = ss.getSheetByName(name);
    if (sh) sh.clearContents();
    getOrCreateSheet(name);
  });
  return { ok: true };
}

// ── FETCH RESULTADOS API (proxy football-data.org) ─
function fetchResultadosAPI(body) {
  const token = (body.apiToken || "").trim();
  if (!token) return { error: "Token vacío" };

  try {
    const url = "https://api.football-data.org/v4/competitions/WC/matches?season=2026";
    const res  = UrlFetchApp.fetch(url, {
      headers: { "X-Auth-Token": token },
      muteHttpExceptions: true
    });

    const code = res.getResponseCode();
    if (code === 401) return { error: "Token inválido — verifica en football-data.org" };
    if (code === 429) return { error: "Límite de requests alcanzado — espera 1 minuto" };
    if (code !== 200) return { error: "Error API: HTTP " + code };

    const data    = JSON.parse(res.getContentText());
    const matches = data.matches || [];

    const ES = {
      "Argentina":"Argentina","Brazil":"Brasil","France":"Francia",
      "Germany":"Alemania","Spain":"España","Portugal":"Portugal",
      "England":"Inglaterra","Netherlands":"Países Bajos","Belgium":"Bélgica",
      "Uruguay":"Uruguay","Croatia":"Croacia","Morocco":"Marruecos",
      "Mexico":"México","Canada":"Canadá","USA":"Estados Unidos",
      "Senegal":"Senegal","Japan":"Japón","South Korea":"Corea del Sur",
      "Australia":"Australia","Switzerland":"Suiza","Ecuador":"Ecuador",
      "Saudi Arabia":"Arabia Saudita","Qatar":"Qatar",
      "Czech Republic":"Chequia","Bosnia and Herzegovina":"Bosnia y Herzegovina",
      "Haiti":"Haití","Scotland":"Escocia","Paraguay":"Paraguay",
      "Turkey":"Turquía","Algeria":"Algeria","Austria":"Austria",
      "Jordan":"Jordania","Colombia":"Colombia","Uzbekistan":"Uzbekistán",
      "DR Congo":"R.D. del Congo","Sweden":"Suecia",
      "Egypt":"Egipto","New Zealand":"Nueva Zelanda",
      "Iraq":"Irak","Cape Verde":"Cabo Verde",
      "Côte d'Ivoire":"Costa de Marfil","Curaçao":"Curazao",
      "South Africa":"Sudáfrica","Ghana":"Ghana","Panama":"Panamá",
      "Norway":"Noruega","Poland":"Polonia","Serbia":"Serbia",
      "Tunisia":"Túnez","Iran":"Irán",
    };
    function es(name) { return ES[name] || name; }

    var oct = [], qua = [], sem = [], f1 = "", f2 = "", campeon = "";

    matches.forEach(function(m) {
      if (m.status !== "FINISHED") return;
      var stage  = m.stage || "";
      var winner = m.score && m.score.winner;
      var home   = es(m.homeTeam.name);
      var away   = es(m.awayTeam.name);

      if (stage === "GROUP_STAGE") {
        if (oct.indexOf(home) === -1) oct.push(home);
        if (oct.indexOf(away) === -1) oct.push(away);
      } else if (stage === "LAST_16") {
        if (oct.indexOf(home) === -1) oct.push(home);
        if (oct.indexOf(away) === -1) oct.push(away);
        var w = winner === "HOME_TEAM" ? home : away;
        if (qua.indexOf(w) === -1) qua.push(w);
      } else if (stage === "QUARTER_FINAL") {
        var w = winner === "HOME_TEAM" ? home : away;
        if (sem.indexOf(w) === -1) sem.push(w);
      } else if (stage === "SEMI_FINAL") {
        var w = winner === "HOME_TEAM" ? home : away;
        if (!f1) f1 = w; else f2 = w;
      } else if (stage === "FINAL") {
        campeon = winner === "HOME_TEAM" ? home : away;
        f1 = home; f2 = away;
      }
    });

    return { resultados: { oct, qua, sem, f1, f2, campeon } };

  } catch(e) {
    return { error: "Error interno: " + e.message };
  }
}
