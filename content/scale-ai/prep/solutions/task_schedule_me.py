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
from dataclasses import dataclass, field
import enum
import pprint
from typing import Any, Dict, List, Tuple
import heapq
from enum import Enum

from numpy import block

class Status(Enum):
    P= 'pending'
    C= 'completed'
@dataclass
class Task:
    name: str
    priority: int
    deps: List[str]= field(default_factory=list)
    status: Status = Status.P
    indegree: int = 0

    def __post_init__(self):
        self.indegree = len(self.deps)
    
@dataclass
class TaskScheduler:
    tasks_heap: List[Tuple(int, str, Task)] = field(default_factory=list)
    task_map: Any=  field(default_factory=dict)
    completed: List[Any] = field(default_factory=list)
    blocked_by_me: Dict[str: list] = field(default_factory=dict)
     
    
    def add_task(self, name, priority, deps=[]) -> Task:
        task = Task(name=name, priority=priority, deps=deps)
        if task.indegree == 0:
            heapq.heappush(self.tasks_heap, (-task.priority, name, task))
        for blocking in deps:
            if blocking not in self.blocked_by_me:
                self.blocked_by_me[blocking] = []
            self.blocked_by_me[blocking].append(task)
        self.task_map[name] = task
        return task
    def _is_ready(self, task: Task):
        return task.indegree == 0
    def get_next(self):
        if not self.tasks_heap:
            return None
         
        pri_neg, name, task = heapq.heappop(self.tasks_heap)
        task.status = Status.C
        self.complete_task(task)
        return task
        # self.tasks_heap.sort(key = lambda x: x[0])
        # for i, (pri_neg, name, task) in enumerate(self.tasks_heap):
        #     if self._is_ready(task):
        #         task.status = Status.C
        #         self.tasks_heap.pop(i)
       # .       self.complete_task(task)

        #         return task
    def complete_task(self, task):
        if task.name not in self.blocked_by_me:
            return
        for blocked in self.blocked_by_me[task.name]:
             
            blocked.indegree -= 1
            if blocked.indegree == 0:
                heapq.heappush(self.tasks_heap, (- blocked.priority, blocked.name, blocked ))

        self.completed.append(task)
                
    
def test_phase1():
    s = TaskScheduler()
    s1 = s.add_task(name='A', priority=1)
    s2 = s.add_task(name='C', priority=2)
    assert len(s.tasks_heap) == 2
    task = s.get_next()
    assert task == s2
    assert s2.status == Status.C

def test_dep():
    s = TaskScheduler()
    s1 = s.add_task(name='A', priority=1)
    s2 = s.add_task(name='C', priority=2, deps = ['A'])
    pprint.pprint(f"{s.blocked_by_me=}")
    assert len(s.tasks_heap) == 1
    task = s.get_next()
    assert task == s1 
    task = s.get_next()
    print(task)
    assert task == s2 

test_dep()