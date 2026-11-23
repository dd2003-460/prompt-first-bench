#!/usr/bin/env python3
"""rep_scan 下游分析：K7 r1-r3 + rep r4-r8 合并 → 每档 depth mean/sd/CI + peak 定位 + 显著性。

口径（对齐 workshop §4.3）：
- 主指标 = depth 轴（不受 cov magnet patch 影响，old/new 可合并）。
- peak 位置 = argmax(每档 mean depth)。
- 显著性主口径 = run-sd（peak 高出 plateau 几个 run-sd，§4.3 现口径）；
  辅口径 = Welch t（正态近似 p，n 小时仅作参考，不强求）。
- 敏感性：realized n_nodes 作为 x 轴（§4.3 caveat：soft cap 档位重叠，
  depth 峰可能归因于 realized nodes 而非 budget 参数）。

用法：
  python3 rep_scan_analyze.py            # 读 K7 + rep-scan-scores(若存在)
  python3 rep_scan_analyze.py --dry      # 只用 K7 验证管线（rep 未落地时）
数据落地后重跑即出 §4.3 可填数字。
"""
import sys, json, math, statistics, glob, os

PFB = '/Users/a1-6/Desktop/workspace/pfb'
# era-matched 单一源: 全用 frozen judge 重算 (机械 depth)。
# 旧源 results-budget-scan.json 的 K7 depth 是 LLM judge_v2_depth (self-biased),
# 与 rep-scan 的机械 depth 混表会产生假 peak (见 T-JUDGE-1-depth-axis-provenance-20261123.md)。
# 文件名不带计数 (11-23 改): rep 落地一棵加一棵, 计数会过期。
ERA = f'{PFB}/modules/B-pipeline-ablation/data/rep-scan/era-matched.json'


def load_era():
    """era-matched (frozen judge 机械 depth)。r7/r8 落地后重算此文件再加。"""
    if not os.path.exists(ERA):
        return []
    rows = []
    for r in json.load(open(ERA)):
        rows.append({'budget': r['budget'], 'rep': r['rep'],
                     'n_nodes': r['n_nodes'], 'depth': r['depth']})
    return rows


def welch_t(a, b):
    """Welch t + 正态近似 p（n 小仅作参考）。"""
    na, nb = len(a), len(b)
    ma, mb = statistics.mean(a), statistics.mean(b)
    va, vb = statistics.variance(a), statistics.variance(b)
    se = math.sqrt(va/na + vb/nb)
    if se == 0:
        return 0.0, 1.0
    t = (ma - mb) / se
    p = math.erfc(abs(t) / math.sqrt(2))  # 正态近似双侧 p
    return t, p


def main():
    rows = load_era()
    src = f'era-matched (frozen judge, 机械 depth; {len(rows)} rows)'
    print(f'=== rep_scan 分析 · {src} ===\n')

    by_budget = {}
    for r in rows:
        by_budget.setdefault(r['budget'], []).append(r)

    # 每档 depth 统计
    print(f'{"budget":>7s} {"n":>3s} {"depth_mean":>10s} {"sd":>7s} {"95%CI":>18s} {"nodes_mean":>11s}')
    stats = {}
    for b in sorted(by_budget):
        d = [r['depth'] for r in by_budget[b]]
        nn = [r['n_nodes'] for r in by_budget[b]]
        m = statistics.mean(d)
        sd = statistics.stdev(d) if len(d) > 1 else 0.0
        # 95% CI：n>3 用 t 近似（t_0.975, df=n-1），小 n 表
        tcrit = {2: 12.706, 3: 4.303, 4: 3.182, 5: 2.776, 6: 2.571, 7: 2.447, 8: 2.365, 9: 2.262, 10: 2.201}
        tc = tcrit.get(len(d), 1.96)
        half = tc * sd / math.sqrt(len(d)) if len(d) > 1 else 0.0
        stats[b] = (m, sd, half, statistics.mean(nn))
        ci = f'[{m-half:.4f},{m+half:.4f}]'
        print(f'{b:>7d} {len(d):>3d} {m:>10.4f} {sd:>7.4f} {ci:>18s} {statistics.mean(nn):>11.0f}')

    # peak 定位
    peak_b = max(stats, key=lambda b: stats[b][0])
    peak_m = stats[peak_b][0]
    # plateau = 非 peak 的中间档（100/300/719，端点 50 趋势已明确）
    plateau_b = [b for b in stats if b != peak_b and b != 50]
    plateau_vals = [r['depth'] for b in plateau_b for r in by_budget[b]]
    run_sd = statistics.stdev([r['depth'] for b in stats for r in by_budget[b]])
    plateau_m = statistics.mean(plateau_vals) if plateau_vals else 0.0
    gap_sd = (peak_m - plateau_m) / run_sd if run_sd else 0.0
    t, p = welch_t([r['depth'] for r in by_budget[peak_b]], plateau_vals)

    print(f'\n=== peak 定位 ===')
    print(f'peak budget = {peak_b} (depth {peak_m:.4f})')
    print(f'plateau (非peak非50) mean = {plateau_m:.4f}, run-sd = {run_sd:.4f}')
    print(f'peak 高出 plateau = {gap_sd:+.2f} run-sd  (n/peak={len(by_budget[peak_b])}, n/plateau={len(plateau_vals)})')
    print(f'Welch t = {t:+.3f}, 正态近似 p = {p:.4f}  (n 小时参考, 非强结论)')
    print(f'口径: §4.3 主口径 = run-sd; |gap|<1 run-sd → suggestive, 非显著。')

    # 敏感性：realized n_nodes 与 depth 的关系（峰是否只是 nodes 多）
    all_nn = [r['n_nodes'] for r in rows]
    all_d = [r['depth'] for r in rows]
    if len(rows) > 2:
        mx, my = statistics.mean(all_nn), statistics.mean(all_d)
        cov = sum((x-mx)*(y-my) for x, y in zip(all_nn, all_d))
        vx = sum((x-mx)**2 for x in all_nn)
        r_nodes = cov / math.sqrt(vx * sum((y-my)**2 for y in all_d)) if vx else 0
        print(f'\n=== 敏感性 (realized n_nodes) ===')
        print(f'depth ~ n_nodes 相关 r = {r_nodes:+.3f} (n={len(rows)})')
        print(f'解读: r 高 → depth 峰可能归因于 realized nodes 而非 budget 参数 (§4.3 caveat)。')


if __name__ == '__main__':
    main()
