# File Guide

This guide distinguishes the role of each file in the `research_design` folder.

## Notebooks

### `notebooks/child_like_agent_workshop.ipynb`

Primary workshop notebook.

Use this when you want:

- a live teaching flow
- explanation mixed with code and outputs
- a more presentation-oriented notebook experience

### `notebooks/child_like_agent_codelab.ipynb`

Codelab-style explanatory notebook.

Use this when you want:

- a step-by-step educational walkthrough
- markdown explanations alongside runnable code cells
- a notebook that mirrors the logic of the standalone Python script

## Script

### `scripts/child_like_agent.py`

Standalone Python implementation.

Use this when you want:

- a minimal local run from the terminal
- one clean source file for the prototype logic
- an easy starting point for modifications

## Documentation

### `docs/codelab.md`

Markdown codelab document.

Use this when you want:

- a written tutorial format
- a document that can be adapted for workshop notes or publishing
- a non-notebook explanation of the prototype

### `docs/file_guide.md`

This file.

Use this when you want:

- a quick orientation to the folder
- a way to distinguish which artifact to open first

## Visual Assets

### `assets/images/belief_update.png`

Supports explanation of how beliefs evolve.

### `assets/images/confidence_evolution.png`

Supports explanation of how confidence changes over time.

### `assets/images/feature_space.png`

Supports explanation of the representational view of the toy system.

## Suggested Workflow

1. Start with `README.md`.
2. Open `notebooks/child_like_agent_workshop.ipynb` for the live explanation.
3. Use `scripts/child_like_agent.py` for the simplest runnable version.
4. Refer to `docs/codelab.md` for written teaching notes.
