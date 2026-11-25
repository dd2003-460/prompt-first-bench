#!/usr/bin/env python3
"""C3a VERIFY — 独立核验:
(b) 单平台 raw workload 手算 flip 计数 (T5000), 对比重算值
(c) flat-rate=0 稳健性: 多 seed + 多 flat 常数, 确认非巧合
"""
import json, math, random
from collections import Counter, defaultdict

COMPS = ['fp4', 'fp16', 'scalar', 'bw']
T5000 = {'fp4': 1035., 'fp16': 258., 'scalar': 2560., 'bw': 273.}
N = 40000


def sample(n, seed):
    rng = random.Random(seed)
    out = []
    for _ in range(n):
        gv = [rng.gammavariate(1.0, 1.0) for _ in range(4)]
        s = sum(gv)
        out.append({c: v / s for c, v in zip(COMPS, gv)})
    return out


# ---- (b) T5000 手算 flip 计数 ----
ws = sample(N, 42)
flips = 0
flip_pairs = Counter()
for f in ws:
    sc = max(COMPS, key=lambda k: f[k])
    dc = max(COMPS, key=lambda k: f[k] / T5000[k])
    if sc != dc:
        flips += 1
        flip_pairs[(sc, dc)] += 1
orig_flip_rate = 0.434375  # from idea53-theory-flip.json T5000
orig_top = {'scalar->fp16': 4721, 'scalar->bw': 4445, 'fp4->fp16': 3899,
            'fp4->bw': 3729, 'scalar->fp4': 356}
my_rate = flips / N
top5 = {f'{a}->{b}': v for (a, b), v in sorted(flip_pairs.items(), key=lambda x: -x[1])[:5]}
print(f"(b) T5000 hand-count: flips={flips}/{N} rate={my_rate:.6f}")
print(f"    orig flip_rate={orig_flip_rate}  match={abs(my_rate - orig_flip_rate) < 1e-6}")
print(f"    my top5={top5}")
print(f"    orig top5={orig_top}  match={top5 == orig_top}")

# ---- (c) flat-rate=0 稳健性: 多 seed x 多 flat 常数 ----
print("\n(c) flat-rate control robustness:")
rows = []
for seed in (42, 1, 12345):
    w = sample(N, seed)
    for const in (1.0, 2.5, 100.0):
        flat = {c: const for c in COMPS}
        flips_f, shift_f = 0, 0.0
        pairs = []
        for f in w:
            sc = max(COMPS, key=lambda k: f[k])
            dc = max(COMPS, key=lambda k: f[k] / flat[k])
            if sc != dc:
                flips_f += 1
            t = {c: f[c] / flat[c] for c in COMPS}
            T = sum(t.values())
            shift_f += abs(t[dc] / T - f[sc])
            pairs.append((sc, dc))
        # H(D|S)
        d = defaultdict(Counter)
        for a, b in pairs:
            d[a][b] += 1
        n = len(pairs)
        hds = 0.0
        for cnt in d.values():
            m = sum(cnt.values())
            for v in cnt.values():
                p = v / m
                hds -= (m / n) * p * math.log2(p)
        ok = flips_f == 0 and shift_f < 1e-9 and hds < 1e-9
        rows.append(ok)
        print(f"    seed={seed:<6} flat_const={const:<5} flips={flips_f} "
              f"shift={shift_f:.2e} H(D|S)={hds:.2e}  {'OK' if ok else 'FAIL'}")
print(f"    ALL_FLAT_ZERO={all(rows)}  ({sum(rows)}/{len(rows)} configs)")

out = {'b_T5000': {'flips': flips, 'rate': my_rate, 'top5': top5,
                   'match_orig_rate': abs(my_rate - orig_flip_rate) < 1e-6,
                   'match_orig_top5': top5 == orig_top},
       'c_flat_zero_all': all(rows), 'c_configs_tested': len(rows)}
with open('verify_results.json', 'w') as fp:
    json.dump(out, fp, ensure_ascii=False, indent=1)
print("\nwrote verify_results.json")
