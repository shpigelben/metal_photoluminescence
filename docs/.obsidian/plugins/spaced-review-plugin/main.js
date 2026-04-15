// Spaced Review Plugin for Obsidian
// Weighted random note selection with spaced repetition

const { Plugin, PluginSettingTab, Setting, Modal, Notice } = require("obsidian");

const DEFAULT_SETTINGS = {
  filterProperty: "type",
  filterValue: "concept",
  initialIntervalDays: 1,
  solidMultiplier: 2.0,
  revisitIntervalDays: 1,
  ribbonIcon: "dice",
};

class SpacedReviewSettingTab extends PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }

  display() {
    const { containerEl } = this;
    containerEl.empty();

    containerEl.createEl("h2", { text: "Spaced Review Settings" });

    new Setting(containerEl)
      .setName("Filter property")
      .setDesc("Frontmatter property to filter notes by")
      .addText((text) =>
        text
          .setPlaceholder("type")
          .setValue(this.plugin.settings.filterProperty)
          .onChange(async (value) => {
            this.plugin.settings.filterProperty = value;
            await this.plugin.saveSettings();
          })
      );

    new Setting(containerEl)
      .setName("Filter value")
      .setDesc("Required value of the filter property")
      .addText((text) =>
        text
          .setPlaceholder("concept")
          .setValue(this.plugin.settings.filterValue)
          .onChange(async (value) => {
            this.plugin.settings.filterValue = value;
            await this.plugin.saveSettings();
          })
      );

    new Setting(containerEl)
      .setName("Initial interval (days)")
      .setDesc("Days before first review of a new note")
      .addText((text) =>
        text
          .setPlaceholder("1")
          .setValue(String(this.plugin.settings.initialIntervalDays))
          .onChange(async (value) => {
            const n = parseFloat(value);
            if (!isNaN(n) && n > 0) {
              this.plugin.settings.initialIntervalDays = n;
              await this.plugin.saveSettings();
            }
          })
      );

    new Setting(containerEl)
      .setName("Solid multiplier")
      .setDesc('Multiply interval by this when you rate "Solid"')
      .addText((text) =>
        text
          .setPlaceholder("2.0")
          .setValue(String(this.plugin.settings.solidMultiplier))
          .onChange(async (value) => {
            const n = parseFloat(value);
            if (!isNaN(n) && n > 1) {
              this.plugin.settings.solidMultiplier = n;
              await this.plugin.saveSettings();
            }
          })
      );

    new Setting(containerEl)
      .setName("Revisit interval (days)")
      .setDesc('Reset interval to this many days when you rate "Revisit"')
      .addText((text) =>
        text
          .setPlaceholder("1")
          .setValue(String(this.plugin.settings.revisitIntervalDays))
          .onChange(async (value) => {
            const n = parseFloat(value);
            if (!isNaN(n) && n > 0) {
              this.plugin.settings.revisitIntervalDays = n;
              await this.plugin.saveSettings();
            }
          })
      );
  }
}

class ReviewModal extends Modal {
  constructor(app, file, plugin) {
    super(app);
    this.file = file;
    this.plugin = plugin;
  }

  onOpen() {
    const { contentEl } = this;
    contentEl.empty();
    contentEl.addClass("spaced-review-modal");

    contentEl.createEl("h3", { text: "How well do you know this?" });
    contentEl.createEl("p", {
      text: this.file.basename,
      cls: "spaced-review-filename",
    });

    const btnContainer = contentEl.createDiv({ cls: "spaced-review-buttons" });

    const revisitBtn = btnContainer.createEl("button", { text: "Revisit" });
    revisitBtn.addClass("spaced-review-btn", "spaced-review-revisit");
    revisitBtn.addEventListener("click", async () => {
      await this.plugin.rateNote(this.file, "revisit");
      this.close();
    });

    const solidBtn = btnContainer.createEl("button", { text: "Solid" });
    solidBtn.addClass("spaced-review-btn", "spaced-review-solid");
    solidBtn.addEventListener("click", async () => {
      await this.plugin.rateNote(this.file, "solid");
      this.close();
    });
  }

  onClose() {
    this.contentEl.empty();
  }
}

class SpacedReviewPlugin extends Plugin {
  async onload() {
    await this.loadSettings();

    this.addRibbonIcon(this.settings.ribbonIcon, "Spaced Review", () => {
      this.drawNote();
    });

    this.addCommand({
      id: "draw-review-note",
      name: "Draw a note for review",
      callback: () => this.drawNote(),
    });

    this.addSettingTab(new SpacedReviewSettingTab(this.app, this));
  }

  async loadSettings() {
    this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
  }

  async saveSettings() {
    await this.saveData(this.settings);
  }

  todayStr() {
    return window.moment().format("YYYY-MM-DD");
  }

  parseDateStr(s) {
    if (!s) return null;
    const m = window.moment(String(s), "YYYY-MM-DD", true);
    return m.isValid() ? m : null;
  }

  /**
   * Get all eligible notes and their weights.
   * A note is eligible if:
   *   - It has the right filter property/value
   *   - It is "due" (next_review <= today) OR has never been reviewed
   */
  getEligibleNotes() {
    const files = this.app.vault.getMarkdownFiles();
    const today = window.moment().startOf("day");
    const candidates = [];

    for (const file of files) {
      const cache = this.app.metadataCache.getFileCache(file);
      if (!cache || !cache.frontmatter) continue;

      const fm = cache.frontmatter;

      // Check filter
      const propVal = fm[this.settings.filterProperty];
      if (!propVal) continue;

      // Handle both string and array property values
      const values = Array.isArray(propVal) ? propVal : [propVal];
      const match = values.some(
        (v) => String(v).toLowerCase() === this.settings.filterValue.toLowerCase()
      );
      if (!match) continue;

      // Compute weight
      const nextReview = this.parseDateStr(fm["next_review"]);
      const interval = fm["review_interval"];

      if (!nextReview) {
        // Never reviewed — eligible, base weight 1
        candidates.push({ file, weight: 1.0 });
      } else if (nextReview.isSameOrBefore(today)) {
        // Due or overdue
        const daysOverdue = today.diff(nextReview, "days");
        candidates.push({ file, weight: 1.0 + daysOverdue * 0.15 });
      }
      // else: not yet due, skip
    }

    return candidates;
  }

  /**
   * Weighted random pick with randomness injected into weights.
   */
  weightedRandomPick(candidates) {
    if (candidates.length === 0) return null;

    // Inject randomness
    const weighted = candidates.map((c) => ({
      ...c,
      effectiveWeight: c.weight * (0.5 + Math.random()),
    }));

    const totalWeight = weighted.reduce((sum, c) => sum + c.effectiveWeight, 0);
    let roll = Math.random() * totalWeight;

    for (const c of weighted) {
      roll -= c.effectiveWeight;
      if (roll <= 0) return c.file;
    }

    return weighted[weighted.length - 1].file;
  }

  async drawNote() {
    const candidates = this.getEligibleNotes();

    if (candidates.length === 0) {
      new Notice(
        "No notes due for review! Pool is empty — all caught up."
      );
      return;
    }

    const file = this.weightedRandomPick(candidates);
    if (!file) return;

    // Open the note
    const leaf = this.app.workspace.getLeaf(false);
    await leaf.openFile(file);

    // Show rating modal
    new ReviewModal(this.app, file, this).open();

    new Notice(
      `${candidates.length} note${candidates.length === 1 ? "" : "s"} in review pool`
    );
  }

  async rateNote(file, rating) {
    const s = this.settings;

    await this.app.fileManager.processFrontMatter(file, (fm) => {
      const currentInterval = fm["review_interval"] || s.initialIntervalDays;
      let newInterval;

      if (rating === "solid") {
        newInterval = Math.round(currentInterval * s.solidMultiplier);
      } else {
        newInterval = s.revisitIntervalDays;
      }

      const nextReview = window
        .moment()
        .add(newInterval, "days")
        .format("YYYY-MM-DD");

      fm["last_reviewed"] = this.todayStr();
      fm["next_review"] = nextReview;
      fm["review_interval"] = newInterval;
    });

    const verb = rating === "solid" ? "Solid" : "Revisit";
    new Notice(`${verb} — see you later.`);
  }
}

module.exports = SpacedReviewPlugin;
