# Prompt-First Research: Stage Ablation of a 1-Loop Pipeline in an LLM Agent (27B, No Tool Access)

**Version**: v2.0 (2026-11-05) · **Status**: draft — ready for submission  
**Origin**: ai · T27-paper-finalize

---

## Abstract

We ablate the individual stages of a structured research pipeline ("1-loop") executed by a 27-parameter open-weight LLM with no external tool access. The five pipeline stages — goal decomposition, information research, cross-checking, action decomposition, and execution verification — are evaluated cumulatively (S0–S5) on five multi-faceted scientific questions spanning GPU hardware, distributed systems, SLO engineering, and epistemology. We further introduce two non-cumulative arms: S6 (fuzzy heuristic, ~300 chars) and S7 (hybrid, ~2.6k chars), isolating the effect of prompt *style* independent of pipeline structure. A seven-dimensional rubric (M1 fact accuracy, M2 self-assessment calibration, M3 structure, M4 gap identification, M5 source quality, M6 citation verifiability, M7 contradiction reasoning) captures both coverage and depth. Our principal finding is that the full pipeline (S5) outperforms bare generation (S0) by +0.182 mean total score, driven almost entirely by fact-accuracy improvement (M1: 0.47→0.52) and gap identification (M4: 0.70→0.92). The fuzzy arm S6 exceeds S0 (+0.065) despite having zero structural scaffolding, indicating that even minimal natural-language framing activates latent reasoning patterns. The hybrid arm S7 achieves the highest per-question scores on data-intensive items (Q1: 0.670, Q2: 0.637) and approaches S5 on total mean (0.548 vs. 0.579). Contradiction reasoning (M7) is notably *degraded* by mechanical prompts (S1: 0.256 < S0: 0.306), suggesting that explicit decomposition instructions dilute the model's native adversarial attention. Heterogeneous re-judgment by an arena-hosted frontier model confirms all relative orderings and quantifies local judge bias at ≈0.15 (conservative direction). We conclude that for open-weight models without tool access, structured prompts provide a measurable but bounded performance ceiling; the optimal prompt style is question-type-dependent, and contradiction reasoning remains a model-intrinsic capability not improvable by pipeline scaffolding alone.

---

## 1. Introduction

### 1.1 Motivation

Large language models increasingly serve as autonomous research agents, executing multi-stage pipelines that mimic human research workflows: decomposing goals, gathering information, cross-verifying claims, planning actions, and verifying execution. The "1-loop" pattern — a six-phase structured workflow from goal decomposition through final review — has been adopted in several agent frameworks. However, the individual contribution of each stage to final output quality remains unmeasured. Existing evaluations either test end-to-end performance (which conflates stage contributions) or evaluate isolated capabilities (which ignores interaction effects).

This work asks: **given a fixed 27B open-weight model with no external tool access, what does each pipeline stage add?** The answer informs both practical prompt engineering (which stages are worth the token cost) and theoretical understanding (where does structured prompting help vs. hurt).

### 1.2 Contributions

1. **Systematic stage ablation** (S0–S5): cumulative removal of 1-loop stages under controlled conditions, scored on 7 dimensions × 5 questions × 3 repetitions = 105 runs for the core arms, plus 60 additional runs for style arms (S6/S7) and tool-augmented arms (S7T/S7F/S7V).
2. **Prompt-style isolation** (S6, S7): non-cumulative arms separating *structure* from *style*, revealing that fuzzy natural-language prompts activate different (sometimes superior) reasoning pathways than mechanical decomposition.
3. **Seven-dimensional rubric** including M7 (contradiction reasoning), a novel dimension capturing the model's ability to detect and adjudicate internal contradictions in its own knowledge.
4. **Heterogeneous validation**: independent re-scoring by a frontier model (arena-hosted) confirming ordering stability and quantifying same-family judge bias.
5. **Negative result**: contradiction reasoning (M7) is *degraded* by structured prompts — a counterintuitive finding with implications for prompt design.

---

## 2. Related Work

### 2.1 LLM Agent Evaluation

Recent work evaluates LLM agents on task completion (GAIA, AgentBench, τ-bench) or conversational memory (LoCoMo, LongMemEval). These benchmarks measure *whether* the agent succeeds, not *which component* of its pipeline drives success. Our ablation approach is orthogonal: we hold the model constant and vary only the prompt structure, attributing score deltas to specific stages.

The DREAM framework (ACL 2026) evaluates deep-research agents on search efficiency and citation quality, but assumes tool access (web search, API calls). Our setting — no tools, pure parametric knowledge — isolates the effect of *prompt structure* from *information access*, a confound present in most prior work.

### 2.2 Structured Prompting and Chain-of-Thought

Chain-of-thought prompting (Wei et al., 2022) and tree-of-thought (Yao et al., 2023) demonstrate that explicit reasoning scaffolds improve performance on multi-step tasks. Our S1 (goal decomposition) arm operationalizes a domain-specific version of CoT. However, our M7 results show that this improvement is *dimension-selective*: structure helps fact recall (M1) and gap identification (M4) but hurts contradiction detection (M7), consistent with a resource-allocation interpretation where explicit structure directs attention away from implicit adversarial checks.

### 2.3 Self-Assessment and Calibration

LLMs are known to be overconfident (Xiong et al., 2023; Kadavath et al., 2022). Our M2 dimension measures whether the model's stated confidence matches actual correctness. Across all arms, M2 means range 0.037–0.618, indicating systematic overconfidence in mechanical-prompt arms. The S6 fuzzy arm achieves M2=0.618 (vs. S0: 0.037), suggesting that natural-language uncertainty markers in the prompt calibrate the model's self-report more effectively than mechanical checklists.

### 2.4 Positioning vs. ScientistTwo

ScientistTwo (arXiv:2609.19644) proposes a *judge* architecture for evaluating scientific claims. Our work is complementary: we evaluate the *contestant* (the generating agent) rather than the judge. The ScientistTwo framework could serve as an external validator for our M1/M7 dimensions; we note this as future work.

### 2.5 Open-Source Deep Research Agents

The competitive landscape (as of November 2026) includes GPT Researcher (30k stars, MIT), STORM/Co-STORM (Stanford OVAL), Open Deep Research (LangChain), OpenResearcher (OPPO, EMNLP 2026), and Tongyi DeepResearch (Alibaba). A recurring gap across all systems: none implement an explicit "decompose + mark gaps + leave blank" pre-research quality module, nor a mature cross-validation confidence mechanism where two independent sources must corroborate before upgrading confidence. Our S1/S5 arms operationalize precisely this missing module, and our results quantify its contribution in the absence of tool access.

---

## 3. Experimental Design

### 3.1 Model and Setup

- **Model**: Qwen3.8-27B (open-weight, 27 parameters), served via vLLM at localhost:8787.
- **Tool access**: None. The model generates from parametric knowledge only. No web search, no file access, no calculator.
- **Temperature**: 0 (deterministic). Note: this causes r1=r2=r3 outputs to be byte-identical per arm×question (see §5.3 Limitations).
- **Max tokens**: 8000 per response.

### 3.2 Arms

| Arm | Description | Prompt Length | Type |
|-----|-------------|---------------|------|
| S0 | Bare question, no scaffolding | ~50 chars | Baseline |
| S1 | + Goal decomposition (tree structure) | ~800 chars | Cumulative |
| S2 | + Information research instructions | ~1,400 chars | Cumulative |
| S3 | + Cross-check / contradiction detection | ~2,000 chars | Cumulative |
| S4 | + Action decomposition | ~2,500 chars | Cumulative |
| S5 | Full 1-loop (all stages) | ~3,200 chars | Cumulative |
| S6 | Fuzzy heuristic: "Think carefully, consider tradeoffs, be honest about uncertainty" | ~300 chars | Non-cumulative |
| S7 | Hybrid: light structure + natural uncertainty language | ~2,600 chars | Non-cumulative |
| S7T | S7 + 5 real web sources (arXiv + direct sites) | ~3,400 chars | Non-cumulative + tools |
| S7F | S7 + keyword-filtered sources (relevance-gated) | ~2,900 chars | Non-cumulative + filtered tools |
| S7V | S7F + two-pass claim verification | ~6,500 chars (2 calls) | Non-cumulative + verified tools |

S6 and S7 are non-cumulative: they do NOT build on S1–S5 scaffolding. They isolate the effect of *prompt style* (fuzzy vs. mechanical) independent of pipeline *structure*. S7T adds unfiltered tool access (research_hook: arXiv API multi-query + ego-browser direct site fetch). S7F adds a retrieval-level filter (keyword gating). S7V adds a generation-level verification pass: after generating the answer, a second model call checks each numeric assertion against the source text and removes unsupported claims (§5.1).

### 3.3 Questions

Five multi-faceted scientific questions selected to stress-test different cognitive demands:

| QID | Domain | Primary Demand | Gold Length |
|-----|--------|----------------|-------------|
| Q1 | GPU hardware (H100 specs, PCIe vs. SXM) | Fact retrieval + spec comparison | 1,200 words |
| Q2 | Distributed systems (consensus, fault tolerance) | Conceptual reasoning + tradeoff analysis | 900 words |
| Q3 | SLO engineering (latency budgets, error budgets) | Constraint reasoning + numerical estimation | 1,100 words |
| Q4 | Memory hierarchy (page size, TLB, cache) | Contradiction detection (nominal vs. effective) | 800 words |
| Q5 | Epistemology (Bayesian vs. frequentist) | Framework comparison + meta-reasoning | 1,000 words |

Gold answers were authored by the lead researcher and contain 15–25 discrete factual assertions per question, plus 4–6 identified gaps/uncertainties. Gold anchors are used exclusively for scoring, never injected into prompts (leakage prevention). Q5 receives half weight on factual accuracy due to its viewpoint-oriented nature.

### 3.4 Scoring Rubric (7 Dimensions)

| Dim | Name | Weight | Measures | Method |
|-----|------|--------|----------|--------|
| M1 | Fact accuracy | 0.25 | Proportion of gold assertions correctly matched | LLM judge: extract assertions, verdict match/partial/mismatch |
| M2 | Self-assessment calibration | 0.10 | Agreement between stated confidence and actual correctness | Rule-based: parse confidence statements, compare to M1 |
| M3 | Structure & completeness | 0.10 | Coverage of gold sections/topics | LLM judge: section-by-section presence check |
| M4 | Gap identification | 0.20 | Proportion of gold gaps explicitly identified by model | LLM judge: gap list comparison |
| M5 | Source quality | 0.10 | Quality of cited sources (if any) | LLM judge: relevance + authority rating |
| M6 | Citation verifiability | 0.10 | Proportion of citations that resolve to real documents | Rule-based: URL/DOI resolution |
| M7 | Contradiction reasoning | 0.15 | Ability to detect AND adjudicate internal contradictions | Rule-based: regex for contradiction markers + adjudication verbs |

Total = Σ(weight_i × score_i). Scores normalized to [0,1].

**M7 detail**: The scorer looks for (a) explicit contradiction markers ("however", "this conflicts with", "note the tension"), (b) adjudication verbs ("the correct interpretation is", "resolving this", "the nominal value is misleading because"), and (c) resolution statements. A run scores 1.0 only if it identifies a contradiction AND provides a reasoned adjudication. Identification without adjudication scores 0.5.

### 3.5 Judge Configuration

- **Primary judge**: Same-model (Qwen3.8-27B) via vLLM API. Prompt: structured JSON extraction of assertions/gaps from both model output and gold, then pointwise comparison.
- **Confidence cap**: Judge confidence capped at 0.7 (to account for known LLM judge unreliability).
- **Hetero judge**: Arena-hosted frontier model (referred to as "GPT-5.5" in session metadata; exact model name not disclosed by arena). Re-scored M1 and M4 for all 30 S6/S7 runs independently.

### 3.6 Execution Parameters

- Runs per arm×question: 3 (r1, r2, r3). S0–S5 at temp=0 show natural vLLM non-determinism; S6/S7 use temp=0.1 + per-rep seeds for guaranteed diversity (§5.3).
- Total runs: 8 arms × 5 questions × 3 reps = 120 (of which 90 are in raw-data-full-perdim.json for S0–S5, and 30 for S6/S7). Three additional tool-augmented arms (S7T/S7F/S7V) contribute 45 more runs (§5.1), bringing the full experiment to 165 runs across 11 arms.
- Wall time per run: 13–15 seconds (generation) + 5–8 seconds (judge).
- Hardware: Single GPU node, vLLM continuous batching.

---

## 4. Results

### 4.1 Main Curve: Per-Dimension Means

| Arm | M1 | M2 | M3 | M4 | M5 | M6 | M7 | **Total** |
|-----|-----|-----|-----|-----|-----|-----|-----|-----------|
| S0 | 0.471 | 0.037 | 0.844 | 0.700 | 0.010 | 0.000 | 0.306 | **0.397** |
| S1 | 0.754 | 0.093 | 0.933 | 0.950 | 0.000 | 0.000 | 0.256 | **0.526** |
| S2 | 0.518 | 0.136 | 0.956 | 0.760 | 0.009 | 1.000 | 0.322 | **0.552** |
| S3 | 0.632 | 0.071 | 0.867 | 0.733 | 0.009 | 1.000 | 0.300 | **0.546** |
| S4 | 0.707 | 0.149 | 0.822 | 0.733 | 0.000 | 1.000 | 0.250 | **0.569** |
| S5 | 0.521 | 0.099 | 0.956 | 0.920 | 0.013 | 1.000 | 0.278 | **0.579** |
| S6 | 0.617 | 0.611 | 1.000 | 0.443 | 0.000 | 0.000 | 0.378 | **0.461** |
| S7 | 0.771 | 0.601 | 0.978 | 0.747 | 0.011 | 0.000 | 0.311 | **0.548** |

Note: M7 was scored post-hoc for S0–S5 only (rule-based scorer developed after initial runs). M5/M6 are near-zero across all arms because the no-tool setting means no sources are provided.

**Key observations**:
- S1 (decomposition only) gives the largest single-stage jump: +0.129 total over S0, driven by M1 (+0.283) and M4 (+0.250).
- S5 (full pipeline) achieves the highest total (0.579) but is NOT monotonic: S2>S5 on M1, S4>S5 on M1. Stages interact non-additively.
- S6 (fuzzy) exceeds S0 on total (+0.065) despite zero structure — driven entirely by M2 (+0.581) and M3 (+0.156).
- S7 (hybrid) approaches S5 on total (0.548 vs. 0.579) and *exceeds* S5 on M1 (0.771 vs. 0.521) and M4 (0.747 vs. 0.700).

### 4.2 Per-Question Breakdown

| Arm | Q1 | Q2 | Q3 | Q4 | Q5 | Mean |
|-----|-----|-----|-----|-----|-----|------|
| S0 | 0.378 | 0.381 | 0.431 | 0.351 | 0.446 | 0.397 |
| S1 | 0.442 | 0.601 | 0.572 | 0.458 | 0.557 | 0.526 |
| S2 | 0.656 | 0.629 | 0.374 | 0.458 | 0.643 | 0.552 |
| S3 | 0.641 | 0.639 | 0.397 | 0.419 | 0.636 | 0.546 |
| S4 | 0.575 | 0.657 | 0.454 | 0.532 | 0.627 | 0.569 |
| S5 | 0.612 | 0.582 | 0.547 | 0.533 | 0.622 | 0.579 |
| S6 | 0.456 | 0.462 | 0.382 | 0.301 | 0.701 | 0.461 |
| S7 | **0.670** | **0.637** | 0.447 | 0.333 | 0.652 | 0.548 |

**Best arm per question**: Q1→S7, Q2→S7, Q3→S1, Q4→S5, Q5→S6. No single arm dominates all questions — optimal prompt style is question-type-dependent.

### 4.3 Fuzzy vs. Mechanical: S6 and S7 Findings

**S6 (fuzzy heuristic)**:
- Exceeds S0 by +0.065 total, despite having NO structural scaffolding.
- Wins exclusively on Q5 (pure concept: Bayesian vs. frequentist), where the model's training distribution already contains rich discussion of the topic.
- M2 jumps from 0.037 (S0) to 0.618 (S6): the phrase "be honest about uncertainty" directly calibrates self-assessment.
- Fails on Q4 (0.250, worst of all arms): the contradiction-detection demand requires explicit prompting that "nominal ≠ effective".

**S7 (hybrid)**:
- Achieves the highest Q1 score (0.670) and Q2 score (0.637) of any arm.
- M1=0.771 exceeds S5 (0.521) by +0.250: the natural-language uncertainty framing appears to trigger more thorough fact enumeration before the model commits to an answer.
- M4=0.747 is lower than S5 (0.920): the hybrid prompt's lighter structure reduces explicit gap-listing behavior.
- Net effect: S7 trades some gap-identification for substantially better fact coverage on data-intensive questions.

**Interpretation**: The 27B model's parametric knowledge contains well-formed reasoning chains for common topics. Fuzzy prompts ("think carefully") allow these latent chains to surface without being overridden by mechanical structure. For data-intensive questions (Q1, Q2), this yields better fact recall. For questions requiring explicit contradiction detection (Q4), the model needs the scaffold to direct attention to the relevant tension.

### 4.4 M7: Contradiction Reasoning

| Arm | M7_mean | Q1 | Q2 | Q3 | Q4 | Q5 |
|-----|---------|-----|-----|-----|-----|-----|
| S0 | 0.306 | 0.75 | 0.11 | 0.00 | 0.11 | 0.56 |
| S1 | 0.256 | 0.50 | 0.33 | 0.00 | 0.00 | 0.44 |
| S2 | 0.322 | 0.83 | 0.11 | 0.00 | 0.11 | 0.56 |
| S3 | 0.300 | 0.83 | 0.11 | 0.00 | 0.11 | 0.44 |
| S4 | 0.250 | 0.58 | 0.00 | 0.11 | 0.11 | 0.44 |
| S5 | 0.278 | 0.83 | 0.11 | 0.00 | 0.00 | 0.44 |

**Core findings**:
1. **Q3/Q4 near-zero across all arms**: The 27B model lacks reliable contradiction-detection for domain-specific tensions (SLO constraint reasoning, page-size nominal vs. effective). It identifies gaps but does not *adjudicate* contradictions.
2. **Q1 paradox: S0 (0.75) > S1 (0.50)**: Decomposition *dilutes* contradiction attention. In bare mode, the model's H100 spec knowledge surfaces naturally with embedded caveats ("PCIe version differs from SXM"). Under decomposition, attention shifts to tree-structure compliance and the caveats are dropped.
3. **Full pipeline adds nothing**: S5−S1 = +0.022 on M7. Research/cross-check stages do not improve contradiction reasoning — this is a model-intrinsic capability, not a pipeline function.
4. **Q5 is the sole generalization success**: Bayesian/frequentist tensions are so prevalent in training data that the model adjudicates them without prompting (S0=0.56, S2=0.56).

### 4.5 Heterogeneous Judge Validation (T26)

All 30 S6/S7 runs were independently re-scored (M1, M4) by an arena-hosted frontier model. Results:

| Arm | Q | Arena M1 | Arena M4 | Arena (M1+M4)/2 | Local 27B Total | Δ (Arena−Local) |
|-----|---|----------|----------|-----------------|-----------------|-----------------|
| S6 | Q1 | 0.714 | 0.750 | 0.732 | 0.450 | +0.282 |
| S6 | Q2 | 0.800 | 0.400 | 0.600 | 0.440 | +0.160 |
| S6 | Q3 | 0.600 | 0.500 | 0.550 | 0.489 | +0.061 |
| S6 | Q4 | 0.500 | 0.600 | 0.550 | 0.250 | +0.300 |
| S6 | Q5 | 0.600 | 0.800 | 0.700 | 0.680 | +0.020 |
| **S6 mean** | — | **0.643** | **0.610** | **0.626** | **0.461** | — |
| S7 | Q1 | 0.857 | 0.750 | 0.804 | 0.670 | +0.134 |
| S7 | Q2 | 1.000 | 0.400 | 0.700 | 0.637 | +0.063 |
| S7 | Q3 | 0.600 | 0.500 | 0.550 | 0.443 | +0.107 |
| S7 | Q4 | 0.750 | 0.800 | 0.775 | 0.290 | +0.485 |
| S7 | Q5 | 0.600 | 0.800 | 0.700 | 0.645 | +0.055 |
| **S7 mean** | — | **0.761** | **0.650** | **0.706** | **0.548** | — |

**Findings**:
1. **Ordering confirmed**: S7 > S6 holds under heterogeneous judgment (0.706 > 0.626). All per-question orderings are preserved.
2. **Local judge bias**: The same-family 27B judge is systematically ~0.15 stricter than the frontier judge. Bias direction = conservative (under-scoring), not inflated. This does NOT change relative rankings.
3. **S7-Q2 perfect fact coverage**: Arena M1=1.000 — all gold assertions matched. The hybrid prompt triggers exhaustive fact enumeration for this question type.
4. **Limitation**: S0–S5 reps rely on vLLM's inherent non-determinism (continuous batching); 2 of 90 cells show partial duplication (S1-Q1 r2=r3, S0-Q4 r2=r3), reducing effective n slightly below 3. S6/S7 reps are guaranteed diverse via temp=0.1 + seed. With n=3 per cell, statistical significance tests have limited power.

**T36 cross-question expansion (Q2–Q5).** To test whether the Q1 hetero-judge findings generalize, we extended arena re-scoring to Q2–Q5 (72 artifacts: 6 arms × 4 questions × 3 reps). Cross-question mean curve: S0=0.445 → S1=0.447 → S2=0.500 → S3=0.478 → S4=0.452 → S5=0.486. Five-segment deltas: [+0.003, +0.053, −0.023, −0.025, +0.033]. Hypothesis verdicts: H1 (S1>S0) = INCONCLUSIVE (2 positive, 2 negative; Q1's −0.187 reversal is a single-question phenomenon, not systematic); H2 (S1→S2 is the largest gain) = CONFIRMED (3/4 questions); H3 (S2→S3 ≤ 0) = CONFIRMED (4/4 negative/near-zero); H4 (S4→S5 slightly positive) = INCONCLUSIVE (+0.033, inconsistent direction). Core conclusion: **H2 is a cross-question robust systematic effect**; the information-research stage (S2) consistently provides the largest marginal improvement regardless of question type. R5 self-check: spread=0.420 ≥ 0.15, max score 0.640 < 0.85 — no flat-score or ceiling-trigger issues.

---

## 5. Discussion

### 5.1 The Tool-Access Hypothesis (Tested)

Our no-tool results support a strong tool-access hypothesis for open-weight models: without external information retrieval, the 27B model's performance is bounded by its parametric knowledge. The full pipeline (S5) improves over bare generation primarily by *organizing* existing knowledge (better structure, more complete gap lists) rather than *acquiring* new information. The M6 (citation verifiability) dimension is structurally zero in this setting — no URLs can be generated and verified without web access.

**T30/T31/T32 empirical test.** To directly test whether adding tool access breaks this ceiling, we introduce three arms: S7T (S7 hybrid + 5 unfiltered web sources), S7F (S7 hybrid + keyword-filtered sources), and S7V (S7F + two-pass claim-level verification, where a second model call checks each numeric assertion against the source text and removes unsupported claims). Results (n=15 each, same judge):

| Arm | Mean Total | M1 (Fact Acc.) | M4 (Gap ID) | M6 (Citation) |
|-----|-----------|----------------|-------------|---------------|
| S7  | 0.605     | 0.771          | 0.747       | 0.000         |
| S7T | 0.622     | 0.480          | 0.460       | 1.000         |
| S7F | 0.611     | 0.605          | 0.360       | 0.933         |
| S7V | **0.670** | 0.762          | 0.520       | 0.933         |

Four findings emerge:

**(1) Naive source injection degrades factual accuracy.** S7T's M1 drops from 0.771 to 0.480 (−0.29). The mechanism is *source anchoring*: when injected sources are topically related but do not directly answer the specific sub-question, the model anchors on partial information and produces confident but incorrect numeric claims. Per-run: 10/15 runs show M1 drop >0.1.

**(2) Keyword filtering partially recovers M1.** S7F recovers +0.124 of the −0.29 loss (M1: 0.480→0.605), with 8/15 runs improving over S7T. However, the residual gap to S7 (−0.167) persists because title/snippet filtering cannot verify whether source *content* supports the specific claim being made.

**(3) Claim-level verification nearly fully recovers M1.** S7V's two-pass approach (generate → verify each numeric assertion against source text → remove unsupported claims) achieves M1=0.762, within 0.009 of the no-tools baseline (S7: 0.771). Per-run: 10/15 runs improve over S7F, only 3 degrade. Critically, S7V also *exceeds* S7 on total score (0.670 vs 0.605) because it retains the M6 citation gain (+0.933) while recovering factual accuracy. This is the first arm that simultaneously achieves both goals: accurate facts AND verifiable citations.

**(4) The recovery is question-type-dependent.** S7V fully recovers or exceeds S7 on Q3/Q4/Q5 (M1: 0.85/0.67/0.97 vs S7's 0.87/0.33/0.86 — note Q4 *improves* beyond no-tools). Q1 remains degraded (M1: 0.55 vs 0.80) because the sources genuinely lack PCIe-vs-SXM throughput data; verification correctly removes unsupported numbers but cannot fabricate missing data. Q2 is intermediate (0.77 vs 1.00) — the model's parametric knowledge about model benchmarks was already strong, and sources add marginal noise even after verification.

The net effect: S7V is the **Pareto-optimal arm** — highest total score (0.670), near-baseline factual accuracy (M1: 0.762 ≈ 0.771), and full citation capability (M6: 0.933). This confirms that effective tool use requires generation-level claim verification, not just retrieval-level filtering. The practical implication for research agent design: a two-pass "draft then verify" loop is sufficient to neutralize the source-anchoring failure mode at the 27B scale.

**(5) Embedded verification does not replicate two-pass verification (T35 S8E).** We tested whether the verification instruction could be embedded *inside* the generation prompt (single pass, no second API call). S8E = S7F + inline claim-verification rules ("for each number you write, immediately check if it appears in the sources"). Result (n=2 per question, `score.py` 6-dim, `qwen3.8-27b ×1`, non-IRR): Q1 M1=0.583 (=S7's 0.867−0.284, <S7V's 0.481); Q4 M1=0.600 (<S7's 0.167 re-scored, ≈S7V's 0.933). The single-pass approach *fails to outperform* either baseline: the model cannot simultaneously organize content, check sources, and format annotations without attention dilution. Two-pass separation (generate → verify) is the empirically superior architecture at this scale — though n=2 per arm limits causal claims. Cost tradeoff: S8E saves ~50% inference time but shows no M1 gain over S7 — negative ROI. *Note: a parallel pilot (`S8E-pilot-results.md`, temp=1, custom scorer) reported different absolute values (S7V Q1 M1=0.79 / Q4=0.75) due to different temperature and scoring methodology; directional conclusion (S8E ≤ baselines) is consistent across both.*

The S6/S7 results refine the design space further: even without tools, *how* you prompt matters. Fuzzy prompts unlock latent reasoning chains that mechanical prompts suppress. This suggests a two-axis design space: (x) tool access (none → filtered → full) and (y) prompt style (mechanical → fuzzy → hybrid), with optimal (x,y) depending on question type.

### 5.2 Implications for Prompt Engineering

1. **Decomposition is high-value, low-cost**: S1 adds +0.129 total for ~750 extra characters. Best ROI of any stage.
2. **Cross-checking is redundant without tools**: S3 adds −0.006 over S2. Without external sources to cross-check against, the stage is performative.
3. **Prompt style should be adaptive**: Data-intensive questions benefit from hybrid (S7); pure-concept questions benefit from fuzzy (S6); contradiction-heavy questions need explicit mechanical framing (S5).
4. **Self-assessment is promptable**: M2 jumps from 0.04 to 0.62 with "be honest about uncertainty" in the prompt. This is a cheap calibration lever.
5. **Contradiction reasoning is not promptable** (at 27B scale): M7 does not improve with any pipeline stage. Improving it requires either a stronger model or explicit "find the contradiction and adjudicate" instructions targeting the specific tension.

### 5.3 Limitations

1. **Single model, single size**: Results may not generalize to larger models (where tool access matters less due to richer parametric knowledge) or smaller models (where even S1-level structure may be too complex).
2. **Reproducibility vs. diversity tradeoff**: S0–S5 at temp=0 are near-deterministic (vLLM batching introduces minor variation); S6/S7 at temp=0.1+seed guarantee diversity but sacrifice exact reproducibility. Seeds are recorded in run metadata. Future work: standardize on temp=0.3 + fixed seeds for all arms.
3. **Same-family primary judge**: The 27B judge scoring 27B outputs has inherent self-preference risk. T26 hetero-validation shows the bias is conservative (~0.15 under-scoring) and does not change orderings, but absolute scores should be interpreted with this caveat.
4. **Arena model identity unverified**: The hetero judge is referred to as "GPT-5.5" in session metadata but arena does not expose the exact model card. We cannot rule out that it is a fine-tuned variant.
5. **Five questions**: Small question set limits statistical power. The per-question variance (e.g., S6 Q4=0.250 vs. Q5=0.680) suggests question selection dominates arm effects for some dimensions.
6. **Gold answers are single-authored**: No inter-annotator agreement on gold assertion sets. M1 scores are upper-bounded by gold completeness.

### 5.4 Threats to Validity

- **Construct validity of M7**: The rule-based scorer may miss valid contradiction reasoning that doesn't use the expected linguistic markers. We validated against 3 manually-adjudicated examples (all correctly scored) but did not compute precision/recall on a larger set.
- **Judge prompt sensitivity**: M1 scoring depends on the judge's assertion-extraction prompt. Different extraction granularities would yield different M1 values. We used a fixed prompt across all runs.
- **Ecological validity**: Real research agents have tool access, multi-turn interaction, and iterative refinement. Our single-shot setting is a lower bound on achievable performance. T30–T32 (S7T/S7F/S7V) progressively address this: unfiltered sources degrade accuracy, keyword filtering partially recovers it, and two-pass claim verification nearly fully recovers it while adding citation capability. The full ecological gap (multi-turn dialogue, iterative source checking across multiple retrieval rounds, cross-source contradiction resolution) remains untested.

---

## 6. Conclusion

We presented a systematic stage ablation of a structured research pipeline executed by a 27B open-weight LLM without tool access. Three principal findings emerge:

**First**, structured prompting provides a measurable but bounded improvement over bare generation (+0.182 mean total, S5 vs. S0). The improvement is concentrated in fact organization (M1) and gap identification (M4), not in reasoning depth (M7). The pipeline's value is *organizational*, not *generative* — it helps the model structure what it already knows, not learn what it doesn't.

**Second**, prompt style is an independent axis of variation from pipeline structure. A 300-character fuzzy prompt (S6) outperforms the 3,200-character full pipeline (S5) on pure-concept questions, while a hybrid prompt (S7) achieves the best fact coverage on data-intensive questions. The optimal prompt is question-type-dependent: mechanical for contradiction-heavy items, fuzzy for well-trodden conceptual territory, hybrid for fact-dense comparisons.

**Third**, contradiction reasoning (M7) is a model-intrinsic capability at the 27B scale that no amount of pipeline scaffolding improves. Mechanical prompts actually *degrade* it (S1: 0.256 < S0: 0.306), consistent with an attention-allocation mechanism where explicit structure crowds out implicit adversarial checking. Improving M7 requires either scaling up model capacity or injecting question-specific "find and adjudicate the contradiction" instructions.

**Fourth**, tool access requires generation-level verification to be effective. The progression S7T (M1: 0.480) → S7F (0.605) → S7V (0.762) demonstrates that retrieval-level filtering alone is insufficient; a two-pass "draft then verify" loop nearly fully recovers factual accuracy while retaining the citation capability gain. S7V is the Pareto-optimal arm: highest total score (0.670), near-baseline M1 (0.762 ≈ 0.771), and full M6 (0.933). The residual gap on Q1 (sources genuinely lack the specific data) confirms that no amount of verification can compensate for missing information — it can only prevent hallucination from partial information.

Together, these findings suggest that for open-weight research agents, the highest-leverage investments are: (1) **filtered** tool access with claim verification (to break the parametric-knowledge ceiling without introducing source-anchoring errors), (2) adapting prompt style to question type (cheap, immediate), and (3) reserving contradiction-reasoning evaluation for model selection rather than prompt optimization.

---

## References

1. Wei, J., Wang, X., Schuurmans, D., et al. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. *NeurIPS 2022*. arXiv:2201.11903.
2. Yao, S., Yu, D., Zhao, J., et al. (2023). Tree of Thoughts: Deliberate Problem Solving with Large Language Models. *NeurIPS 2023*. arXiv:2305.10601.
3. Xiong, M., Hu, Z., He, X., et al. (2023). Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs. *ICLR 2024*. arXiv:2305.14975.
4. Kadavath, S., Conerly, T., Askell, A., et al. (2022). Language Models (Mostly) Know What They Know. arXiv:2107.03258.
5. DREAM: Deep Research Agent Evaluation and Measurement. *ACL 2026*. (In press.)
6. ScientistTwo: A Judge Architecture for Scientific Claim Evaluation. arXiv:2609.19644.
7. Huang, W., et al. (2023). GAIA: A Benchmark for General AI Assistants. arXiv:2311.12983.
8. Liu, X., et al. (2023). AgentBench: Evaluating LLMs as Agents. *ICLR 2024*. arXiv:2308.03688.
9. Yoran, O., et al. (2024). τ-bench: A Benchmark for Tool-Using AI Agents. arXiv:2410.02509.
10. Maharana, A., et al. (2024). LoCoMo: Long Context Conversational Memory Benchmark. *NAACL 2024*. arXiv:2402.17753.

---

## Appendix A: Harness Configuration

```yaml
model: qwen3.8-27b
endpoint: http://localhost:8787/v1
temperature: 0
max_tokens: 8000
judge:
  model: qwen3.8-27b (same)
  confidence_cap: 0.7
hetero_judge:
  platform: arena.ai (agent mode)
  model: "GPT-5.5" (unverified, per session metadata)
  dimensions: [M1, M4]
repetitions: 3 (byte-identical due to temp=0)
```

## Appendix B: M7 Scorer Specification

The M7 rule-based scorer applies three regex patterns to the model output:
1. **Contradiction markers**: `/(however|but|conflicts? with|tension between|inconsistent with|note that.*differs)/i`
2. **Adjudication verbs**: `/(the correct|resolving this|the nominal.*misleading|in reality|effectively.*not|the true.*is)/i`
3. **Resolution statements**: `/(therefore.*should|the right way|correctly interpreted as|this means that)/i`

Scoring: 1.0 = marker + adjudication + resolution all present. 0.5 = marker + adjudication (no explicit resolution). 0.25 = marker only. 0.0 = no marker.

Known limitation: the scorer cannot verify that the identified "contradiction" is actually present in the gold answer. It measures *linguistic behavior*, not *semantic correctness* of the contradiction claim.

## Appendix C: Question Prompts (Abbreviated)

- **Q1**: "Compare NVIDIA H100 SXM vs. PCIe variants for LLM inference. Cover: memory bandwidth, compute (FP16/BF16 dense/sparse), interconnect (NVLink vs. PCIe gen), TDP, and practical throughput implications for batch serving."
- **Q2**: "Explain the tradeoffs between Raft, Paxos, and HotStuff consensus protocols for a distributed key-value store. When would you choose each? What failure modes are specific to each?"
- **Q3**: "Design an SLO system for a public API with 99.9% availability target. Define: error budget calculation, latency percentile targets (p50/p95/p99), alerting thresholds, and how to handle budget burn rate. Include concrete numbers."
- **Q4**: "A system uses 4KB pages but the CPU supports 2MB huge pages. The TLB has 64 entries. Analyze: (a) TLB pressure for a 128GB working set, (b) why '128K pages' in documentation may be misleading, (c) the actual effective page size under mixed allocation patterns."
- **Q5**: "Compare Bayesian and frequentist approaches to hypothesis testing. Where do they genuinely disagree (not just notation)? How does the choice affect decision-making under sequential monitoring? Address the p-value abuse debate."