---
concept: "Triton Kernels"
slug: triton-kernels
tags: [kernels, gpu, cuda, optimization]
repos: [Triton, Unsloth, FlashAttention]
updated: 2026-05-24
---

# Triton Kernels

**Repos:** [[../triton|Triton]] · [[../unsloth|Unsloth]] · [[../flashattention|FlashAttention]]

Triton is a Python-like DSL for writing GPU kernels. Abstracts away low-level CUDA
while still generating highly optimized GPU code.

## Why Triton Over CUDA
- Write in Python syntax — no C++ required
- Automatic handling of shared memory, tiling, vectorization
- Easier to read and contribute to than raw CUDA
- Powers: FlashAttention v2, Unsloth, Liger-Kernel

## Core Concepts
- **Tile**: the unit of work — a 2D block of a tensor processed in SRAM
- **Program ID**: identifies which tile this GPU thread block handles
- `tl.load` / `tl.store`: read/write with masking for boundary handling
- `tl.dot`: fused matrix multiply

## Example Pattern
```python
@triton.jit
def kernel(X_ptr, Y_ptr, N, BLOCK: tl.constexpr):
    pid = tl.program_id(0)
    offs = pid * BLOCK + tl.arange(0, BLOCK)
    x = tl.load(X_ptr + offs, mask=offs < N)
    tl.store(Y_ptr + offs, x * 2, mask=offs < N)
```

## Related
- [[flash-attention|Flash Attention]] — major Triton use case
- [[quantization|Quantization]] — quantization kernels often use Triton

