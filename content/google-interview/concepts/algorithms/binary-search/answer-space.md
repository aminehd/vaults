---
title: "Binary Search on Answer Space"
date: 2026-05-26
tags: [algorithms, binary-search, pigeonhole, mental-models, interview-patterns]
difficulty: medium-hard
related: ["[[google-interview/find-duplicate-number]]"]
---

# Binary Search on Answer Space

The hardest binary search problems aren't searching an array — they're searching **the space of possible answers**.

## The Mental Model Shift

Most people learn binary search as:
> "Find a value in a sorted array by halving the index range."

The real, more powerful version is:
> **"Find the boundary where a property flips — by halving the search space."**

Binary search works whenever you can answer:
*"Is the answer in the left half or the right half?"* in O(n) or less.

The array doesn't need to be sorted. You're not searching the array at all — you're searching the **number line of possible answers**.

---

## The Flip Property

Every binary search on answer space has a property that is monotone:

```
false false false false | true true true true
                        ^
                   find this boundary
```

Your job is to define that property and check which side of `mid` it lives on.

---

## Pigeonhole as a Counting Tool

Many answer-space problems use the **Pigeonhole Principle** as the O(n) check:

> If `n+1` numbers are crammed into `n` slots, at least one slot has two occupants.

For a midpoint `mid` in value space:
- There are exactly `mid` distinct values in `[1, mid]`
- Count how many array elements fall in `[1, mid]`
- If `count > mid` → pigeonhole says a duplicate is hiding in `[1, mid]` → search left
- Otherwise → search right

---

## Template

```python
lo, hi = <min_possible_answer>, <max_possible_answer>
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid):   # property is true at mid → try to go smaller
        hi = mid
    else:               # property is false → must go larger
        lo = mid + 1
return lo
```

**Key rules:**
- `lo = mid + 1` (never `lo = mid`) — prevents infinite loop when hi = lo + 1
- `hi = mid` (not `mid - 1`) — because `mid` itself might be the answer
- Return `lo` (== `hi` at termination)

---

## Real-World Analogies

| Problem | Search space | Flip property |
|---------|-------------|---------------|
| `git bisect` | commit timeline | "does the bug exist?" |
| Load testing | requests/sec | "does the server drop packets?" |
| Find corrupt batch | row ranges | "does this half have bad checksums?" |
| LC 287 | values 1..n | "does [1..mid] have more numbers than slots?" |

---

## Reference Problem: Find the Duplicate Number

**LC 287** · [leetcode.com/problems/find-the-duplicate-number](https://leetcode.com/problems/find-the-duplicate-number/)

Array of `n+1` integers in `[1, n]`, exactly one duplicate. Find it in O(n log n) time, O(1) space.

```python
def findDuplicate(nums: list[int]) -> int:
    lo, hi = 1, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        count = sum(1 for x in nums if x <= mid)
        if count > mid:   # too many numbers squeezed into [1..mid]
            hi = mid
        else:
            lo = mid + 1
    return lo
```

**Common mistakes:**
- Starting `lo = 0` instead of `1` (values start at 1, not 0)
- Counting `x >= mid` instead of `x <= mid` (backwards pigeonhole)
- Writing `lo = mid` instead of `lo = mid + 1` (infinite loop)
- Flipping the condition (`count <= mid → lo`) — wrong direction

---

## Similar Problems Using the Same Pattern

- [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) — search on eating speed
- [Capacity to Ship Packages](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) — search on ship capacity
- [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) — search on max subarray sum
- [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)
