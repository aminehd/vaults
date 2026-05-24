---
concept: "LoRA"
slug: lora
tags: [fine-tuning, peft, adapters, training]
repos: [PEFT, Unsloth, TRL]
updated: 2026-05-24
---

# LoRA

**Repos:** [[../peft|PEFT]] · [[../unsloth|Unsloth]] · [[../trl|TRL]]

Low-Rank Adaptation — fine-tune large models by learning small rank-decomposition
matrices instead of updating all weights.

## Key Idea
Freeze the original weight matrix W. Add a trainable bypass: ΔW = B × A
where B ∈ R^(d×r), A ∈ R^(r×k), and r << min(d, k).

At inference: W' = W + αΔW. Can merge adapters into base weights for zero overhead.

## Why It Works
Most weight updates during fine-tuning are low-rank in practice. LoRA exploits this.

## Typical Settings
- r = 8 to 64 (rank)
- α = r (scaling, often set equal to rank)
- target_modules: q_proj, v_proj, up_proj, down_proj

## Related
- [[qlora|QLoRA]] — LoRA on a 4-bit quantized base model
- [[peft-overview|PEFT Overview]] — broader family of methods

