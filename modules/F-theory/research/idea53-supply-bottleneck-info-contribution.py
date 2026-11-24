#!/usr/bin/env python3
"""#53 信息论因果测量 — 各层对供给侧瓶颈判定的信息贡献 (2026-11-24, D 指令: 直接计算, 不消融不重跑).

D 2026-11-24: "为啥改 消融法, 直接计算不可以吗" — 本脚本 = 直接信息论计算 (互信息/条件熵),
在现有 pfb run 树数据上算, 不消融 (不删层重测), 不重跑 (不重新生成节点).

核心 claim (#53): 展开的推理树中, 深层节点对"系统瓶颈判定"(供给侧) 的信息贡献更大
(非线性模型下). 本脚本给出该 claim 的因果测量 = 信息论量.

与描述性锚点 (idea53-supply-bottleneck-enrichment.py, commit 0e866871c) 的关系:
  锚点测的是 level 分布 (描述性: 供给侧判定节点落在哪层, 卡方显著性).
  本脚本测的是 信息贡献 (因果/信息论: 知道某节点在 level x, 对"它是不是供给侧瓶颈判定"
  减少多少不确定性, 按层分解). 同一口径 (Y = 供给词 ∧ 判定词), 同三份数据源, 但量不同:
  描述性 = P(Y|level) 富集倍数; 信息论 = I(level; Y) 互信息 + 逐层贡献分解.

信息论量 (全部直接计算, 闭式):
  X = level (L1..L4[,L5]), Y = 供给侧瓶颈判定指示 (SUPPLY∧JUDGE, 二值).
  ① H(Y)                     判定标签的熵 (bits) — 不知道层时, 判定本身的不确定性.
  ② H(Y|X=x)                 条件熵 (bits) — 已知节点在层 x 后, 判定剩余的不确定性.
  ③ H(Y|X) = Σ_x P(x)H(Y|X=x)  总条件熵.
  ④ I(X;Y) = H(Y)-H(Y|X)     互信息 (bits) — 知道层, 对判定减少的总不确定性 (因果信息量).
  ⑤ 逐层贡献 c(x) = P(x)·D_KL(P(Y|X=x) || P(Y))  — 精确分解, Σ_x c(x) = I(X;Y).
     这是"信息贡献排名": 每层贡献多少 bits 关于判定的信息, 谁最大谁就是瓶颈判定层.
  ⑥ 非线性核验: 线性模型 (depth 序数 → Y) 的 Pearson ρ + 高斯线性互信息代理
     I_lin = 0.5·log2(1+ρ²) 与逐层命中率曲线 OLS R²; 非线性间隙 = I(X;Y) - I_lin.
     间隙 > 0 且逐层命中率在深层峰值/饱和 → 关系非线性, 线性模型低估深层贡献.

口径 (承重, 与锚点一致):
  Y = SUPPLY.search(text) ∧ JUDGE.search(text), text = claim+evidence+corrected_claim.
  三份数据源 level 口径不同 (①② L1-L4, ③ L1-L5), 不可合并比倍数, 分源算.
  同族 judge (27b 评 27b) 分数仅相对有效 — 本量是树内相对信息贡献, 绝对 bits 不可跨源比.
"""
import json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import importlib.util
_spec = importlib.util.spec_from_file_location('idea53_anchor',
    os.path.join(HERE, 'idea53-supply-bottleneck-enrichment.py'))
_anchor = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_anchor)

SUPPLY, JUDGE = _anchor.SUPPLY, _anchor.JUDGE
text_of, collect_sources = _anchor.text_of, _anchor.collect_sources

EPS = 1e-12


def b2(x):
    """base-2 log, 0 安全."""
    return math.log2(max(x, EPS))


def bern_entropy(p):
    """Bernoulli 熵 (bits)."""
    if p <= EPS or p >= 1 - EPS:
        return 0.0
    return -(p * b2(p) + (1 - p) * b2(1 - p))


def kl_bern(px, p):
    """D_KL(Bern(px) || Bern(p)) (bits)."""
    if px <= EPS or px >= 1 - EPS:
        return 0.0
    return px * b2(px / p) + (1 - px) * b2((1 - px) / (1 - p))


def pearson(xs, ys):
    n = len(xs)
    mx = sum(xs) / n; my = sum(ys) / n
    cov = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    vx = sum((xs[i] - mx) ** 2 for i in range(n))
    vy = sum((ys[i] - my) ** 2 for i in range(n))
    return cov / math.sqrt(vx * vy) if vx * vy > 0 else 0.0


def ols_r2(xs, ys, ws):
    """加权 OLS 的 R² (逐层命中率 p_x 对 depth 的线性拟合)."""
    W = sum(ws)
    mx = sum(w * x for w, x in zip(ws, xs)) / W
    my = sum(w * y for w, y in zip(ws, ys)) / W
    sxx = sum(w * (x - mx) ** 2 for w, x in zip(ws, xs))
    sxy = sum(w * (x - mx) * (y - my) for w, x, y in zip(ws, xs, ys))
    syy = sum(w * (y - my) ** 2 for w, y in zip(ws, ys))
    if sxx <= 0 or syy <= 0:
        return 0.0
    slope = sxy / sxx
    ss_res = sum(w * (y - (my + slope * (x - mx))) ** 2 for w, x, y in zip(ws, xs, ys))
    return max(0.0, 1.0 - ss_res / syy)


def y1_pred(nd):
    """Y1 = 供给侧资源词 ∧ 瓶颈判定词 (主信号, 与描述性锚点 0e866871c 同口径)."""
    t = text_of(nd)
    return bool(SUPPLY.search(t) and JUDGE.search(t))


# D 2026-11-24 点名 6 微架构词 (base.MICRO 的 key) — 精确硬件供给信号 (Y2, 对照 Y1)
_D6 = ['内存带宽', 'SM频率/clock/降频', 'issue rate/发射', '指令吞吐', 'occupancy/占用率', 'warp']


def y2_pred(nd):
    """Y2 = D 点名 6 微架构词命中 (内存带宽/SM频率/发射率/指令吞吐/occupancy/warp)."""
    t = text_of(nd)
    return any(_anchor.MICRO[k].search(t) for k in _D6)


def info_contribution(nodes, y_pred):
    """对一份数据源算全部信息论量. y_pred: 节点→bool 的判定谓词 (Y1/Y2). 返回 dict."""
    from collections import Counter
    n = len(nodes)
    if n == 0:
        return None
    lv_cnt = Counter(); y_cnt = Counter(); lv_y = Counter()
    for nd in nodes:
        x = nd['level']
        y = 1 if y_pred(nd) else 0
        lv_cnt[x] += 1; y_cnt[y] += 1; lv_y[(x, y)] += 1
    p = y_cnt[1] / n                       # P(Y=1) 基率
    H_Y = bern_entropy(p)                  # ①
    levels = sorted(lv_cnt)
    per = {}
    H_YX = 0.0
    for x in levels:
        Px = lv_cnt[x] / n
        px = lv_y.get((x, 1), 0) / lv_cnt[x]
        Hx = bern_entropy(px)
        kl = kl_bern(px, p)
        c = Px * kl                        # ⑤ 逐层贡献 (对 I(X;Y) 的分解)
        g = H_Y - Hx                       # ⑦ 逐层点信息增益 H(Y)-H(Y|X=x)
        H_YX += Px * Hx
        per[x] = dict(P_x=Px, p_x=px, H_Yx=Hx, KL=kl, contrib=c, gain=g)
    I = H_Y - H_YX                         # ④ 互信息
    for x in per:
        per[x]['frac'] = per[x]['contrib'] / I if I > 0 else 0.0
    # ⑥ 非线性核验
    depth = {x: i + 1 for i, x in enumerate(levels)}
    xs = [depth[x] for x in levels]; ys = [per[x]['p_x'] for x in levels]
    ws = [lv_cnt[x] for x in levels]
    r2_ols = ols_r2(xs, ys, ws)
    # Pearson corr(depth, Y) over all nodes
    d_all = [depth[nd['level']] for nd in nodes]
    y_all = [1 if (SUPPLY.search(text_of(nd)) and JUDGE.search(text_of(nd))) else 0 for nd in nodes]
    rho = pearson(d_all, y_all)
    I_lin = 0.5 * math.log2(1 + rho * rho)  # 高斯线性互信息代理
    # 贡献排名
    ranking = sorted(per, key=lambda x: -per[x]['contrib'])
    max_layer = ranking[0]
    # 深层块贡献 (L4 及更深)
    deep = [x for x in levels if depth[x] >= 4]
    c_deep = sum(per[x]['contrib'] for x in deep)
    return dict(n=n, base_rate=p, H_Y=H_Y, H_YX=H_YX, I=I, per=per,
                r2_ols=r2_ols, rho=rho, I_lin=I_lin, nonlin_gap=I - I_lin,
                ranking=ranking, max_layer=max_layer, deep=deep, c_deep=c_deep,
                levels=levels)


def fmt_src(name, r):
    L = []
    L.append(f'\n### {name} | 节点 {r["n"]} | 判定基率 P(Y=1)={r["base_rate"]:.1%}')
    L.append(f'  H(Y)={r["H_Y"]:.4f} bits   H(Y|X)={r["H_YX"]:.4f} bits   '
             f'I(X;Y)={r["I"]:.4f} bits   [层对判定的总信息量]')
    L.append(f'  逐层贡献 c(x)=P(x)·D_KL(P(Y|x)||P(Y)), Σc(x)=I(X;Y):')
    L.append(f'  {"层":>3s} {"P(x)":>7s} {"P(Y|x)":>8s} {"H(Y|x)":>8s} '
             f'{"c(x)bits":>9s} {"占比":>7s}')
    for x in r['levels']:
        q = r['per'][x]
        L.append(f'  {x:>3s} {q["P_x"]:7.1%} {q["p_x"]:8.1%} {q["H_Yx"]:8.4f} '
                 f'{q["contrib"]:9.4f} {q["frac"]:7.1%}')
    L.append(f'  贡献排名 (c(x)=P(x)·KL, Σc=I): ' + ' > '.join(
        f'{x}({r["per"][x]["contrib"]:.4f}b,{r["per"][x]["frac"]:.0%})' for x in r['ranking']))
    # ⑦ 点信息增益排名 (每层独立, 不被层大小稀释)
    granking = sorted(r['per'], key=lambda x: -r['per'][x]['gain'])
    L.append(f'  点信息增益排名 H(Y)-H(Y|x) [bits, 不被层大小稀释]: ' + ' > '.join(
        f'{x}({r["per"][x]["gain"]:.4f}b)' for x in granking))
    L.append(f'  最大贡献层 (按 c(x) 占比) = {r["max_layer"]} (占 I 的 {r["per"][r["max_layer"]]["frac"]:.0%})'
             f' | 最大点增益层 (按 H(Y)-H(Y|x)) = {granking[0]}')
    L.append(f'  深层块 {"/".join(r["deep"])} 合计 {r["c_deep"]:.4f} bits ({r["c_deep"]/r["I"]:.0%} of I)')
    L.append(f'  非线性核验: 命中率曲线 OLS R²={r["r2_ols"]:.3f} | Pearson ρ(depth,Y)={r["rho"]:.3f} '
             f'| 线性互信息代理 I_lin={r["I_lin"]:.4f} bits | 非线性间隙 I-I_lin={r["nonlin_gap"]:.4f} bits')
    return '\n'.join(L)


def main():
    print('#53 信息论因果测量 — 各层对供给侧瓶颈判定的信息贡献 (直接计算, 不消融不重跑)')
    print('两个 Y: Y1=SUPPLY∧JUDGE (主信号) / Y2=D 点名 6 微架构词 (精确硬件信号).')
    results = {}
    for name, nodes in collect_sources():
        r1 = info_contribution(nodes, y1_pred)
        r2 = info_contribution(nodes, y2_pred)
        if r1 is None:
            print(f'\n### {name}: 无节点'); continue
        results[name] = r1
        print(fmt_src(name + ' [Y1 供给侧∧判定]', r1))
        if r2 is not None:
            results[name + ':Y2'] = r2
            print(fmt_src(name + ' [Y2 D点名6微架构词]', r2))
    # 跨源汇总 (Y1)
    print('\n### 跨源汇总 Y1 (level 口径不同, 分源, 不可合并比倍数)')
    print(f'{"源":>26s} {"I(X;Y)":>8s} {"max层":>5s} {"max占比":>7s} '
          f'{"R²_ols":>7s} {"I-I_lin":>8s} {"非线性?":>8s}')
    for name, r in results.items():
        if name.endswith(':Y2'):
            continue
        nonlin = '是' if (r['nonlin_gap'] > 0.005 and r['r2_ols'] < 0.95) else '弱/否'
        print(f'{name:>26s} {r["I"]:8.4f} {r["max_layer"]:>5s} '
              f'{r["per"][r["max_layer"]]["frac"]:7.0%} {r["r2_ols"]:7.3f} '
              f'{r["nonlin_gap"]:8.4f} {nonlin:>8s}')
    # 落盘
    out = {
        'claim': '#53: 深层节点对供给侧瓶颈判定的信息贡献更大 (非线性模型下)',
        'method': '直接信息论计算 (互信息/条件熵/逐层 KL 贡献分解 c(x)=P(x)·D_KL(P(Y|x)||P(Y)), Σc=I), 不消融不重跑',
        'operationalization': 'Y1 = SUPPLY∧JUDGE (与描述性锚点 0e866871c 同口径); Y2 = D 点名 6 微架构词 (内存带宽/SM频率/发射率/指令吞吐/occupancy/warp)',
        'sources': {},
    }
    for name, r in results.items():
        out['sources'][name] = {
            'n': r['n'], 'base_rate': r['base_rate'], 'H_Y': r['H_Y'],
            'H_YX': r['H_YX'], 'I_XY': r['I'],
            'per_level': {x: {k: r['per'][x][k] for k in
                              ('P_x', 'p_x', 'H_Yx', 'KL', 'contrib', 'frac', 'gain')} for x in r['levels']},
            'ranking': r['ranking'], 'max_contribution_layer': r['max_layer'],
            'max_layer_frac': r['per'][r['max_layer']]['frac'],
            'gain_ranking': sorted(r['per'], key=lambda x: -r['per'][x]['gain']),
            'max_gain_layer': sorted(r['per'], key=lambda x: -r['per'][x]['gain'])[0],
            'deep_block': r['deep'], 'deep_block_contrib': r['c_deep'],
            'r2_ols': r['r2_ols'], 'pearson_rho': r['rho'],
            'I_linear_proxy': r['I_lin'], 'nonlinear_gap': r['nonlin_gap'],
        }
    out_path = os.path.join(HERE, 'idea53-info-contribution-results.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f'\n[落盘] {out_path}')
    return out


if __name__ == '__main__':
    main()
