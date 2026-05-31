---
problem: neuron-states
date: 2026-05-31
started: 07:31
status: in-progress
tags: [scale-ai, practice, coding]
---

# Neuron States · 2026-05-31

## Problem

> 📋 **Gotham Loop #7 · 1/10**

Scale AI onsite/phone · **Rare 1/10**

Given a 2D matrix, compute the **next state** of all neurons simultaneously.

Each cell is a neuron. It fires if its value `> 0`, rests if `= 0`.
Count **firing neighbours** (8-directional, including diagonals).

**Transition rules (applied simultaneously to all cells):**

| Condition | Result |
|-----------|--------|
| Firing (`> 0`) AND exactly 3 neighbours firing | set to `6` |
| Non-firing (`= 0`) AND 1 or 0 neighbours firing | decrement by 2 (min 0) |
| Any neuron with **more than 3** neighbours firing | decrement by 1 (min 0) |
| Everything else | unchanged |

All rules applied to the **current state** simultaneously — don't update in-place.

```python
input_state = [
    [0, 0, 0],
    [0, 3, 0],
    [0, 0, 0],
]
# Cell (1,1) has 0 firing neighbours → decrement by 2 → 1
# All border cells have 1 firing neighbour (3>0) → unchanged (0)
```

**Follow-up:** What if the matrix is 10^6 x 10^6 but sparse (mostly zeros)?

---

## My Approach

*Not yet recorded.*

---

## Code Attempts

*No attempts yet.*

---

## Session Summary

*Session in progress...*
