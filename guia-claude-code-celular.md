# Guía Completa: Cómo Usar Claude Code desde el Celular

> Trabaja en proyectos reales, crea aplicaciones y desarrolla código directamente desde tu smartphone.

---

## Tabla de Contenidos

1. [¿Qué es Claude Code y por qué usarlo desde el celular?](#1-qué-es-claude-code-y-por-qué-usarlo-desde-el-celular)
2. [Formas de acceder a Claude Code desde el celular](#2-formas-de-acceder-a-claude-code-desde-el-celular)
3. [Configuración inicial en el navegador móvil](#3-configuración-inicial-en-el-navegador-móvil)
4. [GitHub: La columna vertebral de tu flujo móvil](#4-github-la-columna-vertebral-de-tu-flujo-móvil)
5. [Conectar un repositorio de GitHub a Claude Code](#5-conectar-un-repositorio-de-github-a-claude-code)
6. [Trabajar en proyectos existentes](#6-trabajar-en-proyectos-existentes)
7. [Crear proyectos nuevos desde cero](#7-crear-proyectos-nuevos-desde-cero)
8. [Flujo de trabajo eficiente en pantalla pequeña](#8-flujo-de-trabajo-eficiente-en-pantalla-pequeña)
9. [Comandos y atajos esenciales](#9-comandos-y-atajos-esenciales)
10. [Integración con servidores MCP](#10-integración-con-servidores-mcp)
11. [Casos de uso prácticos desde el celular](#11-casos-de-uso-prácticos-desde-el-celular)
12. [Trucos para escribir código más rápido en móvil](#12-trucos-para-escribir-código-más-rápido-en-móvil)
13. [Limitaciones y cómo superarlas](#13-limitaciones-y-cómo-superarlas)
14. [Seguridad y buenas prácticas](#14-seguridad-y-buenas-prácticas)
15. [Preguntas frecuentes](#15-preguntas-frecuentes)

---

## 1. ¿Qué es Claude Code y por qué usarlo desde el celular?

Claude Code es el agente de programación de Anthropic que entiende lenguaje natural y puede:

- Leer, escribir y editar archivos de código
- Ejecutar comandos en una terminal
- Navegar repositorios completos de GitHub
- Crear aplicaciones enteras desde una descripción
- Hacer revisiones de código, depurar errores y refactorizar

**¿Por qué usarlo desde el celular?**

El celular ya no es solo un dispositivo de consumo. Con Claude Code en el navegador o a través de la app de Claude, puedes:

- Revisar y corregir código en cualquier lugar (transporte, sala de espera, viaje)
- Responder a una urgencia de producción sin necesidad de abrir el laptop
- Avanzar en un proyecto personal durante tiempos muertos
- Prototipar ideas rápidamente antes de olvidarlas
- Dar instrucciones en lenguaje natural sin necesidad de un teclado físico completo

La ventaja clave es que Claude Code corre en la nube, no en tu dispositivo, por lo que la potencia de cómputo no depende de tu celular.

---

## 2. Formas de acceder a Claude Code desde el celular

Hay varias rutas para usar Claude Code en móvil. Elige la que mejor se adapte a tu flujo:

### 2.1 Web App: claude.ai/code

La forma más directa. Abre el navegador de tu celular y ve a **https://claude.ai/code**.

- No requiere instalación
- Funciona en iOS (Safari) y Android (Chrome, Firefox, Samsung Internet)
- Acceso completo a todos los modelos
- Sesiones con entornos de ejecución en la nube

**Recomendado para:** la mayoría de casos de uso.

### 2.2 App Oficial de Claude (iOS / Android)

Descarga la app oficial de Claude desde la App Store o Google Play.

- Interfaz optimizada para móvil
- Sincronización de conversaciones entre dispositivos
- Algunas funcionalidades de Claude Code disponibles en la app
- Notificaciones cuando terminan tareas largas

**Recomendado para:** conversaciones frecuentes y consultas rápidas.

### 2.3 GitHub Codespaces + Claude Code CLI (avanzado)

Si necesitas la experiencia completa de terminal:

1. Abre GitHub desde el celular
2. En cualquier repositorio, presiona `.` (punto) para abrir Codespaces en el navegador
3. Dentro del terminal de Codespaces, instala Claude Code CLI: `npm install -g @anthropic-ai/claude-code`
4. Ejecuta `claude` en el terminal

**Recomendado para:** desarrolladores que necesitan acceso total a terminal y ejecución de pruebas.

### 2.4 SSH a tu propio servidor o Mac

Si tienes una máquina propia corriendo, puedes conectarte por SSH desde el celular usando apps como:

- **Termius** (iOS/Android) — la más recomendada, interfaz limpia
- **Blink Shell** (iOS) — potente, con soporte para mosh
- **JuiceSSH** (Android)

Una vez conectado por SSH, usas Claude Code CLI como si estuvieras en tu escritorio.

**Recomendado para:** usuarios avanzados con infraestructura propia.

---

## 3. Configuración inicial en el navegador móvil

### Paso 1: Preparar el navegador

En Android (Chrome recomendado):
- Ve a Configuración del sitio → activa "Pantalla completa" y "Agregar a pantalla de inicio" para tener acceso rápido como si fuera una app nativa

En iOS (Safari recomendado):
- Ve a **Compartir → Añadir a pantalla de inicio** para crear un ícono de acceso directo a claude.ai/code

### Paso 2: Iniciar sesión

1. Abre claude.ai en el navegador
2. Crea una cuenta o inicia sesión con Google/GitHub
3. Navega a la sección **Claude Code** desde el menú principal

### Paso 3: Configurar preferencias básicas

En la interfaz web de Claude Code puedes ajustar:

- **Modelo activo:** Sonnet (rápido y equilibrado) u Opus (más potente para tareas complejas)
- **Modo de permisos:** cuánta autonomía tiene Claude para ejecutar comandos y editar archivos
- **Tema:** claro u oscuro (importante para comodidad visual en pantalla pequeña)

### Paso 4: Familiarizarte con la interfaz móvil

La interfaz web de Claude Code tiene tres zonas principales:

```
┌─────────────────────────────┐
│  Barra superior: menú,      │
│  modelo activo, sesión      │
├─────────────────────────────┤
│                             │
│  Área de conversación:      │
│  aquí ves el código,        │
│  respuestas y progreso      │
│                             │
├─────────────────────────────┤
│  Input: escribes tus        │
│  instrucciones aquí         │
└─────────────────────────────┘
```

En pantalla pequeña, la barra superior puede colapsar. Usa gestos de deslizamiento para navegar entre paneles si la interfaz lo permite.

---

## 4. GitHub: La columna vertebral de tu flujo móvil

GitHub es donde vive tu código, y desde el celular es el puente entre Claude Code y tu trabajo real. Esta sección cubre todo lo que necesitas saber para operar GitHub desde el móvil en conjunto con Claude Code.

### 4.1 App oficial de GitHub Mobile

Descarga la app de **GitHub Mobile** (iOS / Android). Es el complemento ideal para Claude Code desde el celular:

- Ver y revisar Pull Requests
- Leer y responder Issues
- Navegar repositorios y archivos
- Aprobar o solicitar cambios en PRs
- Recibir notificaciones de CI/CD y revisiones

**Flujo típico combinado:**

```
Claude Code (web)          GitHub Mobile
       │                        │
       ├── Escribe el código     │
       ├── Hace commit           │
       ├── Crea el PR ──────────►│
       │                        ├── Revisas el diff
       │                        ├── Lees los comentarios
       │◄── Recibes comentarios ─┤
       ├── Corriges el código    │
       ├── Actualiza el PR ─────►│
       │                        ├── Apruebas y haces merge
```

### 4.2 Operaciones básicas de Git desde Claude Code

Cuando trabajas con Claude Code en el celular, puedes pedirle que maneje Git completamente por ti:

**Inicializar un repositorio:**
```
"Inicializa un repositorio Git en este proyecto,
 crea un .gitignore apropiado para Node.js y
 haz el primer commit."
```

**Ver el estado del repositorio:**
```
"Muéstrame el estado actual del repo: archivos modificados,
 sin seguimiento y en staging."
```

**Crear y cambiar de ramas:**
```
"Crea una rama llamada feature/autenticacion-oauth
 basada en main y cámbiате a ella."
```

**Hacer commits:**
```
"Haz commit de todos los cambios actuales con el mensaje:
 'feat: agrega login con Google usando OAuth 2.0'"
```

**Ver historial:**
```
"Muéstrame los últimos 10 commits con sus mensajes
 y archivos modificados."
```

**Push a remote:**
```
"Haz push de la rama actual al repositorio remoto en GitHub."
```

**Pull de cambios:**
```
"Trae los últimos cambios de la rama main desde GitHub."
```

**Ver diferencias:**
```
"Muéstrame qué cambios hay en src/auth/ comparado
 con la rama main."
```

### 4.3 Trabajar con Pull Requests desde móvil

Los Pull Requests son el corazón del trabajo colaborativo. Claude Code puede gestionarlos completamente:

**Crear un PR:**
```
"Crea un Pull Request desde la rama feature/nueva-api
 hacia main con el título 'Agrega API de notificaciones'
 y una descripción detallada de los cambios."
```

Claude generará un PR con:
- Título claro y descriptivo
- Descripción con resumen de cambios
- Lista de archivos modificados
- Instrucciones de prueba (si las incluyes en la instrucción)

**Revisar un PR existente:**
```
"Revisa el PR #47 del repositorio. Analiza:
 - Calidad del código
 - Posibles bugs
 - Problemas de seguridad
 - Si sigue las convenciones del proyecto"
```

**Responder a comentarios de revisión:**
```
"En el PR #47, el revisor señala que la función
 processPayment() no maneja el caso de timeout.
 Corrige eso y actualiza el PR."
```

**Hacer merge de un PR:**
```
"Haz merge del PR #47 usando squash merge."
```

### 4.4 Gestión de Issues desde el celular

Los issues son la forma de rastrear tareas, bugs y funcionalidades:

**Crear un issue:**
```
"Crea un issue en el repositorio reportando que
 la página de perfil de usuario da error 500 cuando
 el usuario no tiene foto de perfil. Incluye pasos
 para reproducirlo y el stack trace: [pega el error]"
```

**Consultar issues abiertos:**
```
"Lista todos los issues abiertos con etiqueta 'bug'
 ordenados por prioridad."
```

**Trabajar en un issue:**
```
"Toma el issue #23 (botón de eliminar no funciona
 en móvil) y corrígelo. Crea una rama para eso
 y abre un PR cuando esté listo."
```

**Cerrar un issue:**
```
"Cierra el issue #23 con el comentario 'Corregido
 en el PR #51, disponible desde la versión 2.3.1'"
```

### 4.5 GitHub Actions y CI/CD desde el celular

Puedes monitorear y gestionar tus flujos de CI/CD:

**Revisar el estado de los workflows:**
```
"¿Están pasando los tests en la rama main?
 Muéstrame el resultado del último workflow de CI."
```

**Diagnosticar fallos de CI:**
```
"El workflow de CI está fallando en el paso de tests.
 Muéstrame el log de error y dime qué está mal."
```

**Crear o modificar workflows:**
```
"Crea un GitHub Actions workflow que:
 - Corra en cada push a main y en PRs
 - Instale dependencias con npm ci
 - Ejecute los tests con npm test
 - Haga build con npm run build
 - Notifique a Slack si hay fallos"
```

**Re-ejecutar workflows fallidos:**
```
"El workflow falló por un error de red transitorio.
 Necesito que se vuelva a ejecutar."
```

### 4.6 GitHub Codespaces: Terminal completa desde el celular

Para cuando necesitas más poder que la interfaz web:

**Abrir Codespaces desde el celular:**
1. Ve al repositorio en GitHub Mobile o el navegador
2. Toca el botón verde **Code**
3. Selecciona la pestaña **Codespaces**
4. Crea un nuevo Codespace o abre uno existente
5. Se abre un VS Code completo en el navegador con terminal

**Instalar Claude Code CLI en Codespaces:**
```bash
npm install -g @anthropic-ai/claude-code
claude auth login
claude
```

Ahora tienes Claude Code CLI completo + acceso al repositorio + terminal + extensiones de VS Code, todo desde tu celular.

**Tip:** Los Codespaces guardan el estado. Si cierras el navegador, el Codespace sigue corriendo y puedes volver a él desde cualquier dispositivo.

### 4.7 Proteger ramas y configurar repositorios

Desde Claude Code puedes pedir que te ayude a configurar el repositorio de GitHub:

```
"Configura branch protection para main:
 - Requerir al menos 1 revisión aprobada antes de merge
 - Requerir que los checks de CI pasen
 - No permitir force push
 - No permitir eliminar la rama"
```

```
"Agrega estos secrets al repositorio:
 - DATABASE_URL
 - STRIPE_SECRET_KEY
 - SENDGRID_API_KEY
 (te diré los valores por separado de forma segura)"
```

### 4.8 Colaborar con equipos en GitHub

**Revisar el trabajo de un compañero:**
```
"Mi compañero Rodrigo creó el PR #38.
 Revísalo completamente y dame un resumen de
 qué hace y si tiene algún problema."
```

**Resolver conflictos de merge:**
```
"Hay conflictos de merge al intentar fusionar la
 rama feature/pagos con main. Los archivos en conflicto
 son: src/cart.js y src/checkout.js
 Resuelve los conflictos manteniendo los cambios de
 ambas ramas donde sea posible."
```

**Seguimiento de contribuciones:**
```
"Muéstrame cuántos commits y PRs ha hecho cada
 colaborador del repositorio en el último mes."
```

### 4.9 GitHub desde el celular: Atajos de teclado en la web

Cuando accedes a GitHub desde el navegador del celular, estos trucos te ahorran tiempo:

- Añade `?w=1` al final de la URL de un PR para ignorar cambios de espacios en blanco
- En la vista de un archivo, presiona el ícono de editar (lápiz) para editar directamente en GitHub
- En la URL de cualquier repo, cambia `github.com` por `github.dev` para abrir VS Code en el navegador
- Usa la búsqueda avanzada de GitHub: `repo:usuario/repo is:open is:pr label:bug`

### 4.10 Flujo completo desde cero con GitHub y Claude Code

Este es el flujo típico de crear un proyecto y subirlo a GitHub, todo desde el celular:

```
1. Crear el repositorio en GitHub
   → Claude Code: "Crea un nuevo repo público llamado
     'mi-app-clima' con README y .gitignore para Python"

2. Clonar y configurar localmente (en el entorno de la sesión)
   → Claude Code: "Clona el repositorio y configura
     el entorno de desarrollo"

3. Desarrollar el proyecto
   → Claude Code: "Crea una app de clima en Python con Flask..."

4. Hacer commits progresivos
   → Claude Code: "Haz commit del módulo de API con mensaje
     'feat: integra OpenWeatherMap API'"

5. Crear ramas para features
   → Claude Code: "Crea la rama feature/historial-busquedas"

6. Abrir PRs para cada feature
   → Claude Code: "Abre un PR para fusionar
     feature/historial-busquedas en main"

7. Revisar y hacer merge desde GitHub Mobile
   → Tú revisas el diff en la app de GitHub
   → Apruebas y haces merge

8. Hacer deploy (si tienes integración configurada)
   → GitHub Actions corre automáticamente
   → Tu app se despliega en el servidor
```

---

## 5. Conectar un repositorio de GitHub a Claude Code

Esta es una de las funciones más potentes: Claude Code puede clonar y trabajar directamente en tus repositorios.

### Desde la interfaz web (claude.ai/code)

1. Abre una nueva sesión en Claude Code
2. Escribe algo como:

   > "Conecta el repositorio GitHub `mi-usuario/mi-proyecto` y ayúdame a trabajar en él"

3. Claude te pedirá que autorices el acceso a GitHub mediante OAuth
4. Una vez autorizado, el repositorio queda disponible en el entorno de la sesión

### Desde GitHub directamente (botón de Claude)

Anthropic ha integrado Claude Code en GitHub. En algunos repositorios verás un botón para "Open with Claude Code". Al presionarlo desde el celular:

1. Se abre claude.ai/code con el repositorio ya conectado
2. El entorno se inicializa automáticamente (dependencias, configuración)
3. Puedes empezar a hacer preguntas sobre el código de inmediato

### Desde un issue o PR de GitHub

Una de las formas más útiles desde el celular:

1. Estás viendo un issue en GitHub desde tu celular
2. En los comentarios, menciona `@claude` seguido de tu instrucción
3. Claude Code responderá al issue y, si tiene permisos, puede crear una rama y un PR con la solución

### Autorización de permisos en GitHub

Para que Claude Code pueda interactuar con GitHub (leer repos, crear PRs, push de código), necesita permisos OAuth. Al conectar por primera vez:

1. Claude te redirige a GitHub para autorizar
2. Selecciona los repositorios a los que quieres dar acceso (puedes limitarlo a repos específicos)
3. Aprueba los permisos necesarios
4. Quedas conectado para todas las sesiones futuras

**Permisos típicos que Claude Code necesita:**
- `repo` — leer y escribir en repositorios
- `workflow` — modificar GitHub Actions
- `read:org` — leer información de la organización (si usas repos de equipo)

---

## 6. Trabajar en proyectos existentes

Una vez conectado un repositorio, estas son las tareas más comunes que puedes delegar a Claude Code:

### Explorar el código

```
"Explícame la estructura general de este proyecto"
"¿Qué hace el archivo src/auth/middleware.js?"
"¿Dónde se maneja el login de usuarios?"
"¿Cuáles son los endpoints de la API?"
```

### Corregir un bug

```
"Tengo este error en producción: [pega el stack trace]
 Encuentra la causa y corrígela"
```

```
"La función calcularTotal() en src/utils/cart.js no está
 sumando correctamente los descuentos. Revísala y arréglala."
```

### Agregar una funcionalidad

```
"Agrega validación de email al formulario de registro
 en components/RegisterForm.tsx. Usa regex y muestra
 el error debajo del campo."
```

```
"Crea un endpoint POST /api/products que reciba nombre,
 precio y stock, valide los campos y lo guarde en la
 base de datos MongoDB existente."
```

### Refactorizar código

```
"El archivo controllers/userController.js tiene más de
 500 líneas. Divídelo en módulos más pequeños manteniendo
 la misma funcionalidad."
```

### Escribir pruebas

```
"Escribe pruebas unitarias con Jest para las funciones
 en src/utils/validators.js. Incluye casos borde."
```

### Revisar un Pull Request

```
"Revisa los cambios en el PR #42. Dime si hay problemas
 de seguridad, rendimiento o calidad de código."
```

---

## 7. Crear proyectos nuevos desde cero

Desde el celular puedes describir lo que quieres construir en lenguaje natural y Claude Code lo crea completo.

### Ejemplo 1: API REST con Node.js

```
Crea una API REST con Node.js y Express para gestionar
una lista de tareas (to-do list). Necesito:

- CRUD completo (crear, leer, actualizar, eliminar tareas)
- Base de datos SQLite para persistencia
- Validación de datos con Zod
- Autenticación con JWT
- Tests con Jest
- Dockerfile incluido
```

Claude Code creará todos los archivos, instalará dependencias y te explicará cómo ejecutarlo.

### Ejemplo 2: App web con React

```
Crea una aplicación React de clima que:
- Muestre el clima actual de una ciudad buscada
- Use la API de OpenWeatherMap (te daré el API key)
- Tenga diseño responsivo con Tailwind CSS
- Muestre pronóstico de 5 días
- Guarde las últimas 5 búsquedas en localStorage
```

### Ejemplo 3: Script de automatización

```
Crea un script de Python que:
- Lea todos los archivos CSV de una carpeta
- Combine los datos en un solo DataFrame con pandas
- Genere un reporte en Excel con gráficas de ventas por mes
- Envíe el reporte por email usando smtplib
```

### Ejemplo 4: Bot de Telegram

```
Crea un bot de Telegram en Python que:
- Responda /start con un mensaje de bienvenida
- Tenga comando /clima [ciudad] que llame a una API de clima
- Tenga comando /cambio [monto] [moneda] para conversión de divisas
- Guarde historial de conversaciones en SQLite
```

### Flujo recomendado para crear proyectos desde cero

1. **Describe el proyecto completo** en un solo mensaje detallado
2. **Especifica el stack tecnológico** que prefieres (o pide una recomendación)
3. **Indica restricciones**: presupuesto de API, hosting objetivo, lenguaje
4. **Pide que cree primero la estructura** y confirma antes de que escriba todo el código
5. **Revisa y ajusta** pidiendo cambios específicos
6. **Pide que haga commit y push** al repositorio cuando estés satisfecho

---

## 8. Flujo de trabajo eficiente en pantalla pequeña

Trabajar en un celular tiene sus retos. Aquí estrategias para ser más productivo:

### Usa instrucciones largas y detalladas

En un teclado físico, los devs suelen escribir instrucciones cortas e iterar. En el celular, escribe instrucciones más completas desde el inicio para reducir el número de mensajes:

**Poco eficiente:**
```
"Arregla el bug del login"
```

**Más eficiente:**
```
"En el archivo src/auth/login.js, la función handleLogin()
no está manejando el caso cuando el servidor devuelve 401.
Actualmente solo maneja 200 y errores de red. Agrega manejo
para 401 (credenciales incorrectas), 403 (cuenta bloqueada)
y 429 (demasiados intentos). Muestra mensajes de error
apropiados al usuario en cada caso."
```

### Aprovecha el dictado de voz

Tanto en iOS como en Android, el teclado tiene un ícono de micrófono. Úsalo para dictar instrucciones largas sin escribir:

- Activa dictado con el ícono del micrófono en el teclado
- Habla claramente describiendo lo que quieres
- Revisa el texto antes de enviar y corrige errores del reconocimiento

**Tip:** el dictado funciona especialmente bien para descripciones de funcionalidades y preguntas. Para código específico, mejor escribe manualmente.

### Divide las tareas en sesiones

No intentes completar un proyecto entero en una sola sesión móvil. En cambio:

- Sesión 1 (en transporte): describe el proyecto y crea la estructura base
- Sesión 2 (en pausa): implementa el módulo de autenticación
- Sesión 3 (en casa o trabajo): revisa, prueba y corrige

Cada sesión queda guardada en GitHub (si hiciste commits), así no pierdes trabajo.

### Usa el modo horizontal

Rota el celular para tener más espacio horizontal al leer código. La mayoría de interfaces de Claude Code responden bien al modo landscape.

### Configura atajos de texto en tu celular

Tanto iOS como Android permiten crear atajos de teclado (reemplazos de texto). Crea atajos para frases que usas frecuentemente:

| Atajo | Se expande a |
|-------|-------------|
| `;crea` | `Crea una función que` |
| `;test` | `Escribe pruebas unitarias para` |
| `;bug` | `Encuentra y corrige el bug en` |
| `;api` | `Crea un endpoint que` |
| `;rev` | `Revisa este código y sugiere mejoras:` |

### Usa el modo oscuro siempre

En pantallas pequeñas usadas en muchos contextos (al aire libre, en la cama, transporte), el modo oscuro reduce la fatiga visual significativamente.

---

## 9. Comandos y atajos esenciales

Claude Code tiene comandos especiales que puedes escribir directamente en el chat:

### Comandos slash (slash commands)

| Comando | Qué hace |
|---------|----------|
| `/help` | Muestra ayuda y comandos disponibles |
| `/clear` | Limpia el contexto de la conversación actual |
| `/config` | Abre configuración (modelo, tema, permisos) |
| `/compact` | Comprime el historial para ahorrar contexto |
| `/review` | Inicia una revisión del código actual |
| `/init` | Inicializa un CLAUDE.md con documentación del proyecto |

### Cómo usar los comandos desde móvil

1. Escribe `/` al inicio del mensaje
2. Aparecerá un menú de autocompletado con los comandos disponibles
3. Toca el comando que quieras o sigue escribiendo para filtrar

### Menciones con @

En algunos contextos puedes mencionar archivos o herramientas:

```
"@src/components/Button.tsx refactoriza este componente para
 usar TypeScript estricto"
```

---

## 10. Integración con servidores MCP

MCP (Model Context Protocol) permite a Claude Code conectarse con servicios externos. Desde tu sesión móvil puedes tener Claude Code interactuando con:

### Servicios disponibles (según tu configuración)

- **GitHub:** leer/crear issues, PRs, branches, commits
- **Notion:** leer y crear páginas, bases de datos
- **Google Drive:** acceder y modificar documentos
- **Gmail/Outlook:** leer emails (para contexto) y crear borradores
- **Google Calendar:** consultar disponibilidad
- **Slack:** buscar mensajes, publicar en canales
- **Figma:** leer diseños y exportar assets
- **Bases de datos:** conectar con Postgres, MySQL, SQLite

### Ejemplo de uso desde celular

```
"Busca en mis emails de esta semana alguno que mencione
 el error de la API de pagos, y luego busca en el código
 del repositorio dónde podría estar ese problema."
```

```
"Lee el documento de Notion 'Requisitos del sprint 3'
 y crea las tareas correspondientes como issues en GitHub."
```

```
"Revisa el diseño en Figma del componente de checkout
 y actualiza el CSS en src/styles/checkout.css para que
 coincida con el diseño."
```

---

## 11. Casos de uso prácticos desde el celular

### Caso 1: Urgencia de producción en el camino

Escenario: recibes una alerta a las 8 AM, hay un error 500 en producción y estás en el transporte.

1. Abre claude.ai/code desde el celular
2. Conecta el repositorio de producción
3. Pega el stack trace del error
4. Pide a Claude que lo diagnostique y proponga una solución
5. Revisa el código de la corrección en el chat
6. Pide que haga commit y push a una rama de hotfix
7. Aprueba el PR desde GitHub mobile cuando llegues a donde puedas revisar mejor

### Caso 2: Desarrollar una idea en el momento

Escenario: se te ocurre una funcionalidad mientras esperas en una fila.

1. Abre Claude Code y describe la idea detalladamente por voz
2. Pide que evalúe la viabilidad y sugiera la implementación
3. Si quieres avanzar, pide que cree la estructura de archivos
4. Haz commit de lo que existe para no perder el trabajo
5. Continúas en el escritorio cuando tengas tiempo

### Caso 3: Aprender mientras commutes

Escenario: quieres entender un proyecto open source en el camino al trabajo.

1. Conecta el repositorio que quieres entender
2. Pide explicaciones progresivas: primero arquitectura general, luego módulos específicos
3. Haz preguntas sobre partes que no entiendes
4. Pide ejemplos de cómo extender el proyecto
5. Toma notas en Notion o en un README personal (Claude puede escribirlas por ti)

### Caso 4: Code review desde el celular

Escenario: un compañero pide revisión de un PR y tú no estás en tu escritorio.

1. Pide a Claude que lea el PR de GitHub
2. Claude analiza los cambios y reporta:
   - Problemas de seguridad
   - Posibles bugs
   - Violaciones de estilo o convenciones del proyecto
   - Sugerencias de mejora
3. Aprueba o pide cambios desde GitHub mobile con la información de Claude

### Caso 5: Crear contenido técnico

Escenario: necesitas escribir documentación, un tutorial o un artículo técnico.

1. Pide a Claude que lea el código que quieres documentar
2. Genera la documentación en formato Markdown
3. La documentación puede commitearse directo al repo o publicarse en Notion

---

## 12. Trucos para escribir código más rápido en móvil

### Truco 1: Pega contexto generoso

Cuando reportas un bug o pides ayuda, incluye todo el contexto relevante en un solo mensaje:

```
Archivo: src/api/users.js, línea 47

Error que recibo:
TypeError: Cannot read property 'email' of undefined

Stack trace:
  at getUserEmail (users.js:47)
  at router.get (/api/users/:id, users.js:23)

Código actual de la función:
[código aquí]

Comportamiento esperado: devolver el email del usuario
cuando el ID existe en la base de datos.
```

### Truco 2: Usa emojis para indicar urgencia o tipo

Algunos usuarios establecen una convención personal:

- 🔴 Bug crítico de producción
- 🟡 Bug no urgente
- 🟢 Nueva funcionalidad
- 📝 Documentación
- 🧪 Tests
- ♻️ Refactoring

### Truco 3: Guarda respuestas frecuentes como plantillas

Guarda en las notas de tu celular fragmentos de instrucciones que usas frecuentemente para copiar y pegar.

### Truco 4: Aprovecha el contexto de sesión

Claude Code recuerda todo lo que se ha dicho en la sesión. No necesitas repetir contexto:

```
Mensaje 1: "Estoy trabajando en una app de e-commerce con Node.js,
             Express, MongoDB y Stripe para pagos."

Mensaje 2 (después): "Agrega webhooks de Stripe"
                     (Claude ya sabe el contexto del proyecto)
```

### Truco 5: Pide revisión incremental

En lugar de pedir todo de una vez, itera:

```
"Crea primero solo la estructura de carpetas del proyecto,
 sin código aún. Quiero verla antes de continuar."

(revisas y apruebas)

"Ahora crea el archivo de configuración principal y el
 punto de entrada de la app."

(revisas y apruebas)

"Ahora implementa el módulo de autenticación."
```

### Truco 6: Pide explicaciones en español

Si el código o la documentación está en inglés pero prefieres entender en español:

```
"Explícame en español qué hace esta función y por qué
 podría estar fallando."
```

---

## 13. Limitaciones y cómo superarlas

### Limitación 1: Pantalla pequeña para leer código

**Problema:** leer bloques grandes de código en pantalla de 6" es difícil.

**Soluciones:**
- Pide a Claude que explique el código en texto, no que lo muestre completo
- Usa el modo horizontal del celular
- Pide fragmentos específicos: "muéstrame solo la función X"
- En sesiones importantes, usa un iPad o tablet si está disponible

### Limitación 2: Teclado virtual lento para escribir código

**Problema:** escribir símbolos como `{`, `[`, `=>`, `;` es tedioso en teclado virtual.

**Soluciones:**
- Usa dictado de voz para las instrucciones (no para código)
- Instala un teclado con fila de símbolos de programación:
  - **Coduo** o **Codeboard** (Android)
  - **Keewordz** o teclados con extensión de símbolos (iOS)
- Pide a Claude que escriba el código; tú solo das instrucciones

### Limitación 3: Sesiones que expiran

**Problema:** si cierras el navegador o la app, la sesión puede terminar.

**Soluciones:**
- Haz commit del trabajo frecuentemente: "haz commit de lo que tenemos hasta ahora"
- Usa la opción "Añadir a pantalla de inicio" para que el navegador no suspenda la pestaña
- En iOS, activa "Evitar suspensión de pantalla" mientras trabajas
- Usa la app oficial de Claude que mantiene mejor el estado entre sesiones

### Limitación 4: Sin acceso a terminal completa

**Problema:** en la interfaz web no puedes ejecutar comandos arbitrarios como en CLI.

**Soluciones:**
- Claude Code tiene acceso a terminal dentro del entorno de la sesión
- Pide a Claude que ejecute los comandos: "ejecuta npm test y muéstrame el resultado"
- Para terminal completa, usa GitHub Codespaces (ver sección 2.3)

### Limitación 5: Archivos binarios y assets

**Problema:** no puedes subir imágenes, PDFs u otros archivos fácilmente desde móvil.

**Soluciones:**
- Para imágenes de diseño: usa URLs públicas (Figma, Imgur, etc.)
- Para documentos: pégalos en texto plano o usa la integración con Google Drive/Notion
- Para archivos de datos: sube primero a GitHub y luego referencia el path

### Limitación 6: Revisión de interfaces visuales

**Problema:** es difícil verificar que un componente de UI se ve bien sin un navegador de escritorio.

**Solución:**
- Pide a Claude que cree una versión de preview simple del componente
- Usa el navegador del celular para abrir previews desplegados en Vercel/Netlify
- Confía en Claude para validar responsive design, pero prueba tú en el dispositivo cuando puedas

---

## 14. Seguridad y buenas prácticas

### No expongas credenciales en el chat

**Nunca escribas** en el chat de Claude Code:
- Contraseñas
- API keys
- Tokens de acceso
- Strings de conexión a bases de datos con credenciales reales

En cambio, usa:
```
"El API key estará en la variable de entorno STRIPE_SECRET_KEY"
"Usa el string de conexión de DATABASE_URL del archivo .env"
```

Claude Code sabe cómo manejar variables de entorno correctamente.

### Revisa el código antes de hacer merge a producción

Aunque Claude Code es muy capaz, siempre revisa:
- Los cambios que toca en archivos de configuración críticos
- Modificaciones a lógica de autenticación o pagos
- Migraciones de base de datos
- Cambios en infraestructura (Docker, CI/CD)

### Usa ramas para experimentos

Pide a Claude que trabaje siempre en una rama separada:
```
"Crea una rama llamada feature/nuevo-login y trabaja
 todo en esa rama. No toques main."
```

### Revisa los permisos que das a Claude Code

En la configuración de Claude Code puedes ajustar qué puede hacer sin pedirte confirmación:
- **Modo conservador:** Claude pide permiso para cada acción (recomendado en móvil)
- **Modo normal:** Claude puede ejecutar acciones típicas sin confirmar
- **Modo automático:** Claude opera con máxima autonomía (solo para tareas muy confiadas)

Desde el celular, el modo conservador o normal es el más adecuado para mantener control.

### Sesiones en redes públicas

Si usas WiFi público (cafetería, aeropuerto, transporte):
- Activa una VPN antes de conectarte
- No trabajes con código que contenga datos sensibles de clientes
- Cierra la sesión de Claude Code cuando termines

---

## 15. Preguntas frecuentes

**¿Puedo usar Claude Code completamente gratis desde el celular?**

Claude ofrece un plan gratuito con límites de uso. Para uso intensivo en proyectos reales, un plan de pago (Pro o Team) es recomendable. Revisa los precios actuales en claude.ai.

**¿Claude Code guarda mi código? ¿Es seguro?**

Anthropic tiene políticas de privacidad claras. El código que compartes en sesiones se procesa para generar respuestas. Revisa la política de privacidad en anthropic.com/privacy para entender cómo se maneja tu información.

**¿Funciona Claude Code offline en el celular?**

No. Claude Code requiere conexión a internet ya que el procesamiento ocurre en los servidores de Anthropic.

**¿Puedo trabajar en varios proyectos al mismo tiempo?**

Sí, puedes tener múltiples pestañas o sesiones abiertas. Cada sesión es independiente y puede estar conectada a un repositorio diferente.

**¿Claude Code puede deployar mi aplicación automáticamente?**

Con las integraciones correctas (MCP servers de Vercel, AWS, etc.) puede triggear deployments. Sin esas integraciones, puede preparar todo para que tú ejecutes el deploy manualmente.

**¿Qué pasa si la sesión se pierde antes de hacer commit?**

Si Claude editó archivos en el entorno de la sesión y no se hizo commit, esos cambios pueden perderse. Por eso es importante pedir commits frecuentes. Sin embargo, el historial del chat sigue disponible para recuperar el código que Claude generó.

**¿Puedo usar Claude Code para aprender a programar desde el celular?**

Absolutamente. Es una excelente herramienta para aprender: pide explicaciones, pide que muestre ejemplos paso a paso, pide que corrija tus ejercicios y explique los errores. Puedes aprender un lenguaje nuevo completamente desde el celular.

**¿Claude Code habla español?**

Sí. Puedes escribir todas tus instrucciones en español y Claude Code responderá en español. El código que genera seguirá convenciones estándar de programación (inglés para variables y funciones es la norma), pero las explicaciones serán en el idioma que uses.

**¿Funciona mejor en iOS o en Android?**

Ambas plataformas funcionan bien. En iOS, Safari tiene mejor integración con el sistema y mejor gestión de memoria en pestañas largas. En Android, Chrome ofrece mejor rendimiento de JavaScript en la interfaz web.

---

## Referencia rápida: Frases útiles para el celular

Copia estas frases a tus notas para tenerlas a mano:

```
📁 EXPLORAR
"Explícame la estructura general del proyecto"
"¿Dónde está implementada la lógica de [X]?"
"Lista todos los archivos que tocan la base de datos"

🐛 BUGS
"Tengo este error: [error]. Encuentra la causa y corrígela."
"La función [nombre] no hace [comportamiento esperado]. Revísala."

✨ FUNCIONALIDADES
"Agrega [funcionalidad] a [archivo/componente]"
"Crea un endpoint que [descripción]"
"Implementa [feature] siguiendo el patrón de [otro archivo similar]"

🧹 CALIDAD
"Refactoriza [archivo] sin cambiar su comportamiento"
"Agrega tipos TypeScript a [archivo]"
"Escribe tests para [función/módulo]"

💾 GIT
"Haz commit de los cambios con mensaje '[mensaje]'"
"Crea una rama [nombre] y trabaja en ella"
"Muestra un resumen de los cambios hechos en esta sesión"

📖 DOCUMENTACIÓN
"Documenta este código en español"
"Crea un README para este proyecto"
"Explícame este código como si supiera [nivel] de programación"
```

---

*Guía creada para Claude Code — claude.ai/code*
*Actualizada: Mayo 2026*
