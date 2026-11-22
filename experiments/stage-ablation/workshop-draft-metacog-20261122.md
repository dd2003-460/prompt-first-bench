# Metacognition Under Compute Limits: Monitoring, Repair, and the Non-Monotonic Budget–Quality Curve in a 27B Research Agent

*Workshop draft v0.1 — 2026-11-22 — status: DRAFT (numbers verified from local artifacts; see §6 limitations)*

---

## Abstract

Autonomous research agents are typically evaluated end-to-end, conflating what the model does with what the harness (prompt structure, verification loops, budget control) adds. We study this separation under an explicit compute constraint — a 27B open-weight model on 4×V100, no weight updates — where "more compute = better" cannot be assumed. Using a frozen three-layer mechanical judge (no LLM in the scoring path) and an orthogonal metacognition axis, we report four findings across 100+ runs on three research questions of increasing difficulty. (1) **Monitoring is present, repair is absent**: the agent marks information gaps with a healthy gap rate (84% of *search-source* degraded nodes are correctly classified as "unverifiable" rather than "contradicted"), but its rework loop fixes only 1.6–2.1% of flagged nodes — the metacognitive loop behaves as a *filter* (mark, retrieve, classify), not a *repair cycle*; the tree grows around its 55% unverified nodes rather than repairing them. (2) **Gap marking is functional, not noise**: the defensive-marking rate rises monotonically with question difficulty (nat 0.028 < soc 0.058 < gpu 0.147, era-matched, all pairwise p<0.001), the signature of calibrated uncertainty monitoring. (3) **Budget–quality is flat-to-weakly-non-monotonic**: depth score is highest at budget 150 (0.474) but the 100/300/719 tiers form a plateau (0.428–0.438) within one run-sd of the peak — at n=3/budget the "peak" is suggestive, not significant; a queued replication adds 5 reps to each of the 100/150/300 tiers (n=3→8 per tier, 15 runs) to pin the location. The robust part of the finding is that 719 buys ~700 nodes vs ~380 at 150 with no depth gain: more budget buys *breadth*, not *depth*. (4) **The loop is continuous but not cumulative**: verification rate is flat across depth (43–49% for L2–L4) and no layer fully breaks (18/18 runs), yet the 1.6–2.1% rework fix rate means the tree grows *around* its unverified nodes rather than repairing them — continuity of the search process coexists with the absence of a closed metacognitive repair cycle. Under compute limits, harness metacognition helps most where the model's own monitoring is weakest — the hard questions — and spending more budget past the peak buys nodes, not depth.

---

## 1. Introduction

Research-agent evaluations usually fix the model and vary the task, or fix the task and vary the model. We fix both and vary the **harness** — the prompt structure, verification loop, and node budget — because under a compute constraint the harness is the only degree of freedom left. The question: *what does structured metacognition (gap marking, retrieval, verification, rework) actually add, and when does it stop paying?*

Our setting is deliberately unglamorous: Qwen3-27B (NVFP4) on 4×Tesla V100, serving via vLLM, no weight modification. This is not a limitation to apologize for — it is the experimental condition. Conclusions are scoped to open-weight models in the 27B range; the claim is about the *shape* of the budget–quality relationship and the *location* of the metacognitive breakpoint, both of which should hold across models of similar capability.

Three contributions:
1. A **frozen mechanical judge** (three layers, deterministic, no LLM in the scoring path) that makes harness ablation reproducible.
2. A **metacognition axis** orthogonal to quality: it measures whether the agent monitors its own information state (gap marking) and controls it (retrieval + repair), separately from how good its answers are.
3. **Three findings** (§4): monitoring/repair dissociation, difficulty-calibrated gap marking, and a non-monotonic budget–quality curve.

## 2. Setup

**Questions.** Three research questions of increasing difficulty: *nat* (natural-language reasoning), *soc* (sociotechnical), *gpu* (GPU performance modeling with a 37-node gold decomposition tree). Difficulty ordering is by gold-tree depth and domain specificity, not by our score.

**Pipeline.** A state-machine research loop (S5): decompose → expand nodes → mark gaps → retrieve → verify → rework (max 2 reworks per node). The nominal node budget (max_nodes) is set to 50/100/150/300/719, but it is a *soft* cap — checked once per round, before a round's expansion — so a single round can overshoot it. Realized node counts overlap across tiers (budget 50 → 103–175 nodes; 100 → 122–314; 150 → 167–392; 300 → 364–415; 719 → 665–747). The budget parameter is therefore a *lower bound with overshoot*, not a clean independent variable; the realized node count (which proxies compute cost) is the effective one, and the two are conflated at the low tiers. We report both and scope the budget-tier claims accordingly (§4.3).

**Judge (frozen, v1.0; coverage layer patched 2026-11-23).** Three mechanical layers, no LLM: (L-struct) depth score — fraction of gold-tree depth reached, normalized; (L-cov) coverage — embedding match of model nodes to gold units (cosine ≥ 0.70), counted with per-unit deduplication (a gold unit matched by ≥1 node counts once). The original v1.0 "magnet" rule (a unit matched by ≥3 nodes was *excluded* entirely) was found to be a measurement artifact: it anti-correlated coverage with node count (a 401-node run scored 0.0 while a 316-node run scored 0.22, despite covering more units), so it was removed and retained only as a diagnostic field. Scores computed before the patch (noted in §4.3 and the supplementary) are flagged; the depth-only table in §4.3 is unaffected by the patch. (L-mech) formula/symbol check — diagnostic only (symbol alignment between model and gold is not yet solved, so it is excluded from the composite). Composite = 0.5·depth + 0.5·coverage. Thresholds calibrated on 15 runs (cosine 0.80 collapsed coverage to 0.015; 0.70 gives 0.350 with per-run spread 0.11–0.56 — discriminative). Deterministic: same input → same output.

**Metacognition axis.** Four metrics from node fields (no LLM): gap_rate (defensive markers / total nodes), retrieval_rate (source=search / total), healthy_gap_rate (unverifiable / (unverifiable + contradicted) among degraded nodes), post_retrieval_accuracy (verified / (verified + contradicted)). The v1.1 key correction: "degraded" splits into *unverifiable* (source lacks the value — a healthy "I checked, I can't verify") and *contradicted* (source conflicts — a true failure). Conflating them (v1.0) measured verification strictness, not self-awareness.

**Reproducibility.** Per-run results are *not* reproducible by design (temp 0.7, top_p 0.95, anti-cache perturbation, vLLM concurrent non-determinism). The pipeline and statistical conclusions are: all metrics are deterministic functions of the saved run JSON.

## 3. Related work (positioning, condensed)

- **Metacognition in LLMs**: factual self-awareness is documented (arXiv:2505.21399); metacognitive myopia — monitoring present, control absent — is the open gap (arXiv:2408.05568). We provide a *measured* instance of this dissociation in a research pipeline, with the breakpoint located (repair loop, not monitoring).
- **RSI / self-improvement**: greedy acceptance of single-run score gains misclassifies noise as progress (45.6% of accepts are degradations; statistical gates reduce to 2.8%, arXiv:2611.10787). Our budget scan is a controlled instance: more budget does not monotonically improve the score, so any self-improvement loop on this harness must use statistical gates.
- **Budget/effort scaling in reasoning**: compute-optimal scaling (Kaplan; Chinchilla) fixes the task and varies scale; we fix the task *and* the model and vary the harness budget — the regime where scaling-law promises do not apply (no loss to optimize, metacognition is not a parametric capability).
- **Deep-research benchmarks** (DREAM, DR-Bench, BrowseComp): assume tool access and measure end-to-end success; we isolate the harness under a no-weight-update constraint with a mechanical judge.

## 4. Findings

### 4.1 Monitoring is present; repair is absent

Across 83 runs: healthy_gap_rate mean 0.938 (range 0.667–1.0) — when the agent cannot verify a claim *after a search*, 84% of the time the correct diagnosis is "unverifiable" (the source genuinely lacks the value), not "contradicted". The agent *knows the difference between "I don't know" and "I'm wrong"*.

But the rework loop — the control mechanism — fixes only **1.6–2.1%** of reworked nodes (36/2298 budget-scan, 61/2919 era-matched). Root cause (from evidence-field analysis): 84% of *search-source* degraded nodes are *unverifiable* (the required value is model-specific and absent from generic sources), so rework spends budget re-searching nodes that are unverifiable by construction. Repair budget is misallocated: it should fire only on *contradicted* nodes (~6% of search-source degraded).

**Claim**: the metacognitive breakpoint in a 27B research agent is the repair loop, not monitoring. This refines the myopia framing of 2408.05568: monitoring is healthier than reported; the missing piece is *targeted* control.

### 4.2 Gap marking is difficulty-calibrated

Era-matched (same default budget, same pipeline era), defensive-marking rate rises monotonically with question difficulty:

| question | n | gap_rate | pairwise |
|---|---|---|---|
| nat | 21 | 0.0281 | nat<soc p=0.0003 |
| soc | 26 | 0.0576 | soc<gpu p<0.0001 |
| gpu | 18 | 0.1469 | nat<gpu p<0.0001 |

Kruskal–Wallis H=39.2, p<0.0001. If gap marking were noise, it would not track an independent difficulty ordering. It is the signature of calibrated uncertainty monitoring — the agent is more defensive exactly where it should be.

**Honest boundaries**: (i) within *soc*, gap_rate correlates with node count (ρ=0.488, p=0.010) — part of the soc effect may be a budget effect; (ii) the gradient is verified at one budget point (150); a budget-stratified replication is planned. A 质询 (adversarial check) initially found the 83-run aggregate mixed two populations (sm-* era vs budget-* scan); era-matching *strengthened* the gradient (gpu 0.102→0.147) and showed the budget scan's gap_rate is non-monotonic in budget (50→0.079, 100→0.209, 150→0.147, 300→0.082, 719→0.089) — a budget effect independent of difficulty.

### 4.3 Budget–quality is flat-to-weakly-non-monotonic

Depth score by nominal budget tier (n=3/tier, bootstrap 95% CI; realized node counts in §2):

| budget | mean depth | CI95 |
|---|---|---|
| 50 | 0.3842 | [0.3597, 0.4126] |
| 100 | 0.4352 | [0.4276, 0.4392] |
| **150** | **0.4743** | [0.4300, 0.5184] |
| 300 | 0.4275 | [0.3516, 0.4811] |
| 719 | 0.4376 | [0.4042, 0.4782] |

Run-to-run sd (0.046) vs the 150-vs-plateau gap (0.041, plateau = mean of 100/300/719): the 150 "peak" is **0.9 run-sd above the plateau — suggestive, not significant at n=3**. Dropping the 300-r3 outlier (0.3516) moves 300 to 0.465, within 0.009 of 150. Two caveats scope this claim. First, the budget tiers are soft caps with overlapping realized node counts (§2): tiers 50/100/150 realize 103–392 nodes and overlap, so a depth "peak at 150" cannot be cleanly attributed to the budget parameter rather than to realized node count; the replication must re-analyze on realized node count as the x-axis. Second, the peak's location and significance are exactly what the queued replication (5 added reps per tier at 100/150/300, n=3→8) is designed to settle; until then this finding is a hypothesis with the right sign, not a confirmed curve. The robust, n-independent part of the finding is the *breadth-vs-depth* split, stated on realized node counts: ~700 nodes (tier 719) vs ~380 (tier 150) with no depth gain — the agent spreads budget across sibling branches instead of pushing down the gold tree's spine. (The breadth claim rests on realized node counts and the depth axis, both question-agnostic; the coverage reading of breadth is partially confounded by the construct mismatch in §6.) **Under compute limits, the harness's budget allocation — not the budget size — is the quality variable.**

### 4.4 Failure modes and continuity (per-layer anatomy)

Per-layer status across 18 era-matched gpu runs (5,812 nodes):

| layer | nodes | verified | degraded | pending | ver% |
|---|---|---|---|---|---|
| L1 | 102 | 10 | 0 | 92 | 9.8% (by design: source=given, structural) |
| L2 | 514 | 232 | 212 | 70 | 45.1% |
| L3 | 1668 | 722 | 787 | 159 | 43.3% |
| L4 | 3528 | 1729 | 1799 | 0 | 49.0% |

Four structural observations:
1. **Verification is flat across depth** (43–49% for L2–L4): the agent does not get systematically worse at deeper nodes — depth is not a verification cliff. What degrades with depth is *coverage* (judge §4.3) — though the coverage axis is partially confounded by the construct mismatch in §6 (model and gold not on the same question surface), so the *depth* of the degradation is not yet cleanly attributed.
2. **No chain breaks below L1**: in 18/18 runs, every L2–L4 layer contains at least some verified nodes; the tree never dies at a layer. The loop is *continuous* in the weak sense (always some forward progress).
3. **The loop is continuous but not cumulative**: with a 1.6–2.1% rework fix rate, rework does not repair the 55% of nodes that fail verification — they stay degraded and the tree simply grows *around* them. The metacognitive loop therefore behaves as a **filter** (mark + retrieve + classify), not a **repair cycle** (mark → fix → re-verify → improved). This is the precise sense in which continuity holds while the (a)→(b)→(c) loop fails to close.
4. **The conclusion layer does not converge across budgets** (judge layer 4, "final answer vs gold winner" — distinct from tree-depth L4 above): across all 15 budget-scan runs, **0/15** final recommendations match the gold winner (4× RTX 3090 / W4 / n=2, L0-verified); the full-text string "3090×4" never appears (0/15), while "3090" alone appears in 14/15 as a candidate and in the final recommendation line of 3/15 runs (all as *2×* 3090, never the 4-card winner configuration). The 15 winners scatter across A100 / M3 Max / 2×4090 / 1×4090 / 5090 / W7900. The model *knows the candidate* but never *commits to the configuration* — and more budget does not fix this: the zero-convergence holds at every budget tier. This is a stronger signal than the score non-monotonicity in §4.3: budget buys more nodes, not a more stable answer. **Cross-dataset check (idea-2 arm, n=4, same question):** strict winner-configuration commits remain 0/4, but the loose "3090 in the conclusion layer" split by arm is 2/2 on the resume arm vs 0/2 on the fresh arm — the checkpoint-resumed runs' conclusions sit closer to the gold candidate set without ever committing the full configuration (suggestive at n=2/arm; consistent with the metacognition arm effect in §5).

**Predicted failure mode for the fix**: conditioning rework on degraded-class (§5.1) should raise fix-rate on the ~6% contradicted subset and free ~84% of rework budget; if the freed budget does not convert to depth (judge §4.3), the bottleneck is expansion, not repair — a falsifiable branch point for the next experiment.

## 5. Implications

1. **For harness design**: rework should be conditioned on the degraded-class (fire only on *contradicted*). This is a one-line change with a measurable prediction: repair fix-rate > 0 and budget reallocation toward depth. (Planned as the next experiment; acceptance via statistical gate, not single-run — per §2 related work, greedy gates misclassify 45.6% of accepts.)
2. **For evaluation**: a mechanical, frozen judge is feasible and necessary for harness ablation — LLM judges inject family bias and non-determinism into the very variable being measured.
3. **For compute-limited research**: the non-monotonic curve is a warning against "just give it more budget" — past the peak, extra budget degrades depth.

## 6. Limitations (stated up front)

- **Single model** (27B): no capability curve. The model-capability axis (7b/27b/70b) is planned but not run; claims are scoped to "open-weight, ~27B range".
- **Self-judge bias**: the depth axis is same-family; the report notes r=0.861 with an older LLM-judge cov axis. Heterogeneous re-judging (frontier API) is blocked (no API key) — a known gap, stated, not hidden.
- **n=3/budget**: the non-monotonicity is robust to run noise (sd < spread) but the peak *location* (150 vs 100) needs the queued replication (5 added reps per tier at 100/150/300, n=3→8) to pin down.
- **Mech layer diagnostic-only**: symbol alignment between model and gold unsolved; the formula layer contributes 0 to the composite.
- **One question family** for the gold tree (gpu); nat/soc golds are smaller (6/7 points).
- **Construct mismatch between question text and gold tree** (discovered 2026-11-23): the question states "context window ≥ 32K as a capacity floor" and asks the model to *search* its own hardware candidate set, while the gold tree is anchored at a fixed 64K context and a fixed candidate set (3090/M2Ultra/L40S/A100/V100/TPU). All 20 trees inspected (15 K7 + idea2 A-r1 + B-r1) take the 32K floor; the candidate-set overlap varies by run (K7 trees keep 3090 in-candidate, 7–40 mentions; idea2 B-r1 is closest to gold, 3090×78; idea2 A-r1 is the outlier — it excludes V100 explicitly and never considers 3090). Consequence: part of the low coverage scores reflects the model legitimately solving a *different* question than the gold encodes, not merely insufficient search depth. The depth axis (structural, question-agnostic) is unaffected; the coverage axis is partially confounded. Fix direction: pin context length and candidate set in the question text before drawing coverage-based conclusions.
- **Workshop scope**: this is a measurement + diagnosis paper, not a fix paper. The repair-loop fix is designed and predicted, not yet run.
- **Executor continuity (meta)**: the agent running this study is itself continuity-bound — its actions are passively triggered (user message or background-process completion), so a goal state-machine records *where to resume* but does not *drive* resumption. Continuity here is achieved by synchronous in-session progress + background processes covering GPU waits (auto-wake on completion) + planning written to seamless-resume granularity. Self-triggered unattended action is unavailable to the executor — a property of the research *process*, stated for honesty, distinct from the evaluated 27B system's metacognitive limits.

## 7. Future work

- **Structural stop-criterion axis (L2, new diagnostic layer).** A BOUND-weighted mechanical check of whether the agent expands where the gold decomposition requires expansion and stops where its stopping criteria (information-sufficient / black-box / business-data) apply. Across 14 runs the agent systematically over-expands (50 over- vs 24 under-expansions, 2.08:1) and the axis is near-orthogonal to the depth score (r = −0.23) — the model does not know when to stop. Not yet in the composite (representative-node assignment is the main measurement-error source); a replication with pinned question text is the next step.
- **Tree-level conditional information gain for bottleneck localization.** A follow-up direction: quantify, per reasoning-tree node, the conditional information gain of expanding that node toward the final answer, and use the gain profile to localize which layer of the decomposition is the bottleneck. A collision survey (2026-11-23) found the single components mature (Roofline bottleneck analysis: arXiv:2402.16363; information-gain CoT: arXiv:2411.11984; mechanistic NPU critics: arXiv:2611.24733) but the tree-level combination unclaimed — full-text check of the closest paper (2611.24733, 131K chars) shows zero overlap with reasoning-tree or information-gain content.
- **Replication and capability axis.** The queued replication (5 added reps per tier at 100/150/300, n = 3→8) pins the peak location; a 7b/70b capability curve is planned but not run.

## 8. Data & code

All metrics are deterministic functions of saved run JSONs; judge code, calibration record, metacog axis, and the 15-run budget scan are in the repository (paths in the supplementary). Reproduction: `judge_v1.py` + `metacog_axis.py` over `checkpoints/archive/`.

---

*Draft notes (not for submission): numbers from k7-pareto-15run-20261122.md, metacog-budget-scan-v1.1.json, judge-v1-cov-calibration.md, plan-layered-20261122.md (era-matched recompute). Venue target: ICML 2027 workshop. **Deadline verified 2026-11-23 (icml.cc/Conferences/2027/Dates, source ①)**: main-conference abstract 2027-01-14 AoE, full paper 2027-01-22 AoE; conference 2027-08-02~04 San Diego, workshops 08-05~06. Workshop-specific CFP/deadline not yet published (workshop organizers post separately, typically later than main) — re-verify when CFP drops. Related pending experiments: Idea 2 (checkpoint-as-cache, r1–r2 done: A>B on composite 2/2 reps, cov-driven; B-arm metacog *higher* 2/2 reps — gap rate 0.14 vs 0.06, checkpoint prefix carries verified gap markers, r3 in flight), rep replication (queued), repair-loop fix (designed).*
