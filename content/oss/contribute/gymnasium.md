---
repo: "Gymnasium"
slug: gymnasium
issues_count: 6
updated: 2026-05-25
---

# Gymnasium — Contribution Opportunities

Adding new environments or wrappers is well-defined. Core RL infrastructure.

← [[../gymnasium|Back to Gymnasium]]

## Open Issues (6)

- **[#1585 [Proposal] Faster PyGame Init](https://github.com/Farama-Foundation/Gymnasium/issues/1585)** `enhancement`
  opened 2026-05-24 · 0 comments
  > ### Proposal  Per the comment in https://github.com/Farama-Foundation/PettingZoo/issues/1252  If I'm correct that the suggestion is correct, and we aren't doing this in Gymnasium already, then we prob

- **[#1559 [Proposal] Add fully tunable transition dynamics (including deterministic mode) to LunarLander](https://github.com/Farama-Foundation/Gymnasium/issues/1559)** `enhancement`
  opened 2026-04-21 · 1 comments
  > ### Proposal  I propose extending Gymnasium’s latest ``LunarLander`` implementation with explicit transition-dynamics controls so users can easily tune or disable stochasticity and physical coefficien

- **[#1504 [Bug Report] RecordEpisodeStatistics docstring example shows final_observation/info, but the implementation does not provide them.](https://github.com/Farama-Foundation/Gymnasium/issues/1504)** `bug`
  opened 2025-12-28 · 2 comments
  > ### Describe the bug  There is a discrepancy between the [docstring](https://github.com/Farama-Foundation/Gymnasium/blob/43965e15c2424a2b6955c79e774b0810457fd5be/gymnasium/wrappers/vector/common.py#L6

- **[#1501 [Proposal] Support heterogeneous graph spaces](https://github.com/Farama-Foundation/Gymnasium/issues/1501)** `enhancement`
  opened 2025-12-21 · 1 comments
  > ### Proposal  Gymnasium should support graph spaces which contain multiple types of nodes and multiple types of edges with potentially different sized spaces for each type of node or edge.  ### Motiva

- **[#1476 [Proposal] Make the Tuple space a generic class](https://github.com/Farama-Foundation/Gymnasium/issues/1476)** `enhancement`
  opened 2025-11-05 · 0 comments
  > ### Proposal  Allow developers to specify the "sub-types" when dealing with a Tuple space. E.g., `observation_space: spaces.Tuple[spaces.MultiDiscrete, spaces.Box]`  ### Motivation  It's more clear an

- **[#1468 [Question] Inconsistency Between reset() Docstring and REINFORCE Tutorial: Seeding Every Episode](https://github.com/Farama-Foundation/Gymnasium/issues/1468)** `question`
  opened 2025-10-20 · 0 comments
  > ### Question  In the documentation for the `reset()` method of the `gym.Env` class, it states: "If you pass an integer, the PRNG will be reset even if it already exists. Usually, you want to pass an i
