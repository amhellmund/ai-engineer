# CLAUDE.md

Agent guide for this repository. Read this before authoring or editing tutorials.

## What this repo is

A **120-day, hands-on AI engineering curriculum** published as a [Quarto](https://quarto.org)
website. One tutorial per day (~30 min), grouped into 24 sections of 5 tutorials. The full
topic list — the **source of truth for what each day covers** — is [PLAN.md](PLAN.md); reader
overview is [README.md](README.md).

## Authoring workflow: AI drafts, humans review

Tutorials are **drafted by an AI agent and reviewed by a human** before publishing:

1. **Draft** — author a tutorial via the **`new-tutorial` skill** (see below). New tutorials
   carry `status: draft` in their front matter and go up as a **PR on a branch**, never
   committed straight to `develop`.
2. **Review** — a human checks technical accuracy, structure, and runnable code.
3. **Approve** — the reviewer flips `status: draft` → `status: reviewed`; merging to `develop`
   triggers the GitHub Pages build.

**To write a new tutorial, invoke the `new-tutorial` skill.** It walks the full process and
copies the canonical skeleton at [`_templates/tutorial-template.qmd`](_templates/tutorial-template.qmd).

## Structural invariants (enforced in review)

Every tutorial **must**:

- Follow the 8-part anatomy: **(1)** "In this tutorial" intro callout → **(2)** concept
  sections → **(3)** worked example → **(4)** key takeaways → **(5)** Check your understanding
  → **(6)** Coding tasks → **(7)** References → **(8)** Further references and details
  (annotated external resources to go deeper).
- Contain **exactly 5 control questions**, each with a collapsible answer callout.
- Contain **exactly 2 Python coding tasks**, each with an `{{< colab … >}}` badge and a
  collapsible solution.
- Include **at least one diagram** (`{mermaid}` or `{dot}`) and **at least one formula**
  (`$$ … $$`).
- Have complete front matter: `title`, `day`, `course-section`, `est-time`, `status`,
  `objectives` (3–5 bullets), `prerequisites`, `notebook`. (Use `course-section`, not
  `section` — Quarto reserves `section` for a number.)

## File & path conventions

| Thing | Location | Example |
|-------|----------|---------|
| Tutorial | `sections/NN-section/NN-topic.qmd` | `sections/01-foundations/03-numpy-arrays-and-vectorization.qmd` |
| Paired notebook | `notebooks/NN-section/NN-topic.ipynb` | `notebooks/01-foundations/03-numpy-arrays-and-vectorization.ipynb` |
| Images / figures | `assets/img/NN/<name>.png` | `assets/img/01/broadcasting.png` |

- `NN-section` slugs are fixed and listed in [`_quarto.yml`](_quarto.yml) (the sidebar). The
  leading number on a tutorial file is its **global day number** (1–120) from PLAN.md.
- The `{{< colab >}}` shortcode (in `_extensions/colab/`) builds Colab URLs from the
  `colab-repo` / `colab-branch` keys in `_quarto.yml` — pass it the notebook path only.
- Reference an image from a tutorial with a relative path: `../../assets/img/NN/<name>.png`.

## Reference example

[`sections/01-foundations/03-numpy-arrays-and-vectorization.qmd`](sections/01-foundations/03-numpy-arrays-and-vectorization.qmd)
is the **gold-standard tutorial** — it exercises every required element. Match its shape and
depth when authoring new ones.

## Setup & build

This project uses [`uv`](https://docs.astral.sh/uv/) and Quarto.

```bash
uv sync                         # create .venv from pyproject.toml / uv.lock
uv run quarto preview           # live-reload preview while authoring
uv run quarto render            # full build into _site/
```

### The `freeze` rule (important)

`execute: freeze: auto` is set in `_quarto.yml`. Executed code-cell outputs are cached under
`_freeze/`, **which is committed**. This lets CI render the site **without running code and
without a GPU**. Consequences:

- After changing any `{python}` cell, **re-render locally** so `_freeze/` updates, and commit
  the `_freeze/` changes alongside the `.qmd`.
- **Never put GPU-only code in an executed `{python}` cell.** Show it as a non-executed
  ```` ```python ```` block and keep the runnable version in the paired Colab notebook.

## Generating figures

Prefer code-generated figures. For static images committed to `assets/`, generate them with
an ephemeral env rather than polluting project deps, e.g.:

```bash
uv run --with matplotlib --with numpy python path/to/make_figure.py
```
