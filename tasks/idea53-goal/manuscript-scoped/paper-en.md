# How Much Should a Decomposition-Tree Node Score? A Closed-Form, Negative-Controlled Conditional-Information Measure (A Toy-Model Demonstration)

**Scope statement (first, deliberately).** This is *preliminary work*: it proposes and tests a **computable, measurable** basis for scoring nodes of a decomposition tree. It does not solve reward hacking or Goodhart's problem, does not discover a new objective function, and makes no claim of priority or of being unattempted. The tree, the GPU example, and the mathematical example here are **toy models**, used to define the quantity and exercise its negative controls. Extending the construction to richer structures (Bayesian updating with new data, minimum-description-length structure selection under assumption constraints) is left as open space and is **not implemented** here.

## Abstract

After a judgment is decomposed into a tree, a natural question with no standard answer is: how much information does each node contribute? We give a closed-form conditional-information quantity: separate a *surface judgment* \(S\) (enumeration by share under equal rates) from a *deep judgment* \(D\) (obtained by applying true rates), and measure the deep level's **incremental information** as \(H(D|S)\). The quantity depends only on hardware specifications and a workload prior: no experiments, no training, no labels. Across four platforms and 40,000 sampled workloads, the surface judgment misidentifies the bottleneck type on 43–56% of workloads, the deep correction shifts time share by 0.17–0.23, and deep-only information \(H(D|S)\) is 0.71–0.77 bits. Two negative controls exclude the trivial readings that deep nodes merely forward surface information, or that they win by definition: under a flat-rate control the increment is **exactly zero**, and it is invariant under 24 parameter–depth permutations. Three hand-derived anchors reproduce exactly. With all criteria committed before data generation (preregistration), we present these results as a demonstration of a **scoring basis**, not as a solution to any method or alignment problem.

## 1. Why this quantity

**Share-based attribution is insufficient.** Bottleneck determination is a compositional function of interacting factors. On the Jetson Thor T5000, FP16 accounts for only 30% of a 70/30 workload yet consumes 63% of time after rates are applied (80% at 50/50). Small share is not small contribution; measures inheriting linearity (share, ablation under fixed context) systematically underweight the interacting component.

**An information-family measure, not attribution.** Mutual information captures nonlinear dependence without a linearity assumption: \(I(S;D)>0\) even when \(D\) is a nonlinear function of \(S\). The decomposition \(H(D)=H(D|S)+I(S;D)\) isolates exactly the information about the bottleneck that survives once the surface judgment is known — the quantity we want to credit to deep nodes.

**A two-level structure makes the increment well-defined.** Surface = enumeration of shares under equal rates; deep = the judgment after applying true rates \(t_i=f_i/\mathrm{rate}_i\). \(H(D|S)\) is precisely how much the deep level adds given the surface level.

**Operational form.** The deep level corrects the surface level in two ways: direction correction (bottleneck-type flip, \(S\neq D\)) and granularity correction (time-share shift). Flip rate and share shift are interpretable per-workload scores; \(H(D|S)\) is their strict information-theoretic form.

We state plainly that the chain rule and mutual information are textbook information theory, roofline is textbook computer architecture, and PID's unique/redundant/synergistic split is prior work. We do not claim these tools are new. The contribution is **combining them into a scoring protocol that is closed-form, negative-controlled, and preregistrable**, and testing it completely in one toy domain.

## 2. Model

A workload has four components with shares \(f_i\) sampled from \(\mathrm{Dirichlet}(1,1,1,1)\). Each component has a rate \(\mathrm{rate}_i\).

- Surface judgment \(S\): assume all \(\mathrm{rate}_i=1\), so time share \(\propto f_i\), bottleneck \(=\arg\max_i f_i\).
- Deep judgment \(D\): apply true rates, \(t_i=f_i/\mathrm{rate}_i\), bottleneck \(=\arg\max_i t_i\).

Incremental quantities:

\[
\text{flip}=P(S\neq D),\qquad \text{shift}=\mathbb{E}\,|\mathrm{share}_D-\mathrm{share}_S|,
\]
\[
H(D|S)=H(D)-I(S;D).
\]

Four platforms: RTX 5090 (max/min rate ratio 51.9), Thor T5000 (9.9), RTX 4090 (287.4), A100 (44.3).

## 3. Results

| Platform | flip | shift | \(H(D|S)\) (bits) |
|---|---|---|---|
| RTX 5090 | 0.527 | 0.200 | 0.76 |
| Thor T5000 | 0.434 | 0.166 | 0.71 |
| RTX 4090 | 0.563 | 0.231 | 0.77 |
| A100 | 0.556 | 0.218 | 0.74 |

Three hand-derived anchors reproduce exactly: T5000 50/50 → 80%; T5000 70/30 → 63%; 5090 scalar 40% with issue rate halved → 40% slower.

The correction is not monotone in rate-ratio *extremity*: A100 (ratio 44.3) exceeds 5090 (ratio 51.9) in shift. We therefore claim only dependence on rate-ratio *structure*; with four platforms this is a 4-point structural observation, not a scaling law.

## 4. Negative controls and defenses

**(1) Flat-rate control — measured arm.** Set all rates of a placeholder hardware to 1. Result: flip = 0.0000, shift = 0.0000, \(H(D|S)=0.0\) — **exactly** zero, not merely small. This rules out "deep merely forwards surface information."

**(2) Parameter–depth permutation — measured arm.** Permute the rate vector across the four components in all 24 ways, holding the multiset fixed. If the increment tracked the *label* of which component is called deep, it would change; if it tracks rate-ratio *content*, it should not. Result: identity permutation reproduces the main numbers exactly; across permutations flip varies only within a narrow Monte-Carlo band (5090: 0.5251–0.5304). The criterion is de-depth-ified.

**(3) Intra-level type control — design-level argument.** In our two-level model, surface is enumeration-type and deep is judgment-type, differing only in the rate vector: type is not confounded with depth. An earlier node-level model did confound them, and there the type control ran *against* the hypothesis (enumeration 0.5841 bits > judgment 0.1344 bits). That number comes from a different, confounded model and is not used as evidence.

**HARKing declaration.** All criteria, formulas, and the make-or-break test (deep-only information > 0 on real platforms, = 0 on the flat control) were committed before data generation (commit `eb1b0598c`, 17:39, preceding `718394ece`, 18:06). The only post hoc change *weakened* a secondary hypothesis (monotonicity in extremity → dependence on structure) because the data contradicted the stronger form.

## 5. Tree demonstration (a 4-point observation)

Under a two-way split (compute vs memory), the correction decomposes into branch-level and within-branch components whose four cells sum to 1 (additive self-consistency):

| Platform | co-flip | within-flip | co-correct | within-correct | dominant |
|---|---|---|---|---|---|
| T5000 (9.9) | 0.530 | 0.145 | 0.036 | 0.290 | within |
| A100 (44.3) | 0.399 | 0.442 | 0.045 | 0.114 | branch |
| 5090 (51.9) | 0.409 | 0.335 | 0.064 | 0.191 | branch |
| 4090 (287.4) | 0.394 | 0.451 | 0.044 | 0.112 | branch |

Segment-level flip reproduces the 1D main result exactly. The mildest platform (T5000) is within-branch dominant; the three extreme platforms are branch dominant and cluster internally. This is a 4-point structural observation, not a continuous trade-off curve; the split is fixed to compute/memory and alternatives are untested; the extension is post hoc and unregistered but inherits the preregistered flat control.

## 6. Scope, differentiation, and extension space

**A scoring basis, not a solution.** What we deliver is a protocol for how to compute and falsify a node's information increment. It does not solve reward hacking, recover a true objective, or validate any objective-expansion mechanism.

**Differentiation.** Information gain, roofline, and PID are established tools. Specification Self-Correction (Gallego 2025, arXiv:2507.18742) performs test-time natural-language critique and rewrite of a specification, using no information gain, tree structure, conditional entropy, or quantitative scoring, and no weight updates. Our relation to it is *upstream*: we provide the measurable basis for scoring nodes, and do not touch specification revision.

| Work | Input | Output | Closed-form | Exact-zero control | Preregistered | Spec revision |
|---|---|---|---|---|---|---|
| ID3 information gain | data distribution | split attribute | No (needs data) | No | No | No |
| Roofline | compute/bandwidth spec | bottleneck regime | Yes | No | No | No |
| PID (Williams & Beer) | multi-source distribution | unique/redundant/synergistic | No (needs distribution) | No | No | No |
| SSC (2507.18742) | rubric + output | rewritten specification | No (test-time generation) | No | No | **Yes** |
| This work | hardware spec + prior | node increment \(H(D|S)\) | **Yes** | **Yes (=0)** | **Yes** | No (upstream) |

The table delineates rather than prioritizes: we do not replicate any existing row. We supply one uncovered cell — that a node's information increment is closed-form computable and falsifiable by an exact-zero control.

**Extension space (not implemented).** The tree here is the simplest example structure. Richer versions could introduce Bayesian updating from new data, multiple assumption constraints, and structure selection under a minimum-description-length criterion. None of these is implemented or claimed here; we only state the boundary of extensibility.

## 7. Limitations

- Flip rate and share shift are **interpretable scores**, not mutual information; the strict quantity is \(H(D|S)\).
- The 4090 and A100 lack native FP4; their FP4 rates use a \(0.5\times\) FP16 proxy, so the 4090's extreme ratio is partly a proxy artifact.
- The workload prior is uniform Dirichlet and does not model real low-precision-heavy LLM inference; the flat-control zeroing and structural observation are prior-robust by construction, while absolute flip rates would shift under a biased prior.
- Monotonicity fails (A100 > 5090 in shift); four platforms cannot support a scaling law.
- The tree extension is post hoc, 4-point, and fixed-split; the intra-level type control is a design-level argument, not a measured arm.
- Single domain: all four platforms are GPUs, anchors are hand-derived, no measured trace is used. External spot-checking on public data is future work.

## 8. Conclusion

We demonstrate a closed-form, negative-controlled, preregistrable protocol for scoring decomposition-tree nodes. In the toy domain of GPU bottleneck diagnosis, the surface judgment is wrong 43–56% of the time; the deep increment is 0.17–0.23 in time-share shift and 0.71–0.77 bits of deep-only information, and it vanishes exactly under the flat control. The conclusion is limited to the computability and falsifiability of this scoring basis in this domain: it is computable, reproducible, and falsifiable by its own negative control. It claims neither universality nor a solution to any alignment problem.

---

## Appendix: Venue strategy (working note, not part of the paper)

From the 2026-11-25 arena venue review (session `01a212ae-...`; full text at `../arena-venue-report-raw-20261125.md`). For submission alignment only; not to appear in the formal manuscript.

- **First stop**: an ICLR 2027 workshop, one of — Science and Society of Modern AI (deadline 2027-01-30 AoE, tiny ≤3 pp non-archival, topic includes measurement — closest fit to "preliminary scoring basis"); SciEval (2027-02-01, non-archival, home topic); Verifiable Agent Safety (abstract 2027-01-25 / full 2027-02-01, dates proposed, short 2–4 pp).
- **Next**: workshop → NeurIPS 2027 Evaluations & Datasets (est. 2027-05, unannounced); alternative ICML 2027 "Datasets, Evaluations and Benchmarks" (abstract 2027-01-14 / full 2027-01-22).
- **Cost**: submission and publication are free (no APC; arXiv $0). Only registration/travel cost money; student workshop-only ≈ €130–300, with waivers available.
- **Before submission**: (1) structure figure produced at `fig1-scoring-protocol.tex` (place at end of §1); (2) comparison table included in §6; (3) optional public-data spot-check or artifact appendix.
- **Unverified**: SciEval final page limit/archival status, NeurIPS 2027 E&D CFP and 2027 registration fees, official acceptance rates — must be rechecked before deadlines; do not treat as established facts.
