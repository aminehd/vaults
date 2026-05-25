---
slug: kv-connector
---

# KV Connector

The **KV Connector** in vLLM is a system that manages the transfer of the [[../concepts/kv-cache|KV cache]] between the GPU and other storage tiers, like CPU memory or a file system. This is a form of **offloading**.

## Why it matters

When serving very long sequences or large batches, the KV cache can consume a huge amount of GPU memory. The KV Connector allows vLLM to handle these cases by moving parts of the cache off the GPU, freeing up VRAM for computation and allowing for larger effective context windows than would otherwise be possible.

It's a key component for enabling efficient inference with limited GPU memory.

## Repos

- [[../vllm|vLLM]]
