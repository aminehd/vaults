---
repo: "llm-compressor"
slug: llm-compressor
issues_count: 6
updated: 2026-05-25
---

# llm-compressor — Contribution Opportunities

Directly feeds vLLM. Sequential/algorithmic tasks merge fast. zeel2104 has 2 PRs here.

← [[../llm-compressor|Back to llm-compressor]]

## Open Issues (6)

- **[#2735 DSv4 canonical example drops MTP layer; load_quantizable_moe regex anchored at ^layers excludes mtp.* block](https://github.com/vllm-project/llm-compressor/issues/2735)**
  opened 2026-05-20 · 1 comments
  > ## Summary  The canonical `examples/quantizing_moe/deepseek_v4_example.py` (`kylesayrs/transformers-v5` branch, commit `8c533c21f`, 2026-05-20) calibrates the main 43 routed-expert layers of DeepSeek-

- **[#2698 Remove iMatrixGatherer](https://github.com/vllm-project/llm-compressor/issues/2698)** `enhancement` `good first issue`
  opened 2026-05-11 · 2 comments
  > In https://github.com/vllm-project/llm-compressor/pull/2473 we went back and forth about the implementation and finalized a temporary design. The plan was to implement it then with an iMatrixGatherer 

- **[#2690 [RFC] HIGGS Integration into llm-compressor](https://github.com/vllm-project/llm-compressor/issues/2690)** `enhancement` `RFC`
  opened 2026-05-07 · 4 comments
  > # [RFC] Native HIGGS-style mixed-precision allocation pipeline in `llm-compressor` (NVFP4 / FP8_Dynamic / FP16)  ## Background  We implemented a practical HIGGS-style workflow externally around `llm-c

- **[#2667 Fast KLD metric](https://github.com/vllm-project/llm-compressor/issues/2667)** `enhancement` `good first issue`
  opened 2026-04-29 · 2 comments
  > followup to https://github.com/vllm-project/llm-compressor/issues/2646#issue-4323565620  looking for the fastest way to calculate an accurate kl divergence metric using vllm inference, i think this wo

- **[#2654 [Tests] Extend CI/CD tests to plot recovery values over time](https://github.com/vllm-project/llm-compressor/issues/2654)**
  opened 2026-04-26 · 0 comments
  > ## Follow-up to   ### Context As a follow-up to PR  (restoring LM Eval test stability with `use_deterministic_algorithms`), we should extend our CI/CD pipeline to track and visualize model recovery me

- **[#2646 cheap KLD metric](https://github.com/vllm-project/llm-compressor/issues/2646)** `enhancement` `good first issue`
  opened 2026-04-24 · 10 comments
  > # Background  [KL Divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence) is a useful metric for measuring the similarity between two model's output distributions (i.e. to see h
