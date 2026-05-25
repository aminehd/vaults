---
repo: "NeMo Automodel"
slug: nemo-automodel
languages: [Python, Shell, MDX, Jupyter Notebook]
---

# NeMo Automodel — Codebase Structure

← [[../nemo-automodel|Back to NeMo Automodel]]

## Directory Map

```mermaid
graph TD
    root[Automodel/] --> nemo_automodel[nemo_automodel/ — core]
    root --> examples[examples/]
    root --> tests[tests/]
    root --> docs[docs/]
    root --> tutorials[tutorials/]
    root --> scripts[scripts/]
    root --> tools[tools/]
    nemo_automodel --> llm[llm/ — language models]
    nemo_automodel --> vlm[vlm/ — vision-language]
    nemo_automodel --> collections[collections/]
    examples --> llm_ex[llm_finetune/]
    examples --> vlm_ex[vlm_finetune/]
```

## What Each Directory Does

- **nemo_automodel/llm/** — LLM training: data loading, model configs, training loops
- **nemo_automodel/vlm/** — vision-language models (multimodal training)
- **nemo_automodel/collections/** — dataset and model collection utilities
- **examples/** — one folder per task: pretrain, finetune, generate, benchmark
- **tutorials/** — Jupyter notebooks for learning
- **docs/** — guides, launcher docs, model coverage matrix
- **tools/** — config validation (YAML linter), conversion scripts
- **scripts/** — CI and setup scripts

## Key Entry Points for Contributing

- `tools/` — YAML linting, config validation (zeel2104's pattern — fast merge)
- `docs/` — add tutorial, model coverage, guide
- `examples/` — add a new training example
- `tests/` — unit tests for data loading or model config
