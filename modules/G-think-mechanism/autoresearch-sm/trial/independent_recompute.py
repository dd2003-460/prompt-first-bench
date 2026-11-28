#!/usr/bin/env python3
"""C3a 独立重算 — 不复用 idea53-theory-*.py 的函数, 自己重写 surface/deep/flip/shift/H 逻辑,
用同一 workload (同 seed 同采样) 交叉验证脚本输出的数字是否正确。
同时独立重算 24 置换不变性 + flat 对照。
"""
import json, math, random
from collections import defaultdict, Counter
from itertools import permutations

SEED = 42
N = 40000
COMPS = ['fp4', 'fp16', 'scalar', 'bw']
SPECS = {
    '5090':  {'fp4': 1677., 'fp16': 419., 'scalar': 21760., 'bw': 1792.},
    'T5000': {'fp4': 1035., 'fp16': 258., 'scalar': 2560.,  'bw': 273.},
    '4090':  {'fp4': 57.,   'fp16': 114., 'scalar': 16384., 'bw': 1008.},
    'A100':  {'fp4': 156.,  'fp16': 312., 'scalar': 6912.,  'bw': 2039.},
}


def sample(n, seed):
    # 与原脚本相同的采样: 同 seed 同方法 → 同一 workload
    rng = random.Random(seed)
    out = []
    for _ in range(n):
        gv = [rng.gammavariate(1.0, 1.0) for _ in range(4)]
        s = sum(gv)
        out.append({c: v / s for c, v in zip(COMPS, gv)})
    return out


def surface_comp(f):
    """浅层: rate 全等 → 时间∝workload → 瓶颈=workload 最大分量."""
    return max(COMPS, key=lambda k: f[k])


def deep_comp(spec, f):
    """深层: 真实 rate → 时间占比 t_c=f_c/spec_c → 瓶颈=时间占比最大分量."""
    return max(COMPS, key=lambda k: f[k] / spec[k])


def deep_share(spec, f):
    t = {c: f[c] / spec[c] for c in COMPS}
    T = sum(t.values())
    return t[max(t, key=t.get)] / T


def surface_share(f):
    c = max(COMPS, key=lambda k: f[k])
    return f[c]


def h_bits(counter, n):
    return -sum((v / n) * math.log2(v / n) for v in counter.values() if v)


def h_cond(pairs):
    """H(b|a) for pairs=(a,b)."""
    d = defaultdict(Counter)
    for a, b in pairs:
        d[a][b] += 1
    n = len(pairs)
    h = 0.0
    for a, cnt in d.items():
        m = sum(cnt.values())
        for v in cnt.values():
            p = v / m
            h -= (m / n) * p * math.log2(p)
    return h


def recompute(spec, ws):
    flips = 0
    shift_sum = 0.0
    pairs = []
    for f in ws:
        sc = surface_comp(f)
        dc = deep_comp(spec, f)
        if sc != dc:
            flips += 1
        shift_sum += abs(deep_share(spec, f) - surface_share(f))
        pairs.append((sc, dc))
    n = len(ws)
    h_d = h_bits(Counter(b for _, b in pairs), n)
    h_ds = h_cond(pairs)
    return {'flip': flips / n, 'shift': shift_sum / n,
            'H_D': h_d, 'H_DS': h_ds, 'I_SD': h_d - h_ds}


def main():
    ws = sample(N, SEED)
    print(f"N={len(ws)}  seed={SEED}")
    print(f"\n{'hw':8} {'flip':>8} {'shift':>8} {'H(D)':>7} {'H(D|S)':>8} {'I(S;D)':>7}")
    per_hw = {}
    for g, sp in SPECS.items():
        r = recompute(sp, ws)
        per_hw[g] = r
        print(f"{g:8} {r['flip']:>8.4f} {r['shift']:>8.4f} {r['H_D']:>7.4f} {r['H_DS']:>8.4f} {r['I_SD']:>7.4f}")
    # flat 对照
    flat = {c: 1.0 for c in COMPS}
    rf = recompute(flat, ws)
    per_hw['flat'] = rf
    print(f"{'flat':8} {rf['flip']:>8.4f} {rf['shift']:>8.4f} {rf['H_D']:>7.4f} {rf['H_DS']:>8.4f} {rf['I_SD']:>7.4f}")
    # 24 置换不变性 (独立重算 range)
    print("\n24-perm invariance (independent recompute):")
    print(f"{'hw':8} {'id_flip':>8} {'id_shift':>9} {'flip_rng':>18} {'shift_rng':>18}")
    perm_out = {}
    for g, sp in SPECS.items():
        rates = [sp[c] for c in COMPS]
        flips, shifts = [], []
        for perm in set(permutations(range(4))):
            spec_p = {COMPS[i]: rates[perm[i]] for i in range(4)}
            r = recompute(spec_p, ws)
            flips.append(r['flip']); shifts.append(r['shift'])
        perm_out[g] = {'n': len(flips), 'flip_range': [min(flips), max(flips)],
                       'shift_range': [min(shifts), max(shifts)]}
        fr = [round(min(flips),4), round(max(flips),4)]
        sr = [round(min(shifts),4), round(max(shifts),4)]
        print(f"{g:8} {flips[0]:>8.4f} {shifts[0]:>9.4f} {str(fr):>18} {str(sr):>18}")
    out = {'per_hardware': per_hw, 'perm': perm_out}
    with open('independent_recompute.json', 'w') as fp:
        json.dump(out, fp, ensure_ascii=False, indent=1)
    print("\nwrote independent_recompute.json")


if __name__ == '__main__':
    main()
