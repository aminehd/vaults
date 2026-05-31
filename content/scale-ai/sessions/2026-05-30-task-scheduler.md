---
problem: task-scheduler
date: 2026-05-30
started: 23:00
status: in-progress
tags: [scale-ai, practice, coding]
---

# Task Scheduler · 2026-05-30

## Problem

Design a task scheduler that manages tasks with priorities and dependencies.

**Phase 1 — Basic priority queue**
- `add_task(name, priority)` — add a task
- `get_next()` — return highest-priority task, mark it IN_PROGRESS
- `complete_task(name)` — mark task COMPLETED

**Phase 2 — Dependencies**
- `add_task(name, priority, deps=[])` — task only becomes available when all deps are completed
- `get_next()` — returns highest-priority task with all deps satisfied, or None

**Phase 3 — Follow-up questions (answer in chat)**
- What's the complexity of `get_next()`?
- How would you handle concurrency?
- How would you support cancellation?

**Hint:** Start with `Status(Enum)`, then `Task` (dataclass), then `TaskScheduler`.

---

## My Approach

*Not yet recorded.*

---

## Code Attempts

*No attempts yet.*

---

## Session Summary

*Session in progress...*
