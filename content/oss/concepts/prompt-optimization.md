---
concept: "Prompt Optimization"
slug: prompt-optimization
tags: [agents, dspy, optimization]
repos: [DSPy]
updated: 2026-05-24
---

# Prompt Optimization

**Repos:** [[../dspy|DSPy]]

Automatically optimize prompts (and few-shot examples) to maximize a metric,
rather than hand-crafting them. DSPy's core contribution.

## The Problem with Manual Prompting
Prompts are brittle — changing the model, task, or context breaks them.
Hand-tuning is trial-and-error and doesn't generalize.

## DSPy's Approach
Define your pipeline as *programs* (Predict, ChainOfThought, ReAct).
Define a metric. DSPy optimizes the prompts/examples automatically using:
- **BootstrapFewShot**: mine successful few-shot examples
- **MIPRO**: bayesian optimization over prompt candidates
- **BetterTogether**: jointly optimize prompts + fine-tuning

## When to Use
Use DSPy when you have a clear evaluation metric and want to move past
manual prompt engineering.

## Related
- [[rag|RAG]] — DSPy can optimize multi-hop RAG pipelines

