# ⚽ Polla Mundialera 2026

App de pronósticos para el Mundial 2026 (USA · México · Canadá).  
Publicada en **[polla2026mundial.netlify.app](https://polla2026mundial.netlify.app)**

## Para participantes

1. Abre el link
2. Click en **Inscripción** → escribe tu nombre → Inscribirse
3. Click en **Mis Pronósticos** → predice el marcador de cada partido
4. Guarda antes del **11 de junio de 2026**

## Setup para el admin

### 1. Backend (Google Apps Script)

> ⚠️ Crear SIEMPRE desde Google Sheets, no desde script.google.com

1. Ir a **sheets.google.com** → Nueva hoja → nombre: Polla2026
2. Menú **Extensiones → Apps Script**
3. Borrar todo → pegar contenido de `Code.gs` → Ctrl+S
4. **Implementar → Nueva implementación**
   - Tipo: Aplicación web
   - Ejecutar como: Yo
   - Acceso: Cualquier persona
5. Implementar → **Autorizar** (importante — permite llamadas a internet)
6. Copiar la URL generada

### 2. Conectar la app

1. Abrir la app en el navegador
2. Pegar la URL del Apps Script en el banner rojo → Conectar

### 3. Verificar

Abrir en el navegador:
```
TU_URL_APPS_SCRIPT?action=ping
```
Debe responder: `{"ok":true,"ts":"..."}`

## Datos

| Dato | Valor |
|---|---|
| PIN admin | 2026 |
| Monto entrada | $5.000 CLP |
| Cierre pronósticos | 11 junio 2026 |
| Premios | 50% / 30% / 20% |

## Stack

HTML + CSS + JS vanilla → Netlify (hosting)  
Google Apps Script → Google Sheets (backend, gratis)  
football-data.org (API resultados, gratis)
