---
repo: "Kaito"
slug: kaito
languages: [Go, Python, Jinja, MDX]
---

# Kaito — Codebase Structure

← [[../kaito|Back to Kaito]]

## Directory Map

```mermaid
graph TD
    root[kaito/] --> api[api/ — CRD types]
    root --> pkg[pkg/ — business logic]
    root --> cmd[cmd/ — entrypoints]
    root --> presets[presets/ — model configs]
    root --> config[config/ — K8s manifests]
    root --> test[test/]
    root --> docs[docs/]
    root --> charts[charts/ — Helm]
    api --> v1alpha1[v1alpha1/]
    api --> v1beta1[v1beta1/]
    pkg --> workspace[workspace/]
    pkg --> ragengine[ragengine/]
    cmd --> workspace_cmd[workspace/]
    cmd --> ragengine_cmd[ragengine/]
    presets --> llm_presets[llm models]
```

## What Each Directory Does

- **api/** — Kubernetes CRD types: Workspace, RAGEngine — defines what users declare in YAML
- **pkg/workspace/** — controller logic: provisions GPU nodes, deploys model pods
- **pkg/ragengine/** — RAG pipeline: vector store, retrieval, generation
- **presets/** — YAML configs for supported models (Llama, Mistral, Phi, Falcon)
- **cmd/** — main entrypoints for controller and RAG engine binaries
- **config/** — RBAC, CRD manifests for deployment
- **charts/** — Helm chart for installing Kaito on a cluster
- **docs/proposals/** — design docs for new features

## Key Entry Points for Contributing

- `presets/` — add GPU instance support or a new model preset (zeel2104's pattern)
- `docs/` — add deployment guides, tutorials
- `test/` — add e2e or unit tests
- `pkg/ragengine/` — improve RAG retrieval logic
