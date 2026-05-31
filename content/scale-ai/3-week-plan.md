---
tags: [scale-ai, plan, active]
---

# 3-Week Plan — Scale AI Senior Frontier Agents Engineer

> Coding is already done. This role needs RAG + agents depth. Shift focus.

## Week 1 — Agent Frameworks + Coding Refresh

**Agent frameworks (2hr/day)**
- [ ] Build a LangChain agent end-to-end: tools, memory, chains
- [ ] Build a LlamaIndex RAG pipeline: ingest → chunk → embed → query
- [ ] Know the difference: LangChain (orchestration) vs LlamaIndex (retrieval)
- [ ] Structured outputs: Pydantic + OpenAI function calling

**Coding refresh (1hr/day)**
- [ ] Task Scheduler cold — write from scratch in 25 min, no peeking
- [ ] Party Times — dead zone logic from memory
- [ ] My Calendar Three — sweep line from memory

---

## Week 2 — Production Depth

**RAG systems**
- [ ] Vector DBs: run Chroma locally, understand Pinecone/Weaviate APIs
- [ ] Chunking strategies: fixed, semantic, recursive — know tradeoffs
- [ ] Reranking: cross-encoders, MMR
- [ ] Eval: RAGAS framework — faithfulness, answer relevance, context recall

**Prompt engineering**
- [ ] System prompt architecture for enterprise agents
- [ ] A/B testing methodology for prompts — how to measure
- [ ] Guardrails: structured outputs, input/output validation

**Infrastructure**
- [ ] Dockerize an agent app (write a Dockerfile for a FastAPI + LangChain agent)
- [ ] GCP basics: Cloud Run, Cloud SQL (you already use this — make it a talking point)
- [ ] CI/CD for ML: how to deploy a prompt change safely?

---

## Week 3 — Scale-specific + Mocks

**Know Scale's business**
- [ ] Scale makes money on data labeling + RLHF for frontier model companies
- [ ] Enterprise AI = deploying agents inside Fortune 500 workflows
- [ ] Their differentiator: human-in-the-loop quality + enterprise security/compliance
- [ ] SGP (Scale Generative Platform) — read public docs

**System design mock**
- [ ] "Design an AI agent for enterprise customer support" — 45 min timed
- [ ] "Design the LLM batching system" — from [[interview-insights]]

**Behavioral prep**
- [ ] "Tell me about a time you built something for an external customer" → Amazon CSDAI platform story
- [ ] "How do you translate vague customer requirements into a technical spec?" → ML scientist self-serve story
- [ ] "Tell me about a production AI system you built" → EKS + Kinesis + agent deployment story

**Mock coding**
- [ ] 3 timed LC mediums: graphs, heaps, sliding window
- [ ] Ask Edgar about interview format (coding rounds? system design? take-home?)

---

## Daily Habit
Heartbeat fires at 9am PT every day with:
- One coding problem to drill
- One RAG/agent concept
- One Scale business context reminder
