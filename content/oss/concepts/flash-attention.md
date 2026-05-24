---
concept: "Flash Attention"
slug: flash-attention
tags: [kernels, attention, cuda, training]
repos: [FlashAttention, vLLM, SGLang]
updated: 2026-05-24
---

# Flash Attention

**Repos:** [[../flashattention|FlashAttention]] · [[../vllm|vLLM]] · [[../sglang|SGLang]]

IO-aware exact attention algorithm that computes standard attention 2-4x faster by
minimizing reads/writes to GPU HBM (high-bandwidth memory).

## The Problem
Standard attention materializes the full N×N attention matrix in HBM.
For N=4096, that's 128 MB per layer per batch. IO becomes the bottleneck.

## FlashAttention's Solution
Split Q, K, V into tiles. Compute attention in SRAM (fast, small) tile by tile,
never writing the full matrix to HBM. Uses the online softmax trick to do this
without the full matrix.

## Speedups
- 2-4x faster attention computation
- O(N) memory instead of O(N²)
- Enables much longer context lengths

## Versions
- FA1 (2022): original — 2x speedup
- FA2 (2023): 2x faster than FA1, better GPU utilization
- FA3 (2024): Hopper/H100 optimized

## Related
- [[triton-kernels|Triton Kernels]] — FlashAttention v2 has a Triton implementation
- [[kv-cache|KV Cache]] — FlashAttention computes attention without caching full matrices

