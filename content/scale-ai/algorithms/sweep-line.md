---
tags: [algorithm, sweep-line, timeline, scale-ai]
problems: [calendar-three, party-times]
---

# Sweep Line / Timeline Events

## Core Idea
Convert interval problems into point events on a timeline.
At start: +1. At end: -1. Sweep left to right, track running sum.

## Template (My Calendar III)
```python
import bisect

timeline = []  # sorted list of (timestamp, delta)

def update(ts, delta):
    idx = bisect.bisect_left(timeline, (ts, float('-inf')))
    if idx < len(timeline) and timeline[idx][0] == ts:
        timeline[idx] = (ts, timeline[idx][1] + delta)
    else:
        bisect.insort(timeline, (ts, delta))

def max_overlap():
    curr = max_k = 0
    for _, delta in timeline:
        curr += delta
        max_k = max(max_k, curr)
    return max_k
```

## Key Insight
The max prefix sum of deltas = max simultaneous overlap count.
No need to check every pair of intervals — just scan the events.

## Complexity
- Update: O(n) due to bisect insert (or O(log n) with sorted container)
- Query: O(n) sweep

## When to use
- Booking overlap detection
- Party dead zones (gap = 0 count sections)
- Resource utilization over time
- Meeting room count
