---
repo: "PEFT"
slug: peft
issues_count: 3
updated: 2026-05-25
---

# PEFT — Contribution Opportunities

Adding new PEFT methods is a well-defined contribution path.

← [[../peft|Back to PEFT]]

## Open Issues (3)

- **[#3223 TorchaoLoraLinear: __init__() missing get_apply_tensor_subclass kwarg with torchao 0.17 (PEFT 0.19.1)](https://github.com/huggingface/peft/issues/3223)**
  opened 2026-05-11 · 1 comments
  > ## TL;DR  PEFT 0.19.1's `TorchaoLoraLinear` adapter has a constructor signature incompatibility with torchao 0.17 — `__init__()` is missing the `get_apply_tensor_subclass` kwarg that the dispatcher ex

- **[#3182 RFC: Improve code to resolve LoRA variants](https://github.com/huggingface/peft/issues/3182)**
  opened 2026-04-21 · 10 comments
  > In PEFT, we support different LoRA variants, e.g. DoRA. Which LoRA variant, if any, should be used is currently implemented in `resolve_lora_variant`. For `lora.Linear`, the method looks like this:  h

- **[#2310 Comparison of Different Fine-Tuning Techniques for Conversational AI](https://github.com/huggingface/peft/issues/2310)** `good first issue` `help wanted` `contributions-welcome`
  opened 2025-01-07 · 68 comments
  > ### Feature request  It would be incredibly helpful to have a clear comparison or support for various fine-tuning techniques specifically for conversational AI. This feature could include insights int
