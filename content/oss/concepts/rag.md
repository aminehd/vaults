---
concept: "RAG"
slug: rag
tags: [agents, retrieval, embeddings, llm]
repos: [LangChain, LlamaIndex]
updated: 2026-05-24
---

# RAG

**Repos:** [[../langchain|LangChain]] · [[../llamaindex|LlamaIndex]]

Retrieval-Augmented Generation — ground LLM responses in external knowledge by
retrieving relevant documents at query time and injecting them into the context.

## Pipeline
1. **Index**: chunk documents → embed → store in vector DB
2. **Retrieve**: embed query → similarity search → top-k chunks
3. **Generate**: LLM answers using retrieved chunks as context

## Why Not Just Fine-tune?
- RAG knowledge is updateable without retraining
- Sources are cited and auditable
- Much cheaper than fine-tuning for factual grounding

## Key Components
- **Chunking strategy**: fixed-size, semantic, recursive
- **Embedding model**: text-embedding-3-small, BGE, E5
- **Vector DB**: Chroma, Pinecone, Weaviate, Qdrant
- **Reranking**: cross-encoder after retrieval for better precision

## Related
- [[embeddings|Embeddings]] — the representation used for retrieval
- [[prompt-optimization|Prompt Optimization]] — DSPy can auto-optimize RAG pipelines

