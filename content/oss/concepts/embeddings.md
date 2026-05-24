---
concept: "Embeddings"
slug: embeddings
tags: [agents, retrieval, nlp]
repos: [LangChain, LlamaIndex]
updated: 2026-05-24
---

# Embeddings

**Repos:** [[../langchain|LangChain]] · [[../llamaindex|LlamaIndex]]

Dense vector representations of text where semantic similarity = geometric proximity.
The foundation of RAG, semantic search, and clustering.

## How They're Trained
Contrastive learning: push similar pairs closer, dissimilar pairs apart.
Models: BERT-style encoders fine-tuned on (query, passage) pairs.

## Dimensions
- OpenAI text-embedding-3-small: 1536-dim (can truncate to 256)
- BGE-M3: 1024-dim, multilingual
- E5-large: 1024-dim, strong on benchmarks

## Distance Metrics
- Cosine similarity: angle between vectors (most common)
- Dot product: cosine × magnitude (use when magnitudes matter)
- L2: Euclidean distance

## Related
- [[rag|RAG]] — retrieval uses embeddings for similarity search

