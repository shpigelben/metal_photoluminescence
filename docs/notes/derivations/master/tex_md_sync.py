#!/usr/bin/env python3
"""Round-trip converter between rosei_master.tex and rosei_master.md.

Design goal: byte-for-byte reconstruction of the .tex. Only
\\section/\\subsection/\\subsubsection lines are turned into Markdown
headers (so Obsidian gets outline navigation and folding); everything
else -- math, tables, the paracol columns, labels, prose -- is passed
through completely unchanged as raw text. The .tex preamble and the
closing \\end{document} are embedded verbatim in HTML comments at the
top/bottom of the .md, so the single .md file is self-contained.

A MathJax macro block (\\gdef versions of the preamble's \\newcommand
math macros) is inserted for live preview in Obsidian; it is stripped
out again when converting back to .tex, so edit macros in the .tex
preamble, not in that block.

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
MACRO_BEGIN = "<!-- MACROS-FOR-OBSIDIAN-PREVIEW-START -->"
MACRO_END = "<!-- MACROS-FOR-OBSIDIAN-PREVIEW-END -->"

HEADER_RE = re.compile(
    r'^\\(section|subsection|subsubsection)(\*)?\{(.*?)\}(?:\\label\{([^}]+)\})?\s*$'
)
LEVEL = {'section': '#', 'subsection': '##', 'subsubsection': '###'}
LEVEL_REV = {'#': 'section', '##': 'subsection', '###': 'subsubsection'}

MD_HEADER_RE = re.compile(
    r'^(#{1,3})\s+(.*?)(?:\s*\{\{label:([^}]+)\}\})?(?:\s*(\{\{starred\}\}))?\s*$'
)

NEWCOMMAND_RE = re.compile(r'\\newcommand\{(\\[a-zA-Z]+)\}(\[[0-9]\])?\{(.*)\}')

# text-mode-only commands: macros whose body uses these are layout, not
# math, and would break inside a $$...$$ MathJax preview block.
TEXT_MODE_MARKERS = (r'\par', r'\vspace', r'\noindent', r'\nobreak',
                     r'\ignorespaces', r'\textbf', r'\emph', r'\Needspace')


def newcommand_to_gdef(preamble_text):
    lines = []
    for name, arity, body in NEWCOMMAND_RE.findall(preamble_text):
        if any(marker in body for marker in TEXT_MODE_MARKERS):
            continue
        if arity:
            n = int(arity.strip('[]'))
            args = ''.join(f'#{i + 1}' for i in range(n))
            lines.append(rf'\gdef{name}{args}{{{body}}}')
        else:
            lines.append(rf'\gdef{name}{{{body}}}')
    return lines


def to_md(tex_path, md_path):
    lines = pathlib.Path(tex_path).read_text().split('\n')
    begin_idx = next(i for i, l in enumerate(lines) if l.strip() == r'\begin{document}')
    end_idx = next(i for i, l in enumerate(lines) if l.strip() == r'\end{document}')
    preamble = '\n'.join(lines[:begin_idx + 1])
    body_lines = lines[begin_idx + 1:end_idx]
    footer = '\n'.join(lines[end_idx:])

    out_body = []
    for l in body_lines:
        m = HEADER_RE.match(l)
        if m:
            kind, star, title, label = m.groups()
            marker = ''
            if label:
                marker += f' {{{{label:{label}}}}}'
            if star:
                marker += ' {{starred}}'
            out_body.append(f'{LEVEL[kind]} {title}{marker}')
        else:
            out_body.append(l)

    macro_lines = newcommand_to_gdef(preamble)
    macro_block = (
        f'{MACRO_BEGIN}\n$$\n' + '\n'.join(macro_lines) + '\n$$\n'
        '*(live-preview macros only, mirrors the .tex preamble; '
        'stripped on reconversion -- edit macros there, not here)*\n'
        f'{MACRO_END}'
    )

    md = (
        f'{PREAMBLE_BEGIN}\n{preamble}\n{PREAMBLE_END}\n\n'
        f'{macro_block}\n\n'
        + '\n'.join(out_body).strip('\n') + '\n\n'
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

    macro_start = rest.index(MACRO_BEGIN)
    macro_end = rest.index(MACRO_END) + len(MACRO_END)
    rest = rest[:macro_start] + rest[macro_end:]

    footer_start = rest.index(FOOTER_BEGIN)
    body = rest[:footer_start]
    footer, _ = _extract(FOOTER_BEGIN, FOOTER_END, rest[footer_start:])

    out_lines = []
    for l in body.split('\n'):
        m = MD_HEADER_RE.match(l)
        if m:
            hashes, title, label, starred = m.groups()
            kind = LEVEL_REV[hashes]
            star = '*' if starred else ''
            lab = f'\\label{{{label}}}' if label else ''
            out_lines.append(f'\\{kind}{star}{{{title.strip()}}}{lab}')
        else:
            out_lines.append(l)

    tex = preamble.strip('\n') + '\n' + '\n'.join(out_lines).strip('\n') + '\n\n' + footer.strip('\n') + '\n'
    pathlib.Path(tex_path).write_text(tex)


if __name__ == '__main__':
    mode, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    if mode == 'to-md':
        to_md(src, dst)
    elif mode == 'to-tex':
        to_tex(src, dst)
    else:
        raise SystemExit('mode must be to-md or to-tex')
