---
problem: job-tracker
date: 2026-05-31
started: 07:31
status: in-progress
tags: [scale-ai, practice, coding]
---

# Async Job Status Tracker · 2026-05-31

## Problem

> 📋 **Gotham Loop** · Async Job Status Tracker · 5/10

Real Scale AI problem - rated **10/10 popularity**.

You're building a job tracking service for long-running data processing jobs on a labeling platform. Jobs transition through states and clients poll for status updates.

---

**Part 1 — Job State Machine**

Implement a `JobTracker` class that manages job lifecycles.

Valid transitions:
```
PENDING → RUNNING → SUCCEEDED
PENDING → RUNNING → FAILED
PENDING → CANCELLED
RUNNING → CANCELLED
```
No other transitions are valid.

```python
class JobTracker:
    def create_job(self, job_id: str, metadata: dict) -> dict:
        # Create in PENDING state. Raise ValueError if job_id already exists.

    def transition(self, job_id: str, new_state: str) -> dict:
        # Raise ValueError on invalid transitions or unknown job_id.

    def get_status(self, job_id: str) -> dict:
        # Return current job state and metadata. Raise KeyError if not found.

    def list_jobs_by_state(self, state: str) -> list[dict]:
        # Return all jobs in given state, sorted by creation time ascending.
```

Each job record: `job_id`, `state`, `metadata`, `created_at`, `updated_at`.

---

**Part 2 — Stuck Job Detection**

```python
def find_stuck_jobs(tracker: JobTracker, current_time: float, timeout_seconds: int) -> list[str]:
```

A job is "stuck" if it has been in `RUNNING` state for longer than `timeout_seconds` without a state change. Return job_ids sorted by how long they've been stuck (longest first).

---

**Part 3 — Job History**

Extend `JobTracker` to record state transition history.

```python
def get_job_history(job_id: str) -> list[dict]:
    # Returns:
    # [
    #   {"from_state": None,      "to_state": "PENDING",   "timestamp": 1700000000.0},
    #   {"from_state": "PENDING", "to_state": "RUNNING",   "timestamp": 1700000060.0},
    #   {"from_state": "RUNNING", "to_state": "SUCCEEDED", "timestamp": 1700000300.0},
    # ]
```

---

**Follow-ups (answer in chat):**
1. How would you add retry logic — auto-transitioning FAILED → PENDING up to N times?
2. 10,000 concurrent jobs, clients polling every second — how do you architect for horizontal scale?

**Constraints:** Use `time.time()` for timestamps (mock it in tests). `metadata` should not be mutated after creation.

---

## My Approach

*Not yet recorded.*

---

## Code Attempts

*No attempts yet.*

---

## Session Summary

*Session in progress...*
