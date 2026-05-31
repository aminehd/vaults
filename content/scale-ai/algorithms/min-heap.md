---
tags: [algorithm, heap, priority-queue, scale-ai]
problems: [task-scheduler, kth-largest, llm-batching]
---

# Min-Heap / Priority Queue

## Core Idea
heapq is a **min-heap**. For max-heap or priority inversion: **negate the value**.

## Templates
```python
import heapq

# Push/pop
heapq.heappush(heap, item)
item = heapq.heappop(heap)
item = heap[0]  # peek without popping

# Min-heap of size k (for kth largest)
heap = []
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)
return heap[0]  # kth largest

# Priority queue with negation (highest priority first)
heapq.heappush(heap, (-priority, name, task))
priority_neg, name, task = heapq.heappop(heap)
```

## Kahn's Algorithm (heap + indegree for topo sort)
```python
# indegree[node] = number of unresolved dependencies
# Only push to heap when indegree == 0
# On complete: decrement indegree of all unlocked nodes, push if hits 0
```

## Complexity
- Push/pop: O(log n)
- Peek: O(1)
- Build heap from list: O(n)

## When to use
- Task scheduler (priority + deps)
- Kth largest/smallest
- Dijkstra's shortest path
- LLM batching (priority requests)
