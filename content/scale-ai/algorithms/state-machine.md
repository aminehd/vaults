---
tags: [algorithm, state-machine, scale-ai]
problems: [job-tracker]
---

# State Machine

## Core Idea
Define valid transitions as a dict. Check membership before transitioning. Track history as append-only list.

## Template
```python
from enum import Enum

class State(str, Enum):
    A = "A"
    B = "B"
    C = "C"

VALID = {
    State.A: {State.B, State.C},
    State.B: {State.C},
    State.C: set(),  # terminal
}

def transition(current, new):
    if new not in VALID[current]:
        raise ValueError(f"Invalid: {current} → {new}")
    return new
```

## Stuck job detection
```python
stuck = [j for j in jobs if j['state'] == 'RUNNING'
         and current_time - j['updated_at'] > timeout]
stuck.sort(key=lambda j: current_time - j['updated_at'], reverse=True)
```

## When to use
- Job/task lifecycle tracking
- Order status pipelines
- Workflow engines
- Protocol state management
