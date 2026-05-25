---
repo: "vLLM"
slug: vllm
languages: [Python, CUDA, Rust, C++]
---

# vLLM — Codebase Structure

← [[../vllm|Back to vLLM]]

## Directory Map

```mermaid
graph TD
    root[vllm/] --> vllm[vllm/ — core library]
    root --> csrc[csrc/ — CUDA/C++ kernels]
    root --> tests[tests/]
    root --> benchmarks[benchmarks/]
    root --> docs[docs/]
    root --> examples[examples/]
    root --> scripts[scripts/]
    root --> tools[tools/]
    vllm --> attention[attention/]
    vllm --> executor[executor/]
    vllm --> model_executor[model_executor/]
    vllm --> worker[worker/]
    csrc --> csrc_attention[attention/]
    csrc --> csrc_moe[moe/]
    csrc --> csrc_quant[quantization/]
```

## What Each Directory Does

- **vllm/** — Python core: scheduler, engine, attention backends, model loading, sampling
- **csrc/** — CUDA/C++ kernels: attention ops, MoE routing, quantization kernels
- **tests/** — unit + integration tests, one file per module
- **benchmarks/** — throughput/latency scripts, kernel benchmarks
- **examples/** — end-to-end usage scripts (offline, server, multimodal)
- **docs/** — user docs, architecture guides
- **scripts/** — CI helpers, model conversion tools
- **tools/** — profiling, debugging utilities

## Key Entry Points for Contributing

- `tests/` — add a test for an existing feature, very likely to merge
- `examples/` — add a usage example for a model or feature
- `docs/` — improve or add documentation
- `vllm/model_executor/models/` — add support for a new model architecture
