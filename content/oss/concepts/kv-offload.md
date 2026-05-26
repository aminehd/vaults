---
name: "KV Offload"
slug: "kv-offload"
---

# KV Offload

KV Offload is a technique used in large language models to reduce the memory footprint of the KV cache. The KV cache stores the key and value pairs for each token in the sequence, and it can grow very large for long sequences. KV Offload moves the KV cache from the GPU memory to the CPU memory or even to disk.

This matters because it allows running larger models or longer sequences on the same hardware. It solves the problem of the KV cache becoming a bottleneck for memory-intensive applications.

**Appears in:**
- [[../vllm|vLLM]]

**Related:**
- [[../kv-cache|KV Cache]]
- [[../paged-attention|Paged Attention]]
