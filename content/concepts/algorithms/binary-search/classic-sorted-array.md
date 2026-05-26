---
title: "Binary Search: Classic Sorted Array"
date: 2026-05-26
tags: [algorithms, binary-search, arrays, fundamentals]
difficulty: easy
related: ["[[template-rules]]", "[[answer-space]]"]
---

# Binary Search: Classic Sorted Array

The foundation. Works on any sorted collection where you can do random access.

---

## The Core Idea

Instead of scanning left to right (O(n)), always check the middle:
- Too small → throw away left half
- Too big → throw away right half
- Each step halves the search space → O(log n)

---

## Implementation

```python
def binary_search(arr: list[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

---

## Variants

**First occurrence** (leftmost duplicate):
```python
lo, hi = 0, len(arr) - 1
result = -1
while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == target:
        result = mid
        hi = mid - 1    # keep searching left
    elif arr[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
return result
```

**Last occurrence** (rightmost duplicate):
```python
# same but: lo = mid + 1 when arr[mid] == target
```

**First position ≥ target** (lower bound):
```python
lo, hi = 0, len(arr)   # hi = len, not len-1
while lo < hi:
    mid = (lo + hi) // 2
    if arr[mid] < target:
        lo = mid + 1
    else:
        hi = mid
return lo   # insertion point
```

---

## Complexity

| | Value |
|--|--|
| Time | O(log n) |
| Space | O(1) |

---

## Practice Problems

- [Binary Search](https://leetcode.com/problems/binary-search/) — LC 704, exact template
- [Search Insert Position](https://leetcode.com/problems/search-insert-position/) — lower bound variant
- [Find First and Last Position](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) — both first and last occurrence
- [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) — classic with a twist
