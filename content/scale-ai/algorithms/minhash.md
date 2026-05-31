---
tags: [algorithm, hashing, similarity, scale-ai]
problems: [dedup-pipeline]
---

# MinHash / Jaccard Similarity

## Core Idea
Estimate Jaccard similarity between two sets without comparing every pair.
Jaccard(A,B) = |A∩B| / |A∪B|

## Shingling
Break text into overlapping k-character windows (shingles):
```python
def shingle(text, k=3):
    return {text[i:i+k] for i in range(len(text)-k+1)}
# "hello" k=3 → {"hel","ell","llo"}
```

## MinHash fingerprint
```python
def fingerprint(text, num_hashes=64):
    shingles = shingle(text)
    return [min(hash((s, seed)) for s in shingles)
            for seed in range(num_hashes)]
```

## Jaccard estimate
```python
def jaccard_estimate(fp1, fp2):
    return sum(a == b for a, b in zip(fp1, fp2)) / len(fp1)
```

## LSH (Locality-Sensitive Hashing) for scale
Split fingerprint into b bands of r rows each.
Two docs are candidates if ANY band matches exactly.
- More bands → higher recall (find more near-dups), more false positives
- Fewer bands → higher precision, miss some near-dups
- Threshold ≈ (1/b)^(1/r)

## Complexity
- O(n) fingerprint, O(n²) naive comparison → O(n) with LSH candidates
