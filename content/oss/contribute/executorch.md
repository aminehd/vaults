---
repo: "ExecuTorch"
slug: executorch
issues_count: 3
updated: 2026-05-26
---

# ExecuTorch — Contribution Opportunities

MLX operator team actively solicits implementations. Formula-based, testable, isolated.

← [[../executorch|Back to ExecuTorch]]

## Open Issues (3)

- **[#19718 Arm backend: Refactor run.sh into run.py](https://github.com/pytorch/executorch/issues/19718)** `partner: arm`
  opened 2026-05-21 · 0 comments
  > ### 🚀 The feature, motivation and pitch  Refactor run.sh into run.py  ### Alternatives  _No response_  ### Additional context  _No response_  ### RFC (Optional)  _No response_  cc @digantdesai @fredda

- **[#19650 Seed unit tests](https://github.com/pytorch/executorch/issues/19650)**
  opened 2026-05-18 · 0 comments
  > Set a deterministic seed for unit test jobs. This should reduce the incidence of tolerance flakes.

- **[#19647 fail to build 'llama' using examples/arm/run.sh](https://github.com/pytorch/executorch/issues/19647)** `partner: arm` `module: arm`
  opened 2026-05-18 · 0 comments
  > ### 🐛 Describe the bug  Wth this command:  `./examples/arm/run.sh --model_name=llama`  I get this error:  ``` Running e2e flow for model 'llama' with flags '--delegate --quantize ' -------------------
