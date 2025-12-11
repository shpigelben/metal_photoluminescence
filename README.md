```bash
/opt/homebrew/bin/python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

```text
repo/
├─ README.md
├─ .gitignore
├─ code/
│  ├─ src/
│  │  └─ ...               # Python modules
│  ├─ tests/               # Optional: unit tests
│  └─ requirements.txt     # Python dependencies
|
└─ docs/                   # Obsidian vault + research notes
   ├─ .obsidian/           # Obsidian configuration
   ├─ notes/               # Markdown research notes, daily logs, scratch files
   ├─ references/          # PDFs, citations, literature summaries
   ├─ figures/             # Images, diagrams, exported plots
   └─ assets/              # Misc supporting files (snippets, templates, etc.)
```

