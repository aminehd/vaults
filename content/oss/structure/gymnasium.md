---
repo: "Gymnasium"
slug: gymnasium
languages: [Python, Dockerfile, Shell]
---

# Gymnasium — Codebase Structure

← [[../gymnasium|Back to Gymnasium]]

## Directory Map

```mermaid
graph TD
    root[Gymnasium/] --> gymnasium[gymnasium/ — core library]
    root --> tests[tests/]
    root --> docs[docs/]
    gymnasium --> envs[envs/ — all environments]
    gymnasium --> spaces[spaces/ — action/obs spaces]
    gymnasium --> wrappers[wrappers/ — env transforms]
    gymnasium --> vector[vector/ — vectorized envs]
    gymnasium --> utils[utils/]
    envs --> classic[classic_control/]
    envs --> toy[toy_text/]
    envs --> mujoco[mujoco/]
    tests --> envs_t[envs/]
    tests --> spaces_t[spaces/]
    tests --> wrappers_t[wrappers/]
```

## What Each Directory Does

- **gymnasium/envs/** — all environments: classic_control (CartPole, MountainCar), toy_text, MuJoCo, Atari
- **gymnasium/spaces/** — observation and action space types (Box, Discrete, Dict, Tuple)
- **gymnasium/wrappers/** — env transformations: TimeLimit, RecordEpisodeStatistics, NormalizeObservation
- **gymnasium/vector/** — vectorized env execution (sync and async)
- **gymnasium/utils/** — env checking, passive checkers, seeding
- **tests/** — matches src structure exactly

## Key Entry Points for Contributing

- `gymnasium/wrappers/` — add a new environment wrapper (clear interface, fast merge)
- `gymnasium/envs/` — add a new environment or fix an existing one
- `tests/wrappers/` — add tests for existing wrappers
- `docs/` — improve environment documentation
