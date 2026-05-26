---
name: "ColBERT"
slug: "colbert"
---

# ColBERT

ColBERT (Contextualized Late Interaction over BERT) is a retrieval model that uses a late interaction mechanism to score the relevance of a document to a query. Unlike traditional models that use a single vector to represent the document, ColBERT represents the document as a bag of embeddings, one for each token. It then computes the similarity between each query embedding and all the document embeddings.

This matters because it allows for a more fine-grained similarity matching, leading to better retrieval performance. It solves the problem of single-vector representations losing information about the local context of the document.

**Appears in:**
- [[../vllm|vLLM]]

**Related:**
- [[../embeddings|Embeddings]]
- [[../rag|Retrieval-Augmented Generation (RAG)]]
