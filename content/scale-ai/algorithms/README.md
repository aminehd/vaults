---
tags: [scale-ai, algorithms, reference]
---

# Algorithm Reference — Scale AI Interview Prep

| Algorithm | Problems | Key Idea |
|-----------|----------|----------|
| [[merge-intervals]] | party-times, dedup | Sort → merge greedy → find gaps |
| [[min-heap]] | task-scheduler, kth-largest, llm-batching | Negate for max, size-k for kth |
| [[state-machine]] | job-tracker | VALID_TRANSITIONS dict, append-only history |
| [[minhash]] | dedup-pipeline | k-shingles → min hash per seed → Jaccard estimate |
| [[bfs-dfs]] | node-distance, task-scheduler | BFS = shortest path, DFS = topo sort |
| [[sweep-line]] | calendar-three, party-times | +1 at start, -1 at end, max prefix sum |
