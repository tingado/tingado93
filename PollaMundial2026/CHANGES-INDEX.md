# Cambios pendientes para index.html de PollaMundial2026

> Aplicar estos cambios al archivo `index.html` en https://github.com/tingado/PollaMundial2026
> Antes de aplicar, verificar si el usuario ya incorporó algunos de estos cambios.

---

## 1. CSS — Agregar estilos para right-panel y facts widget

En el bloque `<style>`, agregar ANTES del cierre `</style>`:

```css
/* ══ RIGHT PANEL ══ */
.right-panel {
  width: 240px; flex-shrink: 0;
  position: sticky; top: 0; height: 100vh;
  overflow-y: auto; padding: 1.25rem 1rem;
  border-left: 1px solid var(--border);
  background: var(--panel);
  display: flex; flex-direction: column; gap: 1rem;
}
.facts-widget {
  background: #1f0a14; border-radius: 14px; padding: 1rem;
}
.facts-label {
  font-size: 10px; font-weight: 800; letter-spacing: 1.5px;
  text-transform: uppercase; color: var(--rosa);
  margin-bottom: 0.75rem; display: flex; align-items: center; gap: 6px;
}
.fact-text {
  font-size: 12px; color: #ffb3d9; line-height: 1.7;
  min-height: 80px; transition: opacity 0.5s ease;
}
.fact-dots {
  display: flex; gap: 4px; margin-top: 0.75rem; justify-content: center;
}
.fact-dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: rgba(255,179,217,0.3); transition: background 0.3s;
}
.fact-dot.active { background: var(--rosa); }

@media (max-width: 1100px) { .right-panel { display: none; } }
```

---

## 2. HTML — Quitar el ticker horizontal

Eliminar este bloque completo:
```html
<!-- TICKER -->
<div class="ticker-wrap">
  <div class="ticker-label">⚡ Sabías que</div>
  <div class="ticker-track">
    <div class="ticker-content" id="ticker-content"></div>
  </div>
</div>
```

Y también eliminar el CSS del ticker (`.ticker-wrap`, `.ticker-label`, `.ticker-track`, `.ticker-content`, `.ticker-item`, `@keyframes ticker`).

---

## 3. HTML — Agregar right panel

Después de `</main>` y ANTES del cierre `</div>` del `.layout`, agregar:

```html
<!-- RIGHT PANEL: Sabías que -->
<div class="right-panel">
  <div class="facts-widget">
    <div class="facts-label">⚡ ¿Sabías que?</div>
    <div class="fact-text" id="fact-text">Cargando...</div>
    <div class="fact-dots" id="fact-dots"></div>
  </div>
  <div style="font-size:11px;color:var(--muted);text-align:center;line-height:1.5;">
    🌍 Copa Mundial<br>11 Jun — 19 Jul 2026<br>USA · MX · CAN
  </div>
</div>
```

---

## 4. HTML — Agregar botón "Cómo se calcula" en sidebar

En `.sidebar-nav`, agregar después del botón de Inscripción:
```html
<button class="nav-btn" onclick="showView('calculos',this)">🧮 Cómo se calcula</button>
```

En `.mobile-nav`, agregar también:
```html
<button class="mobile-nav-btn" onclick="showView('calculos',this)">
  <span>🧮</span>Cálculo
</button>
```

---

## 5. HTML — Agregar vista "Cómo se calcula"

Después de `#view-inscripcion` y antes de `#view-admin`:

```html
<!-- ══ VIEW: CÓMO SE CALCULA ══ -->
<div id="view-calculos" class="view">
  <div class="view-header">
    <div class="view-title">🧮 Cómo se calcula</div>
  </div>

  <div class="form-card">
    <div class="form-title">📋 Sistema de Pronósticos</div>
    <p style="font-size:13px;color:var(--muted);line-height:1.7;margin-bottom:1rem;">
      La Polla Mundialera 2026 funciona en <strong>dos etapas</strong>: predecir quién termina
      1° y 2° en cada grupo, y luego predecir qué equipos avanzan en cada ronda eliminatoria.
    </p>
    <div class="steps">
      <div class="step">
        <div class="step-num">1️⃣</div>
        <div class="step-title">Fase de Grupos</div>
        <div class="step-desc">Predice el 1° y 2° lugar de cada uno de los 12 grupos (A–L)</div>
      </div>
      <div class="step">
        <div class="step-num">2️⃣</div>
        <div class="step-title">Eliminatorias</div>
        <div class="step-desc">Predice qué equipos llegan a 16avos, cuartos, semis, final y quién es campeón</div>
      </div>
      <div class="step">
        <div class="step-num">3️⃣</div>
        <div class="step-title">Ranking</div>
        <div class="step-desc">Se suman los puntos a medida que avanza el torneo</div>
      </div>
    </div>
  </div>

  <div class="form-card">
    <div class="form-title">⚽ Fase de Grupos — Puntos</div>
    <p style="font-size:12px;color:var(--muted);margin-bottom:1rem;">Por cada grupo (A hasta L), predices qué equipo termina primero y segundo.</p>
    <div style="display:flex;flex-direction:column;gap:6px;">
      <div class="score-row" style="background:rgba(16,163,74,0.08);border:1px solid rgba(16,163,74,0.2);">
        <span>🥇 1° lugar del grupo correcto</span>
        <span style="color:var(--verde);font-weight:800;font-size:15px;">+2 pts</span>
      </div>
      <div class="score-row" style="background:rgba(16,163,74,0.05);border:1px solid rgba(16,163,74,0.15);">
        <span>🥈 2° lugar del grupo correcto</span>
        <span style="color:var(--verde);font-weight:800;font-size:15px;">+1 pt</span>
      </div>
    </div>
    <div style="margin-top:1rem;padding:10px 13px;background:#f9fafb;border-radius:9px;font-size:12px;color:var(--muted);">
      Máximo en grupos: <strong style="color:var(--rosa);">12 grupos × 3 pts = 36 pts</strong>
    </div>
  </div>

  <div class="form-card">
    <div class="form-title">🏆 Fase Eliminatoria — Puntos</div>
    <div style="display:flex;flex-direction:column;gap:6px;">
      <div class="score-row"><span>Equipo correcto en 16avos (32 equipos)</span><span style="color:var(--verde);font-weight:700;">+2 pts</span></div>
      <div class="score-row"><span>Equipo correcto en Cuartos (8 equipos)</span><span style="color:var(--verde);font-weight:700;">+4 pts</span></div>
      <div class="score-row"><span>Equipo correcto en Semis (4 equipos)</span><span style="color:var(--verde);font-weight:700;">+6 pts</span></div>
      <div class="score-row"><span>Subcampeón correcto (2 finalistas)</span><span style="color:var(--dorado);font-weight:700;">+8 pts</span></div>
      <div class="score-row" style="background:rgba(245,188,0,0.08);border:1px solid rgba(245,188,0,0.25);">
        <span>🏆 Campeón del Mundo correcto</span>
        <span style="color:var(--dorado);font-weight:800;font-size:15px;">+10 pts</span>
      </div>
    </div>
  </div>

  <div class="form-card">
    <div class="form-title">💡 Ejemplo Práctico</div>
    <div style="font-size:13px;line-height:1.8;color:var(--text);">
      <p>Predices en el <strong>Grupo A</strong>: 1° México, 2° Corea del Sur.</p>
      <p>Al terminar el grupo, México quedó 1° ✅ → <strong style="color:var(--verde);">+2 pts</strong></p>
      <p>Corea del Sur quedó 3° ❌ → 0 pts</p><br>
      <p>Predices que <strong>Argentina</strong> llega a Semis.</p>
      <p>Argentina llega a Semis ✅ → <strong style="color:var(--verde);">+6 pts</strong></p><br>
      <p style="color:var(--muted);font-size:12px;">💡 Los pronósticos cierran el 11 de junio. ¡Guarda antes!</p>
    </div>
  </div>
</div>
```

---

## 6. HTML — Refactorizar "Mis Pronósticos"

Reemplazar el contenido dentro de `#view-pronosticos` (el `<div id="pronosticos-lista">` permanece, solo cambia cómo se llena con JS).

---

## 7. HTML — Actualizar Sistema de Puntaje en Inscripción

Reemplazar el bloque actual del "Sistema de Puntaje" (buscar `Resultado exacto` y `Ganador correcto`) con:

```html
<div class="form-card">
  <div class="form-title">📊 Sistema de Puntaje</div>
  <div style="font-size:11px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">Fase de Grupos</div>
  <div style="display:flex;flex-direction:column;gap:5px;margin-bottom:1rem;">
    <div class="score-row"><span>🥇 1° lugar de grupo correcto</span><span style="color:var(--verde);font-weight:700;">+2 pts</span></div>
    <div class="score-row"><span>🥈 2° lugar de grupo correcto</span><span style="color:var(--verde);font-weight:700;">+1 pt</span></div>
  </div>
  <div style="font-size:11px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">Fase Eliminatoria</div>
  <div style="display:flex;flex-direction:column;gap:5px;">
    <div class="score-row"><span>Equipo en 16avos</span><span style="color:var(--verde);font-weight:700;">+2 pts</span></div>
    <div class="score-row"><span>Equipo en Cuartos</span><span style="color:var(--verde);font-weight:700;">+4 pts</span></div>
    <div class="score-row"><span>Equipo en Semis</span><span style="color:var(--verde);font-weight:700;">+6 pts</span></div>
    <div class="score-row"><span>Subcampeón</span><span style="color:var(--dorado);font-weight:700;">+8 pts</span></div>
    <div class="score-row" style="background:rgba(245,188,0,0.08);">
      <span>🏆 Campeón correcto</span>
      <span style="color:var(--dorado);font-weight:700;">+10 pts</span>
    </div>
  </div>
</div>
```

---

## 8. JS — Reemplazar ELIM_RONDAS

Buscar `const ELIM_RONDAS = [` y reemplazar el bloque completo:

```js
const ELIM_RONDAS = [
  { key:'oct', label:'16avos de Final',    pts:2, max:32, desc:'Selecciona los 32 equipos que crees que clasifican de grupos (los mejores 3ros también pasan)' },
  { key:'qua', label:'Cuartos de Final',   pts:4, max:8,  desc:'Selecciona los 8 equipos que crees que llegan a cuartos' },
  { key:'sem', label:'Semifinales',        pts:6, max:4,  desc:'Selecciona los 4 equipos que crees que llegan a semis' },
  { key:'fin', label:'Final (Finalistas)', pts:8, max:2,  desc:'Selecciona los 2 finalistas — subcampeón = +8 pts' },
];
```

---

## 9. JS — Reemplazar calcPtsGrupos()

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

---

## 10. JS — Reemplazar calcPtsElim()

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

---

## 11. JS — Reemplazar initTicker() con initFacts()

Buscar `function initTicker()` y reemplazar:

```js
let factIdx = 0;
function initFacts(){
  const el=$id('fact-text'), dots=$id('fact-dots');
  if(!el) return;
  const facts = DATOS.slice(0,10);
  dots.innerHTML = facts.map((_,i)=>`<div class="fact-dot${i===0?' active':''}" id="fdot-${i}"></div>`).join('');
  function showFact(i){
    el.style.opacity='0';
    setTimeout(()=>{
      el.textContent='⚽ '+facts[i];
      el.style.opacity='1';
      dots.querySelectorAll('.fact-dot').forEach((d,j)=>d.classList.toggle('active',j===i));
    },500);
  }
  showFact(0);
  setInterval(()=>{ factIdx=(factIdx+1)%facts.length; showFact(factIdx); },6000);
}
```

Y en la sección INIT, cambiar `initTicker()` → `initFacts()`.

---

## 12. JS — Reemplazar cargarPronostico()

```js
function cargarPronostico(){
  const jugador=$id('sel-jugador').value;
  const cont=$id('pronosticos-lista');
  const btn=$id('btn-save-pron');
  if(!jugador){cont.innerHTML='';btn.style.display='none';return;}
  btn.style.display='block';
  const p=state.pronosticos[jugador]||{};
  const cerrado=new Date()>=FECHA_CIERRE;
  if(cerrado){
    cont.innerHTML='<div class="form-card" style="text-align:center;padding:2rem;border-color:rgba(255,61,90,0.3);">⏰ <strong>Pronósticos cerrados</strong><br><span style="color:var(--muted);font-size:13px;">El plazo terminó el 11 de junio.</span></div>';
    btn.style.display='none'; return;
  }
  const gp = p.grupos || {};
  cont.innerHTML =
    '<div style="margin-bottom:12px;padding:10px 14px;background:rgba(245,188,0,0.07);border:1px solid rgba(245,188,0,0.2);border-radius:10px;font-size:12px;color:var(--muted);">🏆 Predice quién termina <strong>1° y 2°</strong> en cada grupo.</div>' +
    Object.entries(GRUPOS).map(([g,equipos])=>{
      const gg=gp[g]||{};
      const o1=equipos.map(eq=>`<option value="${eq}"${gg.p1===eq?' selected':''}>${flag(eq)} ${eq}</option>`).join('');
      const o2=equipos.map(eq=>`<option value="${eq}"${gg.p2===eq?' selected':''}>${flag(eq)} ${eq}</option>`).join('');
      return `
        <div class="form-card" style="margin-bottom:10px;padding:1rem;">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
            <div style="background:var(--rosa);color:#fff;font-family:'Bebas Neue',sans-serif;font-size:1.1rem;padding:4px 10px;border-radius:8px;letter-spacing:1px;">Grupo ${g}</div>
            <div style="font-size:12px;color:var(--muted);">${equipos.map(eq=>flag(eq)+' '+eq).join(' · ')}</div>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
            <div>
              <label style="color:var(--dorado);">🥇 1° Lugar</label>
              <select id="pron-g${g}-p1" style="margin-bottom:0;">
                <option value="">-- Elige --</option>${o1}
              </select>
            </div>
            <div>
              <label style="color:var(--plata);">🥈 2° Lugar</label>
              <select id="pron-g${g}-p2" style="margin-bottom:0;">
                <option value="">-- Elige --</option>${o2}
              </select>
            </div>
          </div>
        </div>`;
    }).join('');
}
```

---

## 13. JS — Reemplazar guardarPronostico()

```js
async function guardarPronostico(){
  const jugador=$id('sel-jugador').value;
  if(!jugador)return;
  const pron=state.pronosticos[jugador]?JSON.parse(JSON.stringify(state.pronosticos[jugador])):{};
  pron.grupos={};
  Object.keys(GRUPOS).forEach(g=>{
    const p1=$id(`pron-g${g}-p1`)?.value||'';
    const p2=$id(`pron-g${g}-p2`)?.value||'';
    if(p1||p2) pron.grupos[g]={p1,p2};
  });
  setLoad('btn-save-pron',true);
  try{
    await api({action:'guardarPron',nombre:jugador,pronostico:pron});
    setMsg('msg-pron','✅ Pronósticos de grupos guardados correctamente.');
    invalidarCache(); await cargarDatos(true);
    setTimeout(()=>clearMsg('msg-pron'),4000);
  }catch(e){setMsg('msg-pron',e.message,'err');}
  finally{setLoad('btn-save-pron',false);}
}
```

---

## 14. JS — Agregar renderAdminGrupos() y guardarResultadosGrupos()

```js
function renderAdminGrupos(){
  const cont=$id('admin-grupos-grid');
  if(!cont) return;
  const rg=state.resultados.grupos||{};
  cont.innerHTML=Object.entries(GRUPOS).map(([g,equipos])=>{
    const rr=rg[g]||{};
    const o1=equipos.map(eq=>`<option value="${eq}"${rr.p1===eq?' selected':''}>${flag(eq)} ${eq}</option>`).join('');
    const o2=equipos.map(eq=>`<option value="${eq}"${rr.p2===eq?' selected':''}>${flag(eq)} ${eq}</option>`).join('');
    return `
      <div style="background:#f9fafb;border:1px solid var(--border);border-radius:10px;padding:10px;">
        <div style="font-family:'Bebas Neue',sans-serif;font-size:1rem;color:var(--rosa);margin-bottom:8px;letter-spacing:1px;">Grupo ${g}</div>
        <label style="color:var(--dorado);">🥇 1°</label>
        <select id="res-g${g}-p1" style="margin-bottom:6px;"><option value="">-- País --</option>${o1}</select>
        <label style="color:var(--plata);">🥈 2°</label>
        <select id="res-g${g}-p2" style="margin-bottom:0;"><option value="">-- País --</option>${o2}</select>
      </div>`;
  }).join('');
}

async function guardarResultadosGrupos(){
  const grupos={};
  Object.keys(GRUPOS).forEach(g=>{
    const p1=$id(`res-g${g}-p1`)?.value||'';
    const p2=$id(`res-g${g}-p2`)?.value||'';
    grupos[g]={p1,p2};
  });
  try{
    await api({action:'guardarResultadosGrupos',grupos});
    setMsg('msg-admin-grupos','✅ Resultados de grupos guardados.');
    invalidarCache(); await cargarDatos(true);
    setTimeout(()=>clearMsg('msg-admin-grupos'),4000);
  }catch(e){setMsg('msg-admin-grupos',e.message,'err');}
}
```

Llamar `renderAdminGrupos()` dentro de `applyState()`.

---

## 15. HTML — Admin: Agregar sección resultados de grupos

Antes de la tarjeta "✍️ Ingreso Manual de Resultados" en `#view-admin`:

```html
<!-- RESULTADOS DE GRUPOS -->
<div class="admin-card" style="border-color:rgba(245,188,0,0.2);">
  <div class="admin-title">🏟️ Resultados Finales de Grupos</div>
  <p style="font-size:12px;color:var(--muted);margin-bottom:1rem;">Ingresa quién terminó 1° y 2° en cada grupo al finalizar la fase de grupos.</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;" id="admin-grupos-grid"></div>
  <div id="msg-admin-grupos"></div>
  <button class="btn btn-gold btn-full" style="margin-top:10px;" onclick="guardarResultadosGrupos()">💾 Guardar resultados de grupos</button>
</div>
```

---

## 16. JS — Actualizar descripción en Eliminatorias

Buscar el texto `Puntos: octavos` y reemplazar la línea por:
```
Predice qué equipos llegan a cada ronda. Puntos: 16avos <strong style="color:var(--verde);">+2</strong>, cuartos <strong style="color:var(--verde);">+4</strong>, semis <strong style="color:var(--verde);">+6</strong>, subcampeón <strong style="color:var(--dorado);">+8</strong>, campeón <strong style="color:var(--dorado);">+10</strong>
```
