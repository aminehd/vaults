---
concept: "Policy Gradient / RL Basics"
slug: policy-gradient
tags: [rl, gymnasium, training]
repos: [Gymnasium]
updated: 2026-05-24
---

# Policy Gradient / RL Basics

**Repos:** [[../gymnasium|Gymnasium]]

Reinforcement learning framework: an agent takes actions in an environment,
receives rewards, and learns a policy to maximize cumulative reward.

## Key Concepts
- **State (s)**: what the agent observes
- **Action (a)**: what the agent does
- **Reward (r)**: feedback signal from environment
- **Policy π(a|s)**: probability of action given state
- **Value function V(s)**: expected cumulative reward from state s
- **Advantage A(s,a)**: how much better action a is vs average

## Policy Gradient Theorem
∇J(θ) = E[∇log π_θ(a|s) · A(s,a)]

Update policy to increase probability of actions that got better-than-average reward.

## Gymnasium Role
Provides the standard `env.step(action)` → `(obs, reward, done, info)` API.
Every RL algorithm trains against this interface.

## Related
- [[rlhf|RLHF]] — applies RL to align LLMs with human preferences

