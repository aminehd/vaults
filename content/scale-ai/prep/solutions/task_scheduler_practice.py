from ast import Set
from dataclasses import dataclass, field
from typing import List, Any, Dict, Tuple, Set
import heapq
from enum import Enum

class Status(Enum):
    P = 'pending'
    I = 'in-progress'
    C = 'completed'
@dataclass
class Task:
    name: str 
    priority: int
    status : Status = Status.P
    dep: List = field(default_factory=list)
    indegree : int = 0
    

    def is_ready(self):
        return self.indegree == 0 
    
    
@dataclass
class TaskScheduler:
    pending_heap : List[Tuple(int, str, Task)] = field(default_factory=list)
    completed: Set = field(default_factory=set)
    task_map: Dict[str, Task] = field(default_factory=dict)
    unblock_next: Dict[str, List] = field(default_factory=dict)
    
    
    def add_task(self, name: str, priority: int, dep=[]) -> Task:
        task = Task(name=name, priority=priority, dep=dep)

        
        # data structure to keep pending tasks is a min heap
        indegree = sum(1 for x in dep if x not in self.completed)
        task.indegree = indegree
        
        if indegree == 0:
            heapq.heappush(self.pending_heap, (-priority, name, task))
        self.task_map[name] = task
        
        
        # add blocking info
        for task_name in dep: 
            if task_name not in self.unblock_next:
                self.unblock_next[task_name] = []
            self.unblock_next[task_name].append(task)
            
            
        return task
    
    def next_task(self):
        if not self.pending_heap:
            return None

        neg_pri, name, task =  heapq.heappop(self.pending_heap) 
        task.status = Status.I
        return task

        
        # for i, (neg_pri, name , task) in enumerate(self.pending_heap):
        #     if task.is_ready():
        #         task.status = Status.I
        #         self.pending_heap.pop (i)
        #         return task
        
        return None
    def complete_task(self, task_name: str):
        task = self.task_map[task_name]
        task.status = Status.C

        

        self.completed.add(task.name)

        
        # also unblock it 
        
        for unblocked_task in self.unblock_next.get(task_name, []):
            unblocked_task.indegree -= 1
            if unblocked_task.indegree == 0:
                heapq.heappush(self.pending_heap, (-unblocked_task.priority, unblocked_task.name, unblocked_task))
            
        

    
    
    
def test_dep():
    s = TaskScheduler()
    s1 = s.add_task(name='A', priority = 2)
    s2 = s.add_task(name='B', priority=5, dep=['A'])
    assert len(s.pending_heap) == 1
    assert s.unblock_next['A'] == [s2] 
    
    
    first_task = s.next_task()
    assert first_task == s1
    s.complete_task(s1.name)
    last_task = s.next_task()
    assert last_task == s2
    
test_dep()



# def test_ordered():
#     s = TaskScheduler()
#     s1 = s.add_task(name='A', priority = 2)
#     s2 = s.add_task(name='B', priority=5)
#     assert len(s.pending_heap) == 2
#     next_task = s.next_task()
#     assert next_task == s2
#     assert s2.status == Status.I
    
#     s.complete_task(s2.name)
    
#     last_task = s.next_task()
#     assert last_task == s1
#     s.complete_task(s1.name)
#     assert len(s.completed) == 2