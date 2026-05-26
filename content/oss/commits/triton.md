---
repo: "Triton"
slug: triton
commits_7d: 19
updated: 2026-05-26
---

# Triton — Recent Commits (7d)

**19 commits this week** · [GitHub](https://github.com/openai/triton/commits)

← [[../triton|Back to Triton]]

## Commits

- `609ced5` [[KERNELS] Perf tuning knobs for _reduce_forward kernel. (#10361)](https://github.com/triton-lang/triton/commit/609ced5e3f04e55234115524eb734822331a37d7) — Yongjik Kim · 2026-05-24
- `e283e01` [[CONSAN] Add barrier before NaN init (#10352)](https://github.com/triton-lang/triton/commit/e283e0150581139e02f7a2d9b39db5d58b9d3f21) — pawelszczerbuk · 2026-05-22
- `96a22b5` [Disallow sub-byte local_alloc (#10351)](https://github.com/triton-lang/triton/commit/96a22b5ed6c58106b900cc287544d5db98ef26b9) — Thomas Raoux · 2026-05-21
- `419fd86` [[FollowUp] Remove unused variable in `lowerTMemLdSt` (after #10321) (#10347)](https://github.com/triton-lang/triton/commit/419fd86723a1405bb866549443484db804b63bb7) — masahi · 2026-05-21
- `87d45ca` [Include examples/ in source distribution (#10349)](https://github.com/triton-lang/triton/commit/87d45ca9d2a573837690718910186e81abb4af2c) — Andrey Talman · 2026-05-21
- `00e397f` [[FRONTEND] [FPSAN] Introduce `tl.expect_zero` primitive (#10330)](https://github.com/triton-lang/triton/commit/00e397fbd15e7445e381a5bf90490df923020bac) — apgoucher · 2026-05-21
- `0158f1d` [[BACKEND] Fix modeling of ld acquire op (#10346)](https://github.com/triton-lang/triton/commit/0158f1d0e9d1773732815ed821f213114fde683b) — Thomas Raoux · 2026-05-21
- `2c72e74` [[AMD][GLUON] Expose padd layout deduction logic to Python (#10302)](https://github.com/triton-lang/triton/commit/2c72e747f2c402a561133b092bf1563b9c232787) — xiaohuguo2023 · 2026-05-21
- `7a5d6a3` [Fix small-K swizzled MXFP4 matmul (#10343)](https://github.com/triton-lang/triton/commit/7a5d6a3dec31f865d0e6a6ce751fed1cc10a5f5a) — Roman Novak · 2026-05-21
- `0914a04` [Fix alignment error in unpacked tmem store with `16x32bx2` message (#10321)](https://github.com/triton-lang/triton/commit/0914a04af03c8345d15fa41af6f2fab618f07b43) — masahi · 2026-05-21
- `c7391a2` [Enable microscaled lhs with dense FP16/BF16 matmul weights (#10316)](https://github.com/triton-lang/triton/commit/c7391a203e8f7772b11093e85508d5d7c6a9c665) — Roman Novak · 2026-05-21
- `57a214f` [[AMD] Fix invalid LLVM intrinsic name for float buffer atomic max/min (#10340)](https://github.com/triton-lang/triton/commit/57a214fda2d58312c6e76e3c9baadd01e4f6ee18) — Justin Rosner · 2026-05-20
- `5fa19a1` [[AMD] Handle padded layout in MemDescReinterpretOp verifier (#10184)](https://github.com/triton-lang/triton/commit/5fa19a164d80bee7626d8a1b1e605d99b914580b) — yangshuxin · 2026-05-20
- `7ee763f` [[PROTON] Update .gitignore to include additional stub files (#10339)](https://github.com/triton-lang/triton/commit/7ee763fc7e53ce4a85f8afa5e98440724e4469ff) — Keren Zhou · 2026-05-19
- `a0370fe` [[Tests] Drop pytest-forked in favour of run_in_process (#10335)](https://github.com/triton-lang/triton/commit/a0370fe129ccfb6949371ed23aa8c629da6b7fbc) — peterbell10 · 2026-05-19
- `8b2e898` [[CONSAN] Fix cluster_barrier handling (#10323)](https://github.com/triton-lang/triton/commit/8b2e898154e7367ef03dcc7b0ab3a3d9a860d705) — Mario Lezcano Casado · 2026-05-19
- `ed8317b` [[AMD][GFX9] Optimize warp-uniform direct to LDS predicates (#10332)](https://github.com/triton-lang/triton/commit/ed8317b20881e443aaf6c91d161cbacf6143dc53) — Alexander Weinrauch · 2026-05-19
- `fdfc3f9` [[PROTON] Allow out-of-tree backends to register Proton profilers, devices and runtimes. (#10246)](https://github.com/triton-lang/triton/commit/fdfc3f92f533901adb32ad4fb6b9271d9353fb4e) — George Wigley · 2026-05-19
- `0bdab22` [Allow Gluon local_store with mismatched CGA layout (#10296)](https://github.com/triton-lang/triton/commit/0bdab22f0ff751016fb5c3ff92a9867d1fb69483) — Thomas Raoux · 2026-05-19
