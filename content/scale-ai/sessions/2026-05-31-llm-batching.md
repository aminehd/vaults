---
problem: llm-batching
date: 2026-05-31
started: 07:31
status: in-progress
tags: [scale-ai, practice, coding]
---

# LLM Batching System · 2026-05-31

## Problem

> 📋 **LeetCode Discuss** · Scale AI System Design · [Source](https://leetcode.com/discuss/post/6738698/)

Scale AI system design question — but as code.

Build a batching layer in front of an LLM API. Requirements:
- Requests come in one at a time with an `id` and `text`
- The LLM API accepts up to **10 requests per batch**
- You should **wait up to 100ms** to accumulate a batch before sending
- Process batches concurrently (multiple batches can be in-flight)
- Each caller gets their result back when their request is processed

**Mock LLM API:**
```python
def mock_llm_api(batch):  # batch = list of {id, text}
    time.sleep(0.5)  # simulates network
    return [{"id": r["id"], "result": f"processed: {r['text']}"} for r in batch]
```

**Think about:** How do you handle the 100ms window? What data structure holds pending requests?

---

## My Approach

*Not yet recorded.*

---

## Code Attempts

*No attempts yet.*

---

## Session Summary

*Session in progress...*
