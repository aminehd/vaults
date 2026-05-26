---
repo: "Agent Governance Toolkit"
slug: agent-governance-toolkit
issues_count: 6
updated: 2026-05-26
---

# Agent Governance Toolkit — Contribution Opportunities

No GFI labels but accepts unsolicited docs/tooling PRs. zeel2104 has 4 PRs. Microsoft name.

← [[../agent-governance-toolkit|Back to Agent Governance Toolkit]]

## Open Issues (6)

- **[#2537 feat: language parity for wire-protocol-aware policy evaluation (TS, Rust, .NET, Go)](https://github.com/microsoft/agent-governance-toolkit/issues/2537)** `enhancement` `needs-review:MEDIUM`
  opened 2026-05-23 · 1 comments
  > ## Summary  Track language parity for the wire-protocol-aware policy evaluation feature being delivered for Python in #2487 (which closes #2483).  #2483 / #2487 only cover the **Python** implement

- **[#2480 feat: transparent proxy mode for zero-code interception](https://github.com/microsoft/agent-governance-toolkit/issues/2480)** `enhancement`
  opened 2026-05-22 · 1 comments
  > ## Summary  Add a transparent proxy/tunnel mode so AGT's governance sidecar can intercept agent traffic without requiring the agent to make explicit API calls.  ## Problem  AGT's current sidecar

- **[#2479 feat: policy regression testing framework](https://github.com/microsoft/agent-governance-toolkit/issues/2479)** `enhancement`
  opened 2026-05-22 · 1 comments
  > ## Summary  Add a `agt test` CLI command that replays recorded policy decisions against rule changes and fails when a verdict flips unexpectedly.  ## Problem  Policy rules evolve over time. When

- **[#2478 feat: human-in-the-loop and LLM judge approval chains for PolicyEvaluator](https://github.com/microsoft/agent-governance-toolkit/issues/2478)** `enhancement`
  opened 2026-05-22 · 0 comments
  > ## Summary  Add a `require_approval` verdict to PolicyEvaluator that routes ambiguous or high-risk decisions to human reviewers or LLM judges before allowing execution.  ## Problem  PolicyEvalua

- **[#2477 feat: wire detection modules into enforcement lifecycle](https://github.com/microsoft/agent-governance-toolkit/issues/2477)** `enhancement`
  opened 2026-05-22 · 0 comments
  > ## Summary  Several detection modules exist in AGT but are not automatically wired into the enforcement lifecycle via \BaseIntegration\. This means they appear in the feature matrix but don't fire i

- **[#2470 RFC: Support Azure Functions-based policy enforcement through AI Gateway for Foundry prompt-based agents](https://github.com/microsoft/agent-governance-toolkit/issues/2470)** `enhancement` `triage` `size/XL`
  opened 2026-05-22 · 2 comments
  > ### Summary  Propose support for a governance pattern in which AI Gateway policy can invoke Azure Functions to evaluate and enforce policy decisions for Microsoft Foundry prompt-based agent traffic, i
