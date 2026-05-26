---
name: "Mamba"
slug: "mamba"
---

# Mamba

Mamba is a new state space model (SSM) architecture that improves on the transformer architecture by enabling linear-time sequence modeling. Unlike transformers, which have quadratic complexity in the attention mechanism, Mamba's design allows it to process long sequences much more efficiently.

This matters because it makes it feasible to train on much longer contexts, which is crucial for tasks like document summarization, video understanding, and time-series analysis. Mamba solves the scalability problem of transformers while maintaining or exceeding their performance on many benchmarks.

**Appears in:**
- [[../vllm|vLLM]]

**Related:**
- [[../transformer-architecture|Transformer Architecture]]
