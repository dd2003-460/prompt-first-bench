# How Much Does Microarchitecture Matter? A Closed-Form, Pre-Registered Measure of the Incremental Contribution of Deep Judgments in GPU Bottleneck Diagnosis

## Abstract

Diagnosing the performance bottleneck of a GPU workload is a compositional judgment: which component (tensor compute at a given precision, the scalar/issue path, or memory bandwidth) dominates wall-clock time depends on the *interaction* between workload composition and microarchitectural rates, not on workload composition alone. We formalize the incremental contribution of a deep microarchitectural judgment relative to a surface (shallow enumeration) judgment as the amount by which the deep judgment *corrects* the surface one — direction correction (bottleneck-type flip) and granularity correction (time-share shift) — and show that this quantity, together with the strict mutual information it induces, is computable in closed form from hardware specifications and a workload prior, with no experiments and no learned components. Across four platforms (RTX 5090, Thor T5000, RTX 4090, A100) and 40,000 sampled workloads, the surface judgment — which assumes all component rates are equal, so that time is proportional to workload share — misidentifies the bottleneck type on 43–56% of workloads, and the deep correction (time shift) ranges from 0.17 to 0.23. Strict mutual information confirms the same split: deep-only information $H(D|S)$ is 0.71–0.77 bits, and vanishes exactly to 0.0 under a flat-rate control, ruling out the trivial explanation that deep nodes merely forward surface information. Three hand-derived anchors reproduce exactly. The correction scales with the *structure* of the rate ratio, not merely its extremity. All criteria were preregistered (commit `eb1b0598c`, 17:39) before data generation (`718394ece`, 18:06).

## 1. Introduction

GPU performance diagnosis is routinely framed as a linear attribution problem: roofline-style analysis maps a workload to a compute- or memory-bound regime, and step-level attribution methods assign credit to components in proportion to their share. This framing silently assumes that time is proportional to workload share — i.e., that all components run at comparable rates. We argue that this assumption is precisely the part a diagnosis is supposed to test.

Two observations motivate the paper. First, bottleneck determination is nonlinear in its inputs: on the Jetson Thor T5000, FP16 accounts for only 30% of a 70/30 FP4/FP16 workload, yet after rate interaction it consumes 63% of time — and 80% at 50/50. A small share is not a small contribution. Linear attribution systematically underestimates such interaction terms, which is why we measure *information* rather than share or ablation. Second, the diagnosis has a natural two-level structure: a *surface* judgment that enumerates workload classes under equal rates, and a *deep* judgment that applies true microarchitectural rates. The question we ask is quantitative: how much does the deep level add?

We answer with a closed-form surface-vs-deep model. The surface judgment $S$ assumes $\text{rate}_i = 1$ for all components, so time share is proportional to workload share and the bottleneck is the dominant workload class. The deep judgment $D$ applies the true per-component rates, $t_i = f_i / \text{rate}_i$, and takes the bottleneck as $\arg\max_i t_i$. The incremental contribution of $D$ is defined as the amount by which $D$ corrects $S$: the flip rate $P(S \neq D)$ and the expected time-share shift. We complement these interpretable scores with strict mutual information $H(D)$, $H(D|S)$, $I(S;D)$ over the bottleneck-class distribution.

**Claim.** Under nonlinear bottleneck determination, the incremental contribution of a deep microarchitectural judgment node equals the amount by which it corrects the surface judgment; this quantity is computable in closed form, grows with the structure of the rate ratio, and vanishes under the negative control in which all rates are equal.

**Contributions.** (i) A closed-form surface-vs-deep model validated by three exactly reproduced hand-derived anchors. (ii) Measurement across four hardware platforms and 40,000 workloads: 43–56% flip, 0.17–0.23 time shift, 0.71–0.77 bits of deep-only mutual information. (iii) A flat-rate control that zeroes the correction exactly, plus a parameter–depth reordering arm, resolving the forwarding-triviality and tautology objections. (iv) A preregistration record: criteria committed before data generation.

## 2. Why This Quantity: From Nonlinearity to a Correction Measure

A reviewer's first question is why the incremental contribution of a deep node should be measured at all, and why by this quantity. The chain of reasoning is:

**Nonlinearity rules out share-based attribution.** Bottleneck determination is a compositional function of interacting factors: precision compute rates, workload composition, scalar/issue share, and bandwidth. The T5000 instance makes the nonlinearity concrete: FP16 at 30% workload share becomes 63% of time once rates are applied, and 80% at 50% share. Under a linear model, share and contribution coincide; here they diverge by a factor of two. Any measure that inherits the linearity assumption (share, ablation under fixed context) will systematically underweight the interacting component.

**Information, not attribution, is the right family of measures.** Mutual information captures nonlinear dependence without a linearity assumption: $I(S;D) > 0$ holds even when $D$ is a nonlinear function of $S$. Moreover, the decomposition $H(D) = H(D|S) + I(S;D)$ isolates exactly the quantity we care about — $H(D|S)$ is the information about the bottleneck that survives even after the surface judgment is known, i.e., the deep-only contribution.

**A two-level structure makes the increment well-defined.** The diagnosis decomposes into a surface level (enumeration of workload classes under equal rates) and a deep level (microarchitectural rate application). Conditioning the deep judgment on the surface one, $H(D|S)$, is the natural "incremental information" of the deep level given the surface level. This is the same structure as any hierarchical explanation: the value of a refinement is what it changes in the coarser judgment.

**The correction is the operational form of the increment.** Concretely, $D$ corrects $S$ in two ways: (i) *direction correction* — the bottleneck type flips ($S \neq D$), e.g., surface says "not compute-bound" while the microarchitecture says "40% slower than the surface estimate"; (ii) *granularity correction* — the time share of the true bottleneck component is revised, e.g., surface "possibly compute-bound" becomes "FP16 is 78% of time plus a hidden bandwidth killer." Flip rate and time shift are the interpretable, per-workload scores of this correction; strict MI is its information-theoretic formalization. Both are computable in closed form from specifications and a workload prior.

## 3. Method: A Closed-Form Surface-vs-Deep Model

**Setup.** We consider a workload with four components $i \in \{\text{FP4}, \text{FP16}, \text{scalar}, \text{bandwidth}\}$ with shares $f_i$ (a probability simplex) and per-component rates $\text{rate}_i$ derived from hardware specifications. The bottleneck is the component with maximal time share.

**Surface judgment $S$.** Assume all rates are equal ($\text{rate}_i = 1$). Then time share is proportional to workload share, $t_i = f_i$, and the surface bottleneck is $\arg\max_i f_i$ — the dominant workload class. This is the judgment a pure enumeration of workload composition yields.

**Deep judgment $D$.** Apply the true rates: $t_i = f_i / \text{rate}_i$ (normalized), and the deep bottleneck is $\arg\max_i t_i$. Rates are normalized so that the dominant component's rate is the reference; the *rate-ratio structure* (max/min and which component dominates) is the only hardware input.

**Incremental contribution (interpretable scores).** For each sampled workload we compute:
- **Flip rate** $\hat{P}(S \neq D)$: the fraction of workloads on which the deep judgment changes the bottleneck type (direction correction).
- **Time shift** $\mathbb{E}\big[|t^D_{b^*} - t^S_{b^*}|\big]$ where $b^* = D$'s bottleneck: the expected magnitude by which the deep judgment revises the time share of the true bottleneck (granularity correction).

**Strict mutual information.** Let $S, D \in \{1,\dots,4\}$ be the bottleneck-class variables under the workload prior. We compute $H(D)$, $H(D|S)$, and $I(S;D) = H(D) - H(D|S)$ exactly from the joint distribution $P(S,D)$ induced by sampling. $H(D|S)$ is the deep-only information: the bottleneck uncertainty that remains even after the surface judgment is known.

**Hardware.** Four platforms, dense (non-sparse) specifications:

| Platform | FP16 TFLOPS | FP4 TFLOPS | Bandwidth GB/s |
|---|---|---|---|
| RTX 5090 (GB202) | 419 | 1677 | 1792 |
| Thor T5000 (Jetson) | ~258 (derived) | 1035 | 273 |
| RTX 4090 (AD102) | 114 | — (no native FP4) | 1008 |
| A100 80G SXM (Ampere) | 312 | — (no native FP4) | 2039 |

The 4090 and A100 lack native FP4; their FP4 rates are taken as $0.5 \times$ FP16 (a conservative proxy; see Limitations). Scalar/issue rates follow the per-platform issue-path assumptions used in the anchors below.

**Workload prior.** $f \sim \text{Dirichlet}(1,1,1,1)$ (uniform over the simplex), $N = 40{,}000$ samples per platform.

**Validation anchors.** The model must exactly reproduce three hand-derived cases: (1) T5000, 50/50 FP16/FP4 → FP16 occupies 80% of time; (2) T5000, 70/30 → 63%; (3) 5090, scalar at 40% with issue rate halved → overall 40% slower. All three are reproduced (computed 0.800, 0.632, 1.400×); we treat this as the model-correctness gate.

## 4. Results

**Main result: the surface judgment is wrong on a majority of workloads.** Per platform, over $N=40{,}000$ sampled workloads:

| Platform | Rate ratio (max/min) | Flip rate $P(S \neq D)$ | Time shift | Typical flips |
|---|---|---|---|---|
| 4090 | 287.4 | 0.563 | 0.2307 | bandwidth→FP4, scalar→FP4 |
| 5090 | 51.9 | 0.527 | 0.2004 | scalar→FP16, bandwidth→FP16 |
| A100 | 44.3 | 0.556 | 0.2183 | scalar→FP4, bandwidth→FP4 |
| T5000 | 9.9 | 0.434 | 0.1655 | scalar→FP16, scalar→bandwidth |

The surface judgment misidentifies the bottleneck type on 43–56% of workloads, and the deep judgment revises the bottleneck's time share by 0.17–0.23 in expectation. The T5000 — the mildest rate structure (ratio 9.9) — shows the smallest correction; the 4090, with the most extreme ratio (287.4, driven by the absence of native FP4), the largest.

**Strict mutual information.** The information-theoretic formalization over the bottleneck-class variables:

| Platform | $H(D)$ (bits) | $H(D|S)$ (bits) | $I(S;D)$ (bits) |
|---|---|---|---|
| 5090 | 1.1429 | 0.7667 | 0.3762 |
| T5000 | 1.3511 | 0.7639 | 0.5871 |
| 4090 | 0.9857 | 0.7128 | 0.2729 |
| A100 | 1.0312 | 0.7464 | 0.2848 |
| **flat control** | 1.9999 | **0.0** | 1.9999 |

Deep-only information $H(D|S)$ is 0.71–0.77 bits on every real platform: even after the surface judgment is fully known, most of the bottleneck uncertainty remains. Under the flat control (all rates equal by construction), $H(D|S) = 0.0$ exactly — the deep level carries no information beyond the surface one, as it must, since the two judgments are then identical. The deep-only information is thus attributable to the rate-ratio structure, not to any generic property of having a second level.

**Structure, not extremity.** The correction tracks the *structure* of the rate ratio, not merely its extremity: the A100 (ratio 44.3, shift 0.2183) exceeds the 5090 (ratio 51.9, shift 0.2004), breaking strict monotonicity in max/min ratio. Which component dominates matters more than the ratio's magnitude — on the A100 the bandwidth/FP4 interaction dominates, on the 5090 the scalar/FP16 interaction does. We therefore state the scaling law as: the correction grows with the rate-ratio *structure*, not with extremity alone.

**Anchors.** All three hand-derived validation cases reproduce exactly (0.800 vs 80%, 0.632 vs 63%, 1.400× vs 40% slower), confirming the model's correctness before the main results are interpreted.

## 5. Control Arms

Three controls target the three objections a reviewer would raise against "deep beats surface."

**① Flat-rate control (forwarding triviality).** A placeholder hardware with all rates equal to 1. Result: flip = 0.0000, time shift = 0.0000, $H(D|S) = 0.0$ — the correction is *exactly* zero, not merely small. This rules out the trivial explanation that a deep node's information is just a forward of the surface information (which would be mathematically guaranteed for any enumerable quantity): the measured increment is attributable to the rate-ratio structure alone.

**② Parameter–depth reordering (tautology).** The objection: "deep" is defined by depth, so of course deeper nodes carry more information — the claim is tautological. We break the definition by reordering which *parameters* sit at which depth while holding the parameter set fixed: the gain follows the *parameters* (the rate-ratio information), not the depth label. A node placed deeper but carrying no rate information contributes nothing; a shallow node carrying the rate ratio contributes the full increment. The criterion is thereby de-depth-ified: it measures information content, not position.

**③ Intra-level type control (type × depth confound).** Within the same level, we compare judgment-type nodes (applying a rate ratio) against enumeration-type nodes (reporting a share). The judgment-type node's contribution exceeds the enumeration-type node's at equal depth, isolating the *type* effect from the *depth* effect and showing the increment is not an artifact of node classification.

## 6. Preregistration and Defense

**HARKing declaration.** All criteria, formulas, and the make-or-break test (deep-only information $> 0$ on real platforms and $= 0$ on the flat control) were committed to the project repository *before* the data were generated: preregistration commit `eb1b0598c` at 17:39 precedes the data-producing commit `718394ece` at 18:06 on 2026-11-24; the ordering is verifiable via `git log`. No criterion was adjusted after seeing the results; the one post-hoc change was a *weakening* of a secondary hypothesis (monotonicity in extremity → dependence on structure, §4), made because the data contradicted the stronger form.

**Forwarding-triviality response.** For any *enumerable* quantity, a deep node that merely re-expresses surface information is guaranteed to add nothing new — and, conversely, any deep node that restates the surface judgment adds information only in the trivial sense of forwarding it. The flat control (control ①) shows the measured increment is not of this kind: with the rate-ratio structure removed, the increment is exactly zero, so the 0.71–0.77 bits of deep-only information on real platforms is carried by the rate-ratio structure specifically.

**Tautology response.** "Deep nodes contribute more" is tautological only if "deep" is the definition of "contributes." Control ② severs this: the gain tracks the parameters, not the depth label, so the claim is an empirical statement about where rate-ratio information sits in the decomposition, not a restatement of the definition.

**Scope of the claim.** We claim a *measurement result* — the incremental contribution of deep microarchitectural judgments is large, closed-form, and attributable to rate-ratio structure — not a universal law about reasoning systems. The setting is GPU bottleneck diagnosis with four real platforms and a uniform workload prior; generalization to other domains is left open.

## 7. Limitations

- **Interpretable scores vs. strict MI.** Flip rate and time shift are interpretable per-workload scores; they are not themselves mutual information. We complement them with strict $H(D)$, $H(D|S)$, $I(S;D)$ computed over the bottleneck-class distribution (§4), which is the formal quantity the claim rests on.
- **No native FP4 on two platforms.** The 4090 and A100 lack native FP4 units; their FP4 rates are taken as $0.5 \times$ FP16 as a proxy (unverified against silicon). The 4090's extreme rate ratio (287.4) is partly an artifact of this proxy, and its flip/shift values should be read with that caveat.
- **Workload prior.** $f \sim \text{Dirichlet}(1,1,1,1)$ is uniform over the simplex and does not model the precision mix of real LLM inference workloads (which are typically low-precision-heavy). The absolute flip rates would shift under a biased prior; the flat-control zeroing and the structural-scaling observation are prior-robust by construction.
- **Monotonicity is not strict.** The correction correlates with rate-ratio *structure*, not with extremity alone: A100 (ratio 44.3) exceeds 5090 (ratio 51.9) in time shift. We state the scaling law accordingly and do not claim a monotone function of max/min ratio.
- **Single-domain validation.** All four platforms are GPUs and all anchors are hand-derived from specifications; no measured trace is used. External validation on real workloads is future work.

## 8. Conclusion and Related Work

**Conclusion.** We measured the incremental contribution of a deep microarchitectural judgment relative to a surface enumeration judgment in GPU bottleneck diagnosis, in closed form, with preregistered criteria. The surface judgment is wrong on 43–56% of workloads; the deep correction is 0.17–0.23 in time shift and 0.71–0.77 bits of deep-only mutual information; and the correction vanishes exactly when the rate-ratio structure is removed. The practical reading: in nonlinear compositional diagnosis, the deep level is not a refinement — it is the load-bearing part of the judgment, and its contribution is computable before any experiment is run.

**Related work.** Roofline analysis and step-level attribution methods assume time is proportional to resource share and attribute linearly; our result quantifies exactly the error that assumption makes, per platform. Information-theoretic analyses of reasoning trajectories (e.g., step-entropy and probing-trajectory measurements) measure information in *observed* chains; here the quantity is *derived* from specifications, which is what makes the closed-form and the negative control possible. Bottleneck diagnosis in systems (e.g., Amdahl-style decomposition) treats rates as given inputs; we instead treat the *judgment about* the rates as the object of measurement.
