---
problem: travel-optimizer
date: 2026-05-31
started: 07:31
status: in-progress
tags: [scale-ai, practice, coding]
---

# Travel Optimizer (TSP) · 2026-05-31

## Problem

> 📋 **LeetCode Discuss** · Rejected Scale AI Backend Interview · [Source](https://leetcode.com/discuss/post/6782775/)

Real Scale AI backend practical. Two steps:

**Step 1 — API integration** (use the mock server at `http://localhost:5001`):
- `GET /places?name=<name>` → `{"place_id": "pid_..."}`
- `GET /routes?from=<id>&to=<id>` → `{"duration_minutes": 45}`

Convert a list of resort names + home address to place IDs, then get driving times between every pair.

**Step 2 — Find the optimal route**:
Start at home, visit every resort exactly once, return home. Minimize total driving time.
This is TSP. Brute force is fine for small N (≤ 8). Greedy nearest-neighbor for larger.

```python
home = "123 Main St, Vancouver"
resorts = ["Whistler Blackcomb", "Sun Peaks Resort", "Big White Ski Resort"]
```

**Mock server is already in `ScaleAI/Coding/mock_api_server.py`** — run it first.

---

## My Approach

*Not yet recorded.*

---

## Code Attempts

*No attempts yet.*

---

## Session Summary

*Session in progress...*
