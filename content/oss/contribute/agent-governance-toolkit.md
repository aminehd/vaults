---
repo: "Agent Governance Toolkit"
slug: agent-governance-toolkit
issues_count: 6
updated: 2026-05-25
---

# Agent Governance Toolkit — Contribution Opportunities

No GFI labels but accepts unsolicited docs/tooling PRs. zeel2104 has 4 PRs. Microsoft name.

← [[../agent-governance-toolkit|Back to Agent Governance Toolkit]]

## Open Issues (6)

- **[#2573 feat: transparent proxy mode for non-Python SDKs (TypeScript, .NET, Rust, Go)](https://github.com/microsoft/agent-governance-toolkit/issues/2573)** `enhancement` `needs-review:MEDIUM`
  opened 2026-05-25 · 2 comments
  > ## Summary  Extend the transparent proxy / zero-code interception capability (originally proposed in #2480 for Python) to the other AGT language SDKs: TypeScript, .NET, Rust, and Go.  ## Backgroun

- **[#2537 feat: language parity for wire-protocol-aware policy evaluation (TS, Rust, .NET, Go)](https://github.com/microsoft/agent-governance-toolkit/issues/2537)** `enhancement` `needs-review:MEDIUM`
  opened 2026-05-23 · 1 comments
  > ## Summary  Track language parity for the wire-protocol-aware policy evaluation feature being delivered for Python in #2487 (which closes #2483).  #2483 / #2487 only cover the **Python** implement

- **[#2535 feat: credential injection and offload -- port to TypeScript, Rust, .NET, Go SDKs](https://github.com/microsoft/agent-governance-toolkit/issues/2535)** `enhancement` `needs-review:MEDIUM`
  opened 2026-05-23 · 1 comments
  > ## Summary  Port the credential injection and offload primitive landed for Python in #2481 / #2534 to the remaining AGT language SDKs: **TypeScript, Rust, .NET, and Go**.  The Python implementatio

- **[#2480 feat: transparent proxy mode for zero-code interception](https://github.com/microsoft/agent-governance-toolkit/issues/2480)** `enhancement`
  opened 2026-05-22 · 1 comments
  > ## Summary  Add a transparent proxy/tunnel mode so AGT's governance sidecar can intercept agent traffic without requiring the agent to make explicit API calls.  ## Problem  AGT's current sidecar

- **[#2479 feat: policy regression testing framework](https://github.com/microsoft/agent-governance-toolkit/issues/2479)** `enhancement`
  opened 2026-05-22 · 1 comments
  > ## Summary  Add a `agt test` CLI command that replays recorded policy decisions against rule changes and fails when a verdict flips unexpectedly.  ## Problem  Policy rules evolve over time. When

- **[#2478 feat: human-in-the-loop and LLM judge approval chains for PolicyEvaluator](https://github.com/microsoft/agent-governance-toolkit/issues/2478)** `enhancement`
  opened 2026-05-22 · 0 comments
  > ## Summary  Add a `require_approval` verdict to PolicyEvaluator that routes ambiguous or high-risk decisions to human reviewers or LLM judges before allowing execution.  ## Problem  PolicyEvalua
