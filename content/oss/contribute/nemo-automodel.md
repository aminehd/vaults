---
repo: "NeMo Automodel"
slug: nemo-automodel
issues_count: 6
updated: 2026-05-25
---

# NeMo Automodel — Contribution Opportunities

YAML tooling, docs, dataset PRs merge fast. zeel2104 has 3 PRs. NVIDIA name on resume.

← [[../nemo-automodel|Back to NeMo Automodel]]

## Open Issues (6)

- **[#2279 Feature Request: Make `save_consolidated` parallelism resilient to non-standard upstream shard filenames (Qwen3.5 family) — currently wastes hundreds of GPU-hours on hangs](https://github.com/NVIDIA-NeMo/Automodel/issues/2279)** `enhancement` `community-request` `waiting-on-maintainers`
  opened 2026-05-19 · 0 comments
  > ## TL;DR  When `checkpoint.save_consolidated: true` is enabled and the base HF model uses non-standard shard filenames (e.g., Qwen3.5 series: `model.safetensors-NNNNN-of-NNNNN.safetensors`), nemo_auto

- **[#2267 Support configurable HSDP in both expert and non-expert groups for MoEs](https://github.com/NVIDIA-NeMo/Automodel/issues/2267)** `enhancement`
  opened 2026-05-18 · 0 comments
  > From [Cursor 2.5 blog](https://cursor.com/blog/composer-2-5):  > HSDP forms multiple FSDP replicas and all-reduces gradients across corresponding shards. We use separate HSDP layouts for non-expert an

- **[#2241 Support Falcon H1](https://github.com/NVIDIA-NeMo/Automodel/issues/2241)** `enhancement` `good first issue`
  opened 2026-05-15 · 2 comments
  > - tiiuae/Falcon-H1-0.5B-Instruct   - tiiuae/Falcon-H1-1.5B-Deep-Instruct    - tiiuae/Falcon-H1-7B-Instruct   - tiiuae/Falcon-H1-34B-Instruct

- **[#2226 Support Wan 2.2](https://github.com/NVIDIA-NeMo/Automodel/issues/2226)** `enhancement`
  opened 2026-05-13 · 0 comments
  > **Is your feature request related to a problem? Please describe.** A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]  **Describe the solution you'd like** A 

- **[#2220 Expand ty type-checking coverage in AutoModel](https://github.com/NVIDIA-NeMo/Automodel/issues/2220)** `enhancement` `coverage`
  opened 2026-05-12 · 0 comments
  > ## Feature Request  Expand AutoModel's `ty` type-checking coverage beyond the current Phase 1 modules.  `ty` is already configured in `pyproject.toml` and enforced in CI, but strict checks are current

- **[#2218 Support for Multilora training](https://github.com/NVIDIA-NeMo/Automodel/issues/2218)** `enhancement`
  opened 2026-05-12 · 0 comments
  > **Is your feature request related to a problem? Please describe.** A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]  **Describe the solution you'd like** A 
