#!/usr/bin/env python3
"""#53 理论路线: 瓶颈因子树 × 每节点信息增益 (闭式, 纯数学, 无 LLM/实验).
D 2026-11-24 纠正: 信息增益=理论计算 (spec+workload 先验→条件互信息), 非 judge 标注.
验证锚: 必须复现 D 三例数字, 复现不了标 [模型不对].
"""
import json, math, random
from collections import Counter, defaultdict

SEED = 42
N = 20000  # 每硬件 workload 采样数 (Dirichlet(1,1,1,1) = simplex 均匀)
COMPS = ['fp4', 'fp16', 'scalar', 'bw']

# spec (相对速率). fp4/fp16=dense TFLOPS, scalar≈CUDA 核数, bw=GB/s
# 单位混合=近似 (标量/带宽与 FLOPS 不同量纲), 论文需标注
SPECS = {
    '5090':  {'fp4': 1677., 'fp16': 419., 'scalar': 21760., 'bw': 1792.},
    'T5000': {'fp4': 1035., 'fp16': 258., 'scalar': 2560.,  'bw': 273.},
    '4090':  {'fp4': 57.,   'fp16': 114., 'scalar': 16384., 'bw': 1008.},  # 无原生 FP4→0.5×fp16 [待核验]
    'A100':  {'fp4': 156.,  'fp16': 312., 'scalar': 6912.,  'bw': 2039.},  # 同上
}


def bottleneck(spec, f):
    t = {c: f[c] / spec[c] for c in COMPS}
    T = sum(t.values())
    b = max(t, key=t.get)
    return b, t[b] / T, t


def b_label(spec, f):
    b, s, _ = bottleneck(spec, f)
    return (b, min(9, int(s * 10)))  # 类型(4) × 占比 bin(10)


def node_vals(spec, f):
    """4 节点, 全是 workload 参数 (spec 是固定上下文, 不进节点):
    0=L1 枚举型(workload 主导类, 4 值)
    1=L2 枚举型(算力精度混合 fp16/(fp4+fp16), 5 bin)
    2=L3 判断型(标量 workload 占比, 微架构级, 5 bin)
    3=L4 判断型(带宽 workload 占比, 微架构级, 5 bin)
    揭示序 coarse→fine: 先枚举哪类, 再精度混合, 再微架构占比.
    B 是 workload 的确定性函数 (t_i=f_i/rate_i), 全揭示→B 确定."""
    dom = max(COMPS, key=lambda c: f[c])
    pc = f['fp4'] + f['fp16']
    mix = 0 if pc < 1e-9 else min(4, int((f['fp16'] / pc) * 5))
    scal = min(4, int(f['scalar'] * 5))
    bw = min(4, int(f['bw'] * 5))
    return (dom, mix, scal, bw)


def cond_H(data, idx_list):
    """H(B | 节点 idx_list)  data: [(node_tuple, b_label)]"""
    d = defaultdict(Counter)
    for nv, bl in data:
        d[tuple(nv[i] for i in idx_list)][bl] += 1
    h, n = 0.0, len(data)
    for cnt in d.values():
        m = sum(cnt.values())
        for v in cnt.values():
            p = v / m
            h -= (m / n) * p * math.log2(p)
    return h


def gains(data, order):
    """按 depth 顺序 order 算每节点边际增益 I(B; p_k | 前序)"""
    h, out = cond_H(data, []), []
    for i in range(len(order)):
        h_new = cond_H(data, order[:i + 1])
        out.append(h - h_new)
        h = h_new
    return out, h


def sample_data(specs, n=N, seed=SEED):
    rng = random.Random(seed)
    data = []
    for g, sp in specs.items():
        for _ in range(n):
            gv = [rng.gammavariate(1.0, 1.0) for _ in range(4)]
            s = sum(gv)
            f = {c: v / s for c, v in zip(COMPS, gv)}
            data.append((node_vals(sp, f), b_label(sp, f)))
    return data


def main():
    out = {'design': 'factor tree × per-node conditional MI, closed-form, no LLM'}
    # ---- 验证锚: D 三例 ----
    repro = []
    sp = SPECS['T5000']
    f1 = {'fp4': .5, 'fp16': .5, 'scalar': 0., 'bw': 0.}
    b, s, _ = bottleneck(sp, f1)
    repro.append({'case': 'T5000 50/50 FP16/FP4', 'expect': 'FP16 占 78-80%',
                  'got': f'{b} {s:.3f}', 'match': abs(s - 0.80) < 0.03})
    f2 = {'fp4': .7, 'fp16': .3, 'scalar': 0., 'bw': 0.}
    b, s, _ = bottleneck(sp, f2)
    repro.append({'case': 'T5000 70/30', 'expect': 'FP16 占 63%',
                  'got': f'{b} {s:.3f}', 'match': abs(s - 0.63) < 0.03})
    # 5090 标量 40% 时间占比, issue 砍半 → 慢 40%
    sp5 = SPECS['5090']
    fc = 0.6
    fs = (2 / 3) * (fc / sp5['fp16']) * sp5['scalar']  # 解出标量 FLOP 量使时间占比=40%
    f3 = {'fp4': 0., 'fp16': fc, 'scalar': fs, 'bw': 0.}
    T0 = sum(f3[c] / sp5[c] for c in COMPS)
    scalar_share = (f3['scalar'] / sp5['scalar']) / T0
    sp5h = dict(sp5); sp5h['scalar'] /= 2
    T1 = sum(f3[c] / sp5h[c] for c in COMPS)
    repro.append({'case': '5090 标量 40% + issue 砍半', 'expect': '标量占 40%, 慢 40% (T1/T0=1.4)',
                  'got': f'scalar_share={scalar_share:.3f}, T1/T0={T1 / T0:.3f}',
                  'match': abs(scalar_share - 0.4) < 0.02 and abs(T1 / T0 - 1.4) < 0.02})
    out['reproduce_check'] = repro
    model_ok = all(r['match'] for r in repro)
    out['model_ok'] = model_ok

    # ---- 主计算: 每硬件 + 跨硬件 ----
    order = [0, 1, 2, 3]  # L1..L4 自然分析序
    per_hw, pooled = {}, {}
    for g in SPECS:
        d = sample_data({g: SPECS[g]})
        g_, rem = gains(d, order)
        per_hw[g] = {'per_node_bits': [round(x, 4) for x in g_],
                     'residual_H_bits': round(rem, 4)}
    d_all = sample_data(SPECS)
    g_all, rem_all = gains(d_all, order)
    pooled = {'per_node_bits': [round(x, 4) for x in g_all],
              'residual_H_bits': round(rem_all, 4)}
    out['per_hardware'] = per_hw
    out['pooled_cross_hw'] = pooled

    # ---- 对照臂 ----
    ctrls = {}
    # ① 占位硬件: 所有 rate=1 → L3(CUDA 规模) 常数 → 增益应→0
    flat = {g: {c: 1.0 for c in COMPS} for g in SPECS}
    dflat = []
    rng = random.Random(SEED)
    for g in flat:
        for _ in range(N):
            gv = [rng.gammavariate(1.0, 1.0) for _ in range(4)]
            s = sum(gv); f = {c: v / s for c, v in zip(COMPS, gv)}
            dflat.append((node_vals(flat[g], f), b_label(flat[g], f)))
    gf, _ = gains(dflat, order)
    ctrls['placeholder_flat_rates'] = {'per_node_bits': [round(x, 4) for x in gf],
                                       'expect': 'rate 全相等→B=主导类, 细节点增益应显著低于真实 spec'}
    # ② 参数-深度重排: 20 个随机序, 平均每 depth 槽增益 (增益跟参数走还是跟深度走?)
    rng2 = random.Random(SEED + 1)
    slot = defaultdict(list)
    for _ in range(20):
        o = order[:]; rng2.shuffle(o)
        if o == order:
            continue
        gp, _ = gains(d_all, o)
        for depth, (oi, gi) in enumerate(zip(o, gp)):
            slot[depth].append(gi)
    ctrls['param_depth_reassign'] = {
        'mean_gain_per_depth_slot': {str(k): round(sum(v) / len(v), 4) for k, v in sorted(slot.items())},
        'expect': '若增益跟参数走→各槽≈该参数原增益(与 depth 无关); 跟深度走→槽增益随 depth 升'}
    # ③ 层内类型对照: 枚举型(节点0,1) vs 判断型(节点2,3) 平均增益
    ctrls['type_control'] = {
        'enum_nodes_mean': round(sum(g_all[:2]) / 2, 4),
        'judge_nodes_mean': round(sum(g_all[2:]) / 2, 4),
        'expect': '判断型>枚举型 → 贡献由类型驱动非深度驱动'}
    out['controls'] = ctrls

    # ---- 结论 ----
    deep = sum(g_all[2:]) / 2
    shal = sum(g_all[:2]) / 2
    consistent = all(
        (sum(per_hw[g]['per_node_bits'][2:]) / 2) > (sum(per_hw[g]['per_node_bits'][:2]) / 2)
        for g in per_hw)
    out['conclusion'] = (
        f'深层(判断型)每节点 {deep:.4f} bits vs 浅层(枚举型) {shal:.4f} bits; '
        f'跨硬件一致={consistent}; 生死线={"成立" if deep > shal and consistent else "不成立/部分"}')
    with open('idea53-theory.json', 'w') as fp:
        json.dump(out, fp, ensure_ascii=False, indent=1)
    print(f"model_ok={model_ok}")
    for r in repro:
        print(f"  {r['case']}: {r['got']} match={r['match']}")
    print(f"pooled per-node: {pooled['per_node_bits']}")
    for g in per_hw:
        print(f"  {g}: {per_hw[g]['per_node_bits']}")
    print(f"ctrl flat: {ctrls['placeholder_flat_rates']['per_node_bits']}")
    print(f"ctrl reassign: {ctrls['param_depth_reassign']['mean_gain_per_depth_slot']}")
    print(f"ctrl type: enum={ctrls['type_control']['enum_nodes_mean']} judge={ctrls['type_control']['judge_nodes_mean']}")
    print(out['conclusion'])


if __name__ == '__main__':
    main()
