---
repo: "Transformers"
slug: transformers
commits_7d: 36
updated: 2026-05-26
---

# Transformers — Recent Commits (7d)

**36 commits this week** · [GitHub](https://github.com/huggingface/transformers/commits)

← [[../transformers|Back to Transformers]]

## Commits

- `ceb7ba6` [Fix Gemma4 use_bidirectional_attention="all" mask behavior (#46079)](https://github.com/huggingface/transformers/commit/ceb7ba69722a2f677ed0138e3d6933f34f4164ce) — Oliver Holworthy · 2026-05-26
- `4a2e365` [Fix loading with only 1 device or distributed config (#46197)](https://github.com/huggingface/transformers/commit/4a2e3652facc3579704fe8b10b8fbd4ab2879620) — Cyril Vallez · 2026-05-26
- `ece1ea0` [Fix TypeError on list-typed ignore_keys_at_rope_validation in RoPE config (#46142)](https://github.com/huggingface/transformers/commit/ece1ea0635367989ad4dfab0c084bcc57e5d897b) — Carlos Redondo · 2026-05-25
- `7bc093b` [Support XPU autocast dtype fallback for FlashAttention (#46199)](https://github.com/huggingface/transformers/commit/7bc093b71ecc42204b48cd6abf65a437f73655ad) — YangKai0616 · 2026-05-25
- `eaaaf84` [Fix path traversal when saving named chat templates (#46191)](https://github.com/huggingface/transformers/commit/eaaaf8494dd5386634ae37d1d122212fdc315be5) — Ziyu Lin · 2026-05-25
- `47949d3` [Fix is_last off-by-one in MaskGenerationPipeline for partial batches (#46136)](https://github.com/huggingface/transformers/commit/47949d3a0e1cf9248f2a3eb3cd0deb12ee37b9e9) — Jeremy Perera · 2026-05-25
- `118ddfb` [Fix wrong variable in check_model_type isinstance check (#46080)](https://github.com/huggingface/transformers/commit/118ddfb69cc9911255e6d3465f61c78d1627102b) — Sebastien Tardif · 2026-05-25
- `0b2da85` [Enable passing kwargs through RoFormer models (#46171)](https://github.com/huggingface/transformers/commit/0b2da85d4e8ec7f3e10606d0955ca127cabd4b7d) — ir2718 · 2026-05-25
- `e65c3a2` [Update cohere2_moe tp_plan (#46189)](https://github.com/huggingface/transformers/commit/e65c3a2d1461e6c43f6f5d4157c583846f63f71d) — Cyril Vallez · 2026-05-25
- `e4b2983` [Update release tool (#46193)](https://github.com/huggingface/transformers/commit/e4b2983002bbb9d1fe82de3ddf6f820d67b5a726) — Cyril Vallez · 2026-05-25
- `a214caa` [[loading] Fix base_model_prefix issues in conversions (#46067)](https://github.com/huggingface/transformers/commit/a214caa386c7835cddc9455df974246737bcbf75) — Cyril Vallez · 2026-05-25
- `7f2c8c9` [Fix caching allocator warmup byte estimation for EP model loading (#46149)](https://github.com/huggingface/transformers/commit/7f2c8c904f56a8a7100d90948071a18baedc4c41) — Wang, Yi · 2026-05-25
- `a31fc72` [Bump dev version (#46188)](https://github.com/huggingface/transformers/commit/a31fc7277a436ee96c0092d55dc3473ad6a3d54b) — Cyril Vallez · 2026-05-25
- `1055551` [Fix image-segmentation pipeline support for RF-DETR (#46130)](https://github.com/huggingface/transformers/commit/10555512868d663ee1ff627e4f5c5c260114235b) — Yoni Gozlan · 2026-05-21
- `797bb0d` [Update self-comment-ci (#46137)](https://github.com/huggingface/transformers/commit/797bb0d6c6478615eb89bd0e6ee41628b9059ceb) — guarin · 2026-05-21
- `52b82b2` [[ALM] flaky alm tests (#46074)](https://github.com/huggingface/transformers/commit/52b82b299171721fbe7b04fe056187f7aed2e2cc) — eustlb · 2026-05-20
- `9188b5e` [Add new cohere2_moe model (#46115)](https://github.com/huggingface/transformers/commit/9188b5e1391e4f6a46cbe6be7befcb10f3d6bdcd) — Cyril Vallez · 2026-05-20
- `ae7e60d` [[loading] Free up tensors faster inside ConversionOps (#46110)](https://github.com/huggingface/transformers/commit/ae7e60d7aae6a64b9b4d53bd115b4a9b5ac351e7) — Cyril Vallez · 2026-05-20
- `7a52743` [Restore test utils fix (#46065)](https://github.com/huggingface/transformers/commit/7a52743626cea1948df33a85a4582e83909c407a) — Rémi Ouazan · 2026-05-20
- `0137dee` [Allow `ydshieh2` for now for testing migration (#46105)](https://github.com/huggingface/transformers/commit/0137deeb65e4d03f9015a1c9cfccec524ac52fe9) — Yih-Dar · 2026-05-20
