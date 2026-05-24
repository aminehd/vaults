---
concept: "QLoRA"
slug: qlora
tags: [fine-tuning, quantization, peft, training]
repos: [PEFT, Unsloth, bitsandbytes]
updated: 2026-05-24
---

# QLoRA

**Repos:** [[../peft|PEFT]] · [[../unsloth|Unsloth]] · [[../bitsandbytes|bitsandbytes]]

Quantized LoRA — fine-tune a 4-bit quantized base model with LoRA adapters on top.
Enables fine-tuning 70B models on a single A100.

## How It Works
1. Quantize base model to NF4 (4-bit NormalFloat) using bitsandbytes
2. Add LoRA adapters (kept in fp16/bf16)
3. Gradients flow through adapters only — base weights never update

## Memory Savings
70B model: ~35 GB (bf16) → ~18 GB (NF4) with minimal quality loss.

## Related
- [[lora|LoRA]] — the adapter method
- [[quantization|Quantization]] — the compression technique

