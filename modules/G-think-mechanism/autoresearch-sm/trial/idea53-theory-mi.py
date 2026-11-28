#!/usr/bin/env python3
"""#53 T8: 严格互信息补强 (flip/shift → MI).
核心量:
  H(D)      深层(真实 rate)瓶颈判断的熵
  H(D|S)    已知表面判断后深层判断的残余熵 = 深层独有信息(修正量)
  I(S;D)    = H(D)-H(D|S) = 表面判断对深层的预测力
claim: H(D|S) 显著 > 0 (表面判不准深层) 且 flat 对照下 H(D|S)→0 (深层信息纯来自 rate-ratio).
"""
import json, math, random
from collections import defaultdict, Counter

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
    rng = random.Random(seed)
    out = []
    for _ in range(n):
        gv = [rng.gammavariate(1.0, 1.0) for _ in range(4)]
        s = sum(gv)
        out.append({c: v / s for c, v in zip(COMPS, gv)})
    return out


def surface(f):
    return max(COMPS, key=lambda k: f[k])


def deep(spec, f):
    t = {c: f[c] / spec[c] for c in COMPS}
    return max(t, key=t.get)


def H(pairs):
    """pairs: list of (a, b) -> H(b)."""
    cnt = Counter(b for _, b in pairs)
    n = len(pairs)
    return -sum((v / n) * math.log2(v / n) for v in cnt.values())


def H_cond(pairs, idx_a, idx_b):
    """H(b | a) for pairs of tuples."""
    d = defaultdict(Counter)
    for t in pairs:
        d[t[idx_a]][t[idx_b]] += 1
    n = len(pairs)
    h = 0.0
    for cnt in d.values():
        m = sum(cnt.values())
        for v in cnt.values():
            p = v / m
            h -= (m / n) * p * math.log2(p)
    return h


def mi(spec, ws):
    pairs = [(surface(f), deep(spec, f)) for f in ws]
    h_d = H(pairs)
    h_d_given_s = H_cond(pairs, 0, 1)
    i_sd = h_d - h_d_given_s
    flip = sum(1 for a, b in pairs if a != b) / len(pairs)
    return {'H_D_bits': round(h_d, 4), 'H_D_given_S_bits': round(h_d_given_s, 4),
            'I_S_D_bits': round(i_sd, 4), 'flip_rate': round(flip, 4)}


def main():
    ws = sample(N, SEED)
    out = {'design': 'strict MI: H(D), H(D|S)=deep-only info, I(S;D)=surface predictive power'}
    per_hw = {}
    for g in SPECS:
        per_hw[g] = mi(SPECS[g], ws)
    flat = {c: 1.0 for c in COMPS}
    per_hw['flat_control'] = mi(flat, ws)
    out['per_hardware'] = per_hw
    # 结论
    real = [per_hw[g]['H_D_given_S_bits'] for g in SPECS]
    out['conclusion'] = (
        f'H(D|S) 深层独有信息 [bits]: '
        + ', '.join(f'{g}={per_hw[g]["H_D_given_S_bits"]}' for g in SPECS)
        + f'; flat_control={per_hw["flat_control"]["H_D_given_S_bits"]} (应≈0); '
        + f'生死线={"成立(深层独有信息显著>0 且 flat→0)" if min(real) > 0.1 and per_hw["flat_control"]["H_D_given_S_bits"] < 0.01 else "部分"}')
    with open('idea53-theory-mi.json', 'w') as fp:
        json.dump(out, fp, ensure_ascii=False, indent=1)
    print(f"{'hw':14} {'H(D)':>6} {'H(D|S)':>8} {'I(S;D)':>7} {'flip':>6}")
    for g in list(SPECS) + ['flat_control']:
        a = per_hw[g]
        print(f"{g:14} {a['H_D_bits']:>6} {a['H_D_given_S_bits']:>8} {a['I_S_D_bits']:>7} {a['flip_rate']:>6}")
    print(out['conclusion'])


if __name__ == '__main__':
    main()
