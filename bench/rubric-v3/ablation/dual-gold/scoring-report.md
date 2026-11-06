# Dual Gold Scoring Report — T48

> origin: ai · 2026-11-06 · Lead (local execution, arena channel dead)
> Purpose: B2 info-boundary reconstruction — quantify single-source bias in O3 construct validity.

## Method

Two independent gold trees for the same question (Q1: H100 PCIe vs SXM inference throughput):
- **Gold A** (original): `bench/rubric-v3/ablation/gold-tree.md` — 31 nodes, constructed during T0 local-27b experiment, values from calc.py + NVIDIA datasheet.
- **Gold B** (independent): `bench/rubric-v3/ablation/dual-gold/gold-tree-independent.md` — 15 scored assertions, constructed from first principles + public specs WITHOUT reading Gold A's values or calc.py.

## Value Overlap

| Metric | Gold A | Gold B | Match |
|--------|--------|--------|-------|
| HBM BW SXM [TB/s] | 3.35 | 3.35 | ✓ |
| HBM BW PCIe [TB/s] | 2.00 | 2.00 | ✓ |
| Decode ratio | 1.68x | 1.68x | ✓ |
| FP16 TFLOPS SXM | 989 | 989 | ✓ |
| FP16 TFLOPS PCIe | 756 | 756 | ✓ |
| Prefill ratio | 1.31x | 1.31x | ✓ |
| NVLink [GB/s] | 900 | 900 | ✓ |
| PCIe Gen5 x16 [GB/s] | ~64 | ~64 | ✓ |
| Interconnect ratio | ~14x | ~14x | ✓ |
| TDP SXM [W] | 700 | 700 | ✓ |
| TDP PCIe [W] | 350 | 350 | ✓ |
| HBM capacity [GB] | 80 | 80 | ✓ |

**Value overlap: 12/12 = 100%**

## Structural Element Overlap

| Element | In A | In B |
|---------|------|------|
| Decode = BW bottleneck | ✓ | ✓ |
| Prefill = compute bottleneck | ✓ | ✓ |
| NVLink only matters for TP≥2 | ✓ | ✓ |
| TDP difference (700/350W) | ✓ | ✓ |
| "14x" = interconnect ratio ≠ throughput ratio | ✓ | ✓ |
| Gap identification (workload/framework/price/measured data) | ✓ | ✓ |

**Structural overlap: 6/6 = 100%**

## Interpretation for O3 (Construct Validity)

The two golds converge on identical values and structure because the underlying facts are **stable public knowledge** (NVIDIA datasheet, PCI-SIG spec). This means:

1. **Single-source bias is LOW for stable-knowledge questions**: an independent constructor reaches the same answer. The O3 claim that "gold tree encodes constructor's specific research path" does NOT apply to hardware spec questions — the path is constrained by public fact.

2. **Where bias WOULD matter**: volatile-data questions (Q3 API pricing) where the "correct" value changes over time and depends on when/where you looked. Dual gold would show divergence there.

3. **Implication for rubric v3.3**: M1 scoring of methodology-type golds via public-fact verification is robust to gold source for stable-knowledge domains. The judge doesn't need the specific gold text — it needs the domain's public fact base.

## Caveats

- This is a SINGLE question (Q1) with a SINGLE independent construction. n=1 per side.
- Gold B was constructed by the same entity (Lead agent) that supervised Gold A's creation — true independence would require a different model/session with no prior exposure. Arena was intended as that independent constructor but the session died.
- The 100% overlap is EXPECTED for stable specs (there's one correct answer). It does NOT prove the rubric works for ambiguous/volatile questions.

## Verdict

**O3 R-06 limitation PARTIALLY resolved**: for stable-knowledge questions, dual gold confirms no single-source bias. Full resolution requires (a) volatile-data question (Q3) dual gold, and/or (b) truly independent constructor (different model family).

Status: PARTIAL — sufficient to footnote §O3 with "stable-knowledge subset validated", not sufficient to remove the limitation entirely.
