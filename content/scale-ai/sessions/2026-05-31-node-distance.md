---
problem: node-distance
date: 2026-05-31
started: 07:31
status: in-progress
tags: [scale-ai, practice, coding]
---

# Node Distance in a Tree · 2026-05-31

## Problem

> 📋 **Gotham Loop #8 · 1/10**

Scale AI onsite/phone · **Rare 1/10**

Given a tree as a dict and two nodes, find the **shortest distance** between them.

```python
tree = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2, 6],
    6: [5],
}
distance(tree, 4, 6)  # -> 3  (4 -> 2 -> 5 -> 6)
distance(tree, 3, 6)  # -> 4  (3 -> 1 -> 2 -> 5 -> 6)
```

**Part 1:** Single pair `(a, b)` — return shortest path length.

**Part 2:** Given two sets `a_nodes = [a1, a2]` and `b_nodes = [b1, b2]`, find the shortest distance between **any** pair `(x, y)` where `x in a_nodes` and `y in b_nodes`.

**Part 3:** Generalise Part 2 to arbitrary-length sets.

**Key insight:** In a tree, there's exactly one path between any two nodes. The shortest path goes through the **Lowest Common Ancestor (LCA)**.
Distance = `depth(a) + depth(b) - 2 * depth(LCA(a, b))`

---

## My Approach

*Not yet recorded.*

---

## Code Attempts

*No attempts yet.*

---

## Session Summary

*Session in progress...*
