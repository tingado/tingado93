# 📋 INSTRUCCIONES MANUALES — Polla Mundialera 2026
**Solo 2 pasos manuales necesarios. Todo lo demás ya está listo.**

---

## ⏱ Tiempo estimado: 10 minutos

---

## PASO 1 — Crear el backend desde Google Sheets (no desde script.google.com)

> Esta es la forma correcta. Crear desde Sheets evita el error de permisos.

### 1.1 Crear la hoja
1. Abre **sheets.google.com** en tu navegador
2. Click en el botón **"+"** (Nueva hoja de cálculo)
3. Click en el título "Sin título" → escribe **Polla2026** → Enter

### 1.2 Abrir el editor de scripts
1. En el menú superior click en **"Extensiones"**
2. Click en **"Apps Script"**
3. Se abre una nueva pestaña con el editor

### 1.3 Pegar el código
1. En el editor, selecciona todo el texto (Cmd+A en Mac)
2. Bórralo
3. Abre el archivo **Code.gs** de esta carpeta con cualquier editor de texto
4. Selecciona todo (Cmd+A) → Copia (Cmd+C)
5. Vuelve al editor de Apps Script → Pega (Cmd+V)
6. Guarda (Cmd+S) → Escribe el nombre **Polla2026** → OK

### 1.4 Implementar
1. Click en el botón azul **"Implementar"** (arriba a la derecha)
2. Click en **"Nueva implementación"**
3. Click en el ícono **⚙️** junto a "Seleccionar tipo"
4. Click en **"Aplicación web"**
5. Configura así:
   - Descripción: **Polla2026**
   - Ejecutar como: **Yo**
   - Quién tiene acceso: **Cualquier persona**
6. Click **"Implementar"**

### 1.5 Autorizar (IMPORTANTE — aquí se arregla el error)
Aparece una ventana de Google:
1. Click **"Autorizar acceso"**
2. Elige tu cuenta Google (aidelgado@uc.cl)
3. Si aparece **"Google no verificó esta app"**:
   - Click en **"Configuración avanzada"** (texto pequeño abajo)
   - Click en **"Ir a Polla2026 (no seguro)"**
4. Click **"Permitir"**

### 1.6 Copiar la URL
Aparece una ventana con la URL. Se ve así:
```
https://script.google.com/macros/s/XXXXXXXXXXXXXXXXXX/exec
```
**Copia esa URL completa.** La necesitas en el siguiente paso.

---

## PASO 2 — Conectar la app con el backend nuevo

1. Abre **lapollamundial2026.netlify.app** en el navegador
2. Si no aparece el banner rojo de configuración:
   - Abre las DevTools (Cmd+Option+I)
   - Ve a la pestaña **"Application"** → **"Local Storage"** → **"lapollamundial2026.netlify.app"**
   - Borra las entradas **"polla2026_url"** y **"p2026_cache"**
   - Recarga la página (Cmd+R)
3. Aparece el banner rojo → pega la URL nueva → click **"Conectar"**
4. Debería aparecer ✅ y el leaderboard vacío (sin participantes aún)

---

## PASO 3 — Actualizar el HTML en Netlify (solo si subiste uno anterior)

1. Ve a **app.netlify.com** → tu sitio **lapollamundial2026**
2. Click en **"Deploys"** en el menú izquierdo
3. Arrastra el archivo **index.html** de esta carpeta a la zona de deploys
4. Espera 30 segundos → listo

---

## PASO 4 — Probar que todo funciona

1. Abre **lapollamundial2026.netlify.app**
2. Ve a **Inscripción** → escribe tu nombre → click "Inscribirse"
3. Si aparece ✅ → el backend está funcionando
4. Ve a **Admin** → PIN: **2026**
5. Pega el token de la API: `7dcb1c274a5a4c8582337e0752055982`
6. Click **"Sincronizar"** → debería decir "Sin datos nuevos aún" (el torneo no ha empezado)

---

## PASO 5 — Compartir con tus amigos

Copia este mensaje para WhatsApp:

```
⚽🏆 POLLA MUNDIALERA 2026 🏆⚽

¡El Mundial se viene y nos jugamos la plata!

💰 Entrada: $5.000
🥇 1° lugar → 50% del pozo
🥈 2° lugar → 30% del pozo
🥉 3° lugar → 20% del pozo

👉 Entra aquí:
https://lapollamundial2026.netlify.app

Pasos:
1️⃣ Click en "Inscripción" → escribe tu nombre
2️⃣ Click en "Mis Pronósticos" → predice el marcador de cada partido
3️⃣ Guarda antes del 11 de junio

¡El que sepa de fútbol que lo demuestre! 🤙
```

---

## ❓ Problemas frecuentes

| Problema | Solución |
|---|---|
| "Sin conexión — mostrando datos anteriores" | El backend no está conectado. Repetir PASO 2. |
| "Acción no reconocida: fetchResultadosAPI" | El Code.gs es el viejo. Repetir PASO 1 con el Code.gs de esta carpeta. |
| "Cannot read properties of null (getSheetByName)" | Creaste el script desde script.google.com en vez de desde Sheets. Repetir PASO 1. |
| PIN admin no funciona | El PIN es **2026** (cuatro dígitos). |
| No aparece el banner rojo | Borrar localStorage como se indica en PASO 2. |

---

## 📌 Datos importantes

| Dato | Valor |
|---|---|
| URL de la app | https://lapollamundial2026.netlify.app |
| PIN admin | 2026 |
| Monto entrada | $5.000 CLP |
| Cierre pronósticos | 11 junio 2026, 15:00 hrs |
| Token football-data.org | 7dcb1c274a5a4c8582337e0752055982 |
| Final del torneo | 19 julio 2026 |
