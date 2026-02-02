# Metal Photoluminescence Analysis

## Project Overview
This project is a computational study of photoluminescence in metals, focusing on modeling and analyzing electronic transitions (intraband and interband). It combines numerical simulations implemented in Python with comprehensive documentation and research notes managed in LaTeX and Obsidian.

## Project Structure

### `code/`
Contains the source code for simulations and analysis.
-   **`main/`**: The core production-ready scripts.
    -   `_preamble_and_funcs.py`: Shared physical constants and utility functions.
    -   `plot_style.py`: Centralized configuration for Matplotlib styles to ensure publication-quality figures.
    -   Numbered scripts (e.g., `0_numeric_convergence.py`) correspond to specific analysis stages or sections in the documentation.
-   **`sketches/`**: Jupyter notebooks (`.ipynb`) used for prototyping, exploratory analysis, and deriving mathematical approximations.
-   **`misc/`**: Interactive scripts and one-off tests.

### `docs/`
Contains the project's documentation and research notes.
-   **`.LaTeX/`**: The LaTeX source for the project's formal report/thesis.
    -   `main.tex`: The root document.
    -   `Makefile`: Instructions for building the PDF.
-   **`.obsidian/`**: Configuration for the Obsidian knowledge base, including plugins and themes.
-   **`notes/`**: Markdown files containing research notes, literature reviews, and daily logs.

### `figures/`
Stores generated plots and diagrams. These are often created by the scripts in `code/` and referenced in the LaTeX documentation.

## Setup and Usage

### Python Environment
The project uses a Python virtual environment.
1.  **Create/Activate Environment:**
    
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
2.  **Install Dependencies:**
    
    ```bash
    pip install -r code/requirements.txt
    ```

### Running Simulations
Scripts in `code/main/` are designed to be executed directly. They typically generate plots and save them to the `figures/` directory.

**Example:**
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
-   **Code Style:**
    -   Python 3 type hints are encouraged.
    -   Matplotlib configuration is centralized in `plot_style.py` to maintain visual consistency.
    -   Physical constants and shared math functions reside in `_preamble_and_funcs.py`.
-   **Workflow:**
    -   **Prototyping:** Use Jupyter notebooks in `code/sketches/` for initial derivation and testing.
    -   **Production:** Refine validated logic into scripts within `code/main/`.
    -   **Documentation:** Update Obsidian notes with findings, then formalize into LaTeX sections.

## Gemini Agent Protocols

### Canvas Workflow (`Gemini.canvas`)
This project utilizes an interactive "Canvas" workflow for non-linear research and Q&A. The master canvas is located at `docs/notes/Outline & Questions/Gemini.canvas`.

**Trigger Command:** `canvas reply`

**Persona:** Solid State Physics Research Assistant. Tone is academic and precise.

**Answer Style (Very Important):**
*   **Thoroughness:** Prefer a complete, structured answer over a short one. State assumptions and limitations.
*   **Math-first:** Focus on mathematics and derivations whenever possible (Hamiltonians, matrix elements, Kubo/Golden-rule forms, scaling, units).
*   **Actionable:** When relevant, include algorithmic steps, convergence criteria, and what to compute/plot to validate results.

**Formatting:**
*   **Markdown:** Use standard Markdown for structure.
*   **LaTeX:** Use `$$ ... $$` for both block and inline math (to ensure reliable rendering in Obsidian Canvas nodes).

**Execution Logic (Detailed Workflow the CLI Must Follow):**
1.  **Load and Validate Canvas JSON**
    *   Read `docs/notes/Outline & Questions/Gemini.canvas` as JSON.
    *   Verify the top-level keys `nodes` and `edges` exist and are lists. Abort with an explicit error message if parsing fails.
    *   Treat each `nodes[i]` object as authoritative (do not infer missing fields beyond safe defaults like `width/height`).
2.  **Identify the Active Question Node**
    *   A "question node" is a `type: "text"` node whose `text` begins with `# Question` or `Question`.
    *   Prefer the most recent *leaf* question node: a question node with **no outgoing** edge (i.e., it is not `fromNode` of any edge).
    *   If there are multiple leaf question nodes, choose the one with the greatest `y` coordinate (visually lowest) as a deterministic tie-breaker.
    *   If there are no leaf question nodes, fall back to the most recently added question node by array order.
3.  **Trace Context Backwards (Conversation Thread)**
    *   Build the ancestor chain by following **incoming** edges into the active question node:
        *   For a node `N`, its parents are any `edge.fromNode` where `edge.toNode == N.id`.
        *   Continue recursively until no parents exist.
    *   Collect the ordered thread context as: root context nodes -> intermediate notes -> active question node.
    *   If there is a `context_abstract` node, always include it at the start of context if it is connected in the ancestor chain.
4.  **Internal Research Pass (Local Vault-First)**
    *   Search `docs/notes/` for relevant prior material using ripgrep (preferred) on keywords extracted from the question and context:
        *   Examples: "intraband", "interband", "Kubo", "Fermi golden rule", "matrix element", "dielectric", "Drude", "broadening".
    *   Prefer using existing project notes and definitions over re-deriving from scratch if the derivation already exists.
    *   When referencing internal notes, use Obsidian links `[[Exact Filename]]` and verify the file exists (match the vault filename).
5.  **External Verification Pass (Only If Needed)**
    *   If internal notes are insufficient, do a targeted web lookup for standard formulas/constants or canonical references.
    *   Use reputable sources (textbooks, DOI papers, arXiv with care). Record enough bibliographic detail to be verifiable.
    *   Never invent citations or URLs.
6.  **Synthesize the Answer (Math-Heavy, Thorough)**
    *   Start with a compact "what to compute" statement, then provide the mathematical framework:
        *   Define quantities and units.
        *   Give the governing expressions (e.g., Golden rule/Kubo-Greenwood) and how intraband vs interband separate.
        *   State approximations (constant relaxation time, parabolic bands, rigid-band, etc.).
    *   Provide a practical recipe:
        *   Numerical steps (k-grid, smearing/broadening choice, convergence checks).
        *   Diagnostics (sum rules, limiting behavior, causality, scaling).
    *   If multiple valid approaches exist, present them as branches (A/B), with pros/cons and when each is appropriate.
7.  **Write the Answer Back to the Canvas (New Branch)**
    *   Create a new `type: "text"` node with a unique `id` (random hex or UUID-like string is fine).
    *   **Placement must be collision-free (this is the #1 failure mode):**
        *   Obsidian Canvas does **not** auto-flow or re-layout nodes. Editing JSON is like placing rectangles on a plane.
        *   "Appending" JSON does not mean the node appears "after" others; it appears exactly at its (`x`,`y`) coordinates.
        *   Therefore, before writing a new node you must perform a global collision check against **all existing nodes**.
    *   **Compute bounding boxes for collision checks**
        *   For every node `n`, define its axis-aligned bounding box (AABB):
            *   `left = n.x`
            *   `top = n.y`
            *   `right = n.x + n.width`
            *   `bottom = n.y + n.height`
        *   Two boxes intersect if:
            *   `new.left < old.right` AND `new.right > old.left` AND `new.top < old.bottom` AND `new.bottom > old.top`
        *   Treat an intersection as a hard error for layout (do not write overlapping nodes).
    *   **Never move existing nodes automatically**
        *   Do **not** shift or "push down" old nodes to make room. This is fragile and quickly ruins the user's hand-tuned layout.
        *   The only safe default is: keep all existing nodes unchanged; find free space for the new node.
    *   **Choose a deterministic placement strategy**
        *   Determine the "answer cluster" for the active question:
            *   Collect all edges where `edge.fromNode == question.id`.
            *   The connected `toNode` ids are existing answers/children; include their bounding boxes in placement decisions.
        *   Preferred layout: place answers to the right of the question, stacked top-to-bottom without overlap.
            *   Let `anchor_x = question.x + question.width + 40`
            *   Let `anchor_y = question.y`
            *   Use consistent sizes unless there is a reason not to (e.g., `width=420`, `height=240`).
        *   If there are existing answers already in that right-hand "column", place the new node **below the lowest bottom**:
            *   Let `col_nodes = all existing nodes whose AABB intersects the vertical strip [anchor_x, anchor_x + width]`
            *   Compute `y = max(bottom of col_nodes) + 40` (or `anchor_y` if none exist).
        *   If that still collides (because other unrelated nodes are in the way), search for the next free slot:
            *   Try `y += 40` repeatedly up to a cap (e.g., 50 attempts).
            *   If still blocked, shift to a new column: `x += width + 80` and restart the y-scan.
        *   Always re-check collisions after each candidate position.
    *   **Avoid the "spatial blindness" bug explicitly**
        *   Do not place a new node solely relative to the *previous* answer node. Example failure:
            *   If `Answer 1b` already starts at `y=680` and you place `Answer 1c` at `y=460` with `height=440`,
              then `Answer 1c` occupies `y=460..900` and overlaps `Answer 1b` (`y=680..1040`).
        *   The correct rule is global: `new_node` must not intersect **any** existing node AABB.
    *   Add a new edge connecting the question to the answer:
        *   `fromNode = question.id`, `toNode = answer.id`.
        *   Choose `fromSide`/`toSide` to reflect the placement (`right->left` if to the right, `bottom->top` if below).
    *   Preserve existing nodes/edges; only append.
8.  **Post-Write Checks**
    *   Re-parse the written JSON to ensure it remains valid.
    *   Confirm the new node id is present exactly once and that the new edge refers to existing node ids.
    *   Confirm no node bounding boxes overlap (optional but recommended): iterate all pairs and assert no intersections.

**Technical Note:**
To reply, read the `.canvas` file as JSON. Create a new `text` node with the response, positioned logically (e.g., to the right or below the question), and add an entry to the `edges` array connecting the question node to the new response node. Write the updated JSON back to the file.

**Citation Rules:**
*   **Internal:** Use Obsidian-style links `[[Filename]]`. Verify the filename exists.
*   **External:** Use `[Title](URL)`. Use only verified, reputable sources (DOIs, ArXiv, Textbooks). **No hallucinations.**
