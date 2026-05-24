---
concept: "PagedAttention"
slug: paged-attention
tags: [inference, memory, kv-cache]
repos: [vLLM, SGLang]
updated: 2026-05-24
---

# PagedAttention

**Repos:** [[../vllm|vLLM]] · [[../sglang|SGLang]]

Memory management technique for LLM inference. Stores KV cache in non-contiguous
blocks (like virtual memory paging in an OS) — eliminates fragmentation and enables
much higher GPU utilization.

## Key Idea
Instead of allocating a fixed contiguous chunk per sequence, allocate fixed-size
*pages* and map them dynamically. A sequence can grow without wasting GPU memory.

## Why It Matters
Enabled vLLM to serve 2-4x more concurrent requests than naive implementations.
Now the standard approach in production inference.

## Related
- [[kv-cache|KV Cache]] — what PagedAttention manages
- [[continuous-batching|Continuous Batching]] — works together with PagedAttention

