---
repo: "Kaito"
slug: kaito
issues_count: 6
updated: 2026-05-26
---

# Kaito — Contribution Opportunities

Growing fast. zeel2104 merged GPU spot instance PR. Cloud + AI intersection.

← [[../kaito|Back to Kaito]]

## Open Issues (6)

- **[#2057 Model prefetch and streaming](https://github.com/kaito-project/kaito/issues/2057)** `enhancement`
  opened 2026-05-20 · 0 comments
  > **Is your feature request related to a problem? Please describe.** Currently, workspace starts to download the model weights after the GPU is provisioned, which leads to a long wait before the model i

- **[#2044 Model deployment stuck at load testing phase due to drain timeout](https://github.com/kaito-project/kaito/issues/2044)** `bug`
  opened 2026-05-12 · 1 comments
  > **Describe the bug** Currently, Kaito will run a load test to measure model throughput before marking the workspace InferenceReady. Once the test finishes, Kaito call _drain() in benchmark_entrypoint.

- **[#2029 Support FlashInfer attention/moe backend in Kaito](https://github.com/kaito-project/kaito/issues/2029)** `enhancement`
  opened 2026-05-07 · 2 comments
  > **Is your feature request related to a problem? Please describe.** FlashInfer is a commonly-used attention and moe backends in vLLM: https://docs.vllm.ai/en/latest/design/attention_backends/#backend-p

- **[#2002 Support quantized models (GGUF and AWQ formats)](https://github.com/kaito-project/kaito/issues/2002)** `enhancement`
  opened 2026-04-28 · 1 comments
  > **Is your feature request related to a problem? Please describe.**  Currently, KAITO lacks first-class support for quantized models. Users who want to run smaller, more efficient model variants (e.g.,

- **[#1980 Feature Request: Auto-Upgrade Support for Base Serving Image in InferenceSet](https://github.com/kaito-project/kaito/issues/1980)** `enhancement`
  opened 2026-04-22 · 1 comments
  > ## Background  KAITO users running inference workloads in production currently have no built-in mechanism to upgrade the underlying serving stack (base image, vLLM runtime) without manual intervention

- **[#1972 Implement AWSKarpenterProvisioner — NodePool lifecycle management (create/delete)](https://github.com/kaito-project/kaito/issues/1972)** `enhancement`
  opened 2026-04-17 · 1 comments
  > ## Description  Implement the `AWSKarpenterProvisioner` for `ProvisionNodes()` and `DeleteNodes()` methods, which create and delete per-Workspace NodePools on AWS EKS clusters using the [AWS Karpenter
