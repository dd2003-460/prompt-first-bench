# Number Trace — think-mechanism-paper

Maps every quantitative statement in `paper.tex` to its source file and line.
Source files:
- CORE = `/Users/a1-6/Desktop/workspace/projects/AI-计算科学/D1-persona-align/memory/d-thinking-mechanism-first-principles-20261124.md`
- TPL  = `/Users/a1-6/Desktop/workspace/projects/AI-计算科学/D1-persona-align/memory/general-thinking-template-20261124.md`

## Claim numbers (all traceable)

| # | Statement in paper | Value | Source | Line(s) |
|---|--------------------|-------|--------|---------|
| 1 | Core definition: understanding = lossless round-trip fixed point, D∘C = id | D∘C=id | CORE | 8 |
| 2 | Losslessness = unique + reproducible (= predictive quality) | unique+reproducible | CORE | 10 |
| 3 | Self-reference is finite (x'=x, solve Ce^t), Gödel only for pathological self-reference | finite | CORE | 11 |
| 4 | Four facets: predictive power / perturbation / fitness / leading-term anchoring | 4 | CORE | 15–18 |
| 5 | Facet 1 predictive power = temporal-direction lossless expansion, error controlled nonzero | — | CORE | 15 |
| 6 | Facet 2 perturbation = leading term + successive corrections, convergence radius, add higher orders only when necessary | — | CORE | 16 |
| 7 | Facet 3 fitness = no "wrong", continuous fitness; progress = gradient descent, local robust to random | — | CORE | 17 |
| 8 | Facet 4 leading-term anchoring = leading term is widest valley, anchor then perturb | — | CORE | 18 |
| 9 | Derivation 1: perturbation/hierarchy algebraically equivalent (leading term + corrections); differ in order semantics (precision vs concept); coupling breaks equivalence | — | CORE | 22 |
| 10 | Optimal basis = sparsest expansion coefficients = most compressed representation | — | CORE | 23 |
| 11 | Hierarchy/tree strict counterpart = multiresolution bases (Haar/Daubechies/Faber-Schauder); locality + nestedness V_j⊂V_{j+1}; jump = 2^j; L² orthogonality preserved | multiresolution | CORE | 24 |
| 12 | Multiplicative = tensor product (1D⊗1D⊗…); single root = branching, multi-root = tensor product, unified under MRA | tensor product | CORE | 25 |
| 13 | Derivation 2: general compression selects domain, formula compression refines within domain; order irreversible (refine-before-select = derive in wrong domain) | 2-stage | CORE | 29 |
| 14 | Explains "formula better in some aspects but not general" | — | CORE | 30 |
| 15 | Domain selection = 3-step process: ① verify axiom range ② transfer still-holding axioms (conditions) ③ think/experiment new conditions | 3 steps | CORE | 31 |
| 16 | Meta-criterion: any math metaphor = compression+selection; value = yields falsifiable predictions | — | CORE | 32 |
| 17 | Consistency test: 7 thinking-style hypotheses, 7/7 hit (old "compression+prediction" 5/7) | 7/7, 5/7 | CORE | 50 |
| 18 | Five injectable templates T1–T5 (cost model / unified coverage / quantitative landing / analogy audit / criterion bottleneck), each trigger + action | 5 | TPL | 30–40 |
| 19 | T1 cost model: trigger = concrete solution found or "is X optimal"; action = write cost model + unified form, verify original is special case, name missing assumption | T1 | TPL | 31–32 |
| 20 | T2 unified coverage: trigger = multiple unrelated methods; action = one formula/analogy covering all + degeneracy conditions | T2 | TPL | 33–34 |
| 21 | T3 quantitative landing: trigger = qualitative conclusion; action = quantify to testable number, else mark "needs measurement" + cheapest probe | T3 | TPL | 35–36 |
| 22 | T4 analogy audit: trigger = borrowing case/analogy/prior; action = check Δ per dimension + sensitivity s_k, ε·uniform floor | T4 | TPL | 37–38 |
| 23 | T5 criterion bottleneck: trigger = framework formed; action = find step lacking cheap reliable ground truth; remedy "make world closed" | T5 | TPL | 39–40 |
| 24 | Evolution trajectory v1→v4 (compression+prediction 5/7 → perturbation+fitness 7/7 → fixed point → hierarchy) | v1–v4 | CORE | 58 |
| 25 | Pilot: 5 prompts × 2 conditions, A baseline 3/5, B treatment 5/5, B−A delta only on P1 (T1) and P5 (T5) | 3/5, 5/5, 10 runs | PILOT | pilot/runs.json + scores.json |
| 26 | Pilot: 9/10 runs finish_reason=length at max_tokens=1500 (P5-A stop at 1458); single model qwen3.8-27b-mtp, temperature 0.7, n=1/cell | 9/10, 1500 | PILOT | pilot/runs.json |

## Non-claim numerics (formatting only, not traced)
- `11pt` document class, table column widths (4.6/5.2/5.4 cm), `\begin{thebibliography}{9}` label, `2^{j}` scale symbol, `5/7`/`7/7` ratios already traced above.

## Coverage
All claim-bearing numbers in the paper (7/7, 5/7, 5 templates, 4 facets, 2 structural observations, 3-step domain selection, D∘C≈id, multiresolution 2^j, tensor product, v1–v4, pilot 3/5 vs 5/5 + 9/10 truncation) are mapped above. No number in the paper lacks a source mapping.

PILOT = `/Users/a1-6/Desktop/workspace/pfb/tasks/think-mechanism-paper/pilot/` (T4b round-2, commit c704a6637; Lead verify_t4b.py ALL PASS: 10/10 runs ok, raw byte-equal to runs.json).
