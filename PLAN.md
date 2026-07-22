# Plan de trabajo — App Garmin de entrenamiento (Connect IQ)

> App para **crear y guiar sesiones de entrenamiento** en el reloj: definir sesiones,
> cargas (peso/intensidad), pausas (descansos) y avisar cuando una sesión queda **completa**.

---

## 1. Objetivo y alcance

Construir una **aplicación Connect IQ (Device App)** en **Monkey C** que corra en el reloj
Garmin y permita:

- **Definir/seleccionar sesiones** de entrenamiento (ej. rutina de fuerza con varios ejercicios).
- Registrar **cargas**: peso, reps y/o intensidad por serie.
- Gestionar **pausas / descansos** con cuenta regresiva automática entre series.
- **Avisar cuando la sesión está completa** (vibración + tono + pantalla grande).

**Fuera de alcance (v1):** análisis histórico avanzado, planes de varios meses, integración
con nutrición. Se contemplan como fases futuras.

---

## 2. Decisiones tomadas

| Decisión | Elección |
|---|---|
| Enfoque | **App Connect IQ nativa** (Monkey C) |
| Dispositivos objetivo | **Venu (gen 1)** — principal · **Venu Sq** — compatible |
| Repositorio | `app-gym-garmin-chile` (repo dedicado, privado) |
| Lenguaje | Monkey C |
| SDK | Connect IQ SDK (última versión estable) |
| Creación de rutinas | **En el móvil** (Connect IQ App Settings en Garmin Connect) → sincroniza al reloj |

> **Restricción de memoria observada:** en el reloj del usuario quedan **~7.41 MB** libres.
> La app debe ser **ligera**: datos compactos, sin recursos pesados innecesarios y carga de
> sesiones bajo demanda.

### Dispositivos objetivo — implicaciones de diseño

| | **Venu (gen 1)** | **Venu Sq** |
|---|---|---|
| Pantalla | **Redonda** AMOLED 390×390 | **Rectangular** MIP-LCD ~148×205 |
| Altavoz | **No** | **No** |
| Vibración / tonos | Sí | Sí |

Consecuencias:
- **Sin audio/voz:** ningún modelo tiene altavoz → los avisos son **vibración + tono + pantalla**. Se descarta el audio pregrabado.
- **UI adaptable:** layout debe verse bien en **redondo (Venu)** y **rectangular más pequeño (Venu Sq)**. Usar layouts por dispositivo y evitar asumir centro/tamaño.
- **MIP en Venu Sq:** menos colores y siempre encendida → priorizar **alto contraste** sobre gradientes/AMOLED puro.

### Nota técnica sobre "que diga sesiones completas"
Connect IQ **no expone text-to-speech (TTS)**, y además **estos modelos no tienen altavoz**. Los avisos se logran con:
1. **Vibración** (`Toybox.Attention.vibrate`) — patrones distintos por evento.
2. **Tonos** (`Toybox.Attention.playTone`) — "fin de serie", "descanso" y "sesión completa".
3. **Pantalla clara**: mensaje grande tipo **"SESIÓN COMPLETA ✅"** con color y animación.

---

## 2.b Diferenciadores vs. apps de referencia

Apps de referencia probadas por el usuario que **no lo convencen al 100%**:
_Gym Workout Tracker_, _Gym – Set Counter with Rest Timer_, _KTrain for Kieser_.

Problemas detectados (los 4 confirmados por el usuario) y cómo los resolvemos:

| Problema en apps existentes | Solución en nuestra app |
|---|---|
| **Captura de datos tediosa** (girar ruedas / +/- a mitad de serie) | La rutina viene **prearmada desde el móvil**; en el reloj el gesto principal es **un botón grande "Serie hecha"**. Ajuste de carga solo si hace falta, con pasos rápidos (±2.5 kg). Mínimo input durante el esfuerzo. |
| **No hay sesiones prearmadas** | **Creador de rutinas en el móvil** (App Settings) + rutinas de ejemplo; el reloj solo **ejecuta** lo ya definido. |
| **Avisos / pausas pobres** | Módulo `Feedback` fuerte: **vibración marcada + tonos diferenciados por evento + pantalla grande**. Descanso con **cuenta regresiva prominente**. |
| **UI fea / poco clara** | Diseño **limpio y de alto contraste**: un dato principal por pantalla, números grandes, **color por estado** (ejercicio / descanso / completo), adaptado a pantalla redonda (Venu) y rectangular (Venu Sq). |

---

## 3. Preparación del entorno (Fase 0)

- [ ] Instalar **Connect IQ SDK** + **SDK Manager** (macOS/Windows/Linux).
- [ ] Instalar la extensión **Monkey C** en **VS Code**.
- [ ] Descargar los **device profiles** de los relojes objetivo (Venu 2/3, Vivoactive 5).
- [ ] Configurar el **simulador** de Connect IQ.
- [ ] Crear cuenta de **desarrollador Garmin** (necesaria para publicar).
- [ ] Generar `manifest.xml` inicial y estructura de proyecto (`source/`, `resources/`, `monkey.jungle`).

**Entregable:** proyecto vacío que compila y arranca en el simulador ("Hola mundo" en Venu).

---

## 4. Modelo de datos

```
Sesion
 ├─ id, nombre, fecha
 ├─ estado: pendiente | en_curso | completa
 └─ ejercicios: [Ejercicio]

Ejercicio
 ├─ nombre (ej. "Sentadilla")
 ├─ series: [Serie]
 └─ descansoEntreSeries (seg)

Serie
 ├─ reps
 ├─ carga (kg / % / RPE)
 ├─ completada: bool
 └─ descansoPost (seg, opcional override)
```

- Almacenamiento local con **`Toybox.Application.Storage`** / `Properties` (persistencia entre sesiones).
- Sesiones de ejemplo empaquetadas como **recursos** para el MVP.
- **Sincronización desde el móvil vía App Settings** (ver sección 4.b): la rutina definida en el
  teléfono llega al reloj como `Properties` y se parsea al modelo de arriba.

### 4.b Creación de rutinas desde el móvil — enfoque realista

App Settings de Connect IQ es un editor de **ajustes** (listas, números, texto, toggles) dentro de
Garmin Connect; **no** es un constructor visual libre. Por eso lo escalonamos:

- **v1 (simple):** rutinas de ejemplo ya incluidas + App Settings para **elegir rutina** y **ajustar
  parámetros** (descanso por defecto, unidades kg/lb, volumen de avisos).
- **v2 (rutina propia):** definir ejercicios/series/cargas desde App Settings usando campos de lista y
  números; internamente se serializa a un **string JSON compacto** que el reloj parsea.
- **v3 (opcional):** evaluar una **app/página companion** para un editor visual completo si App
  Settings se queda corto para tu flujo.

---

## 5. Arquitectura (patrón Connect IQ)

App Connect IQ sigue **App → View → Delegate (Input)**:

- **`TrainingApp`** (`AppBase`): ciclo de vida, carga de datos.
- **Vistas (`WatchUi.View`):**
  - `SessionListView` — elegir sesión.
  - `ExerciseView` — ejercicio actual, serie, carga, botón "hecho".
  - `RestView` — cuenta regresiva del descanso.
  - `CompleteView` — pantalla "SESIÓN COMPLETA".
- **Delegates (`WatchUi.BehaviorDelegate`):** manejo de botones/táctil.
- **Servicios:**
  - `SessionManager` — estado, avance de series, marcar completada.
  - `Timer` (`Toybox.Timer`) — descansos y cuentas regresivas.
  - `Feedback` — encapsula vibración/tono (sin audio: los modelos objetivo no tienen altavoz).

---

## 6. Fases y entregables

### Fase 1 — Núcleo funcional (MVP)
- [ ] Lista de sesiones predefinidas y selección.
- [ ] Vista de ejercicio con serie/carga/reps y botón "serie hecha".
- [ ] Avance automático entre series y ejercicios.
- [ ] Descanso con cuenta regresiva + vibración al terminar.
- [ ] Pantalla "SESIÓN COMPLETA" con vibración + tono.
- **Entregable:** flujo completo de una sesión en el simulador.

### Fase 2 — Feedback y experiencia
- [ ] Patrones de tono/vibración diferenciados por evento.
- [ ] Layouts diferenciados para pantalla redonda (Venu) y rectangular (Venu Sq).
- [ ] Registro de cargas por serie y persistencia local del progreso.
- [ ] UI pulida y de alto contraste (colores, tipografías, layout táctil) para Venu y Venu Sq.
- **Entregable:** app usable y agradable en dispositivo real.

### Fase 3 — Personalización desde el móvil
- [ ] **App Settings v1:** elegir rutina + ajustes (descanso por defecto, unidades kg/lb, volumen de avisos).
- [ ] **App Settings v2:** definir rutina propia (ejercicios/series/cargas) serializada a JSON compacto → parseo en el reloj.
- [ ] Historial simple de sesiones completadas (fecha + duración).
- **Entregable:** el usuario arma y sincroniza sus propias sesiones desde el teléfono, sin tocar código.

### Fase 4 — Pruebas, pulido y publicación
- [ ] Pruebas en **simulador** para cada perfil de dispositivo.
- [ ] Pruebas en **hardware real** (Venu/Vivoactive).
- [ ] Optimización de memoria/batería.
- [ ] Iconos, capturas y descripción para la tienda.
- [ ] **Publicación en la Connect IQ Store** (o carga privada `.iq` para uso personal).

---

## 7. Pruebas

- **Simulador** por modelo (**Venu** y **Venu Sq**): verificar layouts redondo vs. rectangular.
- **Casos clave:** avanzar serie, saltar descanso, pausar/reanudar, completar sesión, salir a mitad y retomar.
- **Hardware real:** validar vibración/tono y consumo de batería en una sesión larga.

---

## 8. Publicación

- **Uso personal:** compilar `.iq` y cargarlo por USB/Garmin Express (no requiere revisión).
- **Público:** subir a la **Connect IQ Store** (revisión de Garmin: iconos, permisos, screenshots).
- Permisos a declarar en `manifest.xml`: los mínimos (probablemente ninguno de red en v1).

---

## 9. Riesgos y consideraciones

| Riesgo | Mitigación |
|---|---|
| Sin TTS ni altavoz (Venu/Venu Sq) | Avisos por tonos + vibración + pantalla grande |
| Dos formas de pantalla (redonda/rectangular) | Layouts por dispositivo; no asumir tamaño/centro fijos |
| Capacidades varían por modelo | Detección en runtime (`System.getDeviceSettings`) y `has :feature` |
| Memoria limitada del reloj | Datos compactos, cargar sesiones bajo demanda |
| Curva de Monkey C | Empezar por el MVP y ejemplos oficiales del SDK |

---

## 10. Próximos pasos inmediatos

1. Crear el repo dedicado **`app-gym-garmin-chile`** y migrar ahí este plan + el esqueleto.
2. Montar entorno (Fase 0) y proyecto base que compile en el simulador de **Venu** y **Venu Sq**.
3. Definir **1 sesión de ejemplo real** tuya (ejercicios, series, cargas, descansos) para probar el MVP.
4. Arrancar **Fase 1**.

---

_Documento de planificación. Ajustable a medida que avancemos._
