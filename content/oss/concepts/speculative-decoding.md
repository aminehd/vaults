---
name: "Speculative Decoding"
slug: "speculative-decoding"
---

# Speculative Decoding

Speculative decoding is a technique to speed up inference in large language models. It works by using a smaller, faster "drafter" model to generate a sequence of tokens, and then using the larger, more powerful "target" model to verify the generated sequence in parallel.

This matters because it can significantly reduce the latency of generating long sequences of text. It solves the problem of the high computational cost of running the target model for every single token.

**Appears in:**
- [[../nemo-automodel|NeMo Automodel]]

**Related:**
- [[../transformer-architecture|Transformer Architecture]]
