---
paper: https://arxiv.org/abs/2301.08243
day: 1/9
date: 2026-06-09
tags: [papers, daily-reading]
---

# Day 1 · 2026-06-09

## What this section is about
Day 1 — the abstract and opening of the intro to **I-JEPA**, a self-supervised method for learning image features *without* hand-crafted augmentations. The trick: from one "context" patch, predict the *representations* (not pixels) of other masked patches in the same image. It's framed against the two dominant SSL camps — invariance-based and generative.

## Key concepts introduced
- **Self-supervised learning (SSL):** learn features from unlabeled images by inventing a pretext task (here: "predict the hidden parts").
- **Invariance-based methods:** train an encoder so two augmented views of the same image get *similar* embeddings. Strong features, but the augmentations bake in biases.
- **Generative methods:** reconstruct the missing raw signal (e.g. masked pixels).
- **JEPA:** predict the *embedding* of a target from a context via a predictor network — not raw pixels, not just "make views match."
- **Energy framing:** low energy = compatible pair, high energy = incompatible. A common lens for all three architectures (Fig 2).
- **Masking strategy:** the make-or-break design choice — targets must be *large/semantic*, context must be *spatially spread out/informative*.

## The core idea (no jargon)
Both existing camps have a catch. Invariance methods make *you* pick augmentations, which secretly tells the model "ignore color, ignore position" — great for classification, bad when a task actually needs those. Generative methods predict raw pixels, burning capacity on irrelevant detail (exact texture, noise) instead of meaning. I-JEPA's bet: **predict in representation space** — show part of an image, ask the model to guess the *features* of the masked parts. That pushes it toward semantics, no augmentation-engineering required, and it's cheaper (ViT-Huge in <72h on 16 A100s).

## Math decoded
No equations yet — but internalize the **energy** idea: a scalar score the model learns to push *low* for compatible (context, target) pairs and *high* for incompatible ones. The three architectures are just different machines for computing/minimizing that score.

## Why it matters
It plants the paper's thesis: you can get semantic representations without augmentation-engineering *or* pixel reconstruction — by predicting abstract features instead.

## Tomorrow
Probably the rest of the intro: the concrete case for *why* predicting in latent space beats the other two families.
