---
problem: dedup-pipeline
date: 2026-05-31
started: 10:34
status: in-progress
tags: [scale-ai, practice, coding]
---

# Crowdsourced Data Deduplication Pipeline · 2026-05-31

## Problem

> 📋 **Gotham Loop** · Crowdsourced Data Dedup · 5/10

**Common 5/10** — Scale AI literally runs this on their labeling data.

Scale ingests crowdsourced text contributions that often contain duplicate or near-duplicate records. Build a deduplication pipeline.

---

**Part 1 - Exact Dedup**

```python
def exact_dedup(records: list[dict]) -> list[dict]
```

Each record has `id` (int) and `content` (str). Remove exact duplicates (same `content`), keeping the record with the **smallest id**. Return deduplicated list.

---

**Part 2 - MinHash Fingerprint**

```python
def shingle(text: str, k: int = 3) -> set[str]:
    # All k-character substrings of text
    # "hello" k=3 -> {"hel", "ell", "llo"}

def fingerprint(text: str, num_hashes: int = 64) -> list[int]:
    # For each of num_hashes seeds, compute min hash over all shingles
    # Use: hash((shingle, seed)) for each shingle, take the min
```

---

**Part 3 - Near-Duplicate Clustering**

```python
def near_dedup(records, threshold=0.8, k=3, num_hashes=64)
    -> (list[dict], list[list[int]])
```

1. Compute fingerprints for all records
2. Estimate Jaccard similarity between pairs: `similarity = matching_hashes / num_hashes`
3. Group into clusters where any two records have similarity >= threshold
4. Keep the smallest-id record per cluster, discard the rest
5. Return `(deduplicated_list, clusters)` where clusters are lists of original IDs

---

**Part 4 - Scale (discuss in chat)**

Naive O(n²) pairwise is too slow for millions of records. Explain how **LSH (Locality-Sensitive Hashing)** reduces the candidate pair space. What's the time complexity improvement?

---

**Follow-ups:**
1. How would you handle deduplication across multiple languages?
2. How would you run this incrementally as new records stream in?
3. What quality metrics would you track?

---

## My Approach

*Not yet recorded.*

---

## Code Attempts

*No attempts yet.*

---

## Session Summary

*Session in progress...*
