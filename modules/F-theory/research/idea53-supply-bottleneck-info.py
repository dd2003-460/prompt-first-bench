#!/usr/bin/env python3
"""#53 信息论量 — 深层节点对供给侧瓶颈判定的信息贡献 (2026-11-24).

D 2026-11-24 taste: general + 简洁/压缩(一个概念) + 预言力(约束).
测量 = 直接信息论计算 (互信息/条件熵), 不消融、不重跑. 这是 #53 的因果测量
(信息论量), 不是描述性 level 分布 (后者见 idea53-supply-bottleneck-enrichment.py).

核心量 (一个概念: level → 瓶颈判定 的信息通道):
  Y  = 供给侧瓶颈判定信号 (节点 claim+evidence+corrected_claim 命中)
  L  = run 树 level (L1..L4/L5)
  I(L;Y) = H(Y) - H(Y|L)                       总互信息 (bit)
  contribution(ℓ) = P(L=ℓ)·[H(Y) - H(Y|L=ℓ)]   正确加性分解, Σ_ℓ = I(L;Y), 各项 ≥0
    (注意: 不能用 P(lv)·pmi(Y;lv) — pmi 的期望是联合分布, 不满足 Σ P(lv)·pmi = I(L;Y),
     会出负项/份额>100%, 已实测验证. 正确形式是 P(lv) 乘"条件熵差".)
    因果读法 (不消融的"降级贡献"): 若 level ℓ 对 Y 无预测力 (H(Y|L=ℓ)=H(Y)),
    则 contribution(ℓ)=0, I(L;Y) 降级 contribution(ℓ) — 即"降级贡献". 排名 = 哪层
    对瓶颈判定信号贡献最大.
  D claim 直接检验: I(Deep;Y) vs I(Shallow;Y), Deep={L3,L4(,L5)},
  Shallow={L1,L2} — 深层指示符 vs 浅层指示符 各自携带多少瓶颈判定信息.
  I(Deep;Y) = Σ_{ℓ∈Deep} contribution(ℓ) (加性分解的直接推论).

两个 Y (同源自比):
  Y1 = SUPPLY ∧ JUDGE (供给侧资源词 ∧ 瓶颈判定词) — 主信号
  Y2 = D 点名 6 微架构词 (内存带宽/SM频率/发射率/指令吞吐/occupancy/warp) — 精确硬件信号

分源测 (三份 level 口径不同, 不可合并). ③ stage-ablation 另出 L1-L4 口径
(L5=数值核验层, 与 L1-L4 不可比). 节点抽取 100% 复用 base 脚本 (同节点同口径).
"""
import os, json, math, importlib.util
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def _load_base():
    p = os.path.join(HERE, 'idea53-supply-bottleneck-enrichment.py')
    spec = importlib.util.spec_from_file_location('idea53base', p)
    assert spec is not None and spec.loader is not None
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


BASE = _load_base()

# D 点名 6 微架构词 (base.MICRO 里的 key)
D6 = ['内存带宽', 'SM频率/clock/降频', 'issue rate/发射', '指令吞吐', 'occupancy/占用率', 'warp']


def H2(p):
    """二元熵 (bit)."""
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -(p * math.log2(p) + (1 - p) * math.log2(1 - p))


def y1_fn(nd):
    t = BASE.text_of(nd)
    return bool(BASE.SUPPLY.search(t) and BASE.JUDGE.search(t))


def y2_fn(nd):
    t = BASE.text_of(nd)
    return any(BASE.MICRO[k].search(t) for k in D6)


def chi2_2x2(k_hit, n_hit, k_all, n_all):
    """2x2 卡方 (L=ℓ vs 其余): 命中节点落 ℓ 比例 vs 全体. 返回 (chi2, p, df=1)."""
    e11 = n_hit * k_all / n_all
    e12 = n_hit - e11
    e21 = k_all
    e22 = n_all - k_all
    chi = 0.0
    for o, e in [(k_hit, e11), (n_hit - k_hit, e12), (k_all, e21), (n_all - k_all, e22)]:
        if e > 0:
            chi += (o - e) ** 2 / e
    return chi, math.erfc(math.sqrt(chi / 2))


def info_measure(name, nodes, Yfn, label):
    """算 I(L;Y) + 每层 contribution 分解 + 每层显著性. 返回 dict."""
    n = len(nodes)
    if n == 0:
        print(f'  [{label}] 无节点')
        return None
    lv_all = Counter(); y_by_lv = Counter(); y_tot = 0
    for nd in nodes:
        lv = nd['level']; lv_all[lv] += 1
        if Yfn(nd):
            y_tot += 1; y_by_lv[lv] += 1
    p1 = y_tot / n
    Hy = H2(p1)
    levels = sorted(lv_all)
    HyL = 0.0
    per = {}
    for lv in levels:
        nl = lv_all[lv]
        py = y_by_lv.get(lv, 0) / nl          # P(Y=1|L=lv)
        HyL += (nl / n) * H2(py)
        contrib = (nl / n) * (Hy - H2(py))    # contribution(lv), Σ = I(L;Y), ≥0
        chi, p = chi2_2x2(y_by_lv.get(lv, 0), y_tot, lv_all[lv], n)
        per[lv] = dict(n=nl, p_lv=nl / n, p_y_given_lv=py, n_y=y_by_lv.get(lv, 0),
                       contrib=contrib, chi2=chi, p=p)
    I_LY = Hy - HyL
    ssum = sum(v['contrib'] for v in per.values())
    assert abs(ssum - I_LY) < 1e-9, (ssum, I_LY)   # 加性自洽
    for lv in per:
        per[lv]['share'] = per[lv]['contrib'] / I_LY if I_LY > 0 else 0.0
    rank = sorted(per.items(), key=lambda kv: -kv[1]['contrib'])
    top = rank[0]
    print(f'  [{label}] n={n} Y={y_tot} ({p1:.1%})  H(Y)={Hy:.4f} H(Y|L)={HyL:.4f} I(L;Y)={I_LY:.4f} bit')
    print(f'    {"lv":>3} {"n":>5} {"P(lv)":>6} {"P(Y|lv)":>7} {"contrib":>9} {"share":>6} {"chi2":>7} {"p":>9}')
    for lv in levels:
        v = per[lv]
        print(f'    {lv:>3} {v["n"]:5d} {v["p_lv"]:6.1%} {v["p_y_given_lv"]:7.1%} '
              f'{v["contrib"]:9.4f} {v["share"]:6.1%} {v["chi2"]:7.2f} {v["p"]:9.4f}')
    print(f'    贡献最大层: {top[0]} (contrib={top[1]["contrib"]:.4f} bit, share={top[1]["share"]:.0%})')
    return dict(n=n, y=y_tot, p1=p1, Hy=Hy, HyL=HyL, I_LY=I_LY, per=per, top=top[0])


def deep_vs_shallow(name, nodes, Yfn, label, deep_levels=('L3', 'L4')):
    """D claim 直接检验: 深层指示符 vs 浅层指示符 各自携带多少瓶颈判定信息."""
    n = len(nodes)
    if n == 0:
        return None
    deep_set = set(deep_levels)
    n_deep = sum(1 for nd in nodes if nd['level'] in deep_set)
    y_deep = sum(1 for nd in nodes if nd['level'] in deep_set and Yfn(nd))
    n_sh = n - n_deep
    y_tot = sum(1 for nd in nodes if Yfn(nd))
    y_sh = y_tot - y_deep
    p1 = y_tot / n
    Hy = H2(p1)
    pd = y_deep / n_deep if n_deep else 0.0
    ps = y_sh / n_sh if n_sh else 0.0
    I_deep = (n_deep / n) * (Hy - H2(pd))      # = I(Deep;Y) = Σ_{ℓ∈Deep} contrib(ℓ)
    I_sh = (n_sh / n) * (Hy - H2(ps))          # = I(Shallow;Y) = Σ_{ℓ∈Shallow} contrib(ℓ)
    chi, p = chi2_2x2(y_deep, y_tot, n_deep, n)
    winner = 'DEEP' if I_deep > I_sh else ('SHALLOW' if I_sh > I_deep else 'TIE')
    print(f'  [{label}] Deep{deep_levels} vs Shallow: I(Deep;Y)={I_deep:.4f} bit '
          f'(P(Y|deep)={pd:.1%}, n={n_deep})  I(Shallow;Y)={I_sh:.4f} bit '
          f'(P(Y|shallow)={ps:.1%}, n={n_sh})  → {winner} 携带更多瓶颈判定信息 '
          f'(χ²={chi:.2f} p={p:.4f})')
    return dict(deep=list(deep_levels), I_deep=I_deep, I_shallow=I_sh, winner=winner,
                p_y_deep=pd, p_y_shallow=ps, n_deep=n_deep, n_shallow=n_sh, chi2=chi, p=p)


def main():
    print('#53 信息论量 — 深层节点对供给侧瓶颈判定的信息贡献 (I(L;Y) + 每层 contribution 分解)')
    print('不消融、不重跑: 直接从联合分布算互信息/条件熵. 节点抽取复用 base 脚本.')
    results = {}
    for name, nodes in BASE.collect_sources():
        print(f'\n### {name}')
        results[name] = {}
        r1 = info_measure(name, nodes, y1_fn, 'Y1 供给侧∧判定')
        if r1:
            results[name]['Y1'] = r1
        r2 = info_measure(name, nodes, y2_fn, 'Y2 D点名6微架构词')
        if r2:
            results[name]['Y2'] = r2
        d1 = deep_vs_shallow(name, nodes, y1_fn, 'Y1 Deep vs Shallow')
        if d1:
            results[name]['Y1_deep_shallow'] = d1
        d2 = deep_vs_shallow(name, nodes, y2_fn, 'Y2 Deep vs Shallow')
        if d2:
            results[name]['Y2_deep_shallow'] = d2
        # ③ stage-ablation: L1-L4 口径 (L5=数值核验层, 与 L1-L4 不可比)
        if 'L1-L5' in name:
            nodes4 = [nd for nd in nodes if nd['level'] in ('L1', 'L2', 'L3', 'L4')]
            print(f'\n### {name} → L1-L4 口径 (去 L5 数值核验层)')
            results[name + ':L1-L4'] = {}
            r1b = info_measure(name + ':L1-L4', nodes4, y1_fn, 'Y1 供给侧∧判定')
            if r1b:
                results[name + ':L1-L4']['Y1'] = r1b
            r2b = info_measure(name + ':L1-L4', nodes4, y2_fn, 'Y2 D点名6微架构词')
            if r2b:
                results[name + ':L1-L4']['Y2'] = r2b
            d1b = deep_vs_shallow(name + ':L1-L4', nodes4, y1_fn, 'Y1 Deep vs Shallow')
            if d1b:
                results[name + ':L1-L4']['Y1_deep_shallow'] = d1b
            d2b = deep_vs_shallow(name + ':L1-L4', nodes4, y2_fn, 'Y2 Deep vs Shallow')
            if d2b:
                results[name + ':L1-L4']['Y2_deep_shallow'] = d2b

    # 汇总
    print('\n### 汇总 (各源 贡献最大层 + Deep vs Shallow)')
    for name, r in results.items():
        parts = []
        if 'Y1' in r:
            d = r['Y1']
            parts.append(f'Y1: I(L;Y)={d["I_LY"]:.4f} bit, 贡献最大层={d["top"]}')
        if 'Y1_deep_shallow' in r:
            ds = r['Y1_deep_shallow']
            parts.append(f'Deep vs Shallow: I(Deep)={ds["I_deep"]:.4f} vs I(Shallow)={ds["I_shallow"]:.4f} → {ds["winner"]}')
        if 'Y2_deep_shallow' in r:
            ds = r['Y2_deep_shallow']
            parts.append(f'Y2 Deep vs Shallow: I(Deep)={ds["I_deep"]:.4f} vs I(Shallow)={ds["I_shallow"]:.4f} → {ds["winner"]}')
        print(f'  {name}: ' + ' | '.join(parts))
    out = os.path.join(HERE, 'idea53-supply-bottleneck-info.json')
    json.dump(results, open(out, 'w'), ensure_ascii=False, indent=2)
    print(f'\n[written] {out}')


if __name__ == '__main__':
    main()
