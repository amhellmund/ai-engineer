---
name: new-tutorial
description: Scaffold and write a new course tutorial for a given day/topic. Use when asked to "write/draft/add a tutorial" for this AI-engineering curriculum, or for a specific day number or topic from PLAN.md. Produces a Quarto .qmd plus its paired Colab notebook following the repo template, as a draft for human review.
---

# Author a new tutorial

This skill drafts one tutorial for the 120-day curriculum. Tutorials are AI-drafted and
**human-reviewed**: your output is a `status: draft` PR, not a publish. See `CLAUDE.md` for
conventions and structural invariants.

## Inputs

Identify the target tutorial from the user's request — usually a **day number (1–120)** or a
topic name. If ambiguous, ask.

## Steps

1. **Look up the topic.** Open [PLAN.md](../../../PLAN.md), find the day by its global number,
   and note its title + section. This is the source of truth for scope.

2. **Derive slug & paths.** From the section and topic, build:
   - Tutorial: `sections/NN-section/NN-topic.qmd` (leading `NN` = the global day number).
   - Notebook: `notebooks/NN-section/NN-topic.ipynb`.
   - Images (if any): `assets/img/NN/<name>.png`.

   The `NN-section` slug must match an existing folder / the sidebar in `_quarto.yml`. Reuse a
   neighboring tutorial's filename style for consistency (kebab-case).

3. **Copy the template.** Start from [`_templates/tutorial-template.qmd`](../../../_templates/tutorial-template.qmd).
   Study the gold-standard
   [`sections/01-foundations/03-numpy-arrays-and-vectorization.qmd`](../../../sections/01-foundations/03-numpy-arrays-and-vectorization.qmd)
   for the target depth and tone.

4. **Fill the front matter.** `title` ("Day N — …"), `day`, `course-section`,
   `est-time: "30 min"`, `status: draft`, 3–5 `objectives`, `prerequisites`, and the
   `notebook:` path. (Use `course-section`, not `section` — `section` is reserved by Quarto.)

5. **Write the body.** Keep it ~30 minutes of reading + doing. Include:
   - The "In this tutorial" intro callout (what / why / prerequisites).
   - Concept sections with **≥1 diagram** (`{mermaid}` or `{dot}`) and **≥1 formula** (`$$`).
   - A **worked example**. Lightweight code goes in executed `{python}` cells; **GPU-only code
     must be a non-executed ```` ```python ```` block** with the runnable version in the notebook.
   - **Key takeaways.**
   - **References & further reading** (flat list of sources cited) plus a **Further references
     and details** section: annotated external resources to go deeper, each line noting *what*
     it adds and *why* it's worth the reader's time.

6. **Write exactly 5 control questions**, each answer in a `::: {.callout-tip title="Show
   answer" collapse="true"}` block.

7. **Write exactly 2 Python coding tasks.** Each has a problem statement, a
   `{{< colab notebooks/NN-section/NN-topic.ipynb >}}` badge, and a collapsible solution.

8. **Create the paired notebook** at the `notebook:` path: a title/intro markdown cell, then
   for each task a markdown prompt + a starter code cell with `TODO`s (not the solution).
   Keep it valid `nbformat` 4. Heavy sections should note the Colab GPU runtime.

9. **Generate figures** if used. Prefer code-generated plots; for committed static images use
   an ephemeral env: `uv run --with matplotlib --with numpy python <script>`. Save to
   `assets/img/NN/`.

10. **Render to verify.** `uv run quarto render sections/NN-section/NN-topic.qmd`. Fix any
    errors. Because of `freeze`, commit the resulting `_freeze/` changes too.

11. **Self-check the invariants** before opening the PR:
    - [ ] 8-part anatomy present and in order (incl. "Further references and details")
    - [ ] exactly **5** control questions, each with a collapsible answer
    - [ ] exactly **2** coding tasks, each with a Colab badge + collapsible solution
    - [ ] ≥1 diagram and ≥1 formula
    - [ ] complete front matter incl. `status: draft` and `notebook:`
    - [ ] paired notebook exists, is valid, and has starter (not solved) cells
    - [ ] no GPU code in executed `{python}` cells
    - [ ] renders cleanly

12. **Open a PR** on a branch for human review. Do not flip `status` to `reviewed` — that's the
    human reviewer's call.
