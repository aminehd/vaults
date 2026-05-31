---
title: "Binary Search: The Two Templates"
date: 2026-05-26
tags: [algorithms, binary-search, templates, interview-patterns]
difficulty: medium
related: ["[[answer-space]]", "[[classic-sorted-array]]"]
---

# Binary Search: The Two Templates

Binary search has two common forms that confuse everyone. Know which one fits your problem.

---

## Template 1 — exact match in sorted array

```python
lo, hi = 0, len(arr) - 1
while lo <= hi:           # ← note: <=
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid        # ← return inside the loop
    elif arr[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
return -1                 # not found
```

**Use when:** you're looking for an exact value and want to return early.

---

## Template 2 — find a boundary

```python
lo, hi = <left_bound>, <right_bound>
while lo < hi:            # ← note: strict <
    mid = (lo + hi) // 2
    if feasible(mid):     # property is true → try smaller
        hi = mid          # ← mid stays in range
    else:
        lo = mid + 1      # ← mid is eliminated
return lo                 # lo == hi at termination
```

**Use when:** you're finding the *smallest* value where a condition becomes true.

---

## The Rules That Trip Everyone Up

| Question | Answer |
|----------|--------|
| `lo <= hi` or `lo < hi`? | `<=` for exact match, `<` for boundary |
| `hi = mid` or `hi = mid - 1`? | `mid` in template 2 (mid might be the answer), `mid-1` in template 1 |
| `lo = mid + 1` or `lo = mid`? | **Always `mid + 1`** — `lo = mid` infinite-loops when `hi = lo + 1` |
| What to return? | Template 1: return inside loop or -1. Template 2: return `lo` |

---

## Why `lo = mid` is a Trap

When `lo = 4, hi = 5`:
```
mid = (4 + 5) // 2 = 4
lo  = mid = 4     ← nothing changed, infinite loop
```

`lo = mid + 1` moves lo past mid, guaranteeing progress.

---

## Deciding Which Template

Ask: *"Am I looking for an exact value, or the first position where something becomes true?"*

- Exact value → Template 1
- First/smallest/minimum that satisfies a condition → Template 2
- Binary search on answer space → always Template 2
