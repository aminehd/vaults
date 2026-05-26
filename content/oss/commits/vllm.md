---
repo: "vLLM"
slug: vllm
commits_7d: 100
updated: 2026-05-26
---

# vLLM — Recent Commits (7d)

**100 commits this week** · [GitHub](https://github.com/vllm-project/vllm/commits)

← [[../vllm|Back to vLLM]]

## Commits

- `ec5de7f` [[../concepts/lora|LoRA]] Add one shot [[../concepts/triton-kernels|triton kernel]] For [[../concepts/mixture-of-experts|MoE]] LoRA (#42290)](https://github.com/vllm-project/vllm/commit/ec5de7fa7d1303051ccd6c7316171b6d70bac4b4) — Jee Jee Li · 2026-05-26
→ touches: `csrc/moe/` — adds a new Triton kernel for MoE LoRA for faster performance.
- `71d810b` [[XPU] Ensure RNG offset alignment with PyTorch requirements in XPU sampler (#43028)](https://github.com/vllm-project/vllm/commit/71d810bbf44b34f3a019730a6878fbcbf2480499) — Chaojun Zhang · 2026-05-26
→ touches: `vllm/model_executor/` — aligns the random number generator with PyTorch requirements for XPU compatibility.
- `d400445` [[Kernel] Remove NormGateLinear (#43554)](https://github.com/vllm-project/vllm/commit/d4004455d2357985830af10e432709b42c820455) — Jee Jee Li · 2026-05-25
- `716d529` [[Misc] Print accuracy value for PD tests even on success  (#43583)](https://github.com/vllm-project/vllm/commit/716d5294e6db16fe1d8afb09a061694cf4602d7e) — Nicolò Lucchesi · 2026-05-25
- `873758c` [[../concepts/kv-connector|KV Connector]] Handle Mooncake finish after preemption (#43281)](https://github.com/vllm-project/vllm/commit/873758c13a64742e2a0247e0f2c62cadf027dd2b) — Zhewen Li · 2026-05-25
- `5c1aec3` [Reduce memory usage for granite_speech. (#42933)](https://github.com/vllm-project/vllm/commit/5c1aec3dc0600cb816a0389e55ef1f1c17893380) — Yihuki · 2026-05-25
- `0c942c6` [[Doc] Add section on escalating stalled contributions (#43568)](https://github.com/vllm-project/vllm/commit/0c942c69d6e486d8e0d879066217aaac19e02da9) — Roy Wang · 2026-05-25
- `81252d4` [[Feat][[../concepts/kv-connector|KVConnector]] Support [[../concepts/deepseek-v4|DSV4]] in SimpleCPUOffloadBackend (#42296)](https://github.com/vllm-project/vllm/commit/81252d4e2446552f93225b1d48873d45999f045e) — Yifan Qiao · 2026-05-25
- `3df1c7c` [[Docker] Non-root support for vllm-openai; add opt-in vllm-openai-nonroot target (#40275)](https://github.com/vllm-project/vllm/commit/3df1c7c43e73c6a06f70390136deecfe856c5969) — Nguyễn Thế Duy · 2026-05-25
- `1b26fa3` [[Docs] Reorganize offline inference docs.  (#43552)](https://github.com/vllm-project/vllm/commit/1b26fa361e7aa459951d08b315533803862f04d2) — wang.yuqi · 2026-05-25
- `6cbe448` [fix: [[../concepts/mixture-of-experts|MoE]] model using shared routed experts crashes on AMD GPUs (#42373)](https://github.com/vllm-project/vllm/commit/6cbe448eed751824d608faf9078ef84724d621c1) — weizhoublue · 2026-05-25
- `b06813e` [[Kernel] Add mhc_pre_big_fuse_with_norm_tilelang  (#43474)](https://github.com/vllm-project/vllm/commit/b06813e87207e15b133e903d641e03f237d85b17) — Jee Jee Li · 2026-05-25
- `d0a100c` [File system secondary tier implemented in python (#41735)](https://github.com/vllm-project/vllm/commit/d0a100c87af832ad97ade60b8ec7610018a08427) — Rotem Shavitt · 2026-05-24
- `d56285c` [Tuning script and configs for [[../concepts/triton-kernels|Triton]] [[../concepts/mamba|Mamba]] SSU kernel (#43083)](https://github.com/vllm-project/vllm/commit/d56285c747ec3133163c740adc3c68f3f5feb4e7) — danisereb · 2026-05-24
- `1806d1a` [[ROCm] [[../concepts/deepseek-v4|DSv4]] [Perf] Support DeepSeek v4 MTP (#43385)](https://github.com/vllm-project/vllm/commit/1806d1adfc9b598bc6eb94de38a330aaad04c291) — TJian · 2026-05-24
- `5940590` [[ROCm][CI] Stabilize 400 error return code for invalid schema inputs (#43016)](https://github.com/vllm-project/vllm/commit/594059085593313d3922ee2f8822467763753091) — Andreas Karatzas · 2026-05-24
- `357fddf` [[[../concepts/kv-offload|kv_offload]]: Add [[../concepts/deepseek-v4|DSv4]] support (#43142)](https://github.com/vllm-project/vllm/commit/357fddf6147780404cb07b5a7d58b8434c9e828d) — Or Ozeri · 2026-05-24
- `0902d8e` [[../concepts/kv-connector|KV Connector]] Keep MooncakeStore full hits block-aligned (#43494)](https://github.com/vllm-project/vllm/commit/0902d8e62fd905f7b02b6ca0b64900d105fb77e9) — Dao007forever · 2026-05-24
- `33d7cbe` [[Model Runner v2] Force v1 runner for tests (#43233)](https://github.com/vllm-project/vllm/commit/33d7cbe02ca100d3f0314cd22f4342d5cd23ba15) — Wentao Ye · 2026-05-23
- `b32fe41` [[Bugfix] Fix reasoning dropped on streaming boundary deltas (#42691)](https://github.com/vllm-project/vllm/commit/b32fe416ea1a036cda7373fc701b12b75bf86ac9) — Flora Feng · 2026-05-23
