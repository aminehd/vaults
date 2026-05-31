---
tags: [scale-ai, interview, insights]
---

# Scale AI — What They Actually Ask

Sourced from 9 LeetCode discuss threads crawled in `ScaleAI/crawled/`.

## Phone Screen / Initial Tech Screen
- **Kth Largest Element** (heap) — LC 215
- **Add Two Numbers** (linked list) — LC 2
- Standard LC mediums, 45 min, one or two problems

## Coding Round (Backend / Senior SWE)
Scale loves **custom domain problems** over vanilla LC — they test whether you can model a real system:

| Problem | Pattern | Status |
|---------|---------|--------|
| Task Scheduler (3 phases) | Heap + Kahn's topo sort | ✅ done |
| Party Times (dead zones) | Interval merge + gap find | ✅ done |
| Travel Optimization (TSP) | API integration + greedy/brute TSP | ✅ done |
| Card Game variants | OOP simulation | ✅ done |
| Poker Hand | Combinatorics / classification | ✅ done |
| My Calendar Three | Sweep line | ✅ done |
| LLM Batching | Queue + batch logic | ✅ done |

## System Design Round
**Actual question asked:** Design a system that:
1. Fetches tasks (JSON blobs) from MongoDB
2. Operators create jobs of up to 5000 tasks
3. Each task processed via 3rd-party LLM API (synchronous)
4. LLM API accepts up to 10 tasks per request (batching)

**Key design decisions:**
- Job queue (Redis / SQS) to decouple task ingestion from processing
- Batch assembler: groups tasks into chunks of 10
- Worker pool: parallel LLM calls with rate limiting
- Status tracking: MongoDB updates per task (PENDING → IN_PROGRESS → DONE)
- Retry logic: exponential backoff on LLM failures

## For the Frontier Agents Role specifically
This role is less backend-infra, more **AI systems**. Expect:
- RAG system design (chunking → embedding → retrieval → generation)
- Agent architecture (tool use, memory, multi-step planning)
- Prompt engineering challenge (given domain, build prompt + eval)
- "Walk me through a production AI system you built" — this is your Amazon story

## Behavioral
- "Tell me about a time you worked directly with a customer to solve a technical problem"
- "How do you handle ambiguous requirements from a non-technical stakeholder?"
- Scale is customer-obsessed on the enterprise side — frame everything through the lens of customer impact
