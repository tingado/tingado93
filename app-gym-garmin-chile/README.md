# App Gym Garmin Chile

App **Connect IQ** (Monkey C) para guiar sesiones de entrenamiento de gimnasio en el reloj:
elige una sesión, sigue **series** y **cargas**, respeta las **pausas** con cuenta regresiva y
recibe un aviso claro cuando la **sesión está completa**.

> Dispositivos objetivo: **Garmin Venu (gen 1)** y **Venu Sq**.
> Estos modelos **no tienen altavoz**, así que los avisos son **vibración + tono + pantalla**.

## Estado

Esqueleto funcional (Fase 0 + inicio de Fase 1 del [plan de trabajo](../PLAN.md)):
flujo completo **Menú → Ejercicio → Descanso → Sesión completa** con una rutina de ejemplo.

## Estructura

```
manifest.xml            # productos (venu, venusq, venusqm), id de app, permisos
monkey.jungle           # config de build
resources/
  drawables/            # ícono de launcher
  strings/              # textos (es/en)
  settings/             # App Settings + valores por defecto (properties)
source/
  GymApp.mc             # entry point; arma el menú de sesiones
  model/
    Session.mc          # Session / Exercise / ExerciseSet
    SampleData.mc       # rutinas de ejemplo (se reemplazan por config del móvil en Fase 3)
  SessionManager.mc     # estado de la sesión en curso
  Feedback.mc           # vibración + tono por evento
  views/
    SessionMenuDelegate.mc
    ExerciseView.mc / ExerciseDelegate.mc
    RestView.mc / RestDelegate.mc
    CompleteView.mc / CompleteDelegate.mc
```

## Cómo compilar y probar

Requiere el **Connect IQ SDK** y la extensión **Monkey C** de VS Code.

1. Instala el SDK con el **SDK Manager** y descarga los device profiles de **venu** y **venusq**.
2. Abre esta carpeta en VS Code.
3. `Ctrl/Cmd+Shift+P` → **Monkey C: Build for Device** o **Run** en el simulador.
4. En el simulador prueba con **Venu** (redondo) y **Venu Sq** (rectangular).

Compilación por línea de comandos (ejemplo):

```
monkeyc -d venu -f monkey.jungle -o bin/gym.prg -y developer_key
connectiq        # abre el simulador
monkeydo bin/gym.prg venu
```

## Interacción

- **Toque en pantalla** o **botón START** → "serie hecha".
- Tras cada serie: **descanso** con cuenta regresiva (toca para saltar).
- Última serie → **SESIÓN COMPLETA** (vibración larga + tono + pantalla verde).

## Próximo (según PLAN.md)

- Ajuste rápido de carga en el reloj (±2.5 kg) cuando haga falta.
- Layouts afinados por dispositivo (redondo vs. rectangular).
- Rutinas propias definidas desde el móvil vía **App Settings** (Fase 3).
