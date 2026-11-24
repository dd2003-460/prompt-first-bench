#!/usr/bin/env python3
"""#53 电阻瓶颈模型 general 化 — 树状瓶颈网络 (2026-11-24, D 指令: 两三层电阻瓶颈模型).

把 #53 claim 从一维 surface-vs-deep (idea53-theory-flip.py, 4 组件平铺) 推广到
树状瓶颈网络: 深层节点的信息贡献 = 它把"瓶颈在哪一段/哪一条支"判对/修正的量.
D 原话: "能把 claim 从『深层修正浅层』推到『树状瓶颈网络里, 深层节点决定哪条分支是瓶颈』".

模型口径 (decomposition-resistor.md):
  树: 2 域 (branch) × 2 段 (segment) = 4 段, 用 4 个真实 spec rate (不编).
      branch0=compute(fp4,fp16), branch1=memory/control(scalar,bw).
  电阻: 每段 r_i = spec rate; 段延迟 time_i = workload_i / r_i (同 1D 版口径).
  瓶颈: B = argmax_i time_i (真实 rate) = 真瓶颈.
  浅层 S: rate 全=1 → time∝workload, B_S = argmax workload.
  深层 D: 真实 rate, B_D = argmax time = B.

树状分解 (本模型的核心, 1D 版没有的):
  段级修正 flip_seg 分解成两部分:
    ① 域级修正 flip_br   = P(B_S_br ≠ B_D_br)  — 深层把"哪条支是瓶颈"判翻转了
    ② 域内修正 flip_within = P(B_S_br = B_D_br 且 B_S_seg ≠ B_D_seg)
       — 域判对了, 深层仍把"域内哪一段是瓶颈"修正了 (深层节点独有贡献)
  新 claim: 深层节点决定哪条分支是瓶颈 = flip_br 显著 > 0 且 H(B_D_br|B_S_br) > 0.

对照臂:
  ① flat: 4 rate 全=1 → 所有 flip/H 必须=0 (解转发平凡性 + 同义反复).
  ② 置换: 随机打乱 4 rate 跨段 (N 次) → 修正量应随 rate 结构变化 (解"修正量是常数").
  ③ 一致性: 段级 flip_seg/H_seg 必须复现 1D 版 paper.md 的数字 (树模型正确扩展 1D).

纯标准库, 不调 LLM, 不跑实验. spec 值复用 idea53-theory-flip.py 的 SPECS.
"""
import json, math, random
from collections import defaultdict

HERE = __import__('os').path.dirname(__import__('os').path.abspath(__file__))
SEED = 42
N = 40000
N_PERM = 24

# 复用 1D 版同一套 spec (保证跨实验可比), 来源 idea53-theory-flip.py
SPECS = {
    '5090':  {'fp4': 1677., 'fp16': 419., 'scalar': 21760., 'bw': 1792.},
    'T5000': {'fp4': 1035., 'fp16': 258., 'scalar': 2560.,  'bw': 273.},
    '4090':  {'fp4': 57.,   'fp16': 114., 'scalar': 16384., 'bw': 1008.},
    'A100':  {'fp4': 156.,  'fp16': 312., 'scalar': 6912.,  'bw': 2039.},
}
# 树结构: 4 段归 2 域. branch0=compute, branch1=memory/control.
SEGMENTS = ['fp4', 'fp16', 'scalar', 'bw']
BRANCH_OF = {0: 0, 1: 0, 2: 1, 3: 1}  # seg idx -> branch
N_BR = 2
# 1D 版 paper.md 的段级数字 (一致性锚, 来源 tasks/idea53-goal/paper.md §4)
PAPER_FLIP = {'5090': 0.527, 'T5000': 0.434, '4090': 0.563, 'A100': 0.556}
PAPER_HSEG = {'5090': 0.7667, 'T5000': 0.7639, '4090': 0.7128, 'A100': 0.7464}


def sample_workloads(n, seed):
    rng = random.Random(seed)
    out = []
    for _ in range(n):
        gv = [rng.gammavariate(1.0, 1.0) for _ in SEGMENTS]
        s = sum(gv)
        out.append([v / s for v in gv])
    return out


def cond_entropy(pairs):
    """H(Y|X) from list of (x, y). bits."""
    n = len(pairs)
    if n == 0:
        return 0.0
    by_x = defaultdict(list)
    for x, y in pairs:
        by_x[x].append(y)
    h = 0.0
    for x, ys in by_x.items():
        px = len(ys) / n
        cnt = defaultdict(int)
        for y in ys:
            cnt[y] += 1
        hx = 0.0
        for y, c in cnt.items():
            p = c / len(ys)
            hx -= p * math.log2(p)
        h += px * hx
    return h


def analyze(rates, ws):
    """返回域级/段级/域内 flip + 条件熵 (深层独有信息)."""
    seg_pairs, br_pairs = [], []
    seg_flip = br_flip = within_flip = 0
    for f in ws:
        t = [f[i] / rates[i] for i in range(4)]
        bd = max(range(4), key=lambda i: t[i])          # 深层段 (真瓶颈)
        bs = max(range(4), key=lambda i: f[i])          # 浅层段 (workload 基)
        seg_pairs.append((bs, bd))
        # 域级: 域内延迟求和, 取最大域
        br_t = [0.0, 0.0]
        br_f = [0.0, 0.0]
        for i in range(4):
            br_t[BRANCH_OF[i]] += t[i]
            br_f[BRANCH_OF[i]] += f[i]
        bdb = max(range(N_BR), key=lambda b: br_t[b])   # 深层域
        bsb = max(range(N_BR), key=lambda b: br_f[b])   # 浅层域
        br_pairs.append((bsb, bdb))
        if bsb != bdb:
            br_flip += 1
        if bs != bd:
            seg_flip += 1
            if bsb == bdb:
                within_flip += 1   # 域判对, 但域内段判错 → 深层节点独有修正
    n = len(ws)
    return {
        'flip_segment': seg_flip / n,
        'H_BD_given_BS_segment': cond_entropy(seg_pairs),
        'flip_branch': br_flip / n,
        'H_BD_given_BS_branch': cond_entropy(br_pairs),
        'flip_within_branch': within_flip / n,
    }


def ratio_extremity(rates):
    return max(rates) / min(rates)


def main():
    ws = sample_workloads(N, SEED)
    out = {'design': 'tree bottleneck network (2 branch x 2 seg); deep node contribution '
                     '= branch-level flip + within-branch flip (deep-only fine correction)',
           'n_workloads': N, 'n_perm': N_PERM, 'specs': {}}
    for g, spec in SPECS.items():
        rates = [spec[c] for c in SEGMENTS]
        a = analyze(rates, ws)
        a['rate_extremity'] = round(ratio_extremity(rates), 1)
        # 一致性: 段级数字必须复现 1D paper.md
        a['consistent_with_paper'] = (
            abs(a['flip_segment'] - PAPER_FLIP[g]) < 0.005 and
            abs(a['H_BD_given_BS_segment'] - PAPER_HSEG[g]) < 0.005)
        # 对照臂②: 置换 rate (打乱跨段), 修正量应随 rate 结构变化
        rng = random.Random(SEED + 1)
        perm_br = []
        for _ in range(N_PERM):
            pr = rates[:]
            rng.shuffle(pr)
            perm_br.append(analyze(pr, ws)['flip_branch'])
        a['perm_flip_branch_range'] = [round(min(perm_br), 4), round(max(perm_br), 4)]
        a['perm_varies'] = (max(perm_br) - min(perm_br)) > 0.01
        out['specs'][g] = a
    # 对照臂①: flat (rate 全=1) → 必须恰好 0
    flat = analyze([1.0, 1.0, 1.0, 1.0], ws)
    out['control_flat'] = {k: round(v, 6) for k, v in flat.items()}
    out['control_flat_zero'] = all(v == 0 for v in flat.values())
    # 树状 claim: 深层节点决定哪条分支是瓶颈
    #   = 所有真实平台 flip_br > 0 且 H(B_D_br|B_S_br) > 0, 且 flat 归零
    all_br_pos = all(out['specs'][g]['flip_branch'] > 0 and
                     out['specs'][g]['H_BD_given_BS_branch'] > 0 for g in out['specs'])
    all_consistent = all(out['specs'][g]['consistent_with_paper'] for g in out['specs'])
    out['tree_claim_holds'] = all_br_pos and out['control_flat_zero'] and all_consistent
    json.dump(out, open(HERE + '/idea53-resistor-model.json', 'w'),
              ensure_ascii=False, indent=2)
    line = ' | '.join(
        f"{g}: flip_br={out['specs'][g]['flip_branch']:.3f} H_br={out['specs'][g]['H_BD_given_BS_branch']:.3f} "
        f"flip_within={out['specs'][g]['flip_within_branch']:.3f}"
        for g in out['specs'])
    concl = ('成立(深层节点决定哪条支是瓶颈: flip_br 全>0, H_br 全>0, flat归零, 段级复现1D)'
             if out['tree_claim_holds'] else '部分/不成立')
    with open(HERE + '/idea53-resistor-model.md', 'w') as fh:
        fh.write('#53 电阻瓶颈模型 (树状 2x2) — 一行结论\n\n' + line +
                 f'\n\nflat归零={out["control_flat_zero"]} 段级复现1D={all_consistent} '
                 f'→ {concl}\n')
    print(line)
    print(f"flat归零={out['control_flat_zero']} 段级复现1D={all_consistent} → {concl}")
    print(f'[落盘] {HERE}/idea53-resistor-model.json')


if __name__ == '__main__':
    main()
