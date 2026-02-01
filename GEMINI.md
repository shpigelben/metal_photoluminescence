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
