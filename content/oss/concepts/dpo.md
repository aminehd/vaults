---
concept: "DPO"
slug: dpo
tags: [alignment, training, fine-tuning, preference]
repos: [TRL]
updated: 2026-05-24
---

# DPO

**Repos:** [[../trl|TRL]]

Direct Preference Optimization — align LLMs with human preferences without a
separate reward model or RL loop.

## Key Insight
The optimal reward function can be expressed analytically in terms of the policy
itself. Eliminates the reward model training + PPO loop.

## Loss Function
L_DPO = -E[(log σ(β log(π(y_w|x)/π_ref(y_w|x)) - β log(π(y_l|x)/π_ref(y_l|x))))]

Where y_w = preferred response, y_l = rejected response.

## Advantages Over RLHF
- Only 2 model copies (policy + frozen reference) instead of 4
- Stable training — no RL instability
- Simpler to implement

## Related
- [[rlhf|RLHF]] — predecessor
- [[lora|LoRA]] — usually combined with DPO for efficiency

