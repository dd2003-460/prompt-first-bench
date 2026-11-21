#!/usr/bin/env python3
"""T53b 统计汇总（cc-state work_unit: stats_summary）。

口径（tasks/T53-bus/TASK-T53b-ablation-runs.md 验收标准 3/4/6）：
- 每题每臂 coverage/depth 均值±SE + 95%CI（per-run 聚合，n 以实际为准）
- 标出"特别好的轮次"（coverage 或 depth > 均值+1SE）
- r7 复现：gpu 题 ≥3 轮 l1_uncertainty=true
- 缺口清单：cc-state done 但 results 无记录的 run
- 口径限定：judge 族 qwen3.8-27b ×1, non-IRR；seed=42

用法: python3 ablation_stats.py [--out ablation-stats.md]

机判边界（SOP verification-sop.md §6）：
- 能验：coverage/depth 数值复算（mean/SE/95%CI 从 run 文件重算）、
  (qid,arm) 分组、同题内 Δ 口径、缺口/blocked 对账（done 但无数据）。
- 不能验：judge 打分本身是否正确（语义级重判需异族 judge 或人工）、
  coverage/depth 是否真反映 rubric 构念效度（相对 qwen3.8-27b 单 judge，
  non-IRR，同族无隔离价值——见 §2）、统计显著性（n<8 时本脚本只报
  点估计+区间+功效不足，不打方向/显著标签，见 §3）。
"""
import argparse, json, os, math, re, sys
from collections import defaultdict
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))

# ── spec 驱动（--spec <name>）：实验形状（qids/arms/rounds/cc-state/seed）从 spec 读 ──
# 无 --spec 时回退 T53b 默认值（向后兼容：无参运行输出与改造前逐字节一致）。
T53B_DEFAULTS = {
    "results": os.path.join(HERE, "..", "..", "modules/B-pipeline-ablation/data/t53b", "results.json"),
    "cc_state": os.path.join(HERE, "..", "..", "tasks", "T53-bus", "cc-state.json"),
    "runs_dir": os.path.join(HERE, "..", "..", "modules/B-pipeline-ablation/data/t53b", "runs"),
    "qids": ["nat", "soc", "gpu"],
    "arms": ["formula", "text"],
    "rounds": list(range(1, 11)),
    "seed": 42,
    # r7 复现检查（T53b 任务书验收项 6）：gpu 题 formula 臂 l1_uncertainty ≥3 轮。
    # 其他实验无此项 → spec 不带 r7 字段则跳过该节。
    "r7": {"qid": "gpu", "arm": "formula", "min_rounds": 3},
}


def load_spec(name):
    """读 spec/<name>.json，合并出统计所需形状参数；缺字段用 T53b 默认。
    spec 的 output.* 路径是相对 repo root（与 driver/batch 的 cd 基准一致）。"""
    p = name if name.endswith(".json") else os.path.join(HERE, "spec", f"{name}.json")
    s = json.load(open(p))
    cfg = dict(T53B_DEFAULTS)
    out = s.get("output", {})
    repo_root = os.path.join(HERE, "..", "..")
    cfg["results"] = os.path.normpath(os.path.join(repo_root, out.get("results", "modules/B-pipeline-ablation/data/t53b/results.json")))
    cfg["runs_dir"] = os.path.normpath(os.path.join(repo_root, out.get("runs_dir", "modules/B-pipeline-ablation/data/t53b/runs")))
    cfg["cc_state"] = os.path.normpath(os.path.join(repo_root, s["cc_state"]))
    cfg["qids"] = s["qids"]
    cfg["arms"] = list(s["arms"].keys())
    cfg["rounds"] = s["rounds"]
    cfg["seed"] = s.get("seed", 42)
    cfg["r7"] = s.get("r7")  # None → 跳过 r7 节
    return cfg


def se(vals):
    n = len(vals)
    if n < 2:
        return float("nan")
    m = sum(vals) / n
    return math.sqrt(sum((v - m) ** 2 for v in vals) / (n - 1)) / math.sqrt(n)


def ci95(vals):
    n = len(vals)
    if n < 2:
        return (float("nan"), float("nan"))
    m = sum(vals) / n
    # t 分布临界值（df=n-1, 双侧 0.05）——n≤15 用查表值，n>15 用 1.96
    t_tab = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447,
             7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179,
             13: 2.160, 14: 2.145, 15: 2.131}
    t = t_tab.get(n - 1, 1.96)
    half = t * se(vals)
    return (m - half, m + half)


def main():
    ap = argparse.ArgumentParser(description="消融实验统计（spec 驱动，--spec 缺省回退 T53b）")
    ap.add_argument("--out", default=None, help="输出 md 路径（缺省=<results 同目录>/ablation-stats.md）")
    ap.add_argument("--spec", default=None, help="spec 名（spec/<name>.json）或完整路径；缺省=T53b 默认")
    args = ap.parse_args()

    if args.spec:
        cfg = load_spec(args.spec)
    else:
        cfg = dict(T53B_DEFAULTS)
    results_path = cfg["results"]
    cc_state = cfg["cc_state"]
    runs_dir = cfg["runs_dir"]
    qids = cfg["qids"]
    arms = cfg["arms"]
    rounds = cfg["rounds"]
    seed = cfg["seed"]
    r7 = cfg["r7"]
    out_path = args.out or os.path.join(os.path.dirname(results_path), "ablation-stats.md")

    d = json.load(open(results_path))
    runs = d["runs"]
    # 去重：同 run 多次记录取最新
    best = {}
    for r in runs:
        key = f"{r['qid']}_{r['arm']}_r{r['round']:02d}"
        if key not in best or r.get("timestamp", "") > best[key].get("timestamp", ""):
            best[key] = r

    # 2026-11-20 口径修正（verification-sop §8）：cc-state done 是权威账本。
    # results 里可能有残留（cc-state 未标 done 的旧记录，如 11-19 作废 run），
    # 直接数 results 会多算；done 但无数据工件的（空 done）不得计入统计。
    done_set = set()
    blocked = []
    s = None
    # run 名正则由 qids/arms 导出（与 driver/batch 的 spec 解析同源）
    pat = re.compile("^(" + "|".join(qids) + ")_(" + "|".join(arms) + ")_r(\\d{2})$")
    if os.path.exists(cc_state):
        s = json.load(open(cc_state))
        for wu in s["work_units"]:
            if not wu.get("done"):
                continue
            m = pat.match(wu.get("name", ""))
            if m:
                done_set.add(f"{m.group(1)}_{m.group(2)}_r{m.group(3)}")

    # 残留：results 有但 cc-state 未标 done（旧作废数据，剔除）
    stale = [k for k in best if done_set and k not in done_set]
    # 空 done：cc-state done 但 results 无记录
    missing = [k for k in done_set if k not in best]
    # blocked 第三态：空 done 中 cc-state 标了 blocked 的（卡死跳过，非完成）
    if done_set and s is not None:
        _blocked_names = set()
        for wu in s["work_units"]:
            if not (wu.get("done") and wu.get("blocked")):
                continue
            m = pat.match(wu.get("name", ""))
            if m:
                _blocked_names.add(f"{m.group(1)}_{m.group(2)}_r{m.group(3)}")
        blocked = [k for k in missing if k in _blocked_names]
        missing = [k for k in missing if k not in blocked]
    # 统计口径：仅 done 且有 results 记录的 run
    if done_set:
        best = {k: v for k, v in best.items() if k in done_set}
    # 无数据工件剔除（verification-sop §8）：results 有记录但 judge 文件不存在
    # 的 run，其 coverage/depth 是占位符（非真分数），不得计入统计均值。
    no_artifact = []
    if best:
        for k in list(best):
            jf = os.path.join(runs_dir, f"{k}_judge.json")
            if not os.path.exists(jf):
                no_artifact.append(k)
                del best[k]

    lines = []
    lines.append("# T53b 统计汇总")
    lines.append("")
    lines.append(f"生成: {datetime.now(timezone.utc).astimezone().isoformat(timespec='seconds')}")
    lines.append(f"口径: per-run 聚合 | judge 族 qwen3.8-27b ×1 (non-IRR) | seed={seed}")
    # SOP verification-sop.md §4 口径限定：tie-break + gold 参照系
    lines.append("口径限定: tie-break 无（coverage/depth 为连续比例，非排名）| "
                 "gold 参照系: rubric gold points（相对该 rubric，非绝对构念效度）")
    lines.append(f"已记录 run: {len(best)} / {len(qids) * len(arms) * len(rounds)} | 缺口(空done): {len(missing)} | blocked: {len(blocked)} | 残留剔除: {len(stale)} | 无judge剔除: {len(no_artifact)}")
    lines.append("")

    # 每题每臂统计
    for qid in qids:
        lines.append(f"## {qid}")
        lines.append("")
        lines.append("| 臂 | n | coverage mean±SE | 95%CI | depth mean±SE | 95%CI | 高轮次(cov/depth>mean+1SE) |")
        lines.append("|---|---|---|---|---|---|---|")
        for arm in arms:
            rs = [best[f"{qid}_{arm}_r{i:02d}"] for i in rounds
                  if f"{qid}_{arm}_r{i:02d}" in best]
            if not rs:
                lines.append(f"| {arm} | 0 | — | — | — | — | — |")
                continue
            covs = [r["coverage"] for r in rs if r.get("coverage") is not None]
            deps = [r["depth"] for r in rs if r.get("depth") is not None]
            cm, cs = sum(covs) / len(covs), se(covs)
            dm, ds = sum(deps) / len(deps), se(deps)
            cl, ch = ci95(covs)
            dl, dh = ci95(deps)
            hi = []
            for r in rs:
                if r.get("coverage") is not None and cm + cs < float("inf") and r["coverage"] > cm + cs:
                    hi.append(f"r{r['round']:02d}c")
                if r.get("depth") is not None and dm + ds < float("inf") and r["depth"] > dm + ds:
                    hi.append(f"r{r['round']:02d}d")
            lines.append(
                f"| {arm} | {len(rs)} | {cm:.3f}±{cs:.3f} | [{cl:.3f},{ch:.3f}] "
                f"| {dm:.3f}±{ds:.3f} | [{dl:.3f},{dh:.3f}] | {','.join(hi) or '—'} |")
        lines.append("")

    # 消融主口径：同题内 formula vs text 差值（跨题绝对值不可比——
    # rubric 粒度不同: nat 6pt/19层, soc 7pt/24层, gpu 38pt/122层,
    # 细粒度子项多 → overall 天然偏低）
    lines.append("## 消融对比（主口径：同题内 Δ = formula − text）")
    lines.append("")
    lines.append("| 题 | n_f | n_t | Δcoverage | Δdepth | 方向 |")
    lines.append("|---|---|---|---|---|---|")
    for qid in qids:
        row = {}
        for arm in arms:
            rs = [best[f"{qid}_{arm}_r{i:02d}"] for i in rounds
                  if f"{qid}_{arm}_r{i:02d}" in best]
            covs = [r["coverage"] for r in rs if r.get("coverage") is not None]
            deps = [r["depth"] for r in rs if r.get("depth") is not None]
            row[arm] = (len(rs),
                        sum(covs) / len(covs) if covs else None,
                        sum(deps) / len(deps) if deps else None)
        # Δ 口径 = arms[0] − arms[1]（T53b: formula − text，与任务书一致）
        a0, a1 = arms[0], arms[1]
        (nf, cf, df_), (nt, ct, dt_) = row[a0], row[a1]
        if cf is not None and ct is not None:
            dc, dd = cf - ct, (df_ - dt_) if (df_ is not None and dt_ is not None) else float("nan")
            # SOP verification-sop.md §3: n<8 禁方向/显著标签（n=3 bootstrap CI 退化，
            # 精确符号检验最小双侧 p=0.25）——只报点估计+区间+功效不足声明
            if min(nf, nt) < 8:
                verdict = f"功效不足（n_f={nf}, n_t={nt}）"
            else:
                verdict = f"{a0} 优" if dc > 0 else (f"{a1} 优" if dc < 0 else "平")
            lines.append(
                f"| {qid} | {nf} | {nt} | {dc:+.3f} | {dd:+.3f} | {verdict} |")
        else:
            lines.append(f"| {qid} | {nf} | {nt} | — | — | 数据不足 |")
    lines.append("")
    lines.append("注: 跨题绝对 coverage/depth 不可直接比较（rubric 粒度差异），上表 Δ 才是消融结论口径。")
    lines.append("")

    # r7 复现检查（spec 带 r7 字段才输出；T53b 默认带）
    if r7:
        rq, ra, rmin = r7["qid"], r7["arm"], r7.get("min_rounds", 3)
        r7_key = lambda i: f"{rq}_{ra}_r{i:02d}"
        r7_hits = [i for i in rounds if r7_key(i) in best and best[r7_key(i)].get("l1_uncertainty")]
        r7_none = [i for i in rounds if r7_key(i) in best and best[r7_key(i)].get("l1_uncertainty") is None]
        lines.append(f"## r7 复现（{rq} 题 L1 不确定性维度）")
        lines.append(f"l1_uncertainty=true 的轮次: {len(r7_hits)}/{len(rounds)} {r7_hits}")
        lines.append(f"判据: ≥{rmin} 轮 → {'PASS' if len(r7_hits) >= rmin else 'FAIL/待数据'}")
        lines.append("注: 11-20 13:27 前的 run 由旧 l1 检测逻辑（glob 旧单文件 ckpt + 读不存在的 scope 字段）生成，"
                     "且树形 ckpt 已被 driver rm -rf，无法用新判据（claim 双关键词）复验——"
                     "旧 run 的 l1 值仅作历史参考，r7 结论以修复后新 run 为准。"
                     + (f" l1=None（无数据）的轮次: {r7_none}" if r7_none else ""))
        lines.append("")

    if missing:
        lines.append("## 缺口（cc-state done 但 results 无记录）")
        lines.append("")
        for k in missing:
            lines.append(f"- {k}")
        lines.append("")

    if blocked:
        lines.append("## blocked（卡死跳过，非完成——不计入 62/62 完成数）")
        lines.append("")
        for k in blocked:
            lines.append(f"- {k}")
        lines.append("")

    out = "\n".join(lines)
    print(out)
    with open(out_path, "w") as f:
        f.write(out + "\n")
    print(f"\n[written] {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
