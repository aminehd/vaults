---
repo: "PEFT"
slug: peft
languages: [Python, Makefile, Dockerfile, CUDA]
---

# PEFT — Codebase Structure

← [[../peft|Back to PEFT]]

## Directory Map

```mermaid
graph TD
    root[peft/] --> src[src/peft/]
    root --> tests[tests/]
    root --> docs[docs/]
    root --> examples[examples/]
    src --> tuners[tuners/ — one dir per method]
    src --> utils[utils/]
    src --> mapping[mapping.py — method registry]
    tuners --> lora[lora/]
    tuners --> qlora[adalora/]
    tuners --> ia3[ia3/]
    tuners --> prefix[prefix_tuning/]
    examples --> lora_ex[causal_language_modeling/]
```

## What Each Directory Does

- **src/peft/tuners/** — one subdirectory per PEFT method: LoRA, AdaLoRA, IA³, prefix tuning, prompt tuning
- **src/peft/mapping.py** — registry mapping method names to classes — update this when adding a new method
- **src/peft/utils/** — shared utilities: model loading, config handling, merging
- **tests/** — one test file per tuner method
- **examples/** — fine-tuning scripts for each method

## Key Entry Points for Contributing

- `src/peft/tuners/` — add a new PEFT method (self-contained, clear template to follow)
- `tests/` — add tests for an existing tuner
- `examples/` — add a fine-tuning example for a specific use case
- `docs/source/` — document a tuner's hyperparameters and usage
