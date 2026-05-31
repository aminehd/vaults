---
tags: [algorithm, intervals, scale-ai]
problems: [party-times, dedup-pipeline]
---

# Merge Intervals + Dead Zones

## Core Idea
Sort intervals by start time. Merge greedily: if next.start <= current.end, extend current.end = max(both ends).

## Template
```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

## Dead Zones (gaps between merged intervals)
```python
dead = sum(merged[i+1][0] - merged[i][1] for i in range(len(merged)-1))
```

## Complexity
- Sort: O(n log n)
- Merge sweep: O(n)

## When to use
- Party times dead zones
- Meeting room scheduling
- Calendar conflict detection
- Dedup: checking coverage gaps

## Common bugs
- Forgetting to sort first
- Using `<` instead of `<=` for merge condition
- Mutating original list
