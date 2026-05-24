---
concept: "Mixture of Experts (MoE)"
slug: mixture-of-experts
tags: [architecture, scaling, inference]
repos: [DeepSeek-V3]
updated: 2026-05-24
---

# Mixture of Experts (MoE)

**Repos:** [[../deepseek-v3|DeepSeek-V3]]

Architecture where each token is processed by only a subset of *expert* FFN layers,
chosen by a router. Increases parameter count without proportionally increasing compute.

## How It Works
Replace each FFN with N experts + a router.
Router selects top-K experts per token (usually K=2 or K=8).
Only selected experts compute — others are skipped.

## DeepSeek-V3 Design
- 671B total params, ~37B active per token
- 256 experts, top-8 routing
- Auxiliary-loss-free load balancing (novel — avoids hurting model quality)
- Multi-Token Prediction (MTP) head for better training signal

## Tradeoffs
- **Pro**: Same compute as a dense ~37B model, but quality of 671B
- **Con**: All 671B params must fit in memory (across GPUs)

## Related
- [[transformer-architecture|Transformer Architecture]] — MoE replaces the FFN block

