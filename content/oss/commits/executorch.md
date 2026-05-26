---
repo: "ExecuTorch"
slug: executorch
commits_7d: 99
updated: 2026-05-26
---

# ExecuTorch — Recent Commits (7d)

**99 commits this week** · [GitHub](https://github.com/pytorch/executorch/commits)

← [[../executorch|Back to ExecuTorch]]

## Commits

- `03e14ef` [Arm backend: Add bf16 support for aten.index_select and aten.unfold_copy (#19751)](https://github.com/pytorch/executorch/commit/03e14ef8b3964deb589f3f172b4bbee7d206795a) — Youngsik Yang · 2026-05-25
- `b73df0b` [NXP backend: Enable Sub Tensor with new Neutron flow (#19588)](https://github.com/pytorch/executorch/commit/b73df0b4696885c6e03f3789daeece8376078364) — roman-janik-nxp · 2026-05-25
- `ee4c90a` [Arm backend: Exclude build metadata from license checks](https://github.com/pytorch/executorch/commit/ee4c90ad03f33398cbfa93cfed09caf04fca6099) — Per Held · 2026-05-25
- `ba6074c` [Back out "Globally serialize XNNPACK execution, add logging" (#19752)](https://github.com/pytorch/executorch/commit/ba6074c3868abb8f602a22565445b52f8b5bdfb1) — Julian Chan · 2026-05-25
- `b69cbcd` [NXP backend: Enable Add Tensor with new Neutron flow (#19550)](https://github.com/pytorch/executorch/commit/b69cbcd6ffefe6e13fa25c4ea9285786b04692ca) — roman-janik-nxp · 2026-05-24
- `d757776` [Add extension_llm_runner to CMake deps (#19749)](https://github.com/pytorch/executorch/commit/d757776f51bc41aedac47fe51dd020474726774c) — Hansong Zhang · 2026-05-23
- `7d8063f` [[ET Device Support] Define AOT device copy ops registry (#19748)](https://github.com/pytorch/executorch/commit/7d8063f9e6221ad8724f122ad3ec4cbb1aae2fc6) — Gasoonjia · 2026-05-23
- `c27cc5d` [[ET Device Support] CudaAllocator: device memory allocator for CUDA backend (#19747)](https://github.com/pytorch/executorch/commit/c27cc5d5bb872603ec90378c486049bc2c77a382) — Gasoonjia · 2026-05-23
- `12f62f2` [[ET Device Support] Module: allocate device memory for planned buffers (#19746)](https://github.com/pytorch/executorch/commit/12f62f2eb869eddbe4c612efe3f957bfc965aff0) — Gasoonjia · 2026-05-23
- `6bda6c4` [Globally serialize XNNPACK execution, add logging (#19742)](https://github.com/pytorch/executorch/commit/6bda6c490ed8c2e2ac02049725b9a454dc92ec07) — Gregory Comer · 2026-05-23
- `158c5d8` [Convert Android LLM extension from Java to Kotlin (#19211)](https://github.com/pytorch/executorch/commit/158c5d8f109479ecfb9ca6ef5e638a4961f5b379) — Hansong Zhang · 2026-05-23
- `ec76470` [Cortex_M backend: Add more model tests (#19720)](https://github.com/pytorch/executorch/commit/ec764702419ddc62570c06a282cb34f6d0ed0172) — Adrian Lundell · 2026-05-22
- `a83e7c4` [Fix 2 broken tests caused by D105910457](https://github.com/pytorch/executorch/commit/a83e7c479568df009375a0154b00123abcf585c7) — Scott Roy · 2026-05-22
- `88eaf81` [Unify static-attention PTE output reconstruction by reusing create_pte_wrapper from run_static_llm (#19723)](https://github.com/pytorch/executorch/commit/88eaf81c32adf0855eff4bca3427bcd240269d34) — YIWENX14 · 2026-05-22
- `80f39be` [Run RISC-V tests with multiple RVV QEMU configurations (#19707)](https://github.com/pytorch/executorch/commit/80f39be7333a551e690a730878ee11d334acbb3f) — Ludovic Henry · 2026-05-22
- `0d6632b` [Add TransducerRunner and rename AsrRunner to Seq2SeqRunner (#18961)](https://github.com/pytorch/executorch/commit/0d6632b04a97f555448c998dba9289ff43f0b078) — Hansong Zhang · 2026-05-22
- `b37653c` [Fix executorch -Wno-missing-prototypes flag for Zephyr/GCC builds (#19071) (#19071)](https://github.com/pytorch/executorch/commit/b37653c11550671082f936edecd78dc0b7b44758) — Karan Dewan · 2026-05-22
- `9dac74d` [Improve Gemma4 MLX perf by removing redundant casts  (#19732)](https://github.com/pytorch/executorch/commit/9dac74d8c087d9d654b554036088aa1668478664) — Scott Roy · 2026-05-22
- `e6b8df8` [Qualcomm AI Engine Direct - Adding QNN backend support for select_scatter core ATen op (#19704)](https://github.com/pytorch/executorch/commit/e6b8df849c145644c06e378b89ffb59cbb4cc3da) — qti-horodnic · 2026-05-22
- `90a7cdb` [Arm backend: fix(arm): validate partitions for dependency cycles after Q/DQ de-tagging (#18191)](https://github.com/pytorch/executorch/commit/90a7cdb5da0119b790a5309a8452f67f1ef918dc) — Beom Woo Kang · 2026-05-22
