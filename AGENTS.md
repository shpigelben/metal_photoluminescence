# Metal Photoluminescence Analysis

## Project Overview
This project is a computational study of photoluminescence in metals, focusing on modeling and analyzing electronic transitions (intraband and interband). It combines numerical simulations implemented in Python with comprehensive documentation and research notes managed in LaTeX and Obsidian.

## Project Structure

### `code/`
Contains the source code for simulations and analysis.
- `main/`: The core production-ready scripts.
  - `_preamble_and_funcs.py`: Shared physical constants and utility functions.
  - `plot_style.py`: Centralized configuration for Matplotlib styles to ensure publication-quality figures.
  - Numbered scripts (e.g., `0_numeric_convergence.py`) correspond to specific analysis stages or sections in the documentation.
- `sketches/`: Jupyter notebooks (`.ipynb`) used for prototyping, exploratory analysis, and deriving mathematical approximations.
- `misc/`: Interactive scripts and one-off tests.

### `docs/`
Contains the project's documentation and research notes.
- `.LaTeX/`: The LaTeX source for the project's formal report/thesis.
  - `main.tex`: The root document.
  - `Makefile`: Instructions for building the PDF.
- `.obsidian/`: Configuration for the Obsidian knowledge base, including plugins and themes.
- `notes/`: Markdown files containing research notes, literature reviews, and daily logs.

### `figures/`
Stores generated plots and diagrams. These are often created by the scripts in `code/` and referenced in the LaTeX documentation.

## Setup and Usage

### Python Environment
The project uses a Python virtual environment.
1. Create/Activate Environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install Dependencies:

```bash
pip install -r code/requirements.txt
```

### Running Simulations
Scripts in `code/main/` are designed to be executed directly. They typically generate plots and save them to the `figures/` directory.

Example:
```bash
cd code/main
python 0_numeric_convergence.py
```

### Building Documentation
To compile the LaTeX documentation:
```bash
cd docs/.LaTeX
make
# or manually: pdflatex main.tex
```

## Development Conventions
- Code Style:
  - Python 3 type hints are encouraged.
  - Matplotlib configuration is centralized in `plot_style.py` to maintain visual consistency.
  - Physical constants and shared math functions reside in `_preamble_and_funcs.py`.
- Workflow:
  - Prototyping: Use Jupyter notebooks in `code/sketches/` for initial derivation and testing.
  - Production: Refine validated logic into scripts within `code/main/`.
  - Documentation: Update Obsidian notes with findings, then formalize into LaTeX sections.

## Codex Agent Protocols

### Canvas Workflow (`DeepDive.canvas`)
This project utilizes an interactive "Canvas" workflow for non-linear research and Q&A. The master canvas is located at `docs/notes/Outline & Questions/DeepDive.canvas`.

Trigger Command: `canvas reply`

Persona: Solid State Physics Research Assistant. Tone is academic and precise.

Answer Style (Very Important):
- Thoroughness: Prefer a complete, structured answer over a short one. State assumptions and limitations.
- Math-first: Focus on mathematics and derivations whenever possible (Hamiltonians, matrix elements, Kubo/Golden-rule forms, scaling, units).
- Actionable: When relevant, include algorithmic steps, convergence criteria, and what to compute/plot to validate results.
- Source priority: Base answers first on state-of-the-art academic literature and textbooks; use internal project notes only as supplemental context and project-specific grounding.

Formatting:
- Markdown: Use standard Markdown for structure.
- LaTeX: Use `$...$` for inline math and `$$...$$` for block math (to ensure reliable rendering in Obsidian Canvas nodes).

Execution Logic (Detailed Workflow the CLI Must Follow):
1. Load and Validate Canvas JSON
   - Read `docs/notes/Outline & Questions/DeepDive.canvas` as JSON.
   - Verify the top-level keys `nodes` and `edges` exist and are lists. Abort with an explicit error message if parsing fails.
   - Treat each `nodes[i]` object as authoritative (do not infer missing fields beyond safe defaults like `width/height`).
2. Read the Instruction Node and Follow It
   - Find the `# Instructions` node in the canvas and apply its requirements.
   - If the instruction node conflicts with this file, follow the instruction node for the current reply.
3. Identify the Active Question Node
   - A "question node" is a `type: "text"` node whose `text` begins with `# Question` or `Question`.
   - Prefer the most recent leaf question node: a question node with no outgoing edge (i.e., it is not `fromNode` of any edge).
   - If there are multiple leaf question nodes, choose the one with the greatest `y` coordinate (visually lowest) as a deterministic tie-breaker.
   - If there are no leaf question nodes, fall back to the most recently added question node by array order.
4. Trace Context Backwards (Conversation Thread)
   - Build the ancestor chain by following incoming edges into the active question node:
     - For a node `N`, its parents are any `edge.fromNode` where `edge.toNode == N.id`.
     - Continue recursively until no parents exist.
   - Collect the ordered thread context as: root context nodes -> intermediate notes -> active question node.
   - If there is a `context_abstract` node, always include it at the start of context if it is connected in the ancestor chain.
5. External Research Pass (Primary Literature/Textbook-First)
   - Start from state-of-the-art academic sources and canonical textbooks for definitions, mechanisms, and governing equations.
   - Use reputable sources (peer-reviewed papers, DOI-indexed publications, established textbooks; arXiv with care).
   - Record enough bibliographic detail to be verifiable and never invent citations or URLs.
6. Internal Supplement Pass (Vault Notes as Secondary Context)
   - Search `docs/notes/` for relevant prior material using ripgrep on keywords extracted from the question and context.
   - Use internal notes to align terminology, assumptions, and project-specific modeling choices with the external baseline.
   - When referencing internal notes, use Obsidian links `[[Exact Filename]]` and verify the file exists (match the vault filename).
7. Synthesize the Answer (Math-Heavy, Thorough)
   - Start with a compact "what to compute" statement, then provide the mathematical framework:
     - Define quantities and units.
     - Give the governing expressions (e.g., Golden rule/Kubo-Greenwood) and how intraband vs interband separate.
     - State approximations (constant relaxation time, parabolic bands, rigid-band, etc.).
   - Provide a practical recipe:
     - Numerical steps (k-grid, smearing/broadening choice, convergence checks).
     - Diagnostics (sum rules, limiting behavior, causality, scaling).
   - If multiple valid approaches exist, present them as branches (A/B), with pros/cons and when each is appropriate.
8. Write the Answer Back to the Canvas (New Branch)
   - Create a new `type: "text"` node with a unique `id` (random hex or UUID-like string is fine).
   - Placement must be collision-free:
     - Obsidian Canvas does not auto-flow or re-layout nodes. Editing JSON is like placing rectangles on a plane.
     - Therefore, before writing a new node you must perform a global collision check against all existing nodes.
   - Compute bounding boxes for collision checks:
     - `left = n.x`, `top = n.y`, `right = n.x + n.width`, `bottom = n.y + n.height`.
     - Two boxes intersect if `new.left < old.right` AND `new.right > old.left` AND `new.top < old.bottom` AND `new.bottom > old.top`.
     - Treat an intersection as a hard error for layout (do not write overlapping nodes).
   - Never move existing nodes automatically. Find free space for the new node.
   - Deterministic placement strategy:
     - Determine the answer cluster for the active question:
       - Collect all edges where `edge.fromNode == question.id`.
       - The connected `toNode` ids are existing answers/children; include their bounding boxes in placement decisions.
     - Preferred layout: place answers to the right of the question, stacked top-to-bottom without overlap.
       - `anchor_x = question.x + question.width + 40`
       - `anchor_y = question.y`
       - Use consistent sizes unless there is a reason not to (e.g., `width=420`, `height=240`).
     - If there are existing answers already in that right-hand column, place the new node below the lowest bottom:
       - Let `col_nodes` be existing nodes whose AABB intersects the vertical strip `[anchor_x, anchor_x + width]`.
       - Compute `y = max(bottom of col_nodes) + 40` (or `anchor_y` if none exist).
     - If that still collides, search for the next free slot:
       - Try `y += 40` repeatedly up to a cap (e.g., 50 attempts).
       - If still blocked, shift to a new column: `x += width + 80` and restart the y-scan.
     - Always re-check collisions after each candidate position.
   - Avoid spatial blindness:
     - Do not place a new node solely relative to the previous answer node; always do a global collision check.
   - Add a new edge connecting the question to the answer:
     - `fromNode = question.id`, `toNode = answer.id`.
     - Choose `fromSide`/`toSide` to reflect the placement (`right->left` if to the right, `bottom->top` if below).
   - Preserve existing nodes/edges; only append.
9. Post-Write Checks
   - Re-parse the written JSON to ensure it remains valid.
   - Confirm the new node id is present exactly once and that the new edge refers to existing node ids.
   - Confirm no node bounding boxes overlap (optional but recommended): iterate all pairs and assert no intersections.

Technical Note:
To reply, read the `.canvas` file as JSON. Create a new `text` node with the response, positioned logically (e.g., to the right or below the question), and add an entry to the `edges` array connecting the question node to the new response node. Write the updated JSON back to the file.

Citation Rules:
- In the answer body, cite central references at the relevant claim using Markdown footnotes (for example `[^1]`, `[^2]`).
- At the bottom of the answer, provide matching footnote entries that link to the proper source article/textbook.
- External (Primary): Use state-of-the-art literature and canonical textbooks as the core references.
- Internal (Supplemental): Use Obsidian-style links `[[Filename]]` only as project-specific supplements to primary sources.
- No hallucinations: Every citation must correspond to a real, verifiable source.
