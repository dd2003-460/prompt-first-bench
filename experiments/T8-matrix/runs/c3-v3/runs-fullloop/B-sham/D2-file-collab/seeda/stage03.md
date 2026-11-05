**Repair Stage:** 02

**Reasoning:**
The input context for Stage 03 (Action Decomposition) relies on the output of Stage 02 (Evidence Verification). However, the provided "Stage 02 Output" is **incomplete and invalid**. It only contains a single Bash command checking for tools (`ralph`, `ego-browser`) and does not contain:
1.  Verified evidence about specific file collaboration/cloud drive solutions (e.g., Nextcloud, Synology Drive, Feishu/Lark, Tencent Docs, etc.).
2.  Cost verification against the ¥30,000/year budget.
3.  Feature verification (version control, granular permissions, offline capability).
4.  Platform compatibility verification (Web/macOS/Windows).

According to the operational rules: *"If the action plan depends on unverified facts, repair_stage write 02 or 02.5."* Since no verified facts exist in the Stage 02 output, I cannot generate a valid Stage 03 action plan that covers the goal without guessing. Therefore, the process must return to Stage 02 to gather actual evidence.

---

### [Artifact Placeholder - Do Not Execute]

*Note: The following structure shows what Stage 03 would look like once Stage 02 provides valid evidence. This is NOT the final output because the precondition (valid Stage 02 evidence) is missing.*

#### Hypothetical Stage 03 Structure (For Reference Only)

**Goal:** Produce a selection report for a team file collaboration solution.

**Precondition Check:**
- [ ] Evidence exists for at least 3 candidate solutions.
- [ ] Costs are verified for all candidates.
- [ ] Feature requirements (Version Control, Permissions, Offline) are verified for each candidate.

**Step 1: Candidate Shortlisting & Filtering**
- **Owner:** agent
- **Input:** Verified list of candidates from Stage 02.
- **Action:** Filter candidates based on hard constraints (Budget ≤¥30k, Web/macOS/Win support).
- **Dependency:** None (Start)
- **Output:** List of viable candidates (e.g., 3-5 options).
- **Acceptance:** All remaining candidates meet budget and platform requirements.

**Step 2: Deep-Dive Feature Validation**
- **Owner:** agent
- **Input:** Viable candidates list.
- **Action:** Verify core needs: Document version management granularity, permission models (folder/file level), offline sync mechanisms.
- **Dependency:** Step 1
- **Output:** Feature comparison matrix.
- **Acceptance:** Each feature requirement is marked as "Met", "Partially Met", or "Not Met" with evidence link.

**Step 3: Cost Modeling & TCO Calculation**
- **Owner:** agent
- **Input:** Pricing pages/documentation for viable candidates.
- **Action:** Calculate annual cost for 30 users. Include hidden costs (storage overage, premium features).
- **Dependency:** Step 1
- **Output:** Detailed cost breakdown per candidate.
- **Acceptance:** Total annual cost ≤ ¥30,000 confirmed or flagged as over-budget.

**Step 4: Draft Selection Report**
- **Owner:** agent
- **Input:** Feature matrix, Cost breakdown, Elimination reasons.
- **Action:** Compile into a structured report: Recommendation, Backup Options, Eliminated Options with Reasons.
- **Dependency:** Step 2, Step 3
- **Output:** Draft Selection Report.md.
- **Acceptance:** Report includes all required sections (Recommendation, Backup, Reasons, Cost).

**Step 5: User Review & Finalization**
- **Owner:** user
- **Input:** Draft Selection Report.md.
- **Action:** User reviews the recommendation and confirms if any business-specific factors (e.g., data residency, integration with existing SSO) need adjustment.
- **Dependency:** Step 4
- **Output:** Final Approved Selection Report.
- **Acceptance:** User signs off or requests specific changes which are incorporated.

**Parallelism:**
- Steps 2 and 3 can run in parallel after Step 1.

**Failure Handling:**
- If no candidate meets all core requirements within budget, flag as "No Solution Found" and recommend relaxing constraints (e.g., increasing budget or dropping offline requirement) for user decision.