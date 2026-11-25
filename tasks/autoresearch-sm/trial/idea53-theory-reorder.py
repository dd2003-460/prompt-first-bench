#!/usr/bin/env python3
"""#53 对照臂② 实测: 参数-深度重排 (tautology 防御, surface-vs-deep 模型内).
设计: 把 rate 向量在 4 个组件间做全部 24 种置换 (保持 rate 多重集不变),
     每种置换算 flip_rate + mean_time_shift.
     若修正量由 rate-ratio 信息 (多重集) 决定, 则 24 种置换下修正量应一致
     (或至多由 workload 先验的对称性决定) → 修正量跟 rate 信息走, 非跟
     "哪个组件被标成深层"走 → 解同义反复 (depth 标签是任意的).
     对照: 打乱 rate 多重集本身 (flat) → 修正=0 (control_flat 已证).
与 idea53-theory-flip.py 同 SPECS/N/SEED/surface/deep, 保证数字可比.
"""
import json, random
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


def sample_workloads(n, seed):
    rng = random.Random(seed)
    out = []
    for _ in range(n):
        gv = [rng.gammavariate(1.0, 1.0) for _ in range(4)]
        s = sum(gv)
        out.append({c: v / s for c, v in zip(COMPS, gv)})
    return out


def surface(f):
    c = max(COMPS, key=lambda k: f[k])
    return c, f[c]


def deep(spec, f):
    t = {c: f[c] / spec[c] for c in COMPS}
    T = sum(t.values())
    c = max(t, key=t.get)
    return c, t[c] / T


def analyze(spec, ws):
    flips, shifts = 0, 0.0
    for f in ws:
        sc, ss = surface(f)
        dc, ds = deep(spec, f)
        if sc != dc:
            flips += 1
        shifts += abs(ds - ss)
    n = len(ws)
    return flips / n, shifts / n


def main():
    ws = sample_workloads(N, SEED)
    out = {'design': 'param-depth reordering control (measured): permute rate vector over components, increment should track rate info not depth label'}
    per_hw = {}
    for g, sp in SPECS.items():
        rates = [sp[c] for c in COMPS]
        perm_results = {}
        for perm in set(permutations(range(4))):
            spec_p = {COMPS[i]: rates[perm[i]] for i in range(4)}
            flip, shift = analyze(spec_p, ws)
            perm_results['-'.join(COMPS[i] + '=' + str(rates[perm[i]])[:4] for i in range(4))] = {
                'flip': round(flip, 4), 'shift': round(shift, 4)}
        flips = [v['flip'] for v in perm_results.values()]
        shifts = [v['shift'] for v in perm_results.values()]
        # 规范序 (identity) 应与主结果一致
        identity = {COMPS[i]: rates[i] for i in range(4)}
        flip_id, shift_id = analyze(identity, ws)
        per_hw[g] = {
            'n_perm': len(perm_results),
            'identity_flip': round(flip_id, 4), 'identity_shift': round(shift_id, 4),
            'flip_range': [round(min(flips), 4), round(max(flips), 4)],
            'shift_range': [round(min(shifts), 4), round(max(shifts), 4)],
            'perm_results': perm_results,
        }
    out['per_hardware'] = per_hw
    out['conclusion'] = (
        '若修正量只跟 rate 多重集走 → 24 置换下 flip/shift 恒定; '
        '若跟组件标签走 → 随置换变. 实测见 per_hardware flip_range/shift_range.')
    with open('idea53-theory-reorder.json', 'w') as fp:
        json.dump(out, fp, ensure_ascii=False, indent=1)
    print(f"{'hw':8} {'id_flip':>8} {'id_shift':>9} {'flip_range':>18} {'shift_range':>18}")
    for g, a in per_hw.items():
        print(f"{g:8} {a['identity_flip']:>8} {a['identity_shift']:>9} "
              f"{str(a['flip_range']):>18} {str(a['shift_range']):>18}")
    print(out['conclusion'])


if __name__ == '__main__':
    main()
