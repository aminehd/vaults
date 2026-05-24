---
concept: "Transformer Architecture"
slug: transformer-architecture
tags: [architecture, attention, nlp, fundamentals]
repos: [Transformers, vLLM, TRL, PEFT]
updated: 2026-05-24
---

# Transformer Architecture

**Repos:** [[../transformers|Transformers]] · [[../vllm|vLLM]] · [[../trl|TRL]] · [[../peft|PEFT]]

The dominant neural network architecture for language models. Introduced in
"Attention is All You Need" (Vaswani et al., 2017).

## Core Components
1. **Token Embeddings**: convert tokens to vectors
2. **Positional Encoding**: inject position information (RoPE, ALiBi, learned)
3. **Attention Block**: Multi-head self-attention (or GQA/MQA)
4. **FFN Block**: two linear layers with activation (SwiGLU in modern models)
5. **LayerNorm**: pre-norm (before attention) in modern architectures

## Modern Variants
- **GQA** (Grouped Query Attention): fewer KV heads than Q heads → less KV cache
- **RoPE**: rotary positional embeddings — relative positions, extrapolates better
- **SwiGLU**: gated activation function, better than ReLU/GELU in practice
- **RMSNorm**: simpler than LayerNorm, same quality

## Key Papers
- Original Transformer (2017)
- BERT (encoder-only, 2018)
- GPT series (decoder-only, 2018+)
- LLaMA (open decoder-only, 2023)

## Related
- [[flash-attention|Flash Attention]] — optimizes the attention computation
- [[kv-cache|KV Cache]] — caches K,V from previous tokens
- [[lora|LoRA]] — adapts transformer weights efficiently

