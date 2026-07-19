#!/usr/bin/env python3
"""Round-trip converter between rosei_master.tex and rosei_master.md.

Unlike a naive header-only pass, this actually turns LaTeX structure
into Markdown structure so Obsidian renders it: \\section -> #, \\item
lists -> - lists, \\textbf/\\emph -> **bold**/*italic*, \\begin{tabular}
-> GFM tables, \\begin{equation}/\\[ \\] -> $$ ... $$ math, the
\\begin{remark}/\\begin{abstract} environments -> Obsidian callouts, and
the single paracol X/L comparison -> a 3-column table (Step | X | L).

Anything not covered by a specific rule (macros, packages, the exact
paracol vspace/Needspace tuning) is preserved verbatim: the .tex
preamble and closing \\end{document} are embedded whole in HTML
comments at the top/bottom of the .md, so nothing needs to be kept in
sync by hand.

Fidelity note: section headers, text style, lists, equations and plain
tables round-trip byte-for-byte. The paracol section round-trips its
*content* exactly (every word/symbol) but its exact LaTeX spacing
commands are regenerated fresh from the same \\colstep machinery,
rather than replayed byte-for-byte -- editing the table in Obsidian and
converting back gives a document that compiles and reads the same, not
a diff-empty rebuild of that one section.

Usage:
    python3 tex_md_sync.py to-md   rosei_master.tex rosei_master.md
    python3 tex_md_sync.py to-tex  rosei_master.md   rosei_master.tex
"""
import re
import sys
import pathlib

PREAMBLE_BEGIN = "<!-- TEX-PREAMBLE (verbatim; edit macros/packages here, not below) -->"
PREAMBLE_END = "<!-- END-TEX-PREAMBLE -->"
FOOTER_BEGIN = "<!-- TEX-FOOTER (verbatim) -->"
FOOTER_END = "<!-- END-TEX-FOOTER -->"

BRACE_ARG = r'((?:[^{}]|\{[^{}]*\})*)'
TEXT_MODE_MARKERS = (r'\par', r'\vspace', r'\noindent', r'\nobreak',
                     r'\ignorespaces', r'\textbf', r'\emph', r'\Needspace')
NEWCOMMAND_RE = re.compile(r'\\newcommand\{(\\[a-zA-Z]+)\}(\[[0-9]\])?\{(.*)\}')


# --------------------------------------------------------------------------
# generic helpers
# --------------------------------------------------------------------------

def extract_braced(text, start):
    """text[start] must be '{'; returns (inner, index_after_closing_brace)."""
    assert text[start] == '{'
    depth = 0
    i = start
    while i < len(text):
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    raise ValueError('unbalanced braces')


def protect_math(text):
    placeholders = []

    def repl(m):
        placeholders.append(m.group())
        return f'\x00MATH{len(placeholders) - 1}\x00'

    text = re.sub(r'\$\$\n.*?\n\$\$', repl, text, flags=re.S)
    text = re.sub(r'(?<!\\)\$[^$]*?(?<!\\)\$', repl, text, flags=re.S)
    return text, placeholders


def restore_math(text, placeholders):
    for i, ph in enumerate(placeholders):
        text = text.replace(f'\x00MATH{i}\x00', ph)
    return text


def build_macro_dict(preamble_text):
    """0-arg math shorthand macros (\\hw, \\kpar, \\Elu, ...) -> literal
    definition. Structural/text-mode macros (e.g. \\colstep, which takes an
    argument and emits \\par/\\textbf) are excluded and left untouched."""
    macros = {}
    for name, arity, body in NEWCOMMAND_RE.findall(preamble_text):
        if arity:
            continue
        if any(re.search(re.escape(marker) + r'(?![a-zA-Z])', body) for marker in TEXT_MODE_MARKERS):
            continue
        macros[name] = body
    return macros


def expand_macros(text, macros):
    """Replace every custom-macro invocation with its literal definition,
    so the resulting math uses only standard MathJax-supported LaTeX with
    no dependency on macro definitions being loaded/ordered correctly."""
    # longest name first so e.g. \Eg doesn't preempt \EgX
    for name in sorted(macros, key=len, reverse=True):
        pattern = re.compile(re.escape(name) + r'(?![a-zA-Z])')
        # brace-wrapped: a bare expansion can glue onto an adjacent control
        # word (\pi\kperp -> \pik_{\perp}, an undefined \pik); {...} forces
        # a clean token boundary on both sides without changing rendering.
        defn = '{' + macros[name] + '}'
        text = pattern.sub(lambda m, d=defn: d, text)
    return text


# --------------------------------------------------------------------------
# text style: \textbf{}/\emph{}/\textit{} <-> **bold**/*italic*
# --------------------------------------------------------------------------

def textstyle_to_md(text):
    protected, placeholders = protect_math(text)
    protected = re.sub(r'\\textbf\{' + BRACE_ARG + r'\}', r'**\1**', protected)
    protected = re.sub(r'\\(?:emph|textit)\{' + BRACE_ARG + r'\}', r'*\1*', protected)
    return restore_math(protected, placeholders)


MD_BOLD_RE = re.compile(r'\*\*((?:[^*]|\*(?!\*))+)\*\*')
MD_ITALIC_RE = re.compile(r'(?<!\*)(?<!\w)\*((?:[^*\n]|\n(?!\n))+)\*(?!\w)(?!\*)')


def textstyle_to_tex(text):
    protected, placeholders = protect_math(text)
    protected = MD_BOLD_RE.sub(lambda m: r'\textbf{' + m.group(1) + '}', protected)
    protected = MD_ITALIC_RE.sub(lambda m: r'\emph{' + m.group(1) + '}', protected)
    return restore_math(protected, placeholders)


# --------------------------------------------------------------------------
# lists
# --------------------------------------------------------------------------

def lists_to_md(body):
    def conv(env, marker):
        pattern = re.compile(r'\\begin\{' + env + r'\}(.*?)\\end\{' + env + r'\}', re.S)

        def repl(m):
            content = m.group(1)
            items = re.split(r'\\item\s*', content)[1:]
            lines = []
            for i, it in enumerate(items):
                it = re.sub(r'\s*\n\s*', ' ', it.strip())
                prefix = f'{i + 1}.' if marker == '1.' else '-'
                lines.append(f'{prefix} {it}')
            return '\n'.join(lines)

        return pattern.sub(repl, body)

    body = conv('itemize', '-')
    body = conv('enumerate', '1.')
    return body


LIST_ITEM_RE = re.compile(r'^(-|\d+\.) (.*)$')


def lists_to_tex(body):
    lines = body.split('\n')
    out = []
    i = 0
    while i < len(lines):
        m = LIST_ITEM_RE.match(lines[i])
        if m:
            is_num = lines[i].lstrip()[0].isdigit()
            items = []
            while i < len(lines):
                m2 = LIST_ITEM_RE.match(lines[i])
                if not m2 or bool(m2.group(1)[0].isdigit()) != is_num:
                    break
                items.append(m2.group(2))
                i += 1
            env = 'enumerate' if is_num else 'itemize'
            out.append(f'\\begin{{{env}}}')
            for it in items:
                out.append(f'\\item {it}')
            out.append(f'\\end{{{env}}}')
        else:
            out.append(lines[i])
            i += 1
    return '\n'.join(out)


# --------------------------------------------------------------------------
# equations: \begin{equation}...\end{equation} <-> $$ ... $$
# (all bare \[ \] / align* in this document live inside the paracol
# block and are handled by convert_paracol instead)
# --------------------------------------------------------------------------

LABEL_LINE_RE = re.compile(r'^[ \t]*\\label\{([^}]+)\}[ \t]*$', re.M)


def strip_label_line(content):
    label = []

    def repl(m):
        label.append(m.group(1))
        return ''

    content = LABEL_LINE_RE.sub(repl, content)
    content = re.sub(r'\n{3,}', '\n\n', content).strip('\n')
    return content, (label[0] if label else None)


def equations_to_md(body):
    def repl(m):
        content, label = strip_label_line(m.group(1))
        block = f'$$\n{content}\n$$'
        if label:
            block += f'\n<!--\\label{{{label}}}-->'
        return block

    return re.sub(r'\\begin\{equation\}(.*?)\\end\{equation\}', repl, body, flags=re.S)


EQ_LABEL_COMMENT_RE = re.compile(r'\n?<!--\\label\{([^}]+)\}-->')


def equations_to_tex(body):
    def repl(m):
        inner = m.group(1)
        label_m = EQ_LABEL_COMMENT_RE.search(inner)
        label = None
        if label_m:
            label = label_m.group(1)
            inner = inner[:label_m.start()]
        inner = inner.strip('\n')
        out = inner
        if label:
            out += f'\n\\label{{{label}}}'
        return f'\\begin{{equation}}\n{out}\n\\end{{equation}}'

    # match a $$ ... $$ block plus an optional following label comment
    pattern = re.compile(r'\$\$\n(.*?)\n\$\$(?:\n<!--\\label\{[^}]+\}-->)?', re.S)

    def repl2(m):
        block = m.group(0)
        content_m = re.match(r'\$\$\n(.*?)\n\$\$', block, re.S)
        content = content_m.group(1)
        label_m = re.search(r'<!--\\label\{([^}]+)\}-->', block)
        out = content
        if label_m:
            out += f'\n\\label{{{label_m.group(1)}}}'
        return f'\\begin{{equation}}\n{out}\n\\end{{equation}}'

    return pattern.sub(repl2, body)


# --------------------------------------------------------------------------
# abstract / remark -> Obsidian callouts
# --------------------------------------------------------------------------

def blockquote(text):
    return '\n'.join('> ' + l if l.strip() else '>' for l in text.strip('\n').split('\n'))


def unblockquote(text):
    lines = []
    for l in text.split('\n'):
        if l.startswith('> '):
            lines.append(l[2:])
        elif l.strip() == '>':
            lines.append('')
        else:
            lines.append(l)
    return '\n'.join(lines)


def abstract_to_md(body):
    def repl(m):
        return f'> [!abstract]\n{blockquote(m.group(1))}'

    return re.sub(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', repl, body, flags=re.S)


def abstract_to_tex(body):
    def repl(m):
        content = unblockquote(m.group(1))
        return f'\\begin{{abstract}}\n{content.strip()}\n\\end{{abstract}}'

    pattern = re.compile(r'> \[!abstract\]\n((?:>.*\n?)*)')
    return pattern.sub(repl, body)


REMARK_RE = re.compile(r'\\begin\{remark\}(?:\[' + BRACE_ARG + r'\])?\\label\{([^}]+)\}(.*?)\\end\{remark\}', re.S)


def remark_to_md(body):
    def repl(m):
        title, label, content = m.groups()
        title_part = f'{title} ' if title else ''
        header = f'> [!note] Remark: {title_part}{{{{label:{label}}}}}'
        return f'{header}\n{blockquote(content)}'

    return REMARK_RE.sub(repl, body)


MD_REMARK_RE = re.compile(
    r'> \[!note\] Remark: (.*?)\s*\{\{label:([^}]+)\}\}\n((?:>.*\n?)*)'
)


def remark_to_tex(body):
    def repl(m):
        title, label, content = m.groups()
        content_tex = unblockquote(content).strip()
        title_part = f'[{title}]' if title.strip() else ''
        return f'\\begin{{remark}}{title_part}\\label{{{label}}}\n{content_tex}\n\\end{{remark}}'

    return MD_REMARK_RE.sub(repl, body)


# --------------------------------------------------------------------------
# tabular (inside \begin{center}) -> GFM table
# --------------------------------------------------------------------------

def tabular_to_md(colspec, content):
    content = re.sub(r'\\(top|mid|bottom)rule', '', content)
    row_chunks = re.split(r'\\\\', content)
    rows = []
    pending_color = False
    row_colored = []
    for chunk in row_chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        m = re.match(r'\\rowcolor\{[^}]*\}\s*(.*)', chunk, re.S)
        if m:
            pending_color = True
            chunk = m.group(1).strip()
            if not chunk:
                continue
        cells = [escape_cell(re.sub(r'\s+', ' ', c.strip())) for c in re.split(r'(?<!\\)&', chunk)]
        rows.append(cells)
        row_colored.append(pending_color)
        pending_color = False

    if not rows:
        return f'<!--colspec:{colspec}-->\n'

    lines = [f'<!--colspec:{colspec}-->']
    lines.append('| ' + ' | '.join(rows[0]) + ' |')
    lines.append('| ' + ' | '.join(['---'] * len(rows[0])) + ' |')
    for cells, colored in zip(rows[1:], row_colored[1:]):
        if colored:
            cells = [f'**{c}**' if c else c for c in cells]
        lines.append('| ' + ' | '.join(cells) + ' |')
    return '\n'.join(lines)


def tables_to_md(body):
    out = []
    pos = 0
    for m in re.finditer(r'\\begin\{tabular\}', body):
        out.append(body[pos:m.start()])
        brace_start = m.end()
        colspec, after_colspec = extract_braced(body, brace_start)
        end_m = re.search(r'\\end\{tabular\}', body[after_colspec:])
        content = body[after_colspec:after_colspec + end_m.start()]
        out.append(tabular_to_md(colspec, content))
        pos = after_colspec + end_m.end()
    out.append(body[pos:])
    return ''.join(out)


TABLE_BLOCK_RE = re.compile(
    r'<!--colspec:([^>]*)-->\n(\|.*\|)\n(\|[\s:|-]*\|)\n((?:\|.*\|\n?)*)'
)


def escape_pipe(s):
    return s.replace('|', r'\|')


def escape_cell(s):
    """Escape pipes for GFM table-cell safety, without corrupting bar
    notation (|P|^2) inside math: bare | inside $...$ becomes \\vert{}
    (visually identical, avoids colliding with the LaTeX \\| = Vert
    command), everything else is backslash-escaped as usual."""
    def repl(m):
        inner = re.sub(r'(?<!\\)\|', r'\\vert{}', m.group(1))
        return f'${inner}$'
    s = re.sub(r'(?<!\\)\$([^$]*)(?<!\\)\$', repl, s)
    return escape_pipe(s)


def unescape_pipe(s):
    return s.replace(r'\|', '|')


def parse_md_row(line):
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]
    return [unescape_pipe(c.strip()) for c in re.split(r'(?<!\\)\|', line)]


def tables_to_tex(body):
    def repl(m):
        colspec, header_line, _, data_block = m.groups()
        header = parse_md_row(header_line)
        rows_tex = ['\\begin{tabular}{' + colspec + '}', '\\toprule',
                    ' & '.join(header) + r' \\', '\\midrule']
        data_lines = [l for l in data_block.split('\n') if l.strip()]
        for l in data_lines:
            cells = parse_md_row(l)
            bold_re = re.compile(r'^\*\*(.*)\*\*$')
            is_colored = all(bool(bold_re.match(c)) for c in cells if c.strip())
            if is_colored:
                cells = [bold_re.sub(r'\1', c) for c in cells]
                rows_tex.append('\\rowcolor{corerow}')
            rows_tex.append(' & '.join(cells) + r' \\')
        rows_tex.append('\\bottomrule')
        rows_tex.append('\\end{tabular}')
        return '\n'.join(rows_tex)

    return TABLE_BLOCK_RE.sub(repl, body)


# --------------------------------------------------------------------------
# paracol X/L comparison -> 3-column table (Step | X | L)
# --------------------------------------------------------------------------

PARACOL_RE = re.compile(r'\\begin\{paracol\}\{2\}(.*?)\\end\{paracol\}', re.S)
PARACOL_TITLE_RE = re.compile(r'\\underline\{\{\\Large\\bfseries\s*(.*?)\s*\}\}$', re.S)


def paracol_title_to_md(raw):
    m = PARACOL_TITLE_RE.match(raw.strip())
    if m:
        title = m.group(1).strip().replace(r'\quad', r'$\quad$')
        return '**' + title + '**'
    return raw


def paracol_title_to_tex(raw):
    m = re.match(r'^\*\*(.*)\*\*$', raw.strip(), re.S)
    if m:
        title = m.group(1).strip().replace(r'$\quad$', r'\quad')
        return r'\underline{{\Large\bfseries ' + title + '}}'
    return raw

HEADER_PAIR_RE = re.compile(
    r'\\begin\{center\}(.*?)\\end\{center\}\s*\\switchcolumn\s*'
    r'\\begin\{center\}(.*?)\\end\{center\}\s*\\switchcolumn\*',
    re.S,
)


BR_RUN_RE = re.compile(r'(?:\s*<br>\s*)+')


def cellify_forward(raw):
    raw = raw.strip()
    raw = re.sub(r'[ \t]*\n[ \t]*', ' ', raw)

    def conv_bracket(m):
        return '<br><br>$' + m.group(1).strip() + '$<br><br>'

    raw = re.sub(r'\\\[(.*?)\\\]', conv_bracket, raw, flags=re.S)

    def conv_align(m):
        return r'<br><br>$\begin{aligned}' + m.group(1).strip() + r'\end{aligned}$<br><br>'

    raw = re.sub(r'\\begin\{align\*\}(.*?)\\end\{align\*\}', conv_align, raw, flags=re.S)

    raw = BR_RUN_RE.sub('<br><br>', raw).strip()
    if raw.startswith('<br><br>'):
        raw = raw[len('<br><br>'):]
    if raw.endswith('<br><br>'):
        raw = raw[:-len('<br><br>')]
    return raw.strip()


def cellify_backward(cell):
    segments = [s for s in re.split(r'<br><br>', cell) if s.strip()]
    out = []
    for seg in segments:
        seg = seg.strip()
        m = re.match(r'^\$(.*)\$$', seg, re.S)
        if m:
            inner = m.group(1)
            am = re.match(r'^\\begin\{aligned\}(.*)\\end\{aligned\}$', inner.strip(), re.S)
            if am:
                out.append('\\begin{align*}\n' + am.group(1).strip() + '\n\\end{align*}')
            else:
                out.append('\\[' + inner.strip() + '\\]')
        else:
            out.append(seg)
    return '\n'.join(out)


def paracol_to_md(body):
    m = PARACOL_RE.search(body)
    if not m:
        return body
    inner = m.group(1)

    hm = HEADER_PAIR_RE.match(inner.lstrip('\n'))
    title_x = paracol_title_to_md(hm.group(1).strip())
    title_l = paracol_title_to_md(hm.group(2).strip())
    rest = inner[inner.index(hm.group(0)) + len(hm.group(0)):]

    colstep_starts = [cm.start() for cm in re.finditer(r'\\colstep\{', rest)]
    newpage_before = set()
    for idx, start in enumerate(colstep_starts):
        preceding = rest[:start]
        last_switch = preceding.rfind(r'\switchcolumn')
        gap = preceding[max(last_switch, 0):]
        if r'\newpage' in gap:
            newpage_before.add(idx)

    entries = []
    for cm in re.finditer(r'\\colstep\{([^}]*)\}(.*?)(?=\\switchcolumn|\Z)', rest, re.S):
        entries.append((cm.group(1), cm.group(2)))

    rows = []
    for i in range(0, len(entries), 2):
        name_x, content_x = entries[i]
        name_l, content_l = entries[i + 1]
        assert name_x == name_l, f'step name mismatch: {name_x!r} vs {name_l!r}'
        rows.append({
            'name': name_x,
            'x': cellify_forward(content_x),
            'l': cellify_forward(content_l),
            'pagebreak': i in newpage_before,
        })

    lines = ['<!--paracol-->',
             '| Step | ' + title_x + ' | ' + title_l + ' |',
             '| --- | --- | --- |']
    for r in rows:
        name = ('{{pagebreak}} ' if r['pagebreak'] else '') + f"**{r['name']}**"
        lines.append(f"| {escape_cell(name)} | {escape_cell(r['x'])} | {escape_cell(r['l'])} |")
    md_table = '\n'.join(lines)

    return body[:m.start()] + md_table + body[m.end():]


PARACOL_TABLE_RE = re.compile(
    r'<!--paracol-->\n(\|.*\|)\n(\|[\s:|-]*\|)\n((?:\|.*\|\n?)*)'
)


def paracol_to_tex(body):
    m = PARACOL_TABLE_RE.search(body)
    if not m:
        return body
    header_line, _, data_block = m.groups()
    header = parse_md_row(header_line)
    title_x, title_l = header[1], header[2]

    out = [r'\begin{paracol}{2}']
    out.append(r'\begin{center}' + paracol_title_to_tex(title_x) + r'\end{center}')
    out.append(r'\switchcolumn')
    out.append(r'\begin{center}' + paracol_title_to_tex(title_l) + r'\end{center}')
    out.append(r'\switchcolumn*')

    data_lines = [l for l in data_block.split('\n') if l.strip()]
    for i, l in enumerate(data_lines):
        cells = parse_md_row(l)
        name_cell, x_cell, l_cell = cells
        pagebreak = '{{pagebreak}}' in name_cell
        name = name_cell.replace('{{pagebreak}}', '').strip()
        name = re.sub(r'^\*\*(.*)\*\*$', r'\1', name.strip())
        if pagebreak:
            out.append(r'\newpage')
        out.append(f'\\colstep{{{name}}}')
        out.append(cellify_backward(x_cell))
        out.append(r'\switchcolumn')
        out.append(f'\\colstep{{{name}}}')
        out.append(cellify_backward(l_cell))
        if i < len(data_lines) - 1:
            out.append(r'\switchcolumn*')
    out.append(r'\end{paracol}')

    return body[:m.start()] + '\n'.join(out) + body[m.end():]


# --------------------------------------------------------------------------
# section headers
# --------------------------------------------------------------------------

HEADER_RE = re.compile(
    r'^\\(section|subsection|subsubsection)(\*)?\{(.*?)\}(?:\\label\{([^}]+)\})?\s*$'
)
LEVEL = {'section': '#', 'subsection': '##', 'subsubsection': '###'}
LEVEL_REV = {'#': 'section', '##': 'subsection', '###': 'subsubsection'}

MD_HEADER_RE = re.compile(
    r'^(#{1,3})\s+(.*?)(?:\s*\{\{label:([^}]+)\}\})?(?:\s*(\{\{starred\}\}))?\s*$'
)


def headers_to_md(body_lines):
    out = []
    for l in body_lines:
        m = HEADER_RE.match(l)
        if m:
            kind, star, title, label = m.groups()
            marker = ''
            if label:
                marker += f' {{{{label:{label}}}}}'
            if star:
                marker += ' {{starred}}'
            out.append(f'{LEVEL[kind]} {title}{marker}')
        else:
            out.append(l)
    return out


def headers_to_tex(body):
    out = []
    for l in body.split('\n'):
        m = MD_HEADER_RE.match(l)
        if m and l.startswith('#'):
            hashes, title, label, starred = m.groups()
            kind = LEVEL_REV[hashes]
            star = '*' if starred else ''
            lab = f'\\label{{{label}}}' if label else ''
            out.append(f'\\{kind}{star}{{{title.strip()}}}{lab}')
        else:
            out.append(l)
    return '\n'.join(out)


# --------------------------------------------------------------------------
# top-level to-md / to-tex
# --------------------------------------------------------------------------

def to_md(tex_path, md_path):
    lines = pathlib.Path(tex_path).read_text().split('\n')
    begin_idx = next(i for i, l in enumerate(lines) if l.strip() == r'\begin{document}')
    end_idx = next(i for i, l in enumerate(lines) if l.strip() == r'\end{document}')
    preamble = '\n'.join(lines[:begin_idx + 1])
    body = '\n'.join(lines[begin_idx + 1:end_idx])
    footer = '\n'.join(lines[end_idx:])

    body = expand_macros(body, build_macro_dict(preamble))
    body = paracol_to_md(body)
    body = abstract_to_md(body)
    body = remark_to_md(body)
    body = lists_to_md(body)
    body = equations_to_md(body)
    body = tables_to_md(body)
    body = textstyle_to_md(body)
    body = '\n'.join(headers_to_md(body.split('\n')))

    md = (
        f'{PREAMBLE_BEGIN}\n{preamble}\n{PREAMBLE_END}\n\n'
        + body.strip('\n') + '\n\n'
        f'{FOOTER_BEGIN}\n{footer}\n{FOOTER_END}\n'
    )
    pathlib.Path(md_path).write_text(md)


def _extract(begin, end, s):
    i = s.index(begin) + len(begin)
    if s[i:i + 1] == '\n':
        i += 1
    j = s.index(end, i)
    inner = s[i:j]
    if inner.endswith('\n'):
        inner = inner[:-1]
    return inner, s[j + len(end):]


def to_tex(md_path, tex_path):
    text = pathlib.Path(md_path).read_text()

    preamble, rest = _extract(PREAMBLE_BEGIN, PREAMBLE_END, text)

    footer_start = rest.index(FOOTER_BEGIN)
    body = rest[:footer_start]
    footer, _ = _extract(FOOTER_BEGIN, FOOTER_END, rest[footer_start:])

    body = headers_to_tex(body)
    body = tables_to_tex(body)
    body = equations_to_tex(body)
    body = lists_to_tex(body)
    body = remark_to_tex(body)
    body = abstract_to_tex(body)
    body = paracol_to_tex(body)
    body = textstyle_to_tex(body)

    tex = preamble.strip('\n') + '\n' + body.strip('\n') + '\n\n' + footer.strip('\n') + '\n'
    pathlib.Path(tex_path).write_text(tex)


if __name__ == '__main__':
    mode, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    if mode == 'to-md':
        to_md(src, dst)
    elif mode == 'to-tex':
        to_tex(src, dst)
    else:
        raise SystemExit('mode must be to-md or to-tex')
