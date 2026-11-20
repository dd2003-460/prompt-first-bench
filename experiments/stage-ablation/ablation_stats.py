#!/usr/bin/env python3
"""T53b 统计汇总（cc-state work_unit: stats_summary）。

口径（tasks/T53-bus/TASK-T53b-ablation-runs.md 验收标准 3/4/6）：
- 每题每臂 coverage/depth 均值±SE + 95%CI（per-run 聚合，n 以实际为准）
- 标出"特别好的轮次"（coverage 或 depth > 均值+1SE）
- r7 复现：gpu 题 ≥3 轮 l1_uncertainty=true
- 缺口清单：cc-state done 但 results 无记录的 run
- 口径限定：judge 族 qwen3.8-27b ×1, non-IRR；seed=42

用法: python3 ablation_stats.py [--out ablation-stats.md]
"""
import argparse, json, os, math, re, sys
from collections import defaultdict
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "ablation-results.json")
CC_STATE = os.path.join(HERE, "..", "..", "tasks", "T53-bus", "cc-state.json")
QIDS = ["nat", "soc", "gpu"]
ARMS = ["formula", "text"]


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
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(HERE, "ablation-stats.md"))
    args = ap.parse_args()

    d = json.load(open(RESULTS))
    runs = d["runs"]
    # 去重：同 run 多次记录取最新
    best = {}
    for r in runs:
        key = f"{r['qid']}_{r['arm']}_r{r['round']:02d}"
        if key not in best or r.get("timestamp", "") > best[key].get("timestamp", ""):
            best[key] = r

    # 缺口：cc-state done 但 results 无
    missing = []
    if os.path.exists(CC_STATE):
        s = json.load(open(CC_STATE))
        pat = re.compile(r"^(nat|soc|gpu)_(formula|text)_r(\d{2})$")
        for wu in s["work_units"]:
            if not wu.get("done"):
                continue
            m = pat.match(wu.get("name", ""))
            if not m:
                continue
            key = f"{m.group(1)}_{m.group(2)}_r{m.group(3)}"
            if key not in best:
                missing.append(key)

    lines = []
    lines.append("# T53b 统计汇总")
    lines.append("")
    lines.append(f"生成: {datetime.now(timezone.utc).astimezone().isoformat(timespec='seconds')}")
    lines.append(f"口径: per-run 聚合 | judge 族 qwen3.8-27b ×1 (non-IRR) | seed=42")
    lines.append(f"已记录 run: {len(best)} / 60 | 缺口: {len(missing)}")
    lines.append("")

    # 每题每臂统计
    for qid in QIDS:
        lines.append(f"## {qid}")
        lines.append("")
        lines.append("| 臂 | n | coverage mean±SE | 95%CI | depth mean±SE | 95%CI | 高轮次(cov/depth>mean+1SE) |")
        lines.append("|---|---|---|---|---|---|---|")
        for arm in ARMS:
            rs = [best[f"{qid}_{arm}_r{i:02d}"] for i in range(1, 11)
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
    for qid in QIDS:
        row = {}
        for arm in ARMS:
            rs = [best[f"{qid}_{arm}_r{i:02d}"] for i in range(1, 11)
                  if f"{qid}_{arm}_r{i:02d}" in best]
            covs = [r["coverage"] for r in rs if r.get("coverage") is not None]
            deps = [r["depth"] for r in rs if r.get("depth") is not None]
            row[arm] = (len(rs),
                        sum(covs) / len(covs) if covs else None,
                        sum(deps) / len(deps) if deps else None)
        (nf, cf, df_), (nt, ct, dt_) = row["formula"], row["text"]
        if cf is not None and ct is not None:
            dc, dd = cf - ct, (df_ - dt_) if (df_ is not None and dt_ is not None) else float("nan")
            lines.append(
                f"| {qid} | {nf} | {nt} | {dc:+.3f} | {dd:+.3f} "
                f"| {'formula 优' if dc > 0 else ('text 优' if dc < 0 else '平')} |")
        else:
            lines.append(f"| {qid} | {nf} | {nt} | — | — | 数据不足 |")
    lines.append("")
    lines.append("注: 跨题绝对 coverage/depth 不可直接比较（rubric 粒度差异），上表 Δ 才是消融结论口径。")
    lines.append("")

    # r7 复现检查
    gpu_l1 = [i for i in range(1, 11)
              if f"gpu_formula_r{i:02d}" in best and best[f"gpu_formula_r{i:02d}"].get("l1_uncertainty")]
    gpu_l1_none = [i for i in range(1, 11)
                   if f"gpu_formula_r{i:02d}" in best and best[f"gpu_formula_r{i:02d}"].get("l1_uncertainty") is None]
    lines.append("## r7 复现（gpu 题 L1 不确定性维度）")
    lines.append(f"l1_uncertainty=true 的轮次: {len(gpu_l1)}/10 {gpu_l1}")
    lines.append(f"判据: ≥3 轮 → {'PASS' if len(gpu_l1) >= 3 else 'FAIL/待数据'}")
    lines.append("注: 11-20 13:27 前的 run 由旧 l1 检测逻辑（glob 旧单文件 ckpt + 读不存在的 scope 字段）生成，"
                 "且树形 ckpt 已被 driver rm -rf，无法用新判据（claim 双关键词）复验——"
                 "旧 run 的 l1 值仅作历史参考，r7 结论以修复后新 run 为准。"
                 + (f" l1=None（无数据）的轮次: {gpu_l1_none}" if gpu_l1_none else ""))
    lines.append("")

    if missing:
        lines.append("## 缺口（cc-state done 但 results 无记录）")
        lines.append("")
        for k in missing:
            lines.append(f"- {k}")
        lines.append("")

    out = "\n".join(lines)
    print(out)
    with open(args.out, "w") as f:
        f.write(out + "\n")
    print(f"\n[written] {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
