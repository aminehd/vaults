---
repo: "Transformers"
slug: transformers
languages: [Python, Dockerfile, Makefile, Shell]
---

# Transformers — Codebase Structure

← [[../transformers|Back to Transformers]]

## Directory Map

```mermaid
graph TD
    root[transformers/] --> src[src/transformers/]
    root --> tests[tests/]
    root --> docs[docs/]
    root --> examples[examples/]
    root --> scripts[scripts/]
    src --> models[models/ — one dir per model]
    src --> trainer[trainer.py + TrainingArgs]
    src --> tokenization[tokenization/]
    src --> pipelines[pipelines/]
    src --> utils[utils/]
    tests --> models_tests[models/]
    examples --> pytorch[pytorch/]
```

## What Each Directory Does

- **src/transformers/models/** — one subdirectory per model family (llama/, qwen2/, gemma/) — the main contribution target
- **src/transformers/pipelines/** — high-level task pipelines (text-generation, question-answering)
- **src/transformers/trainer.py** — training loop, deepspeed/FSDP integration
- **tests/models/** — model-specific tests, one file per model
- **examples/pytorch/** — full fine-tuning and inference scripts
- **docs/source/** — model cards, API docs, tutorials

## Key Entry Points for Contributing

- `src/transformers/models/<new_model>/` — add a new model (most common contribution)
- `tests/models/` — add missing model tests
- `docs/source/` — improve model documentation
- `src/transformers/pipelines/` — add a new task pipeline
