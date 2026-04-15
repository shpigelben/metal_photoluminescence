# Spaced Review

A lightweight Obsidian plugin for weighted-random spaced review of your notes.

## How it works

1. **Press the dice icon** (or run the "Draw a note for review" command)
2. The plugin filters your vault for notes matching a frontmatter property (default: `type: concept`)
3. It picks one at random, weighted so overdue notes are more likely to appear
4. The note opens, and a modal asks: **Solid** or **Revisit**
5. Based on your rating, the plugin updates the note's frontmatter with review metadata

### Spacing logic

- **New notes** (never reviewed): immediately eligible, weight = 1
- **Overdue notes** (`next_review` ≤ today): eligible, weight increases with days overdue
- **Not yet due**: skipped entirely
- **Solid**: interval doubles (1 → 2 → 4 → 8 → 16 → 32 days...)
- **Revisit**: interval resets to 1 day
- Random noise is injected into weights so draws aren't fully deterministic

### Frontmatter properties managed by the plugin

```yaml
last_reviewed: 2026-03-16
next_review: 2026-03-18
review_interval: 2
```

Your notes just need the filter property you configure (default: `type: concept`). The plugin adds the rest on first review.

## Installation

1. Copy the `spaced-review` folder into your vault at:
   ```
   <your-vault>/.obsidian/plugins/spaced-review/
   ```
2. The folder should contain: `manifest.json`, `main.js`, `styles.css`
3. In Obsidian, go to **Settings → Community Plugins → Installed Plugins**
4. Enable **Spaced Review**
5. (Optional) Configure the filter property/value and intervals in the plugin settings

## Settings

| Setting            | Default   | Description                                      |
|--------------------|-----------|--------------------------------------------------|
| Filter property    | `type`    | Frontmatter property to filter by                |
| Filter value       | `concept` | Required value of that property                  |
| Initial interval   | 1 day     | First review interval for new notes              |
| Solid multiplier   | 2.0       | Multiply interval by this on "Solid"             |
| Revisit interval   | 1 day     | Reset interval to this on "Revisit"              |
