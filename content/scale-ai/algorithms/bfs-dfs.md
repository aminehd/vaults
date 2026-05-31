---
tags: [algorithm, graph, tree, scale-ai]
problems: [node-distance, task-scheduler]
---

# BFS / DFS

## BFS (shortest path in unweighted graph)
```python
from collections import deque

def bfs(graph, start, end):
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1  # not found
```

## DFS (cycle detection, topological sort)
```python
def dfs(graph, node, visited, stack):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    stack.append(node)  # post-order for topo sort
```

## BFS in a tree (guaranteed shortest path)
In a tree, there's exactly **one** path between any two nodes.
BFS always finds it. Distance = number of edges traversed.

## Multi-source BFS (Part 2/3 of Node Distance)
Run BFS from all source nodes simultaneously.
Or: precompute BFS distances from each source, take min.

## Complexity
- BFS/DFS: O(V + E)
- Tree distance: O(N) per query
