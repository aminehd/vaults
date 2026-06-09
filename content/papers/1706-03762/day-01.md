---
paper: https://arxiv.org/abs/1706.03762
day: 1/5
date: 2026-06-09
tags: [papers, daily-reading]
---

# Day 1 · 2026-06-09

## What this section is about
Day 1 of the paper that launched Transformers. The abstract + opening intro propose the **Transformer**: a sequence model built *entirely* on attention, throwing out recurrence (RNNs/LSTMs) and convolutions. The pitch: better translation quality, far more parallelizable, much cheaper to train.

## Key concepts introduced
- **Sequence transduction:** turning one sequence into another (e.g. English → German translation).
- **Recurrent models (RNN/LSTM/GRU):** process a sequence one position at a time, carrying a hidden state `hₜ` forward. The default before this paper.
- **Encoder–decoder:** one network reads the input, another produces the output.
- **Attention mechanism:** lets the model look at *any* position in the sequence directly, regardless of distance. Previously bolted *onto* RNNs; here it's the whole thing.
- **BLEU:** a 0–100ish score for translation quality (higher = better). 28.4 EN→DE and 41.8 EN→FR were SOTA-beating.

## The core idea (no jargon)
RNNs have a structural curse: to compute step `t`, you need step `t−1`'s hidden state, so the work is *inherently sequential* — you can't parallelize across positions within one example, and that bottleneck bites hard on long sequences. The authors' bet: attention already lets you relate any two positions directly, so why keep the slow recurrent backbone at all? Rip it out, build the model from attention alone — and suddenly the whole sequence can be processed in parallel. Faster *and* better.

## Math decoded
Only the recurrence relation so far: `hₜ = f(hₜ₋₁, inputₜ)` — each hidden state is a function of the previous one and the current input. The key takeaway isn't the formula, it's the *dependency*: `hₜ` can't be computed until `hₜ₋₁` exists. That serial chain is exactly the thing the Transformer is designed to eliminate.

## Why it matters
It frames the paper's core motivation — the sequential bottleneck of RNNs — which sets up *why* an all-attention architecture is worth proposing.

## Tomorrow
Likely the rest of the intro + background: how prior work tried to reduce sequential computation (and why attention is the cleaner answer), heading toward the actual architecture.

## Flashcards
#flashcard

- Why does the inherently sequential nature of RNNs limit them on long sequences? :: Each hidden state h_t depends on h_{t-1}, so computation can't be parallelized across positions within an example. At long sequence lengths this serial chain becomes a training-time and memory bottleneck.
- What does the Transformer remove from prior sequence-transduction architectures, and what does it keep? :: It dispenses with recurrence and convolutions entirely, relying solely on attention mechanisms.
- Before the Transformer, how was attention typically used in sequence models? :: As an add-on connecting the encoder and decoder of otherwise recurrent/convolutional models — not as the core computation. The Transformer's insight is making attention the whole architecture.
- Why is being 'more parallelizable' the key practical payoff of the Transformer? :: Removing the step-by-step recurrent dependency lets the whole sequence be processed at once, cutting training time (e.g. SOTA EN-FR BLEU of 41.8 in 3.5 days on 8 GPUs, a fraction of prior costs).
- What evidence suggests the Transformer is a general architecture, not just a translation model? :: It transfers successfully to English constituency parsing with both large and limited training data, in addition to beating SOTA on WMT 2014 EN-DE (28.4 BLEU) and EN-FR (41.8 BLEU).
