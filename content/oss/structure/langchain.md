---
repo: "LangChain"
slug: langchain
languages: [Python, Makefile, Shell]
---

# LangChain — Codebase Structure

← [[../langchain|Back to LangChain]]

## Directory Map

```mermaid
graph TD
    root[langchain/] --> libs[libs/]
    libs --> core[core/ — base abstractions]
    libs --> langchain[langchain/ — main library]
    libs --> partners[partners/ — integrations]
    libs --> text_splitters[text-splitters/]
    libs --> standard_tests[standard-tests/]
    partners --> openai[openai/]
    partners --> anthropic[anthropic/]
    partners --> many[100+ more...]
```

## What Each Directory Does

- **libs/core/** — base classes: BaseChain, BaseRetriever, BaseLLM, BaseMemory — rarely changes
- **libs/langchain/** — main integrations and chains built on core
- **libs/partners/** — one package per integration (OpenAI, Anthropic, Pinecone, etc.) — easiest to contribute
- **libs/text-splitters/** — text chunking strategies for RAG
- **libs/standard-tests/** — shared test suite all integrations must pass

## Key Entry Points for Contributing

- `libs/partners/<new_integration>/` — add a new LLM, embeddings, or vector store integration
- `libs/text-splitters/` — add a new text splitting strategy
- `libs/langchain/` — fix a bug or improve an existing chain
- `libs/standard-tests/` — improve shared test coverage
