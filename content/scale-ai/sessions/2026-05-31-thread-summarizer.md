---
problem: thread-summarizer
date: 2026-05-31
started: 10:36
status: in-progress
tags: [scale-ai, practice, coding]
---

# Conversation Thread Summarizer · 2026-05-31

## Problem

> 📋 **Gotham Loop · 10/10** — directly mirrors Scale AI's LLM fine-tuning data pipeline.

Build a backend tool that processes customer support threads into structured summaries for an LLM training dataset.

**Part 1 — `extract_thread_features(thread) -> dict`**

```json
{
  "thread_id": "th_001",
  "messages": [
    {"message_id": "m_1", "sender_type": "customer", "text": "My order hasn't arrived.", "timestamp": "2024-08-01T09:00:00Z"},
    {"message_id": "m_2", "sender_type": "agent",    "text": "Can you share your order ID?",  "timestamp": "2024-08-01T09:02:00Z"},
    {"message_id": "m_3", "sender_type": "customer", "text": "It's #ORD-5521.",               "timestamp": "2024-08-01T09:03:00Z"}
  ],
  "resolved": true,
  "category": "shipping"
}
```

Returns: `thread_id`, `message_count`, `customer_message_count`, `agent_message_count`, `first_response_time_seconds` (None if no agent), `total_duration_seconds`, `avg_customer_message_length_chars`, `resolved`, `category`.

Messages are **not** guaranteed to be sorted by timestamp.

**Part 2 — `build_turns(thread) -> list[dict]`**

Group consecutive messages from the same sender into turns, joining text with a space:
```python
[
  {"turn": 1, "sender_type": "customer", "combined_text": "My order hasn't arrived.", "message_count": 1},
  {"turn": 2, "sender_type": "agent",    "combined_text": "Can you share your order ID?", "message_count": 1},
  {"turn": 3, "sender_type": "customer", "combined_text": "It's #ORD-5521.", "message_count": 1},
]
```

**Part 3 — `filter_quality_threads(threads, min_turns, max_first_response_seconds, resolved_only) -> (list, dict)`**

Filter threads meeting all criteria. Return `(kept_threads, rejection_summary)`:
```python
{"kept": 840, "rejected_too_few_turns": 42, "rejected_slow_response": 18, "rejected_unresolved": 100}
```
A thread failing multiple criteria counts in the **first** matching bucket.

**Follow-ups:** PII detection? Scale to millions/day? Additional quality signals?

---

## My Approach

*Not yet recorded.*

---

## Code Attempts

*No attempts yet.*

---

## Session Summary

*Session in progress...*
