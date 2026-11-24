#!/usr/bin/env python3
"""#53 信息论直接计算 — 各层对供给侧瓶颈判定的信息贡献 (节点级二值 MI, 纯 math).

claim: LLM 研究树/推理树中, 深层节点对系统瓶颈判定 (供给侧: SM频率/指令吞吐/
发射率/内存带宽/occupancy) 的信息贡献更大.

测量 = 直接信息论计算 (节点级二值互信息, 纯 math, 无嵌入, 不重跑不消融):
  每个节点打二值标签 is_bottleneck = (SUPPLY 词 ∧ JUDGE 词 命中).
  I(layer; is_bottleneck) = H(bottleneck) - H(bottleneck|layer)
    = Σ_k P(L_k)·[H(bottleneck) - H(bottleneck|L_k)]
    ΔH(L_k)   = H(bottleneck) - H(bottleneck|L_k)  层 L_k 的 per-node 信息贡献
    P(L_k)·ΔH = 层 L_k 对总互信息的加权贡献
  n = 节点数 (3849/5497/18243), underpowered 不成立 → 这是 #53 claim 的严格
  信息论版本 (知道节点的层, 能预测它是不是瓶颈判定节点).

为什么不用树级 MI I(L_k; 根判定): n=树数 (15/18/26) < 30 underpowered, 且 L1
(根层) 与根判定天然共线 → L1 的 MI 是编码伪影, 方向反了 (L1 最大), 不支撑
claim. 故删掉, 只保留节点级 MI + 贡献排名.

为什么纯 math 不跑嵌入: bge-m3 CPU 编码 27k 文本 >45min + macOS regex 循环导入
坑. 节点级二值联合分布 n 足够大, 纯 math 即可, 完全 sidestep 嵌入依赖.

诚实边界 (claim 弱化版): 节点级 MI 测的是"层 → 节点是否瓶颈判定"的信息流,
不是"层 → 最终结论(根判定)"的信息流 (后者需树级 MI, n 不够测不了). 所以
#53 claim 目前能支撑的是"深层节点更可能是瓶颈判定节点" (节点级), 不是
"深层节点对最终结论的信息贡献更大" (根级, 测不了). 这是诚实边界.

数据: 复用 idea53-supply-bottleneck-enrichment.py 的三份 GPU run 树 (level 口径
不同, 分源测) + SUPPLY/JUDGE/MICRO 词表.
对照: 需求侧 (DEMAND) 同法算, 看深度梯度是否供给侧特有.
边界: 只算测得动的词 (内存带宽/occupancy/MFU/Kernel Launch n 够); 指令吞吐/issue
率/warp n≈0, 不单独下结论.
"""
import importlib.util, json, math, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, 'idea53-supply-bottleneck-enrichment.py')
_spec = importlib.util.spec_from_file_location('idea53', SCRIPT)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)  # enrichment 顶层只 import json/glob/re/math, 无 transformers, 安全

MEASURABLE = ['内存带宽', 'occupancy/占用率', 'MFU', 'Kernel Launch']
UNMEASURABLE = ['指令吞吐', 'issue rate/发射', 'warp']


def bintext(p):
    """二值熵 (bits). p 在 0/1 边界时熵为 0."""
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -(p * math.log2(p) + (1.0 - p) * math.log2(1.0 - p))


def node_level_mi(nodes, label_fn):
    """节点级二值互信息 I(layer; is_bottleneck), 按层分解. n=节点数, underpowered 不成立."""
    n = len(nodes)
    if n == 0:
        return {}, 0.0, 0.0, 0
    pairs = [(nd['level'], bool(label_fn(mod.text_of(nd)))) for nd in nodes]
    levels = sorted({l for l, _ in pairs})
    n_b = sum(1 for _, b in pairs if b)
    p_b = n_b / n
    H_b = bintext(p_b)
    out = {}
    total = 0.0
    for lv in levels:
        sub = [b for l, b in pairs if l == lv]
        n_lv = len(sub)
        p_lv_b = sum(sub) / n_lv
        H_given = bintext(p_lv_b)
        dH = H_b - H_given          # ≥0, per-node 信息贡献
        P_lv = n_lv / n
        contrib = P_lv * dH         # 加权贡献
        total += contrib
        out[lv] = dict(n=n_lv, n_b=sum(sub), p_b=p_lv_b, H_given=H_given,
                       dH=dH, P=P_lv, contrib=contrib)
    return out, total, H_b, n


def contribution_ranking(nodes):
    """节点级贡献排名: 各层瓶颈判定节点占比 (节点级 MI 的简化, 最稳健)."""
    lv_cnt = Counter(); n = 0
    for nd in nodes:
        n += 1
        if mod.SUPPLY.search(mod.text_of(nd)) and mod.JUDGE.search(mod.text_of(nd)):
            lv_cnt[nd['level']] += 1
    return lv_cnt, sum(lv_cnt.values()), n


def micro_counts(nodes):
    per = {k: Counter() for k in mod.MICRO}
    for nd in nodes:
        t = mod.text_of(nd)
        for k, rx in mod.MICRO.items():
            if rx.search(t):
                per[k][nd['level']] += 1
    return per


SUPPLY_LABEL = lambda t: bool(mod.SUPPLY.search(t) and mod.JUDGE.search(t))
DEMAND_LABEL = lambda t: bool(mod.DEMAND.search(t))


def report(name, nodes, label_fn, tag):
    out, total, H_b, n = node_level_mi(nodes, label_fn)
    if not out:
        print(f'\n### {name} [{tag}]: 无节点'); return
    print(f'\n### {name} [{tag}] | 节点 {n} | H({tag})={H_b:.4f} bits | I(layer;{tag})={total:.4f} bits')
    print(f'{"层":4s} {"n":>6s} {"判定n":>6s} {"判定率":>7s} {"H|层":>8s} {"ΔH贡献":>8s} {"P(层)":>7s} {"加权贡献":>9s}')
    for lv in sorted(out):
        o = out[lv]
        print(f'{lv:4s} {o["n"]:6d} {o["n_b"]:6d} {o["p_b"]:7.1%} '
              f'{o["H_given"]:8.4f} {o["dH"]:8.4f} {o["P"]:7.1%} {o["contrib"]:9.4f}')
    by_dH = sorted(out.items(), key=lambda kv: -kv[1]['dH'])
    by_contrib = sorted(out.items(), key=lambda kv: -kv[1]['contrib'])
    print(f'  per-node 信息贡献最大: {by_dH[0][0]} (ΔH={by_dH[0][1]["dH"]:.4f})')
    print(f'  加权总贡献最大: {by_contrib[0][0]} (P·ΔH={by_contrib[0][1]["contrib"]:.4f})')


def main():
    print('#53 信息论直接计算 — 各层对瓶颈判定的信息贡献 (节点级二值 MI, 纯 math, 无嵌入)')
    srcs = mod.collect_sources()
    result = {'sources': {}, 'node_level_mi_supply': {}, 'node_level_mi_demand': {},
              'contribution_ranking': {}, 'micro_counts': {},
              'measurable_terms': MEASURABLE, 'unmeasurable_terms': UNMEASURABLE}
    for name, nodes in srcs:
        result['sources'][name] = {'n_nodes': len(nodes)}
        report(name, nodes, SUPPLY_LABEL, '供给侧瓶颈')
        report(name, nodes, DEMAND_LABEL, '需求侧对照')
        out_s, total_s, Hb_s, _ = node_level_mi(nodes, SUPPLY_LABEL)
        result['node_level_mi_supply'][name] = {
            'n_nodes': len(nodes), 'H_bottleneck_bits': Hb_s,
            'total_MI_bits': total_s,
            'layers': {lv: o for lv, o in out_s.items()}}
        out_d, total_d, Hb_d, _ = node_level_mi(nodes, DEMAND_LABEL)
        result['node_level_mi_demand'][name] = {
            'n_nodes': len(nodes), 'H_demand_bits': Hb_d,
            'total_MI_bits': total_d,
            'layers': {lv: o for lv, o in out_d.items()}}
        lv_cnt, tot, n = contribution_ranking(nodes)
        result['contribution_ranking'][name] = {
            'total_bottleneck': tot, 'total_nodes': n,
            'layers': {lv: {'count': c, 'frac': c / tot if tot else 0}
                       for lv, c in lv_cnt.items()}}
        per = micro_counts(nodes)
        result['micro_counts'][name] = {k: dict(v) for k, v in per.items()}
        print(f'\n[{name}] 微架构分词:')
        for k in MEASURABLE + UNMEASURABLE:
            c = per[k]; totk = sum(c.values())
            tag = '测得动' if k in MEASURABLE else 'n不足'
            dist = ' '.join(f'{lv}:{c.get(lv, 0)}' for lv in sorted(c))
            print(f'  {k:16s} n={totk:5d} [{tag}] {dist}')
    out_json = os.path.join(HERE, 'idea53-info-theoretic-contribution.json')
    with open(out_json, 'w') as fh:
        json.dump(result, fh, ensure_ascii=False, indent=2)
    print(f'\n[落盘] JSON -> {out_json}')


if __name__ == '__main__':
    main()
