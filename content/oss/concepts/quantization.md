---
concept: "Quantization"
slug: quantization
tags: [kernels, memory, inference, training]
repos: [bitsandbytes, PEFT]
updated: 2026-05-24
---

# Quantization

**Repos:** [[../bitsandbytes|bitsandbytes]] · [[../peft|PEFT]]

Represent model weights in lower precision (INT8, INT4, NF4) to reduce memory
and speed up inference, with minimal quality loss.

## Types
- **INT8**: 8-bit integer. ~2x memory reduction. bitsandbytes LLM.int8()
- **NF4**: 4-bit NormalFloat. Optimal for normally distributed weights. Used in QLoRA.
- **GPTQ**: post-training quantization. Calibration dataset required.
- **AWQ**: activation-aware weight quantization. Better than GPTQ on outliers.

## The Outlier Problem
~0.1% of weights are extreme outliers. Naive INT8 degrades quality.
bitsandbytes solution: keep outlier features in fp16, quantize rest to INT8 (LLM.int8()).

## Memory Estimates (7B model)
- fp32: 28 GB
- bf16: 14 GB
- INT8: 7 GB
- NF4: 3.5 GB

## Related
- [[qlora|QLoRA]] — fine-tuning on NF4 quantized model
- [[lora|LoRA]] — adapters stay in fp16 while base model is quantized

