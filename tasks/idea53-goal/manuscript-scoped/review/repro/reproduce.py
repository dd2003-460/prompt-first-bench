#!/usr/bin/env python3
"""Reviewer-side independent reproduction of the main table in paper-tmlr.tex.
Pure Python (no numpy in sandbox). Model taken verbatim from the manuscript:
  f ~ Dirichlet(1,1,1,1); S = argmax f; D = argmax f_i/rate_i; N = 40000.
Rates copied from modules/F-theory/research/idea53-additive-tree-perturbation.py
(SPECS dict), which the manuscript's rate ratios 51.9/9.9/287.4/44.3 are
derived from.
"""
import math, random, json

N = 40000
COMPS = ["fp4", "fp16", "scalar", "bw"]
SPECS = {
    "5090":  {"fp4": 1677.0, "fp16": 419.0,  "scalar": 21760.0, "bw": 1792.0},
    "T5000": {"fp4": 1035.0, "fp16": 258.0,  "scalar": 2560.0,  "bw": 273.0},
    "4090":  {"fp4": 57.0,   "fp16": 114.0,  "scalar": 16384.0, "bw": 1008.0},
    "A100":  {"fp4": 156.0,  "fp16": 312.0,  "scalar": 6912.0,  "bw": 2039.0},
}

def sample_f(rng):
    # Dirichlet(1,1,1,1) == normalised Exp(1) == normalised -log U
    g = [-math.log(rng.random()) for _ in range(4)]
    s = sum(g)
    return [x / s for x in g]

def entropy_bits(counts, n):
    h = 0.0
    for c in counts:
        if c:
            p = c / n
            h -= p * math.log2(p)
    return h

def analyse(rate_vec, n=N, seed=12345):
    rng = random.Random(seed)
    S = [0]*4; D = [0]*4
    joint = [[0]*4 for _ in range(4)]
    flips = 0
    shift_bneck = 0.0     # |share_D - share_S| on D's bottleneck component
    shift_l1 = 0.0        # L1 distance between share vectors
    for _ in range(n):
        f = sample_f(rng)
        t = [f[i] / rate_vec[i] for i in range(4)]
        zt = sum(t)
        shD = [x / zt for x in t]
        s = max(range(4), key=lambda i: f[i])
        d = max(range(4), key=lambda i: f[i] / rate_vec[i])
        S[s] += 1; D[d] += 1; joint[s][d] += 1
        if s != d:
            flips += 1
        shift_bneck += abs(shD[d] - f[d])
        shift_l1 += sum(abs(shD[i] - f[i]) for i in range(4))
    HD = entropy_bits(D, n)
    # I(S;D) from the joint
    I = 0.0
    for s in range(4):
        for d in range(4):
            if joint[s][d]:
                p = joint[s][d] / n
                ps = S[s] / n; pd = D[d] / n
                I += p * math.log2(p / (ps * pd))
    return {
        "flip": flips / n, "shift_bneck": shift_bneck / n, "shift_l1": shift_l1 / n,
        "H(D)": HD, "I(S;D)": I, "H(D|S)": HD - I,
        "H(S)": entropy_bits(S, n),
        "P(D=scalar)": D[2] / n, "P(D=bw)": D[3] / n, "P(D=fp16)": D[1]/n, "P(D=fp4)":D[0]/n,
    }

def flat_control(seed=12345):
    r = analyse([1.0, 1.0, 1.0, 1.0], seed=seed)
    return {"flip": r["flip"], "shift_l1": r["shift_l1"], "H(D|S)": r["H(D|S)"],
            "H(D)": r["H(D)"], "I(S;D)": r["I(S;D)"]}

def perm_test(name, n=20000):
    import itertools
    rates = [SPECS[name][c] for c in COMPS]
    out = []
    for k, perm in enumerate(itertools.permutations(rates)):
        out.append(analyse(list(perm), n=n, seed=777)["flip"])
    return {"min": min(out), "max": max(out), "spread": max(out)-min(out), "k": len(out)}

if __name__ == "__main__":
    res = {}
    print("== main table (N=40000) ==")
    for name, spec in SPECS.items():
        rates = [spec[c] for c in COMPS]
        ratio = max(rates)/min(rates)
        r = analyse(rates)
        res[name] = {"ratio": ratio, **r}
        print(f"{name:6s} ratio={ratio:7.1f}  flip={r['flip']:.3f}  shift_bneck={r['shift_bneck']:.3f} "
              f"shift_L1={r['shift_l1']:.3f}  H(D)={r['H(D)']:.3f}  I(S;D)={r['I(S;D)']:.3f}  H(D|S)={r['H(D|S)']:.3f}")
        print(f"        P(D): fp4={r['P(D=fp4)']:.3f} fp16={r['P(D=fp16)']:.3f} "
              f"scalar={r['P(D=scalar)']:.3f} bw={r['P(D=bw)']:.3f}   H(S)={r['H(S)']:.3f}")
    print("\n== flat-rate control ==")
    print(flat_control())
    print("\n== permutation spread of flip (N=20000 per perm) ==")
    for name in ["5090", "T5000", "4090", "A100"]:
        print(name, perm_test(name))
    json.dump(res, open("reproduce-main.json", "w"), indent=2)
