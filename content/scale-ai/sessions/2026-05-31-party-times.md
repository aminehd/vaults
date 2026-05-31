---
problem: party-times
date: 2026-05-31
started: 06:02
status: in-progress
tags: [scale-ai, practice, coding]
---

# Party Times (Dead Zones) · 2026-05-31

## Problem

Real Scale AI phone screen problem.

You have parties happening across cities. Each party has a start and end time.

**Part A** — `compute_party_window(parties, geo)`:
For each neighborhood, find the earliest start and latest end across all its parties.
Return `{neighborhood: (earliest_start_hour, latest_end_hour)}`.

**Part B** — `find_dead_zones(parties, geo)`:
A "dead zone" is a gap *between* the earliest start and latest end of all parties where NO party is actually running.
Return total dead hours per town/city.

**Data shape:**
```python
parties = [
    {"party_id": "p1", "start_timestamp": "2024-01-01T08:00", "end_timestamp": "2024-01-01T14:00"},
    {"party_id": "p3", "start_timestamp": "2024-01-01T18:00", "end_timestamp": "2024-01-01T23:00"},
]
geo = [
    {"party_id": "p1", "neighborhood_name": "downtown", "city": "NYC"},
    {"party_id": "p3", "neighborhood_name": "uptown", "city": "NYC"},
]
```

**Think:** merge overlapping intervals first, then find the gaps.

---

## My Approach

*Not yet recorded.*

---

## Code Attempts

*No attempts yet.*

---

## Session Summary

*Session in progress...*
