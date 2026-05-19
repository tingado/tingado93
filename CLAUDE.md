# CLAUDE.md — Polla Mundial 2026 · Continuación de sesión

## Contexto del proyecto

El usuario está construyendo **"La Polla Mundialera 2026"**, un juego de predicciones para el Mundial de Fútbol 2026.

- **App en producción**: https://tingado.github.io/PollaMundial2026/
- **Repo del app**: https://github.com/tingado/PollaMundial2026/tree/main
- **Repo de trabajo** (este): `tingado/tingaod93`, branch `claude/add-notebooklm-mcp-0J9zw`
- **Backend**: Google Apps Script + Google Sheets (JSONP)
- **Apps Script URL activa**: `https://script.google.com/macros/s/AKfycbz7nEAOOnzNj1JvU9SOHgaveW7NDGBN4KegtE9uJ3gHyIOD3KMJ9FB3esflX-qOvZfO/exec`

> ⚠️ El repo `tingado/PollaMundial2026` NO es accesible via GitHub MCP tools (solo `tingado/tingaod93` está permitido). Los cambios a `index.html` deben proporcionarse como código para que el usuario los aplique manualmente en el editor de GitHub, o vía `WebFetch` desde raw.githubusercontent.com.

---

## 🔧 ACCIÓN PENDIENTE PARA LA PRÓXIMA SESIÓN: Migrar al repo correcto

> **El usuario ha solicitado que las próximas sesiones trabajen directamente en `tingado/PollaMundial2026`** en vez de usar `tingado/tingaod93` como intermediario.

**Por qué es importante:** Actualmente Claude Code solo tiene acceso MCP a `tingado/tingaod93`, lo que obliga a preparar los cambios aquí y que el usuario los aplique manualmente en `PollaMundial2026`. Si se configura `tingado/PollaMundial2026` como el repo permitido en la siguiente sesión (al crear el entorno en claude.ai/code), Claude podrá editar `index.html` directamente.

**Para la próxima sesión en claude.ai/code:**
1. Al crear el entorno (o en la configuración), conectar el repo `tingado/PollaMundial2026` en vez de `tingado/tingaod93`
2. Esto permitirá editar `index.html` directo vía GitHub MCP y hacer push sin pasos manuales intermedios

**Mientras tanto**, los archivos actualizados están disponibles en este repo en `PollaMundial2026/`.

---

## Estado actual del backend (Apps Script)

El archivo `PollaMundial2026/apps-script.gs` en este repo contiene el código **completo y actualizado** listo para reemplazar el Apps Script desplegado. Incluye:
- Scoring correcto con los valores confirmados
- Soporte para pronósticos por grupo (p1/p2 por grupo A-L)
- Endpoint `guardarResultadosGrupos`
- Integración con football-data.org API
- Todas las acciones: getAll, inscribir, guardarPron, guardarResultados, guardarResultadosGrupos, fetchResultadosAPI, eliminarJugador, resetear

Para redesplegarlo:
1. Abrir script.google.com → proyecto vinculado al Google Sheet
2. Reemplazar todo el contenido con `apps-script.gs`
3. Deploy > Manage deployments > editar el deployment existente > New version
4. Copiar la misma URL /exec (no cambia si se edita el mismo deployment)

---

## Sistema de puntuación CONFIRMADO

| Acierto | Puntos |
|---------|--------|
| 1° lugar de grupo | **+2 pts** |
| 2° lugar de grupo | **+1 pt** |
| Equipo en 16avos (32 clasificados) | **+2 pts** |
| Equipo en Cuartos (8 equipos) | **+4 pts** |
| Equipo en Semis (4 equipos) | **+6 pts** |
| Subcampeón correcto (2 finalistas) | **+8 pts** |
| Campeón correcto | **+10 pts** |

> ⚠️ El `index.html` actual en el repo PollaMundial2026 tiene valores INCORRECTOS (el viejo sistema de marcadores). Todos los cambios pendientes de abajo deben aplicarse.

---

## Modelo de datos del pronóstico

### Estructura `pron` (por jugador):
```json
{
  "grupos": {
    "A": { "p1": "México", "p2": "Corea del Sur" },
    "B": { "p1": "Canadá", "p2": "Suiza" },
    "C": { "p1": "Brasil", "p2": "Marruecos" },
    "D": { "p1": "Estados Unidos", "p2": "Turquía" },
    "E": { "p1": "Alemania", "p2": "Ecuador" },
    "F": { "p1": "Países Bajos", "p2": "Japón" },
    "G": { "p1": "Bélgica", "p2": "España" },
    "H": { "p1": "España", "p2": "Uruguay" },
    "I": { "p1": "Francia", "p2": "Noruega" },
    "J": { "p1": "Argentina", "p2": "Austria" },
    "K": { "p1": "Portugal", "p2": "Colombia" },
    "L": { "p1": "Inglaterra", "p2": "Croacia" }
  },
  "elim": {
    "oct": ["Brasil", "Argentina", ...],
    "qua": ["Brasil", "Argentina", ...],
    "sem": ["Brasil", "Argentina"],
    "fin": ["Brasil", "Argentina"],
    "f1": "Brasil",
    "f2": "Argentina",
    "campeon": "Argentina"
  }
}
```

### Estructura `resultados` (en Sheets):
```json
{
  "grupos": { "A": {"p1":"México","p2":"Corea del Sur"}, ... },
  "oct": ["Brasil", "Argentina", ...],
  "qua": ["Brasil", "Argentina", ...],
  "sem": ["Brasil", "Argentina"],
  "f1": "Brasil",
  "f2": "Argentina",
  "campeon": "Argentina"
}
```

---

## Cambios pendientes en index.html

El archivo `PollaMundial2026/CHANGES-INDEX.md` en este repo documenta **exactamente qué cambiar** en el `index.html`. Los cambios son:

### 1. Layout 3 columnas (sidebar + main + right-panel)
Agregar CSS para `.right-panel` (240px) y modificar `.layout`.

### 2. Eliminar ticker horizontal
Quitar el `<div class="ticker-wrap">` y su CSS.

### 3. Agregar panel derecho "Sabías que"
Panel lateral derecho con 10 datos curiosos que rotan cada 6 segundos (sin scroll, con fade y dots).

### 4. Agregar vista "Cómo se calcula"
Nueva vista (`#view-calculos`) con tabla de puntajes y ejemplos prácticos.

### 5. Refactorizar "Mis Pronósticos"
Cambiar de 72 inputs de marcadores → 12 tarjetas de grupo con selectores 1°/2° lugar.

### 6. Actualizar puntajes mostrados en Inscripción
Reemplazar la sección "Sistema de Puntaje" con los valores correctos.

### 7. Actualizar ELIM_RONDAS
```js
const ELIM_RONDAS = [
  { key:'oct', label:'16avos de Final', pts:2, max:32, ... },
  { key:'qua', label:'Cuartos de Final', pts:4, max:8, ... },
  { key:'sem', label:'Semifinales',      pts:6, max:4, ... },
  { key:'fin', label:'Final (Finalistas)',pts:8, max:2, ... },
];
```

### 8. Reemplazar calcPtsGrupos()
```js
function calcPtsGrupos(pron, res){
  if(!pron||!res) return 0;
  const pg = pron.grupos || {};
  const rg = res.grupos || {};
  let pts = 0;
  Object.keys(GRUPOS).forEach(g => {
    const pp = pg[g] || {};
    const rr = rg[g] || {};
    if(pp.p1 && rr.p1 && pp.p1 === rr.p1) pts += 2;
    if(pp.p2 && rr.p2 && pp.p2 === rr.p2) pts += 1;
  });
  return pts;
}
```

### 9. Reemplazar calcPtsElim()
```js
function calcPtsElim(pron, res){
  if(!pron||!res) return 0;
  const elim=pron.elim||{};
  let pts=0;
  const rOct=toArr(res.oct), rQua=toArr(res.qua), rSem=toArr(res.sem);
  const rFin=[res.f1||'',res.f2||''].filter(Boolean);
  const rCamp=res.campeon||'';
  (elim.oct||[]).forEach(t=>{ if(rOct.includes(t)) pts+=2; });
  (elim.qua||[]).forEach(t=>{ if(rQua.includes(t)) pts+=4; });
  (elim.sem||[]).forEach(t=>{ if(rSem.includes(t)) pts+=6; });
  (elim.fin||[]).forEach(t=>{ if(rFin.includes(t)) pts+=8; });
  if(elim.campeon&&elim.campeon===rCamp) pts+=10;
  return pts;
}
```

### 10. Reemplazar initTicker() con initFacts()
```js
let factIdx = 0;
function initFacts(){
  const el=$id('fact-text'), dots=$id('fact-dots');
  if(!el) return;
  const facts = DATOS.slice(0,10);
  dots.innerHTML = facts.map((_,i)=>`<div class="fact-dot${i===0?' active':''}" id="fdot-${i}"></div>`).join('');
  function showFact(i){
    el.style.opacity='0';
    setTimeout(()=>{ el.textContent='⚽ '+facts[i]; el.style.opacity='1';
      dots.querySelectorAll('.fact-dot').forEach((d,j)=>d.classList.toggle('active',j===i));
    },500);
  }
  showFact(0);
  setInterval(()=>{ factIdx=(factIdx+1)%facts.length; showFact(factIdx); },6000);
}
```

### 11. Actualizar cargarPronostico() — 12 group pickers
Ver `PollaMundial2026/CHANGES-INDEX.md` para el código completo.

### 12. Admin: Agregar sección resultados de grupos
Ver `PollaMundial2026/CHANGES-INDEX.md` para el código completo.

---

## Nota sobre cambios del usuario en PollaMundial2026

El usuario indicó que realizó cambios en https://github.com/tingado/PollaMundial2026/tree/main para "dejar el repositorio más robusto". 

**Al iniciar la próxima sesión, lo primero que hay que hacer es:**
```bash
# Fetch the latest index.html
WebFetch("https://raw.githubusercontent.com/tingado/PollaMundial2026/main/index.html")
```
para ver qué cambió antes de aplicar los cambios pendientes.

---

## Formato del Mundial 2026

- **48 equipos**, 12 grupos (A-L) de 4 equipos
- Clasifican: top 2 de cada grupo + 8 mejores terceros = **32 equipos** a 16avos
- Sede: USA, México, Canadá
- Inicio: 11 de junio 2026, Final: 19 de julio 2026 (MetLife Stadium, NY)
- Participación Chile: No clasificó

## Grupos
```
A: México, Sudáfrica, Corea del Sur, Chequia
B: Canadá, Suiza, Qatar, Bosnia y Herzegovina
C: Brasil, Marruecos, Haití, Escocia
D: Estados Unidos, Paraguay, Australia, Turquía
E: Alemania, Ecuador, Costa de Marfil, Curazao
F: Países Bajos, Japón, Túnez, Suecia
G: Bélgica, Egipto, Irán, Nueva Zelanda
H: España, Uruguay, Arabia Saudita, Cabo Verde
I: Francia, Senegal, Noruega, Irak
J: Argentina, Algeria, Austria, Jordania
K: Portugal, Colombia, Uzbekistán, R.D. del Congo
L: Inglaterra, Croacia, Ghana, Panamá
```

---

## Parámetros del juego

- Entrada: **$5.000 CLP** por participante
- Distribución del pozo: 50% (1°), 30% (2°), 20% (3°)
- PIN admin: `2026`
- Fecha cierre pronósticos: 11 de junio 2026 (mismo día del inicio)
- Canales Chile: DSports, ChileVisión, Disney+

---

## Estado de tareas

- [x] MCP NotebookLM configurado (`/root/.claude/mcp.json`)
- [x] Google Sheets conectado vía Apps Script JSONP
- [x] Apps Script actualizado (ver `PollaMundial2026/apps-script.gs`)
- [ ] Aplicar cambios al index.html (ver lista arriba)
- [ ] Re-desplegar Apps Script con código actualizado
- [ ] Verificar que pronósticos de grupos funcionan end-to-end
