---
concept: "KV Cache"
slug: kv-cache
tags: [inference, memory, transformers]
repos: [vLLM, SGLang, FlashAttention]
updated: 2026-05-24
---

# KV Cache

**Repos:** [[../vllm|vLLM]] · [[../sglang|SGLang]] · [[../flashattention|FlashAttention]]

During autoregressive generation, the Key and Value tensors from previous tokens
don't change. Caching them avoids recomputing attention over the full context at
each step — reduces generation from O(n²) to O(n) per new token.

## Memory Cost
A single KV cache entry = `2 × num_layers × num_heads × head_dim × dtype_bytes`.
For Llama-3 70B: ~160 GB for a 128k context sequence. This is the main memory
bottleneck in LLM serving.

## Related
- [[paged-attention|PagedAttention]] — how vLLM manages KV cache memory
- [[flash-attention|Flash Attention]] — computes attention without materializing full KV

