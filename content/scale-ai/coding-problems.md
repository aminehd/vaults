---
tags: [scale-ai, coding, interview]
---

# Scale AI — Coding Problems

All problems are in `~/WorkSpace/ClawClaude/ScaleAI/Coding/`

## ✅ Done

### Task Scheduler (3 phases)
**File:** `task_scheduler.py`, `task_schedule_me.py`  
**What:** Priority heap + dependency graph (Kahn's). Phases: basic heap → deps (indegree) → optimized push-on-add  
**Key bugs to remember:**
- `return task` not `return Task`
- `Tuple[int, str]` not `Tuple(int, str)`
- `unblock_next[name]` must be a list, not single task
- `complete_task` and `get_next` are SEPARATE — never mark COMPLETED in get_next
- `field(default_factory=list)` not `field(default=[])`

### Party Times (dead zones)
**File:** `party_times.py`, `party_time_my_attempt.py`  
**What:** Given parties with timestamps and geo data, find dead zone hours per neighborhood (gaps between earliest start and latest end where no party runs). Merge overlapping intervals → find gaps.

### Travel Optimization (TSP)
**File:** `travel_opt.py`, `travel_opt_clean.py`, `mock_api_server.py`  
**What:** Convert resort names → place IDs (API) → build NxN travel time matrix → brute force / greedy TSP. Flask mock server for local testing.

### Card Game (3 variants)
**File:** `card_game_1.py`, `card_game_2.py`, `card_game_3_survival.py`  
**What:** Card game rounds, scoring, survival mode (last player standing)

### Poker Hand Evaluation
**File:** `poker_hand.py`  
**What:** Detect straight, flush, four-of-a-kind, five-of-a-kind, full house, straight flush. Joker wildcard extension.

### LLM Batching
**File:** `llm_batching.py`  
**What:** Batch requests to LLM API (max 10 tasks/request), handle async queueing

### My Calendar Three
**File:** `my_calendar_three.py` (repo root)  
**What:** Sweep line — maintain sorted timeline of (timestamp, delta), prefix sum to find max k-booking. O(N) sweep per booking.

---

## ❌ Not Started

None — all known problems have working solutions.

---

## What to drill before the interview

1. **Task Scheduler cold** — write from scratch in 25 min without looking. It WILL come up.
2. **Party Times** — the dead zone logic trips people up. Know: merge intervals first, then find gaps.
3. **System design** — LLM batching as a full system (MongoDB → job queue → batch processor → LLM API). See [[interview-insights]].
