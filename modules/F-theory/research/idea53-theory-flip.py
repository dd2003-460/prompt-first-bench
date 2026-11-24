#!/usr/bin/env python3
"""#53 理论路线 v2: surface-vs-deep 判断修正 (D 2026-11-24 纠正后).
核心: 浅层枚举 = 表面判断 (假设 rate 相等, 时间∝workload);
      深层微架构判断 = 真实 rate ratio → 时间占比.
      深层节点信息增益 = 它把表面判断翻转/修正了多少 (方向修正 + 粒度细化).
claim: 深层修正量随 rate-ratio 极端度 (非线性放大) 升, 且显著 > 浅层枚举能给的.
验证锚: 复现 D 三例 (T5000 50/50→80%, 70/30→63%, 5090 标量40%+issue砍半→慢40%).
"""
import json, random
from collections import defaultdict

SEED = 42
N = 40000
COMPS = ['fp4', 'fp16', 'scalar', 'bw']
SPECS = {
    '5090':  {'fp4': 1677., 'fp16': 419., 'scalar': 21760., 'bw': 1792.},
    'T5000': {'fp4': 1035., 'fp16': 258., 'scalar': 2560.,  'bw': 273.},
    '4090':  {'fp4': 57.,   'fp16': 114., 'scalar': 16384., 'bw': 1008.},
    'A100':  {'fp4': 156.,  'fp16': 312., 'scalar': 6912.,  'bw': 2039.},
}


def sample_workloads(n, seed):
    rng = random.Random(seed)
    out = []
    for _ in range(n):
        gv = [rng.gammavariate(1.0, 1.0) for _ in range(4)]
        s = sum(gv)
        out.append({c: v / s for c, v in zip(COMPS, gv)})
    return out


def surface(f):
    """浅层枚举: rate 全=1 → 时间∝workload. 返回 (瓶颈类, 时间占比)."""
    c = max(COMPS, key=lambda k: f[k])
    return c, f[c]


def deep(spec, f):
    """深层微架构判断: 真实 rate → 时间占比. 返回 (瓶颈类, 时间占比)."""
    t = {c: f[c] / spec[c] for c in COMPS}
    T = sum(t.values())
    c = max(t, key=t.get)
    return c, t[c] / T


def ratio_extremity(spec):
    """rate-ratio 极端度: 最快/最慢组件速率比 (越大→非线性放大越强)."""
    rates = [spec[c] for c in COMPS]
    return max(rates) / min(rates)


def analyze(spec, ws):
    flips, shifts = 0, 0.0
    flip_by = defaultdict(int)
    for f in ws:
        sc, ss = surface(f)
        dc, ds = deep(spec, f)
        if sc != dc:
            flips += 1
            flip_by[(sc, dc)] += 1
        shifts += abs(ds - ss)
    n = len(ws)
    return {'flip_rate': flips / n, 'mean_time_shift': shifts / n,
            'top_flips': {f'{a}->{b}': v for (a, b), v in sorted(flip_by.items(), key=lambda x: -x[1])[:5]}}


def main():
    out = {'design': 'surface-vs-deep judgment correction; deep info = rate-ratio correction to surface'}
    # 验证锚
    repro = []
    sp = SPECS['T5000']
    _, s1 = deep(sp, {'fp4': .5, 'fp16': .5, 'scalar': 0., 'bw': 0.})
    repro.append({'case': 'T5000 50/50', 'expect': 'FP16 80%', 'got': f'{s1:.3f}', 'match': abs(s1 - .8) < .03})
    _, s2 = deep(sp, {'fp4': .7, 'fp16': .3, 'scalar': 0., 'bw': 0.})
    repro.append({'case': 'T5000 70/30', 'expect': 'FP16 63%', 'got': f'{s2:.3f}', 'match': abs(s2 - .63) < .03})
    sp5 = SPECS['5090']; fc = .6
    fs = (2 / 3) * (fc / sp5['fp16']) * sp5['scalar']
    f3 = {'fp4': 0., 'fp16': fc, 'scalar': fs, 'bw': 0.}
    T0 = sum(f3[c] / sp5[c] for c in COMPS)
    ss = (f3['scalar'] / sp5['scalar']) / T0
    sp5h = dict(sp5); sp5h['scalar'] /= 2
    T1 = sum(f3[c] / sp5h[c] for c in COMPS)
    repro.append({'case': '5090 标量40%+issue砍半', 'expect': '标量40%, 慢40%',
                  'got': f'scal={ss:.3f}, T1/T0={T1 / T0:.3f}',
                  'match': abs(ss - .4) < .02 and abs(T1 / T0 - 1.4) < .02})
    out['reproduce_check'] = repro
    out['model_ok'] = all(r['match'] for r in repro)

    # 主计算: 每硬件 surface-vs-deep 修正
    ws = sample_workloads(N, SEED)
    per_hw = {}
    for g in SPECS:
        a = analyze(SPECS[g], ws)
        a['ratio_extremity'] = round(ratio_extremity(SPECS[g]), 1)
        per_hw[g] = a
    out['per_hardware'] = per_hw

    # 对照臂: 占位硬件 (rate 全相等) → 深层修正应→0 (无 rate ratio 可修正)
    flat = {c: 1.0 for c in COMPS}
    a_flat = analyze(flat, ws)
    out['control_flat'] = {'flip_rate': a_flat['flip_rate'], 'mean_time_shift': a_flat['mean_time_shift'],
                           'expect': 'rate 全等→深层=表面, 修正≈0'}

    # 结论: 修正量是否随 ratio 极端度升 (非线性放大)
    order = sorted(per_hw, key=lambda g: -per_hw[g]['ratio_extremity'])
    shifts = [per_hw[g]['mean_time_shift'] for g in order]
    monotonic = all(shifts[i] >= shifts[i + 1] - 1e-9 for i in range(len(shifts) - 1))
    out['conclusion'] = (
        f'深层修正量(mean_time_shift) 按 ratio 极端度排序 {order}: {[round(x, 4) for x in shifts]}; '
        f'随极端度单调降={monotonic}; 占位硬件修正={out["control_flat"]["mean_time_shift"]:.4f}(应≈0); '
        f'生死线={"成立(深层修正随rate-ratio极端度升, 浅层枚举给不出)" if monotonic and out["control_flat"]["mean_time_shift"] < 0.05 else "部分/不成立"}')
    with open('idea53-theory-flip.json', 'w') as fp:
        json.dump(out, fp, ensure_ascii=False, indent=1)
    print(f"model_ok={out['model_ok']}")
    for r in repro:
        print(f"  {r['case']}: {r['got']} match={r['match']}")
    print(f"{'hw':8} {'ratio':>7} {'flip':>7} {'shift':>8}  top_flips")
    for g in order:
        a = per_hw[g]
        print(f"{g:8} {a['ratio_extremity']:>7} {a['flip_rate']:>7.3f} {a['mean_time_shift']:>8.4f}  {list(a['top_flips'].items())[:3]}")
    print(f"flat control: flip={out['control_flat']['flip_rate']:.4f} shift={out['control_flat']['mean_time_shift']:.4f}")
    print(out['conclusion'])


if __name__ == '__main__':
    main()
