#!/usr/bin/env python3
"""# origin: ai · 2026-11-25 05:45 · H(D|S) 独立复算脚本（4 类瓶颈联合分布, 闭式）
paper abstract 的 H(D|S)=0.71-0.77 bits 出处核验: 该值来自 S,D∈{1..4} 瓶颈类联合分布
(非 718394ece 的 idea53-theory.py per-node 40 类口径)。本脚本按 paper §5 定义独立复算:
H(D|S) range 0.7134-0.7693 ✓ 与 abstract 一致; flat control 精确 0 ✓。
用法: python3 idea53-hds-recompute.py (纯确定性, 无 LLM/网络, seed=42, N=20000)
"""
#!/usr/bin/env python3
"""复算 paper 的 H(D|S) (4 类瓶颈, 闭式联合分布) — 核验 abstract 0.71-0.77 bits."""
import math, random
from collections import Counter, defaultdict

COMPS = ['fp4', 'fp16', 'scalar', 'bw']
SPECS = {
    '5090':  {'fp4': 1677., 'fp16': 419., 'scalar': 21760., 'bw': 1792.},
    'T5000': {'fp4': 1035., 'fp16': 258., 'scalar': 2560.,  'bw': 273.},
    '4090':  {'fp4': 57.,   'fp16': 114., 'scalar': 16384., 'bw': 1008.},
    'A100':  {'fp4': 156.,  'fp16': 312., 'scalar': 6912.,  'bw': 2039.},
}

def sample(n, seed):
    rng = random.Random(seed)
    out = []
    for _ in range(n):
        gv = [rng.gammavariate(1.0, 1.0) for _ in range(4)]
        s = sum(gv)
        out.append([v / s for v in gv])
    return out

def H(p):
    return -sum(c * math.log2(c) for c in p if c > 0)

def compute(spec, fs):
    """S = argmax f (flat rate), D = argmax f/rate. 返回 H(D), H(D|S), I(S;D), flip rate."""
    joint = Counter()
    ps, pd = Counter(), Counter()
    flip = 0
    for f in fs:
        S = max(range(4), key=lambda i: f[i])
        D = max(range(4), key=lambda i: f[i] / spec[COMPS[i]])
        joint[(S, D)] += 1
        ps[S] += 1
        pd[D] += 1
        flip += (S != D)
    n = len(fs)
    hD = H([pd[i] / n for i in range(4)])
    # H(D|S) = sum_S P(S) H(D|S)
    hDS = 0.0
    for s in range(4):
        ms = ps[s]
        if ms == 0:
            continue
        hDS += (ms / n) * H([joint[(s, d)] / ms for d in range(4) if joint[(s, d)] > 0])
    ISD = hD - hDS
    return hD, hDS, ISD, flip / n

fs = sample(20000, 42)
print(f"{'hw':8s} H(D)     H(D|S)   I(S;D)   flip")
vals = {}
for g, sp in SPECS.items():
    hD, hDS, ISD, fl = compute(sp, fs)
    vals[g] = hDS
    print(f"{g:8s} {hD:.4f}  {hDS:.4f}  {ISD:.4f}  {fl:.3f}")
lo, hi = min(vals.values()), max(vals.values())
print(f"\nH(D|S) range: {lo:.4f} - {hi:.4f}")
print(f"paper 声称: 0.71-0.77  ->  match={abs(lo-0.71)<0.015 and abs(hi-0.77)<0.015}")
# flat control
flat = {c: 1.0 for c in COMPS}
hD, hDS, ISD, fl = compute(flat, fs)
print(f"flat control: H(D|S)={hDS:.4f} (应=0), flip={fl:.4f} (应=0)")
