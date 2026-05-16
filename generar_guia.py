from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

# ── Paleta de colores ──────────────────────────────────────────────────────────
C_PRIMARY   = RGBColor(0x1A, 0x1A, 0x2E)   # azul oscuro casi negro
C_ACCENT    = RGBColor(0xE9, 0x4F, 0x37)   # rojo-naranja vibrante
C_ACCENT2   = RGBColor(0x39, 0x3E, 0x46)   # gris pizarra
C_LIGHT_BG  = RGBColor(0xF5, 0xF5, 0xF5)   # fondo gris clarísimo
C_CODE_BG   = RGBColor(0x1E, 0x1E, 0x2E)   # fondo dark code
C_CODE_TEXT = RGBColor(0xCB, 0xD2, 0xEA)   # texto código
C_WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
C_YELLOW    = RGBColor(0xFF, 0xD1, 0x66)
C_GREEN     = RGBColor(0x3D, 0xDC, 0x97)
C_BLUE_MID  = RGBColor(0x16, 0x97, 0xA0)
C_LIGHT_ACC = RGBColor(0xFF, 0xEE, 0xEB)   # fondo suave acento

# ── Helpers XML ───────────────────────────────────────────────────────────────
def shade_cell(cell, color: RGBColor):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd  = OxmlElement('w:shd')
    hex_ = f'{color[0]:02X}{color[1]:02X}{color[2]:02X}'
    shd.set(qn('w:val'),   'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'),  hex_)
    tcPr.append(shd)

def set_cell_border(cell, **kwargs):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        tag = OxmlElement(f'w:{edge}')
        tag.set(qn('w:val'),   kwargs.get('val',   'single'))
        tag.set(qn('w:sz'),    kwargs.get('sz',    '4'))
        tag.set(qn('w:space'), kwargs.get('space', '0'))
        tag.set(qn('w:color'), kwargs.get('color', 'FFFFFF'))
        tcBorders.append(tag)
    tcPr.append(tcBorders)

def set_run_color(run, color: RGBColor):
    run.font.color.rgb = color

def para_space(para, before=0, after=0, line=None):
    pf = para.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after  = Pt(after)
    if line:
        pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY
        pf.line_spacing       = Pt(line)

def page_break(doc):
    para = doc.add_paragraph()
    run  = para.add_run()
    run.add_break(docx_mod.enum.text.WD_BREAK.PAGE)   # fallback — usamos XML
    # mejor con XML:
    p   = para._p
    r   = OxmlElement('w:r')
    br  = OxmlElement('w:br')
    br.set(qn('w:type'), 'page')
    r.append(br)
    p.append(r)

# ── Estilos base ──────────────────────────────────────────────────────────────
def set_doc_styles(doc):
    style = doc.styles['Normal']
    style.font.name  = 'Calibri'
    style.font.size  = Pt(10.5)
    style.font.color.rgb = C_PRIMARY

# ── Portada ───────────────────────────────────────────────────────────────────
def add_cover(doc):
    # bloque de color primario simulado con tabla 1×1
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.rows[0].cells[0]
    shade_cell(cell, C_PRIMARY)
    cell.width = Inches(6.5)

    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para_space(p, before=40, after=10)

    # ícono/emoji texto grande
    r = p.add_run('📱')
    r.font.size = Pt(52)

    p2 = cell.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para_space(p2, before=4, after=4)
    r2 = p2.add_run('CLAUDE CODE')
    r2.font.name  = 'Calibri'
    r2.font.size  = Pt(32)
    r2.font.bold  = True
    set_run_color(r2, C_ACCENT)

    p3 = cell.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para_space(p3, before=0, after=6)
    r3 = p3.add_run('DESDE EL CELULAR')
    r3.font.name  = 'Calibri'
    r3.font.size  = Pt(18)
    r3.font.bold  = True
    set_run_color(r3, C_WHITE)

    p4 = cell.add_paragraph()
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para_space(p4, before=6, after=6)
    r4 = p4.add_run('Guía completa: proyectos, GitHub, agentes y comandos')
    r4.font.name  = 'Calibri'
    r4.font.size  = Pt(11)
    r4.font.italic = True
    set_run_color(r4, RGBColor(0xB0, 0xB8, 0xC8))

    p5 = cell.add_paragraph()
    p5.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para_space(p5, before=20, after=30)
    r5 = p5.add_run('Mayo 2026')
    r5.font.name = 'Calibri'
    r5.font.size = Pt(10)
    set_run_color(r5, RGBColor(0x88, 0x99, 0xAA))

    doc.add_paragraph()   # separador

# ── Encabezado de sección (H1) ─────────────────────────────────────────────────
def section_header(doc, number, title, icon=''):
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    tbl.allow_autofit = False

    # columna número
    c0 = tbl.rows[0].cells[0]
    c0.width = Inches(0.5)
    shade_cell(c0, C_ACCENT)
    set_cell_border(c0, val='none', sz='0', color='FFFFFF')
    p0 = c0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para_space(p0, before=4, after=4)
    r0 = p0.add_run(str(number))
    r0.font.name = 'Calibri'
    r0.font.size = Pt(16)
    r0.font.bold = True
    set_run_color(r0, C_WHITE)

    # columna título
    c1 = tbl.rows[0].cells[1]
    c1.width = Inches(6.0)
    shade_cell(c1, C_PRIMARY)
    set_cell_border(c1, val='none', sz='0', color='FFFFFF')
    p1 = c1.paragraphs[0]
    para_space(p1, before=4, after=4)
    p1.paragraph_format.left_indent = Inches(0.15)
    r1 = p1.add_run(f'{icon}  {title}' if icon else title)
    r1.font.name = 'Calibri'
    r1.font.size = Pt(14)
    r1.font.bold = True
    set_run_color(r1, C_WHITE)

    doc.add_paragraph()

# ── Subtítulo H2 ──────────────────────────────────────────────────────────────
def subsection(doc, title, icon=''):
    p = doc.add_paragraph()
    para_space(p, before=10, after=3)
    p.paragraph_format.left_indent = Inches(0)
    run = p.add_run(f'{icon}  {title}' if icon else title)
    run.font.name  = 'Calibri'
    run.font.size  = Pt(12)
    run.font.bold  = True
    set_run_color(run, C_ACCENT)

    # línea subrayado via borde inferior del párrafo
    pPr   = p._p.get_or_add_pPr()
    pBdr  = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'),   'single')
    bottom.set(qn('w:sz'),    '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), f'{C_ACCENT[0]:02X}{C_ACCENT[1]:02X}{C_ACCENT[2]:02X}')
    pBdr.append(bottom)
    pPr.append(pBdr)

# ── Subtítulo H3 ──────────────────────────────────────────────────────────────
def h3(doc, title):
    p = doc.add_paragraph()
    para_space(p, before=8, after=2)
    r = p.add_run(title)
    r.font.name = 'Calibri'
    r.font.size = Pt(11)
    r.font.bold = True
    set_run_color(r, C_ACCENT2)

# ── Cuerpo de texto ───────────────────────────────────────────────────────────
def body(doc, text, indent=0):
    p = doc.add_paragraph()
    para_space(p, before=2, after=4)
    p.paragraph_format.left_indent = Inches(indent)
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(10.5)
    set_run_color(r, C_PRIMARY)
    return p

# ── Bullet point ──────────────────────────────────────────────────────────────
def bullet(doc, text, bold_prefix='', indent=0.2):
    p = doc.add_paragraph(style='List Bullet')
    para_space(p, before=1, after=1)
    p.paragraph_format.left_indent  = Inches(indent)
    p.paragraph_format.first_line_indent = Inches(-0.18)
    if bold_prefix:
        rb = p.add_run(bold_prefix + ' ')
        rb.font.name  = 'Calibri'
        rb.font.size  = Pt(10.5)
        rb.font.bold  = True
        set_run_color(rb, C_ACCENT2)
    r = p.add_run(text)
    r.font.name = 'Calibri'
    r.font.size = Pt(10.5)
    set_run_color(r, C_PRIMARY)

# ── Bloque de código ──────────────────────────────────────────────────────────
def code_block(doc, code_text, label=''):
    if label:
        pl = doc.add_paragraph()
        para_space(pl, before=6, after=0)
        pl.paragraph_format.left_indent = Inches(0.15)
        rl = pl.add_run(f'  {label}')
        rl.font.name  = 'Consolas'
        rl.font.size  = Pt(8)
        rl.font.bold  = True
        set_run_color(rl, C_ACCENT)

    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    cell = tbl.rows[0].cells[0]
    shade_cell(cell, C_CODE_BG)
    set_cell_border(cell,
        val='single', sz='4',
        color=f'{C_ACCENT[0]:02X}{C_ACCENT[1]:02X}{C_ACCENT[2]:02X}')

    lines = code_text.strip().split('\n')
    for i, line in enumerate(lines):
        if i == 0:
            p = cell.paragraphs[0]
        else:
            p = cell.add_paragraph()
        para_space(p, before=1, after=1)
        p.paragraph_format.left_indent = Inches(0.15)
        r = p.add_run(line if line else ' ')
        r.font.name = 'Consolas'
        r.font.size = Pt(9)
        set_run_color(r, C_CODE_TEXT)

    doc.add_paragraph()

# ── Caja de consejo / tip ─────────────────────────────────────────────────────
def tip_box(doc, title, text, color=None):
    bg = color or C_LIGHT_ACC
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    tbl.allow_autofit = False

    # franja izquierda
    c0 = tbl.rows[0].cells[0]
    c0.width = Inches(0.08)
    shade_cell(c0, C_ACCENT)
    set_cell_border(c0, val='none', sz='0', color='FFFFFF')
    c0.paragraphs[0].add_run(' ')

    # contenido
    c1 = tbl.rows[0].cells[1]
    c1.width = Inches(6.42)
    shade_cell(c1, bg)
    set_cell_border(c1, val='none', sz='0', color='FFFFFF')
    p0 = c1.paragraphs[0]
    para_space(p0, before=4, after=2)
    p0.paragraph_format.left_indent = Inches(0.1)
    rt = p0.add_run(f'  {title}')
    rt.font.name  = 'Calibri'
    rt.font.size  = Pt(10)
    rt.font.bold  = True
    set_run_color(rt, C_ACCENT)

    p1 = c1.add_paragraph()
    para_space(p1, before=2, after=6)
    p1.paragraph_format.left_indent = Inches(0.1)
    rc = p1.add_run(f'  {text}')
    rc.font.name   = 'Calibri'
    rc.font.size   = Pt(10)
    set_run_color(rc, C_PRIMARY)

    doc.add_paragraph()

# ── Tabla estilizada ──────────────────────────────────────────────────────────
def styled_table(doc, headers, rows, col_widths=None):
    ncols = len(headers)
    tbl   = doc.add_table(rows=1 + len(rows), cols=ncols)
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    tbl.style     = 'Table Grid'

    default_w = Inches(6.5 / ncols)
    for ci, hdr in enumerate(headers):
        cell = tbl.rows[0].cells[ci]
        shade_cell(cell, C_PRIMARY)
        w = Inches(col_widths[ci]) if col_widths else default_w
        cell.width = w
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        para_space(p, before=3, after=3)
        r = p.add_run(hdr)
        r.font.name  = 'Calibri'
        r.font.size  = Pt(10)
        r.font.bold  = True
        set_run_color(r, C_WHITE)

    for ri, row_data in enumerate(rows):
        bg = C_LIGHT_BG if ri % 2 == 0 else C_WHITE
        for ci, val in enumerate(row_data):
            cell = tbl.rows[ri + 1].cells[ci]
            shade_cell(cell, bg)
            w = Inches(col_widths[ci]) if col_widths else default_w
            cell.width = w
            p = cell.paragraphs[0]
            para_space(p, before=3, after=3)
            p.paragraph_format.left_indent = Inches(0.05)
            is_first = (ci == 0)
            r = p.add_run(val)
            r.font.name  = 'Calibri'
            r.font.size  = Pt(10)
            r.font.bold  = is_first
            if is_first:
                set_run_color(r, C_ACCENT2)
            else:
                set_run_color(r, C_PRIMARY)

    doc.add_paragraph()

# ── Separador visual ──────────────────────────────────────────────────────────
def divider(doc):
    p = doc.add_paragraph()
    para_space(p, before=6, after=6)
    pPr  = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bot  = OxmlElement('w:bottom')
    bot.set(qn('w:val'),   'single')
    bot.set(qn('w:sz'),    '4')
    bot.set(qn('w:space'), '1')
    bot.set(qn('w:color'), f'{C_ACCENT2[0]:02X}{C_ACCENT2[1]:02X}{C_ACCENT2[2]:02X}')
    pBdr.append(bot)
    pPr.append(pBdr)

# ── Caja de flujo (simulada con tabla) ────────────────────────────────────────
def flow_box(doc, steps):
    """steps: list of (emoji, title, desc)"""
    tbl = doc.add_table(rows=len(steps), cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    tbl.allow_autofit = False

    for i, (ico, title, desc) in enumerate(steps):
        bg = C_PRIMARY if i % 2 == 0 else C_ACCENT2

        c0 = tbl.rows[i].cells[0]   # ícono
        c0.width = Inches(0.5)
        shade_cell(c0, bg)
        set_cell_border(c0, val='none', sz='0', color='FFFFFF')
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        para_space(p0, before=4, after=4)
        r0 = p0.add_run(ico)
        r0.font.size = Pt(14)

        c1 = tbl.rows[i].cells[1]   # título
        c1.width = Inches(1.6)
        shade_cell(c1, bg)
        set_cell_border(c1, val='none', sz='0', color='FFFFFF')
        p1 = c1.paragraphs[0]
        para_space(p1, before=4, after=4)
        p1.paragraph_format.left_indent = Inches(0.1)
        r1 = p1.add_run(title)
        r1.font.name  = 'Calibri'
        r1.font.size  = Pt(10)
        r1.font.bold  = True
        set_run_color(r1, C_ACCENT if i % 2 == 0 else C_YELLOW)

        c2 = tbl.rows[i].cells[2]   # descripción
        c2.width = Inches(4.4)
        shade_cell(c2, bg)
        set_cell_border(c2, val='none', sz='0', color='FFFFFF')
        p2 = c2.paragraphs[0]
        para_space(p2, before=4, after=4)
        p2.paragraph_format.left_indent = Inches(0.1)
        r2 = p2.add_run(desc)
        r2.font.name  = 'Calibri'
        r2.font.size  = Pt(10)
        set_run_color(r2, RGBColor(0xCC, 0xD2, 0xE0))

    doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════════════════
# CONSTRUCCIÓN DEL DOCUMENTO
# ══════════════════════════════════════════════════════════════════════════════
doc = Document()
set_doc_styles(doc)

# Márgenes
for section in doc.sections:
    section.top_margin    = Cm(1.8)
    section.bottom_margin = Cm(1.8)
    section.left_margin   = Cm(2.0)
    section.right_margin  = Cm(2.0)

# ── PORTADA ───────────────────────────────────────────────────────────────────
add_cover(doc)

# salto de página manual via XML
p_break = doc.add_paragraph()
run_br  = p_break.add_run()
br_el   = OxmlElement('w:br')
br_el.set(qn('w:type'), 'page')
run_br._r.append(br_el)

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 1 — QUÉ ES CLAUDE CODE
# ══════════════════════════════════════════════════════════════════════════════
section_header(doc, 1, 'Qué es Claude Code y por qué usarlo desde el celular', '🤖')

body(doc,
    'Claude Code es el agente de programación de Anthropic. Entiende lenguaje '
    'natural y puede leer, escribir y ejecutar código en un entorno real de '
    'desarrollo — sin que necesites abrir ningún IDE ni escribir una sola '
    'instrucción técnica.')

subsection(doc, 'Capacidades principales', '⚡')
bullet(doc, 'Leer y editar archivos de cualquier lenguaje de programación')
bullet(doc, 'Ejecutar comandos en terminal (npm, python, git, docker…)')
bullet(doc, 'Navegar repositorios completos de GitHub')
bullet(doc, 'Crear aplicaciones enteras desde una descripción en español')
bullet(doc, 'Depurar errores, refactorizar y hacer revisiones de código')
bullet(doc, 'Gestionar ramas, commits y Pull Requests automáticamente')

subsection(doc, '¿Por qué desde el celular?', '📱')
body(doc,
    'El procesamiento ocurre en los servidores de Anthropic, no en tu '
    'dispositivo. Eso significa que la potencia de tu celular no importa: '
    'puedes hacer lo mismo que en un MacBook Pro.')

styled_table(doc,
    ['Situación', 'Sin Claude Code', 'Con Claude Code móvil'],
    [
        ['Urgencia en producción', 'Necesitas abrir laptop urgente', 'Corriges desde el celular en el metro'],
        ['Idea repentina',         'La olvidas o la anotas',          'La prototipas en 10 minutos'],
        ['Tiempo muerto',          'Redes sociales',                   'Avanzas en tu proyecto personal'],
        ['Code review',            'Esperas llegar al escritorio',     'Lo revisas desde la sala de espera'],
    ],
    col_widths=[1.6, 2.3, 2.6]
)

divider(doc)

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 2 — CÓMO ACCEDER
# ══════════════════════════════════════════════════════════════════════════════
section_header(doc, 2, 'Formas de acceder desde el celular', '🌐')

subsection(doc, 'Opción A — Web App (Recomendada)', '⭐')
body(doc,
    'Abre el navegador de tu celular y ve a claude.ai/code. '
    'Sin instalación. Funciona en iOS (Safari) y Android (Chrome). '
    'Añade la página a tu pantalla de inicio para acceso inmediato.')
tip_box(doc, 'iOS:', 'Safari → botón Compartir → "Añadir a pantalla de inicio"')
tip_box(doc, 'Android:', 'Chrome → menú ⋮ → "Añadir a pantalla de inicio"')

subsection(doc, 'Opción B — App oficial de Claude', '📲')
bullet(doc, 'Descárgala en App Store o Google Play')
bullet(doc, 'Interfaz optimizada para pantalla pequeña')
bullet(doc, 'Notificaciones cuando terminan tareas largas')
bullet(doc, 'Sincronización de conversaciones entre dispositivos')

subsection(doc, 'Opción C — GitHub Codespaces (Terminal completa)', '💻')
body(doc, 'Para cuando necesitas acceso total a terminal y ejecución de pruebas:')
flow_box(doc, [
    ('1️⃣', 'Abre el repo',      'Ve a tu repositorio en GitHub desde el celular'),
    ('2️⃣', 'Presiona "."',      'Se abre VS Code completo en el navegador'),
    ('3️⃣', 'Instala CLI',       'npm install -g @anthropic-ai/claude-code'),
    ('4️⃣', 'Ejecuta claude',    'Terminal completa + IA + tu código'),
])

subsection(doc, 'Opción D — SSH a tu propio servidor', '🔐')
bullet(doc, 'Termius (iOS/Android) — la más recomendada')
bullet(doc, 'Blink Shell (iOS) — soporte para mosh y conexiones estables')
bullet(doc, 'JuiceSSH (Android) — ligera y rápida')
body(doc, 'Una vez conectado por SSH, usas Claude Code CLI exactamente igual que en escritorio.')

divider(doc)

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 3 — GITHUB COMPLETO
# ══════════════════════════════════════════════════════════════════════════════
section_header(doc, 3, 'GitHub: La columna vertebral de tu flujo móvil', '🐙')

body(doc,
    'GitHub es donde vive el código. Claude Code puede gestionar todo el ciclo '
    'de vida: ramas, commits, Pull Requests, Issues y GitHub Actions, sin que '
    'tengas que escribir un solo comando Git.')

subsection(doc, 'Conectar un repositorio', '🔗')
body(doc, 'Escribe en el chat de Claude Code:')
code_block(doc,
    '"Conecta el repositorio GitHub mi-usuario/mi-proyecto\n'
    ' y ayúdame a trabajar en él."',
    label='CLAUDE CODE CHAT')
body(doc,
    'Claude te redirigirá a GitHub para autorización OAuth. Una vez autorizado, '
    'el repositorio queda disponible en toda la sesión.')

subsection(doc, 'Operaciones Git que Claude hace por ti', '⚙️')
styled_table(doc,
    ['Lo que pides (en español)', 'Lo que Claude ejecuta'],
    [
        ['"Crea una rama para el login con Google"',  'git checkout -b feature/login-google'],
        ['"Guarda los cambios con mensaje X"',        'git add . && git commit -m "X"'],
        ['"Sube la rama al repositorio"',             'git push -u origin feature/login-google'],
        ['"Trae los últimos cambios de main"',        'git pull origin main'],
        ['"Muestra qué cambió en auth/"',             'git diff main -- src/auth/'],
        ['"Fusiona la rama y cierra el issue #12"',   'git merge + cierra issue vía API'],
    ],
    col_widths=[3.5, 3.0]
)

subsection(doc, 'Pull Requests', '🔄')
h3(doc, 'Crear un PR completo')
code_block(doc,
    '"Crea un Pull Request desde feature/nueva-api hacia main.\n'
    ' Título: Agrega API de notificaciones.\n'
    ' Incluye descripción detallada de los cambios y\n'
    ' pasos para probarlos."',
    label='EJEMPLO')

h3(doc, 'Revisar un PR de un compañero')
code_block(doc,
    '"Revisa el PR #47. Analiza calidad de código,\n'
    ' posibles bugs, seguridad y si sigue las\n'
    ' convenciones del proyecto."',
    label='EJEMPLO')

subsection(doc, 'Issues', '🐛')
bullet(doc, 'Crear:', bold_prefix='')
code_block(doc,
    '"Crea un issue: la página de perfil da error 500\n'
    ' cuando el usuario no tiene foto. Stack trace:\n'
    ' [pega el error aquí]"')
bullet(doc, 'Trabajar en un issue existente:')
code_block(doc,
    '"Toma el issue #23 y corrígelo. Crea la rama\n'
    ' correspondiente y abre un PR cuando esté listo."')

subsection(doc, 'GitHub Actions y CI/CD', '🚀')
body(doc, 'Claude puede crear, leer y diagnosticar workflows de GitHub Actions:')
code_block(doc,
    '"El workflow de CI está fallando. Muéstrame el log\n'
    ' y dime qué está causando el error."',
    label='DIAGNÓSTICO')
code_block(doc,
    '"Crea un workflow que: corra en push a main,\n'
    ' instale dependencias, ejecute tests y haga build.\n'
    ' Si algo falla, notifica a Slack."',
    label='CREAR WORKFLOW')

divider(doc)

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 4 — AGENTES
# ══════════════════════════════════════════════════════════════════════════════
section_header(doc, 4, 'Agentes en Claude Code', '🤖')

body(doc,
    'Los agentes son instancias especializadas de Claude que tienen acceso a '
    'herramientas específicas y pueden ejecutar tareas complejas de forma '
    'semi-autónoma. Desde el celular puedes orquestar agentes completos.')

subsection(doc, '¿Qué es un agente?', '🧠')
tip_box(doc,
    'Definición:',
    'Un agente es Claude operando en un bucle: recibe una tarea, decide '
    'qué herramientas usar (leer archivos, ejecutar código, buscar en la web), '
    'actúa, observa el resultado y vuelve a decidir. Repite hasta completar la tarea.',
    color=RGBColor(0xE8, 0xF4, 0xFD))

subsection(doc, 'Tipos de agentes disponibles', '🗂️')
styled_table(doc,
    ['Agente', 'Especialidad', 'Cuándo usarlo'],
    [
        ['claude (default)',   'Agente general completo',           'Cualquier tarea de desarrollo'],
        ['Explore',           'Búsqueda y exploración de código',  'Encontrar archivos, símbolos, patrones'],
        ['Plan',              'Arquitectura y diseño de soluciones','Planificar implementaciones complejas'],
        ['claude-code-guide', 'Preguntas sobre Claude Code y SDK', '¿Cómo hago X en Claude Code?'],
        ['general-purpose',   'Investigación multi-paso',          'Tareas que abarcan múltiples búsquedas'],
    ],
    col_widths=[1.5, 2.3, 2.7]
)

subsection(doc, 'Cómo usar agentes desde el celular', '📲')
body(doc, 'Simplemente describe la tarea compleja y Claude Code orquesta los agentes necesarios internamente:')

h3(doc, 'Ejemplo 1 — Agente explorador')
code_block(doc,
    '"Explora toda la carpeta src/ y dime:\n'
    ' - Qué módulos existen\n'
    ' - Cuáles tienen más de 300 líneas\n'
    ' - Dónde están los puntos de entrada de la API\n'
    ' - Qué archivos no tienen tests"',
    label='TAREA PARA AGENTE EXPLORE')

h3(doc, 'Ejemplo 2 — Agente planificador')
code_block(doc,
    '"Planifica cómo migrar esta aplicación de\n'
    ' JavaScript a TypeScript. Identifica los\n'
    ' archivos críticos, los riesgos, y dame\n'
    ' un plan paso a paso con estimación de tiempo."',
    label='TAREA PARA AGENTE PLAN')

h3(doc, 'Ejemplo 3 — Agentes paralelos')
code_block(doc,
    '"Mientras implementas el módulo de autenticación,\n'
    ' también busca en el código existente todos los\n'
    ' lugares donde se valida el token para\n'
    ' actualizarlos en consecuencia."',
    label='TAREAS PARALELAS')

subsection(doc, 'SDK de Agentes — Construir tus propios', '🔧')
body(doc,
    'Claude Code expone un SDK para que puedas crear agentes personalizados '
    'que se integren en tus propios sistemas:')
code_block(doc,
    'import anthropic\n\n'
    'client = anthropic.Anthropic()\n\n'
    '# Agente con herramientas personalizadas\n'
    'response = client.messages.create(\n'
    '    model="claude-sonnet-4-6",\n'
    '    max_tokens=8096,\n'
    '    tools=[\n'
    '        {\n'
    '            "name": "revisar_pr",\n'
    '            "description": "Revisa un PR de GitHub",\n'
    '            "input_schema": {\n'
    '                "type": "object",\n'
    '                "properties": {\n'
    '                    "pr_number": {"type": "integer"}\n'
    '                }\n'
    '            }\n'
    '        }\n'
    '    ],\n'
    '    messages=[{"role": "user",\n'
    '               "content": "Revisa el PR #42"}]\n'
    ')',
    label='Python — Anthropic SDK')

subsection(doc, 'Modo autónomo (YOLO mode)', '🤖')
tip_box(doc,
    'Advertencia:',
    'El modo autónomo permite a Claude ejecutar acciones sin pedir confirmación. '
    'Útil para tareas largas, pero úsalo solo en repositorios de prueba o '
    'cuando estés seguro de lo que pediste. Desde el celular, el modo '
    'conservador es más seguro.',
    color=RGBColor(0xFF, 0xF3, 0xCD))

code_block(doc,
    '"Actúa de forma autónoma: crea la estructura completa\n'
    ' del proyecto, instala dependencias, escribe los tests\n'
    ' y haz el primer commit. No me preguntes nada."',
    label='MODO AUTÓNOMO')

divider(doc)

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 5 — COMANDOS / SLASH COMMANDS
# ══════════════════════════════════════════════════════════════════════════════
section_header(doc, 5, 'Comandos Slash — La navaja suiza de Claude Code', '⚡')

body(doc,
    'Los comandos slash (/comando) son atajos que activan funcionalidades '
    'especiales de Claude Code. Escribe / en el chat y aparecerá un menú '
    'de autocompletado. Son el equivalente a los atajos de teclado, '
    'pero optimizados para celular.')

subsection(doc, 'Comandos de sesión y contexto', '🔄')
styled_table(doc,
    ['Comando', 'Qué hace', 'Cuándo usarlo'],
    [
        ['/clear',   'Limpia el historial de la sesión actual',         'Cuando quieres empezar una tarea nueva sin contexto anterior'],
        ['/compact', 'Comprime el historial para liberar contexto',     'Sesiones largas donde Claude empieza a "olvidar" el inicio'],
        ['/memory',  'Muestra y edita lo que Claude recuerda de ti',    'Ajustar preferencias persistentes entre sesiones'],
        ['/config',  'Abre configuración: modelo, tema, permisos',      'Cambiar modelo o ajustar permisos de herramientas'],
    ],
    col_widths=[1.3, 2.7, 2.5]
)

subsection(doc, '/goals — Define el objetivo de la sesión', '🎯')
body(doc,
    '/goals es uno de los comandos más poderosos para trabajar desde el '
    'celular. Te permite definir metas claras al inicio de una sesión para '
    'que Claude las mantenga en foco durante toda la conversación.')
code_block(doc,
    '/goals\n\n'
    'Objetivo principal: Implementar autenticación con Google OAuth\n\n'
    'Tareas:\n'
    '[ ] 1. Configurar Google OAuth en Firebase\n'
    '[ ] 2. Crear el botón de Login con Google\n'
    '[ ] 3. Manejar la sesión del usuario\n'
    '[ ] 4. Proteger rutas privadas\n'
    '[ ] 5. Escribir tests de integración\n\n'
    'Restricciones:\n'
    '- Stack: React + Firebase\n'
    '- No usar librerías externas adicionales\n'
    '- Toda la UI en español',
    label='/goals — EJEMPLO COMPLETO')

tip_box(doc,
    'Ventaja móvil:',
    'Con /goals definido, si cierras la app y vuelves más tarde, Claude '
    'puede retomar el trabajo desde donde quedó, sin que tengas que '
    'repetir el contexto. Ideal para sesiones interrumpidas en el celular.',
    color=RGBColor(0xE8, 0xF8, 0xF0))

subsection(doc, '/init — Documenta tu proyecto automáticamente', '📄')
body(doc,
    'Genera un archivo CLAUDE.md con la documentación esencial del proyecto. '
    'Claude Code lo leerá automáticamente en futuras sesiones para entender '
    'el contexto sin que tengas que explicarlo de nuevo.')
code_block(doc, '/init', label='COMANDO')
body(doc, 'Genera automáticamente:')
bullet(doc, 'Descripción del proyecto y stack tecnológico')
bullet(doc, 'Comandos importantes (cómo correr tests, build, deploy)')
bullet(doc, 'Convenciones de código del proyecto')
bullet(doc, 'Estructura de carpetas principales')
bullet(doc, 'Variables de entorno necesarias')

subsection(doc, '/review — Revisión de código profesional', '🔍')
code_block(doc, '/review', label='COMANDO')
body(doc, 'Claude analiza el código actual o los cambios en la rama y reporta:')
bullet(doc, 'Bugs potenciales y casos borde no manejados')
bullet(doc, 'Problemas de seguridad (inyección, XSS, auth, etc.)')
bullet(doc, 'Rendimiento y optimizaciones posibles')
bullet(doc, 'Calidad, legibilidad y adherencia a convenciones')
bullet(doc, 'Cobertura de tests faltante')

subsection(doc, '/help — Lista de comandos disponibles', '❓')
code_block(doc, '/help', label='COMANDO')
body(doc,
    'Muestra todos los comandos disponibles en tu sesión actual, incluyendo '
    'comandos personalizados que hayas configurado en tu CLAUDE.md.')

subsection(doc, 'Tabla completa de comandos', '📋')
styled_table(doc,
    ['Comando', 'Función'],
    [
        ['/goals',      'Define objetivos y tareas de la sesión, Claude los rastrea'],
        ['/init',       'Crea CLAUDE.md con documentación del proyecto'],
        ['/review',     'Revisión completa del código actual'],
        ['/clear',      'Limpia el contexto de la conversación'],
        ['/compact',    'Comprime el historial para liberar espacio de contexto'],
        ['/config',     'Configuración: modelo, tema, permisos de herramientas'],
        ['/memory',     'Ver y editar la memoria persistente de Claude'],
        ['/help',       'Muestra todos los comandos disponibles'],
        ['/fast',       'Activa modo rápido (Claude Opus optimizado para velocidad)'],
        ['/cost',       'Muestra el costo estimado de la sesión actual'],
    ],
    col_widths=[1.5, 5.0]
)

subsection(doc, 'Comandos personalizados (Custom Slash Commands)', '✏️')
body(doc,
    'Puedes crear tus propios comandos en el archivo CLAUDE.md de tu proyecto. '
    'Estos aparecen en el menú de autocompletado igual que los comandos nativos.')
code_block(doc,
    '# En tu CLAUDE.md:\n\n'
    '## Comandos personalizados\n\n'
    '/deploy-staging:\n'
    '  Ejecuta: npm run build && \\\n'
    '           git push origin staging\n\n'
    '/nuevo-componente:\n'
    '  Crea un componente React en src/components/\n'
    '  con TypeScript, tests y Storybook.\n\n'
    '/audit-seguridad:\n'
    '  Revisa todo el código en busca de vulnerabilidades\n'
    '  OWASP Top 10 y genera reporte.',
    label='CLAUDE.md — COMANDOS PERSONALIZADOS')

divider(doc)

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 6 — FLUJO DE TRABAJO MÓVIL
# ══════════════════════════════════════════════════════════════════════════════
section_header(doc, 6, 'Flujo de trabajo eficiente desde el celular', '🔄')

subsection(doc, 'Instrucciones largas = menos mensajes = más eficiencia', '📝')
body(doc, 'En teclado virtual, escribe instrucciones completas desde el inicio:')
tip_box(doc, '❌ Poco eficiente:', '"Arregla el bug del login"')
tip_box(doc,
    '✅ Más eficiente:',
    '"En src/auth/login.js, handleLogin() no maneja el 401 del servidor. '
    'Agrega manejo para 401 (credenciales incorrectas), 403 (cuenta bloqueada) '
    'y 429 (rate limit). Muestra mensajes apropiados en cada caso."',
    color=RGBColor(0xE8, 0xF8, 0xF0))

subsection(doc, 'Dictado de voz para instrucciones largas', '🎙️')
body(doc,
    'El dictado de voz es el superpoder del celular para Claude Code. '
    'Usa el micrófono del teclado para dictar instrucciones detalladas '
    'sin escribir.')
bullet(doc, 'iOS: presiona el ícono de micrófono en el teclado de sistema')
bullet(doc, 'Android: icono de micrófono en el teclado (Gboard, SwiftKey)')
bullet(doc, 'Funciona mejor para: descripciones de funcionalidades, explicaciones, reportes de bugs')
bullet(doc, 'Para código específico o nombres exactos: prefiere escribir manualmente')

subsection(doc, 'Divide el trabajo en sesiones cortas', '⏱️')
flow_box(doc, [
    ('🌅', 'Sesión 1 — Transporte',    'Define el proyecto con /goals, crea la estructura base'),
    ('☕', 'Sesión 2 — Pausa',         'Implementa un módulo específico, haz commit'),
    ('🌙', 'Sesión 3 — Noche',         'Revisa con /review, corrige y haz push'),
    ('🔄', 'Iteración continua',        'Cada sesión avanza y queda guardada en GitHub'),
])

subsection(doc, 'Atajos de texto recomendados', '⌨️')
body(doc, 'Configura estos reemplazos en el teclado de tu celular:')
styled_table(doc,
    ['Atajo que escribes', 'Se expande a'],
    [
        [';crea',   'Crea una función que'],
        [';test',   'Escribe pruebas unitarias para'],
        [';bug',    'Encuentra y corrige el bug en'],
        [';api',    'Crea un endpoint REST que'],
        [';rev',    'Revisa este código y sugiere mejoras:'],
        [';commit', 'Haz commit de los cambios con mensaje:'],
        [';goals',  '/goals\nObjetivo: '],
    ],
    col_widths=[2.0, 4.5]
)

divider(doc)

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 7 — CREAR PROYECTOS
# ══════════════════════════════════════════════════════════════════════════════
section_header(doc, 7, 'Crear proyectos desde cero', '🚀')

body(doc, 'Describe lo que quieres en lenguaje natural y Claude Code lo construye completo.')

subsection(doc, 'Ejemplo — API REST con Node.js', '🟢')
code_block(doc,
    '"Crea una API REST con Node.js y Express para\n'
    ' gestionar una lista de tareas. Necesito:\n'
    ' - CRUD completo (crear, leer, actualizar, eliminar)\n'
    ' - Base de datos SQLite para persistencia\n'
    ' - Validación de datos con Zod\n'
    ' - Autenticación con JWT\n'
    ' - Tests con Jest\n'
    ' - Dockerfile incluido"',
    label='INSTRUCCIÓN COMPLETA')

subsection(doc, 'Ejemplo — App React con Tailwind', '⚛️')
code_block(doc,
    '"Crea una app React de clima que:\n'
    ' - Muestre el clima actual de una ciudad buscada\n'
    ' - Use la API de OpenWeatherMap\n'
    ' - Tenga diseño responsivo con Tailwind CSS\n'
    ' - Muestre pronóstico de 5 días\n'
    ' - Guarde las últimas 5 búsquedas en localStorage"')

subsection(doc, 'Flujo recomendado para proyectos nuevos', '🗺️')
flow_box(doc, [
    ('1️⃣', 'Describe el proyecto',   'Un mensaje detallado con todo el stack y requisitos'),
    ('2️⃣', 'Revisa la estructura',   '"Muéstrame solo la estructura de carpetas primero"'),
    ('3️⃣', 'Aprueba e implementa',   'Claude escribe el código módulo por módulo'),
    ('4️⃣', 'Commit progresivo',      '"Haz commit de lo que tenemos hasta ahora"'),
    ('5️⃣', 'Sube a GitHub',          '"Crea el repositorio y sube todo a GitHub"'),
    ('6️⃣', 'Deploy automático',      'GitHub Actions despliega en Vercel/Railway/AWS'),
])

divider(doc)

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 8 — CASOS DE USO
# ══════════════════════════════════════════════════════════════════════════════
section_header(doc, 8, 'Casos de uso prácticos', '💡')

subsection(doc, 'Caso 1 — Urgencia de producción', '🔴')
flow_box(doc, [
    ('🚨', 'Alerta a las 8am',       'Recibes el error en el celular, estás en transporte'),
    ('📋', 'Pega el stack trace',    'Claude diagnostica la causa raíz'),
    ('🔧', 'Claude corrige',         'Genera el fix y lo commitea en una rama hotfix'),
    ('✅', 'Tú apruebas el PR',      'Desde GitHub Mobile apruebas y haces merge'),
])

subsection(doc, 'Caso 2 — Aprender programación desde el celular', '📚')
code_block(doc,
    '"Enséñame a crear una API REST con Python y FastAPI.\n'
    ' Vamos paso a paso, explícame cada concepto antes\n'
    ' de mostrme el código. Empieza por los conceptos básicos."')

subsection(doc, 'Caso 3 — Code review en sala de espera', '🔍')
code_block(doc,
    '"Mi compañero abrió el PR #38. Revísalo completo\n'
    ' y dame un resumen de qué hace, si tiene bugs\n'
    ' y qué comentarios debo dejarle."')

subsection(doc, 'Caso 4 — Prototipo de idea repentina', '💡')
code_block(doc,
    '"Se me ocurrió una app para dividir gastos entre\n'
    ' amigos. Crea un MVP en React Native con:\n'
    ' grupos de gastos, división equitativa e historial.\n'
    ' Empieza por la estructura y el diseño de pantallas."')

divider(doc)

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 9 — SEGURIDAD
# ══════════════════════════════════════════════════════════════════════════════
section_header(doc, 9, 'Seguridad y buenas prácticas', '🔒')

tip_box(doc,
    '🚫 Nunca escribas en el chat:',
    'Contraseñas · API keys reales · Tokens de acceso · '
    'Strings de conexión con credenciales · Datos personales de clientes',
    color=RGBColor(0xFF, 0xEB, 0xEB))

tip_box(doc,
    '✅ En cambio, usa variables de entorno:',
    '"El API key estará en la variable STRIPE_SECRET_KEY" — '
    'Claude sabe cómo manejarlas correctamente en el código.',
    color=RGBColor(0xE8, 0xF8, 0xF0))

subsection(doc, 'Reglas de oro para móvil', '🛡️')
bullet(doc, 'Siempre trabaja en ramas separadas, nunca directamente en main')
bullet(doc, 'Revisa el código antes de hacer merge a producción')
bullet(doc, 'En WiFi público, activa una VPN antes de conectarte')
bullet(doc, 'Usa modo conservador de permisos en Claude Code desde el celular')
bullet(doc, 'Cierra la sesión de Claude Code cuando termines')
bullet(doc, 'No trabajes con datos sensibles de clientes en redes públicas')

divider(doc)

# ══════════════════════════════════════════════════════════════════════════════
# SECCIÓN 10 — REFERENCIA RÁPIDA
# ══════════════════════════════════════════════════════════════════════════════
section_header(doc, 10, 'Referencia rápida — Frases para copiar y pegar', '📋')

body(doc, 'Guarda estas instrucciones en las notas de tu celular:')

h3(doc, '📁 Explorar el código')
code_block(doc,
    '"Explícame la estructura general del proyecto"\n'
    '"¿Dónde está implementada la lógica de [X]?"\n'
    '"Lista todos los archivos que tocan la base de datos"')

h3(doc, '🐛 Bugs')
code_block(doc,
    '"Tengo este error: [error]. Encuentra la causa y corrígela."\n'
    '"La función [nombre] no hace [esperado]. Revísala."')

h3(doc, '✨ Funcionalidades')
code_block(doc,
    '"Agrega [funcionalidad] a [archivo/componente]"\n'
    '"Crea un endpoint que [descripción]"\n'
    '"Implementa [feature] siguiendo el patrón de [archivo]"')

h3(doc, '💾 Git')
code_block(doc,
    '"Haz commit de los cambios con mensaje \'[mensaje]\'"\n'
    '"Crea una rama [nombre] y trabaja en ella"\n'
    '"Abre un PR desde [rama] hacia main"')

h3(doc, '⚡ Comandos slash rápidos')
code_block(doc,
    '/goals   → Define objetivos de la sesión\n'
    '/init    → Documenta el proyecto\n'
    '/review  → Revisa el código actual\n'
    '/compact → Libera contexto en sesiones largas\n'
    '/clear   → Comienza sesión limpia')

# ── Pie de página ──────────────────────────────────────────────────────────────
p_end = doc.add_paragraph()
para_space(p_end, before=20, after=4)
p_end.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_end = p_end.add_run('Claude Code · claude.ai/code · Mayo 2026')
r_end.font.name   = 'Calibri'
r_end.font.size   = Pt(9)
r_end.font.italic = True
set_run_color(r_end, RGBColor(0x99, 0x99, 0x99))

# ── Guardar ───────────────────────────────────────────────────────────────────
output_path = '/home/user/tingaod93/Guia_ClaudeCode_Celular.docx'
doc.save(output_path)
print(f'Documento generado: {output_path}')
