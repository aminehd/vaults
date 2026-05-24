---
concept: "RLHF"
slug: rlhf
tags: [alignment, rl, training, fine-tuning]
repos: [TRL]
updated: 2026-05-24
---

# RLHF

**Repos:** [[../trl|TRL]]

Reinforcement Learning from Human Feedback — align LLM outputs with human preferences
using a reward model trained on human comparisons.

## Pipeline
1. **SFT** — supervised fine-tune on demonstrations
2. **Reward Model** — train on (chosen, rejected) pairs from human raters
3. **PPO** — optimize policy against reward model using proximal policy optimization

## Limitations
- Expensive (requires human labeling + RM training + PPO loop)
- Reward hacking: policy learns to exploit RM weaknesses
- Three separate model copies needed in memory

## Modern Alternatives
- [[dpo|DPO]] — skips reward model entirely
- [[grpo|GRPO]] — group relative policy optimization (DeepSeek's approach)

## Related
- [[dpo|DPO]] — simpler alternative now preferred
- [[ppo|PPO]] — the RL algorithm used

