---
problem: calendar-three
date: 2026-05-31
started: 07:31
status: in-progress
tags: [scale-ai, practice, coding]
---

# My Calendar III · 2026-05-31

## Problem

> 📋 **LeetCode Discuss** · Scale AI Initial Tech Screen · [Source](https://leetcode.com/discuss/post/7176694/)

LeetCode 732 — but Scale asked this in a phone screen.

Implement a class `MyCalendarThree`:
- `book(start, end)` — adds a booking for time `[start, end)`
- Returns the maximum **k** such that there exist k bookings that all overlap at some point

**Example:**
```
book(10, 20) → 1
book(50, 60) → 1
book(10, 40) → 2   (overlaps with [10,20])
book(5, 15)  → 3   ([10,15] has 3 overlaps)
book(5, 10)  → 3
book(25, 55) → 3
```

**Key insight:** Think of it as a timeline with events. At `start`, overlap count goes up. At `end`, it goes down. Find the max running total.

---

## My Approach

*Not yet recorded.*

---

## Code Attempts

*No attempts yet.*

---

## Session Summary

*Session in progress...*
