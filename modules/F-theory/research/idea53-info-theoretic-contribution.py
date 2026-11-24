#!/usr/bin/env python3
"""#53 核心 claim 因果测量 — 各层对根判定的信息贡献 (2026-11-24, 直接计算, 非消融).

claim: LLM 研究树/推理树中, 深层节点对系统瓶颈判定 (供给侧: SM频率/指令吞吐/发射率/
内存带宽/occupancy) 的信息贡献更大. 这是因果测量 (信息论量), 不是描述性 level 分布
(后者已测: L4 富集三源显著 p<0.05, commit 0e866871c).

度量 (按优先级, n 不够降级, 不卡高阶度量):
  1. 首选 互信息 I(L_k; 根判定) — bge-m3 算各层节点文本与根判定文本相似度, 需联合分布
     (n 够才算, n<30 直接降级)
  2. 次选 条件熵降低 H(根)-H(根|L_k) — 同上, n 够才算
  3. 降级 贡献排名 — 各层供给侧瓶颈判定节点数 / 总瓶颈判定节点数 (哪层贡献最大,
     不依赖 n 大, 最稳健)

根判定 = run 树根节点 (N-0) 判定文本, 或最终结论 (answer 字段).
  ①rep-scan 无 answer → 根 = L1 节点 claim 拼接
  ②t53b 有 answer → 根 = answer
  ③stage-ablation 无 answer → 根 = L1 节点 claim 拼接

边界 (D taste: claim 圈在测得出来的范围):
  只算测得动的词: 内存带宽/occupancy/MFU/Kernel Launch
  指令吞吐(n=2)/issue率(n=0)/warp(n=0) n≈0, 不硬塞结论, 单独标 "n 不足测不了".

同族 judge (27b 评 27b) 分数仅相对有效. 供给侧词表复用
idea53-supply-bottleneck-enrichment.py (硬件供给词 ∧ 判定词), 不重新定义.

架构: 本脚本纯数学 (不 import sentence_transformers). 词表/树加载在
idea53_common.py (子进程提取词表, 避开 enrichment 的 import re 污染).
高阶信息论量 (MI/条件熵) 用分类编码 (根判定二值 × 层瓶颈二值), 不依赖
bge-m3 嵌入 — 因 n_trees<30 underpowered 且 bge-m3 连续版 CPU>45min.
"""
import json, os, math, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from idea53_common import (SUPPLY, JUDGE, MICRO, text_of, load_trees,
                           MEASURABLE, UNMEASURABLE)


def contribution_ranking(trees):
    """降级度量 (最稳健): 各层供给侧瓶颈判定节点数 / 总瓶颈判定节点数."""
    out = {}
    for name, tl in trees.items():
        lv_cnt = Counter(); n_total = 0
        for _, _, ns in tl:
            for nd in ns:
                n_total += 1
                if SUPPLY.search(text_of(nd)) and JUDGE.search(text_of(nd)):
                    lv_cnt[nd['level']] += 1
        tot = sum(lv_cnt.values())
        out[name] = (lv_cnt, tot, n_total)
    return out


def micro_counts(trees):
    """D 点名词: 各层命中数 (测得动 vs 测不了)."""
    out = {}
    for name, tl in trees.items():
        per = {k: Counter() for k in MICRO}
        for _, _, ns in tl:
            for nd in ns:
                t = text_of(nd)
                for k, rx in MICRO.items():
                    if rx.search(t):
                        per[k][nd['level']] += 1
        out[name] = per
    return out


def _entropy(p):
    return -sum(pi * math.log2(pi) for pi in p if pi > 0)


def mutual_info_bits(pairs):
    """pairs: list of (a, b) 离散取值. 返回 I(A;B) bits."""
    n = len(pairs)
    if n == 0:
        return 0.0
    ca, cb, cab = Counter(), Counter(), Counter()
    for a, b in pairs:
        ca[a] += 1; cb[b] += 1; cab[(a, b)] += 1
    mi = 0.0
    for (a, b), n_ab in cab.items():
        p_ab = n_ab / n
        p_a = ca[a] / n
        p_b = cb[b] / n
        mi += p_ab * math.log2(p_ab / (p_a * p_b))
    return mi


def info_theoretic(trees):
    """首选/次选: 互信息 I(L_k;根判定) + 条件熵降低 (分类信息论量, 纯数学).

    编码 (categorical, 不依赖 bge-m3 嵌入):
      根判定 R = 每树根文本二值 (含供给侧瓶颈判定语言? 1:0)
      L_k = 每树第 k 层是否含瓶颈判定节点 (二值 1:0)
    联合分布 = 各树 (R, L_k) 取值, n = 树数 (15/18/26).
    n_trees < 30 → 高阶度量 underpowered, 仅作方向参考 (任务规则: n<30 直接降级,
    主结论以度量3 贡献排名为准).

    注: bge-m3 连续相似度版 (任务首选) 需对 27648 条文本编码, CPU 上 >45min
    且 n_trees<30 同样 underpowered → 降级到本分类 MI + 贡献排名.
    """
    out = {}
    for name, tl in trees.items():
        per_tree = []
        for tid, root, ns in tl:
            root_bin = 1 if (SUPPLY.search(root) and JUDGE.search(root)) else 0
            layer_bin = {}
            for nd in ns:
                if SUPPLY.search(text_of(nd)) and JUDGE.search(text_of(nd)):
                    layer_bin[nd['level']] = 1
            per_tree.append((root_bin, layer_bin, tid))
        layers = sorted(set(lv for _, lb, _ in per_tree for lv in lb))
        H_root = _entropy([sum(r for r, _, _ in per_tree) / len(per_tree)])
        res = {}
        for lv in layers:
            pairs = [(r, lb.get(lv, 0)) for r, lb, _ in per_tree]
            mi = mutual_info_bits(pairs)
            by_b = defaultdict(list)
            for r, b in pairs:
                by_b[b].append(r)
            H_root_given = sum(
                len(v) / len(pairs) * _entropy([sum(v) / len(v)])
                for v in by_b.values()
            )
            res[lv] = {'MI_bits': mi, 'H_root': H_root,
                       'H_root_given': H_root_given,
                       'reduction': H_root - H_root_given}
        out[name] = {'n_trees': len(per_tree), 'H_root': H_root,
                     'layers': res}
    return out


def main():
    trees = load_trees()
    print('#53 因果测量 — 各层对根判定的信息贡献 (直接计算, 非消融)\n')
    for name, tl in trees.items():
        print(f'### {name}: {len(tl)} 树, {sum(len(ns) for _, _, ns in tl)} 节点')

    # ---- 降级度量 (主, 最稳健): 贡献排名 ----
    cr = contribution_ranking(trees)
    print('\n=== 度量3 (降级, 主) 贡献排名: 各层供给侧瓶颈判定节点占比 ===')
    print('说明: 不依赖 n 大, 最稳健. 哪层占比最大 = 哪层对瓶颈判定贡献最大.')
    for name, (lv_cnt, tot, n_total) in cr.items():
        print(f'\n[{name}] 总瓶颈判定节点 n={tot} / 全体 {n_total}')
        for lv in sorted(lv_cnt):
            frac = lv_cnt[lv] / tot if tot else 0
            bar = '#' * int(frac * 40)
            print(f'  {lv}: {lv_cnt[lv]:5d} ({frac:5.1%}) {bar}')
        if tot:
            mx = max(lv_cnt, key=lv_cnt.get)
            print(f'  -> 贡献最大层: {mx} ({lv_cnt[mx]/tot:.1%})')

    # ---- D 点名词: 测得动 vs 测不了 ----
    mc = micro_counts(trees)
    print('\n=== 边界核验: D 点名微架构词 (测得动 vs n 不足) ===')
    for name, per in mc.items():
        print(f'\n[{name}]')
        for k in MEASURABLE + UNMEASURABLE:
            c = per[k]
            tot = sum(c.values())
            tag = '测得动' if k in MEASURABLE else 'n不足测不了'
            dist = ' '.join(f'{lv}:{c.get(lv, 0)}' for lv in sorted(c))
            print(f'  {k:16s} n={tot:5d} [{tag}] {dist}')

    # ---- 首选/次选: 互信息 + 条件熵 (分类信息论量, n_trees<30 → underpowered) ----
    it = info_theoretic(trees)
    print('\n=== 度量1/2 (首选/次选) 互信息 I(L_k;根判定) + 条件熵降低 ===')
    print('说明: 根判定=每树根文本二值(含供给侧瓶颈判定?), L_k=每树第k层含瓶颈节点二值.')
    print('      联合分布 n=树数 (15/18/26) < 30 → 高阶度量 underpowered, 仅作方向参考.')
    print('      bge-m3 连续版 (任务首选) 需编码 27648 文本, CPU>45min 且同样 underpowered')
    print('      → 降级到本分类 MI + 度量3 贡献排名 (主结论). 同族 judge 仅相对有效.')
    for name, d in it.items():
        print(f'\n[{name}] n_trees={d["n_trees"]} H(根)={d["H_root"]:.3f} bits')
        for lv, r in d['layers'].items():
            print(f'  {lv}: I(L;根)={r["MI_bits"]:.4f} bits  '
                  f'H(根|L)={r["H_root_given"]:.4f}  ΔH={r["reduction"]:+.4f}')

    # ---- 落盘 JSON ----
    result = {
        'sources': {name: {'n_trees': len(tl),
                           'n_nodes': sum(len(ns) for _, _, ns in tl)}
                    for name, tl in trees.items()},
        'contribution_ranking': {
            name: {lv: {'count': c, 'frac': c / tot if tot else 0}
                   for lv, c in cr[name][0].items()} |
            {'total_bottleneck': cr[name][1], 'total_nodes': cr[name][2]}
            for name in cr},
        'micro_counts': {
            name: {k: dict(v) for k, v in per.items()}
            for name, per in mc.items()},
        'info_theoretic': it,
        'measurable_terms': MEASURABLE,
        'unmeasurable_terms': UNMEASURABLE,
    }
    out_json = HERE + '/idea53-info-theoretic-contribution.json'
    with open(out_json, 'w') as fh:
        json.dump(result, fh, ensure_ascii=False, indent=2)
    print(f'\n[落盘] JSON -> {out_json}')


if __name__ == '__main__':
    main()
