#!/usr/bin/env python3
"""Verbosity-bias control arm: LLM depth score vs synthesis answer length.

UNBLOCKS a control arm the draft (workshop-draft §4.3) listed as a dead end
("cannot test verbosity bias without GPU re-run"). The 15 K7 synthesis answers
WERE on disk all along — in each archive budget dir's runs-s5-sm-gpu-synth.json
(answer_len 8666–26444). The earlier "15 K7 answers not stored" claim was wrong
(same error class as 补充30: asserted data-missing without checking archive/).

Result (n=15, df=13):
  cor(LLM_depth, answer_length) = +0.648  (t=+3.07, p<0.01)  — significant
  cor(length, budget)           = +0.153  (ns)               — length not budget-driven
  cor(LLM_depth, budget)        = +0.135  (ns)
  partial(LLM, length | budget) = +0.641  — survives controlling budget
  partial(LLM, budget | length) = +0.047  — budget signal VANISHES when length controlled

Mechanism: the LLM depth judge tracks answer LENGTH, not budget. The 150-tier
"peak" (0.474/0.518) is because those two answers happened to be the longest
(24770/24197 chars) and the LLM judge rewards longer answers. This is a
verbosity bias in the same-model LLM rubric judge.

Upgrades the §4.3 attribution: the non-monotonic peak is not merely "rubric
noise on a flat self-biased axis" — it has a concrete mechanism (verbosity
bias). The robust claim (peak absent on the bias-immune mechanical axis) is
unchanged; this explains WHY the self-biased axis shows a peak.

Reproduce: python3 verbosity-bias-control-arm.py
Scope: 15 K7 budget-scan runs, GPU domain, single model (qwen3.8-27b as both
generator and judge). n=15 → suggestive-to-significant (p<0.01 but df=13).
"""
import glob, json, os, re, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
# research/ -> B-pipeline-ablation/ -> modules/ -> pfb root
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RES = os.path.join(ROOT, "modules", "B-pipeline-ablation", "data", "t53b", "results-budget-scan.json")
ARCHIVE = os.path.join(ROOT, "experiments", "stage-ablation", "checkpoints", "archive")

res = json.load(open(RES))
llm = {r["run"]: r["depth"] for r in res}
bud = {r["run"]: r["budget"] for r in res}

ans_len = {}
for d in sorted(glob.glob(os.path.join(ARCHIVE, "budget-*"))):
    m = re.search(r"budget-(\d+)-r(\d+)", os.path.basename(d))
    if not m:
        continue
    run = f"gpu_budget{m.group(1)}_r{m.group(2)}"
    sf = glob.glob(os.path.join(d, "*synth*.json"))
    if not sf:
        continue
    t = json.load(open(sf[0]))
    for r in (t if isinstance(t, list) else [t]):
        ans_len[run] = len(r.get("answer", ""))

runs = [r for r in llm if r in ans_len]
L = np.array([ans_len[r] for r in runs], float)
D = np.array([llm[r] for r in runs], float)
B = np.array([bud[r] for r in runs], float)
n = len(runs)


def corr(a, b):
    return float(np.corrcoef(a, b)[0, 1])


def tval(r):
    return r * np.sqrt(n - 2) / np.sqrt(1 - r * r)


def resid(a, b):
    r = corr(a, b)
    slope = r * a.std() / b.std()
    return a - (slope * (b - b.mean()) + a.mean())


def partial(x, y, z):
    return corr(resid(x, z), resid(y, z))


print(f"pairs: {n}/15")
print(f"cor(LLM, length)    = {corr(D, L):+.3f}  (t={tval(corr(D, L)):+.2f}, df={n-2})")
print(f"cor(length, budget) = {corr(L, B):+.3f}  (t={tval(corr(L, B)):+.2f})")
print(f"cor(LLM, budget)    = {corr(D, B):+.3f}  (t={tval(corr(D, B)):+.2f})")
print(f"partial(LLM, length | budget) = {partial(D, L, B):+.3f}")
print(f"partial(LLM, budget | length) = {partial(D, B, L):+.3f}")
print("\nper-run:")
for r in sorted(llm):
    if r in ans_len:
        print(f"  {r:20s} llm_depth={llm[r]:.3f}  ans_len={ans_len[r]}")
