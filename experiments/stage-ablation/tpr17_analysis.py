#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T-PR-17 T5 分析脚本（纯统计，零 LLM 调用）。

消费 T4 cell JSON（{arm}_{ckpt}_r{rep}.json），产出臂间差分 + bootstrap CI +
Welch/MWU + TOST 等效性检验（F2b 1/2/3 + F5 + 设计笔记 T5 depth 修复）。

用法:
  python3 tpr17_analysis.py [--out DATA_ROOT] [--config CONFIG_PATH]

关键设计（防 p-hacking）:
- Δ_min（等效性检验的最小重要效应）在 T4 数据出来**之前**预设并落盘 config，
  本脚本只读 config，不改。看到数据后调 Δ_min = 检验无效。
- 两个估计量分开报（F2b 1）:
  * operational total effect = verify-off vs canonical（质量+token+tool 一起变，
    方向性假设："能否简化 pipeline 省预算"）
  * sequence-mechanism effect = null-control vs canonical（纯位置扰动 X；
    等效性检验："序列只是搬运工?" = D 收敛假说直接检验）
- checkpoint 分开统计（Handoff Tax: 效应随方向反转，不混池），
  外加跨 checkpoint 方向一致性检查。
- T5 depth 修复: 用 final_tree 重算 depth，repaired_depth = max(chain_depth, level)
  （gap 节点 parent_ids 丢失压低链深，level 字段完好 → 下界修复）。
"""
import argparse
import glob
import json
import os
import sys
from datetime import datetime

DATA_ROOT = "/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation/data/tpr17"
ARMS = ["canonical", "verify-off", "null-control"]
CHECKPOINTS = ["r1", "r2", "r3"]

# 主指标（cell JSON 里的 key）+ 每指标 Δ_min 预设依据
METRICS = {
    "depth": 0.1,              # K7 同序列同预算 run 间 depth 方差 ~0.1（设计文档 F3 实证反证）
    "verified_ratio": 0.1,     # judge/verify LLM 噪声 ~0.1（F5）
    "parent_link_accuracy": 0.05,  # 结构性指标，取 judge 噪声一半（更严的等效声明）
    "failure_rate": 0.1,       # 同上
    "n_nodes": 20,             # ~5% of 381；K7 同序列 run 间节点数差 ~1，跨臂漂移留 5%
    "duplicate_nodes": 2,      # 计数指标，2 个重复 = 实践重要
    "missing_link_nodes": 2,   # 同上
}
# token/tool/evidence 不做等效性检验（operational 方向性指标，F2b 2）
OPERATIONAL_METRICS = ["tokens_total", "tool_calls", "evidence_delta_chars"]


def load_config(path):
    """读预设 Δ_min config（T4 前锁定）。缺失时报错退出——不允许无预设跑分析。"""
    if not os.path.exists(path):
        sys.exit(f"[analysis] FATAL: 预设 config 不存在 {path}——Δ_min 必须在 T4 数据前锁定")
    cfg = json.load(open(path))
    assert "delta_min" in cfg and "prespecified_at" in cfg, "config 缺 delta_min/prespecified_at"
    return cfg


def load_cells(out_root):
    """读 T4 cell JSON → {(arm, ckpt, rep): metrics_dict}。
    校验: 每 cell 有 final_tree（T5 depth 修复需要）+ arm/rep 字段齐全。"""
    cells = {}
    problems = []
    for f in sorted(glob.glob(os.path.join(out_root, "*_r*_r*.json"))):
        base = os.path.basename(f)[:-5]  # strip .json
        # 文件名 {arm}_{ckpt}_r{rep}，arm 含 '-'（verify-off/null-control）→ 从右侧切
        parts = base.rsplit("_r", 1)
        if len(parts) != 2:
            problems.append(f"{base}: 文件名格式不符")
            continue
        stem, rep_s = parts
        arm = None
        for a in ARMS:
            if stem.startswith(a + "_"):
                arm = a
                stem = stem[len(a) + 1:]
                break
        if arm is None:
            problems.append(f"{base}: 无法识别 arm")
            continue
        ckpt = stem
        try:
            rep = int(rep_s)
        except ValueError:
            problems.append(f"{base}: rep 非整数")
            continue
        d = json.load(open(f))
        if "final_tree" not in d:
            problems.append(f"{base}: 缺 final_tree（旧 runner 产物? 需重跑或补 dump）")
        cells[(arm, ckpt, rep)] = d
    return cells, problems


def repaired_depth(tree):
    """T5 修复后 depth: 每节点 depth = max(parent 链深, level)。
    gap 节点 parent_ids 丢失 → 链深被压低；level 字段完好（L{k} 节点真实深度 >= k），
    取 max 作下界修复（设计笔记 T5 分析约束）。返回 (max_repaired_depth, per_node dict)。"""
    id2n = {n["id"]: n for n in tree}

    def chain_depth(nid, seen=None):
        if seen is None:
            seen = set()
        if nid in seen:
            return 0
        seen.add(nid)
        n = id2n.get(nid)
        if n is None:
            return 1
        pids = [p for p in (n.get("parent_ids") or []) if p in id2n]
        if not pids:
            return 1
        return 1 + max(chain_depth(p, seen) for p in pids)

    per = {}
    for n in tree:
        lv = int(str(n["level"]).lstrip("L"))
        per[n["id"]] = max(chain_depth(n["id"]), lv)
    return max(per.values(), default=0), per


# ── 统计原语 ─────────────────────────────────────────────
def _welch(a, b):
    """Welch t-test（不等方差）。返回 (t, p, cohens_d)。"""
    from scipy import stats
    if len(a) < 2 or len(b) < 2:
        return None, None, None
    t, p = stats.ttest_ind(a, b, equal_var=False)
    na, nb = len(a), len(b)
    va, vb = max(var(a), 1e-12), max(var(b), 1e-12)
    sp = ((na - 1) * va + (nb - 1) * vb) / (na + nb - 2)
    # 零/近零方差: Cohen's d 未定义（sp→0 时 d 爆炸）→ 报 None
    d = (mean(a) - mean(b)) / (sp ** 0.5) if sp > 1e-9 else None
    return float(t), float(p), d


def _mwu(a, b):
    """Mann-Whitney U（非参数稳健对照）。返回 (U, p)。"""
    from scipy import stats
    if len(a) < 2 or len(b) < 2:
        return None, None
    u, p = stats.mannwhitneyu(a, b, alternative="two-sided")
    return float(u), float(p)


def _bootstrap_ci(diff, n_boot=2000, seed=42):
    """配对差分（同 rep 配对）的 bootstrap 95% CI。
    diff: list of (a_i - b_i) per rep。返回 (lo, hi, mean_diff)。"""
    import random
    rng = random.Random(seed)
    n = len(diff)
    if n < 2:
        return (None, None, sum(diff) / n if diff else None)
    means = []
    for _ in range(n_boot):
        s = [diff[rng.randrange(n)] for _ in range(n)]
        means.append(sum(s) / n)
    means.sort()
    return means[int(0.025 * n_boot)], means[min(int(0.975 * n_boot), n_boot - 1)], sum(diff) / n


def _tost(a, b, delta_min):
    """TOST 双单侧检验（等效性）。H0: |μa-μb| >= Δ_min。
    返回 dict: equivalent(bool), p_low, p_high, ci95, delta_min。
    等效 ⟺ 95% CI 完全落在 (-Δ_min, +Δ_min) 内。"""
    from scipy import stats
    na, nb = len(a), len(b)
    if na < 2 or nb < 2:
        return {"equivalent": None, "p_low": None, "p_high": None,
                "ci95": None, "delta_min": delta_min}
    _t, _p, _d = _welch(a, b)
    # 单侧: H0 μa-μb <= -Δ vs H1 > -Δ（下界）
    se = (var(a) / na + var(b) / nb) ** 0.5
    diff = mean(a) - mean(b)
    if se < 1e-12:
        # 零方差（常数数据）: CI 退化为点。|diff|<Δ_min ⟹ 等效
        return {"equivalent": abs(diff) < delta_min, "p_low": None, "p_high": None,
                "ci95": (diff, diff, diff), "delta_min": delta_min,
                "note": "zero-variance: CI 退化为点"}
    df = (var(a) / na + var(b) / nb) ** 2 / (
        (var(a) / na) ** 2 / (na - 1) + (var(b) / nb) ** 2 / (nb - 1))
    t_lo = (diff + delta_min) / se
    t_hi = (diff - delta_min) / se
    p_low = float(stats.t.sf(t_lo, df))   # P(μa-μb <= -Δ)
    p_high = float(stats.t.cdf(t_hi, df))  # P(μa-μb >= +Δ)
    ci = _bootstrap_ci([x - y for x, y in zip(a, b)])
    equiv = (ci[0] is not None and -delta_min < ci[0] and ci[1] < delta_min)
    return {"equivalent": equiv, "p_low": p_low, "p_high": p_high,
            "ci95": ci, "delta_min": delta_min}


def mean(x):
    return sum(x) / len(x) if x else 0.0


def var(x):
    if len(x) < 2:
        return 0.0
    m = mean(x)
    return sum((v - m) ** 2 for v in x) / (len(x) - 1)


def _col(cells, arm, ckpt, key):
    """某 arm×ckpt 下各 rep 的某指标列（按 rep 排序，用于配对）。"""
    reps = sorted(rep for (a, c, rep) in cells if a == arm and c == ckpt)
    return [cells[(arm, ckpt, r)].get(key) for r in reps], reps


def _col_repaired_depth(cells, arm, ckpt):
    """从 final_tree 重算 T5 修复后 depth（各 rep）。"""
    reps = sorted(rep for (a, c, rep) in cells if a == arm and c == ckpt)
    vals = []
    for r in reps:
        d = cells[(arm, ckpt, r)]
        tree = d.get("final_tree")
        vals.append(repaired_depth(tree)[0] if tree else None)
    return vals, reps


def compare(cells, ckpt, cfg):
    """单 checkpoint 的两估计量比较。返回 dict。"""
    dm = cfg["delta_min"]
    out = {"checkpoint": ckpt, "operational_total_effect": {}, "sequence_mechanism_effect": {}}
    # 各指标取值（含 T5 修复 depth）
    def grab(arm, key):
        if key == "depth_repaired":
            return _col_repaired_depth(cells, arm, ckpt)[0]
        return _col(cells, arm, ckpt, key)[0]

    for key in list(METRICS.keys()) + ["depth_repaired"]:
        a_can = grab("canonical", key)
        a_voff = grab("verify-off", key)
        a_null = grab("null-control", key)
        # operational: verify-off vs canonical（方向性）
        if a_can and a_voff and min(len(a_can), len(a_voff)) >= 2:
            t, p, d = _welch(a_voff, a_can)
            u, pu = _mwu(a_voff, a_can)
            ci = _bootstrap_ci([x - y for x, y in zip(a_voff, a_can)])
            out["operational_total_effect"][key] = {
                "verify_off_mean": mean(a_voff), "canonical_mean": mean(a_can),
                "diff_voff_minus_can": ci[2], "ci95": [ci[0], ci[1]],
                "welch_t": t, "welch_p": p, "cohens_d": d,
                "mwu_U": u, "mwu_p": pu, "n": (len(a_voff), len(a_can)),
            }
        # mechanism: null-control vs canonical（等效性 TOST）
        if a_can and a_null and min(len(a_can), len(a_null)) >= 2:
            dm_key = METRICS.get(key, 0.1)
            tost = _tost(a_null, a_can, dm_key)
            t, p, d = _welch(a_null, a_can)
            out["sequence_mechanism_effect"][key] = {
                "null_mean": mean(a_null), "canonical_mean": mean(a_can),
                "diff_null_minus_can": tost["ci95"][2] if tost["ci95"] else None,
                "tost": tost, "welch_p": p, "cohens_d": d,
                "n": (len(a_null), len(a_can)),
            }
    # operational 的 token/tool/evidence（F2b 2: verify-off 证据集混杂，必须并列报）
    for key in OPERATIONAL_METRICS:
        a_voff, _ = _col(cells, "verify-off", ckpt, key)
        a_can, _ = _col(cells, "canonical", ckpt, key)
        if a_can and a_voff and min(len(a_can), len(a_voff)) >= 2:
            ci = _bootstrap_ci([x - y for x, y in zip(a_voff, a_can)])
            out["operational_total_effect"][key] = {
                "verify_off_mean": mean(a_voff), "canonical_mean": mean(a_can),
                "diff_voff_minus_can": ci[2], "ci95": [ci[0], ci[1]],
                "n": (len(a_voff), len(a_can)),
            }
    return out


def direction_consistency(comparisons):
    """跨 checkpoint 方向一致性（Handoff Tax 警告：效应随方向反转）。
    对每个估计量×指标，看各 ckpt 的 diff 符号是否一致。"""
    out = {}
    for est in ("operational_total_effect", "sequence_mechanism_effect"):
        out[est] = {}
        keys = set()
        for c in comparisons:
            keys.update(c[est].keys())
        for key in sorted(keys):
            signs = []
            for c in comparisons:
                dd = c[est].get(key, {}).get(
                    "diff_voff_minus_can" if est.endswith("total_effect") else "diff_null_minus_can")
                if dd is not None:
                    signs.append(1 if dd > 0 else (-1 if dd < 0 else 0))
            consistent = len(set(signs)) <= 1 if signs else None
            out[est][key] = {
                "signs_by_ckpt": {c["checkpoint"]: (1 if c[est].get(key, {}).get(
                    "diff_voff_minus_can" if est.endswith("total_effect") else "diff_null_minus_can") > 0 else -1)
                    for c in comparisons if key in c[est]},
                "consistent_direction": consistent,
            }
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="T-PR-17 T5 分析（纯统计，零 LLM）")
    ap.add_argument("--out", default=DATA_ROOT)
    ap.add_argument("--config", default=os.path.join(DATA_ROOT, "tpr17_deltamin_config.json"))
    ap.add_argument("--checkpoints", default=",".join(CHECKPOINTS))
    a = ap.parse_args(argv)

    cfg = load_config(a.config)
    cells, problems = load_cells(a.out)
    if not cells:
        sys.exit("[analysis] 无 cell 数据可分析（T4 未跑?）")

    comparisons = []
    for ckpt in [c.strip() for c in a.checkpoints.split(",") if c.strip()]:
        # 该 ckpt 至少要有 canonical + 一个对照臂 + ≥2 rep 才可比较
        have_can = any(k[0] == "canonical" and k[1] == ckpt for k in cells)
        have_ctrl = any(k[0] in ("verify-off", "null-control") and k[1] == ckpt for k in cells)
        if not (have_can and have_ctrl):
            problems.append(f"{ckpt}: 缺 canonical 或对照臂，跳过")
            continue
        comparisons.append(compare(cells, ckpt, cfg))

    report = {
        "ts": datetime.now().isoformat(timespec="seconds"),
        "prespecified_config": cfg,
        "n_cells": len(cells),
        "problems": problems,
        "comparisons": comparisons,
        "cross_checkpoint_direction": direction_consistency(comparisons),
        "_interpretation": (
            "operational_total_effect = verify-off vs canonical（方向性，答'能否简化省预算'）；"
            "sequence_mechanism_effect = null-control vs canonical（TOST 等效性，答'序列只是搬运工?'="
            "D 收敛假说直接检验）。等效(equivalent=true) ⟹ 效应 < Δ_min ⟹ 序列无实质影响。"
            "cross_checkpoint_direction.consistent_direction=false ⟹ Handoff Tax 方向反转，"
            "该指标跨 ckpt 不可混池。depth_repaired = T5 修复后 depth（max(链深, level)）。"),
    }
    out_path = os.path.join(a.out, "tpr17_analysis.json")
    json.dump(report, open(out_path, "w"), ensure_ascii=False, indent=1)
    print(json.dumps(report, ensure_ascii=False, indent=1))
    print(f"\n[analysis] → {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
