---
concept: "Continuous Batching"
slug: continuous-batching
tags: [inference, throughput, serving]
repos: [vLLM, SGLang]
updated: 2026-05-24
---

# Continuous Batching

**Repos:** [[../vllm|vLLM]] · [[../sglang|SGLang]]

Iteration-level batching: instead of waiting for all sequences in a batch to finish
before starting new ones, insert new requests into the batch at each decoding step.

## Before (Static Batching)
Batch waits for the *longest* sequence. GPU sits idle once short sequences finish.

## After (Continuous Batching)
As soon as a sequence finishes, a new one takes its slot. GPU utilization stays high.

## Result
3-10x higher throughput on real workloads compared to static batching.

## Related
- [[paged-attention|PagedAttention]] — makes continuous batching practical

