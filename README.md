# tingado93

Repositorio con configuración de Claude en la rama predeterminada revisada. No se identificó una aplicación ejecutable en esa rama.

## Empieza aquí

- [Mapa visual, arquitectura y recorrido de los datos](docs/MAPA.md).
- [Revisión documental y pendientes](docs/REVISION.md).

> Revisión documental: 26 de octubre de 2026. La presencia de código no acredita despliegue ni pruebas aprobadas. Esta revisión no cambia lógica, datos ni configuración operativa.

## Qué contiene realmente

```text
.claude/
└── settings.json
```

El archivo declara `ZeroZ-lab/cc-design` como fuente GitHub de un marketplace mediante `extraKnownMarketplaces`. **Declarar la fuente no demuestra que sus plugins o habilidades estén instalados, activos o revisados.**

## Cómo orientarse

- [Mapa de relaciones y límites](docs/MAPA.md).
- [Revisión y decisiones pendientes](docs/REVISION.md).
- [Configuración existente](.claude/settings.json).

La rama predeterminada observada es `claude/add-zeroZ-lab-skills-4nh8R`, no `main`. Se conserva ese nombre y no se altera la configuración. Esta descripción no cubre otras ramas ni el historial completo.

## Antes de activar componentes externos

Revisar el origen, permisos y contenido de los componentes. No añadir tokens, credenciales ni datos privados al repositorio público. Falta decidir si este espacio será una configuración personal, un catálogo o la base de otro proyecto; no se asume que sea un perfil de GitHub ni una aplicación.
