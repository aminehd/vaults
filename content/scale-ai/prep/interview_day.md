# Interview Day — Scale AI · April 10, 2026 · 11:30 AM PT

---

## Your Intro (60 seconds)

> "I'm a software engineer at Amazon on the Customer Service Data and AI Platform team. I built and maintain an internal multi-tenant ML platform — it lets ML scientists self-serve ETL workflows, model training, and agent deployments on sensitive customer data. It runs on EKS, Kubernetes, VPC-isolated environments, and I've built the Python SDK and CLI tooling on top of it. On the data side we handle around 50K TPS with Kinesis and Redis.
>
> What draws me to Scale is you're solving the same class of problems — multi-tenant, regulated environments, enterprise customers — but at the AI data layer, which is where the real leverage is right now. I've been working hands-on with LLMs and agentic workflows, so the GenAI platform work feels like a natural fit."

---

## How We Prepped Today (7:13 AM – 11:30 AM)

### What we worked through in order:

1. **Task Scheduler problem introduced** — read the spec, understood phases 1/2/3
2. **Round 1 (~40 min)** — wrote Phase 1 from scratch: heap, add_task, next_task, Status/Task
3. **Identified bugs** — missing `return task`, `get_next` calling `complete_task`, wrong lifecycle
4. **Added `complete_task`** — separate from `get_next`, correct lifecycle: PENDING → IN_PROGRESS → COMPLETED
5. **Round 2** — added deps: `indegree` on Task, `is_ready()`, heap scan loop, `unblock_next` map
6. **Fixed dep bugs** — `unblock_next` must be list not single task, `return Task` vs `return task`
7. **Round 3 (Kahn's optimization)** — only push indegree==0 to heap in `add_task`, restore `heappop` in `next_task`, unblock in `complete_task`
8. **All tests passing** — Phase 1 + Phase 2 complete
9. **Talked through Scale AI** — what SGP is, multi-cloud deployment model, how it maps to your Amazon experience
10. **Prepped questions to ask them** — deployment model, SDK surface, multi-cloud reality

---

## Coding Order for the Interview

```
1. Status(Enum)       PENDING, IN_PROGRESS, COMPLETED
2. Task               name, priority, deps=[], status, indegree, __post_init__
3. TaskScheduler      heap, task_map, completed(set), unlocks(dict)
4. add_task           build Task, push if indegree==0, build unlocks map
5. get_next           heappop, mark IN_PROGRESS, return task
6. complete_task      mark COMPLETED, decrement deps, push ready tasks
```

---

## Phase 3 Answers

- **`get_next` complexity** → O(log n) — heap pop
- **Concurrency** → `threading.Lock()` around heap ops, or use a queue with GIL-safe ops
- **Cancellation** → add `CANCELLED` to Status, skip in `get_next`, clean up `unlocks`

---

## One Question to Ask Them

> "Is SGP primarily hosted by Scale with customer integrations reaching into their data environments, or do you deploy the full platform into customer-owned accounts for regulated industries? I'm curious where the abstraction boundary sits."

---

## Bugs to NOT make today

- `return Task` → always lowercase `return task`
- `Tuple(int, str)` → `Tuple[int, str]` square brackets
- `Dict[str: list]` → `Dict[str, list]` comma
- `unblock_next[name] = task` → must be a list, `.append(task)`
- calling `complete_task` inside `get_next` — they are separate
- marking `COMPLETED` in `get_next` — mark `IN_PROGRESS` there, `COMPLETED` only in `complete_task`
- forgetting `return task` at end of `get_next`
- `field(default=[])` → `field(default_factory=list)`
