# =============================================================================
# TASK SCHEDULER — Scale AI Coding Interview (Phase 1, 2, 3)
# =============================================================================
#
# Build a service that manages a queue of annotation work.
#
# PHASE 1 — Basic Scheduling:
#   - add_task(task_id, priority)
#   - get_next() → returns the highest priority task and marks it in_progress
#   - complete_task(task_id) → marks task as done
#
#   Priority: higher number = higher priority
#   Tasks have states: pending → in_progress → completed
#
# PHASE 2 — Dependencies:
#   - add_task(task_id, priority, deps=[]) where deps is list of task_ids
#   - get_next() should NOT return a task if any of its deps are not completed
#
# PHASE 3 — Optimization:
#   - What is the runtime of get_next()?
#   - How would you handle two workers calling get_next() at the same time?
#   - What if you need to support task cancellation?
#
# KEY DATA STRUCTURES TO THINK ABOUT:
#   - heap (heapq) → O(log n) get_next
#   - dict  → O(1) task lookup by id
#   - set   → O(1) completed task membership check
#
# =============================================================================

import heapq
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

class Status(Enum):
    PENDING     = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED   = 'completed'

@dataclass
class Task:
    task_id:  str
    priority: int
    deps:     List[str] = field(default_factory=list)
    status:   Status    = Status.PENDING

    # heapq is a min-heap, negate priority for max-heap behaviour
    def __lt__(self, other):
        return self.priority > other.priority


class TaskScheduler:
    def __init__(self):
        self.tasks     = {}   # task_id → Task
        self.heap      = []   # min-heap of Tasks (negated priority)
        self.completed = set()# task_ids that are done

    # ── Phase 1 ──────────────────────────────────────────────────────────────

    def add_task(self, task_id: str, priority: int, deps: List[str] = []):
        # TODO
        pass

    def get_next(self) -> Optional[Task]:
        # TODO: return highest priority task whose deps are all completed
        pass

    def complete_task(self, task_id: str):
        # TODO
        pass


# =============================================================================
# TESTS
# =============================================================================

def test_phase1_basic():
    s = TaskScheduler()
    s.add_task('A', priority=1)
    s.add_task('B', priority=5)
    s.add_task('C', priority=3)

    task = s.get_next()
    assert task.task_id == 'B', f"expected B got {task.task_id}"  # highest priority
    s.complete_task('B')

    task = s.get_next()
    assert task.task_id == 'C', f"expected C got {task.task_id}"
    print("phase 1 basic: PASS")

def test_phase2_deps():
    s = TaskScheduler()
    s.add_task('A', priority=1)
    s.add_task('B', priority=5, deps=['A'])  # B blocked until A done

    task = s.get_next()
    assert task.task_id == 'A', f"expected A (B is blocked), got {task.task_id}"
    s.complete_task('A')

    task = s.get_next()
    assert task.task_id == 'B', f"expected B (now unblocked), got {task.task_id}"
    print("phase 2 deps: PASS")

def test_phase2_no_available():
    s = TaskScheduler()
    s.add_task('A', priority=5, deps=['B'])  # A blocked
    s.add_task('B', priority=3, deps=['A'])  # B blocked — circular!

    task = s.get_next()
    assert task is None, "expected None — all tasks blocked"
    print("phase 2 no available: PASS")

if __name__ == '__main__':
    test_phase1_basic()
    test_phase2_deps()
    test_phase2_no_available()
