---
repo: "LlamaIndex"
slug: llamaindex
languages: [Python, Jupyter Notebook, Makefile]
---

# LlamaIndex — Codebase Structure

← [[../llamaindex|Back to LlamaIndex]]

## Directory Map

```mermaid
graph TD
    root[llama_index/] --> core[llama-index-core/]
    root --> integrations[llama-index-integrations/]
    root --> docs[docs/]
    root --> scripts[scripts/]
    core --> llama_index[llama_index/]
    llama_index --> indices[indices/]
    llama_index --> retrievers[retrievers/]
    llama_index --> llms[llms/]
    integrations --> llms_int[llms/]
    integrations --> embeddings[embeddings/]
    integrations --> graph_stores[graph_stores/]
    integrations --> readers[readers/]
```

## What Each Directory Does

- **llama-index-core/** — base abstractions: indices, retrievers, query engines, node parsers
- **llama-index-integrations/llms/** — one package per LLM provider
- **llama-index-integrations/embeddings/** — one package per embedding model
- **llama-index-integrations/readers/** — data loaders (PDFs, databases, APIs)
- **llama-index-integrations/graph_stores/** — graph database connectors
- **docs/** — API reference, tutorials, example notebooks

## Key Entry Points for Contributing

- `llama-index-integrations/readers/` — add a new data loader (well-defined interface)
- `llama-index-integrations/llms/` — add a new LLM provider
- `llama-index-integrations/embeddings/` — add a new embedding model
- `docs/examples/` — add a notebook example
