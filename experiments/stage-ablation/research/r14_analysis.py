#!/usr/bin/env python3
"""r14 校准分析：edge/level/status 分布 + S_α' + rework 事件。

输入: runs-s5-sm-gpu.json (r14 final, structural test 修正版)
对照: checkpoints/sm-gpu-r2.json (r14 r2 ckpt), runs-s5-sm-gpu.json 旧版(r13, git HEAD)
输出: research/r14-calibration-analysis.md
"""
import json, sys, collections, os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def load(path):
    with open(path) as f:
        return json.load(f)


def dist(nodes, key):
    c = collections.Counter()
    for n in nodes:
        v = n.get(key)
        c[str(v)] += 1
    return c


def analyze(tag, data):
    nodes = data["nodes"]
    rounds = data.get("rounds", [])
    out = {"tag": tag, "n_nodes": len(nodes)}
    out["by_level"] = dict(dist(nodes, "level"))
    out["by_edge"] = dict(dist(nodes, "edge_type"))
    out["by_status"] = dict(dist(nodes, "status"))
    out["by_source"] = dict(dist(nodes, "source"))
    # level × edge cross-tab
    cross = collections.Counter((str(n.get("level")), str(n.get("edge_type"))) for n in nodes)
    out["level_x_edge"] = {f"{k[0]}|{k[1]}": v for k, v in sorted(cross.items())}
    # status by level
    st_cross = collections.Counter((str(n.get("level")), str(n.get("status"))) for n in nodes)
    out["level_x_status"] = {f"{k[0]}|{k[1]}": v for k, v in sorted(st_cross.items())}
    if rounds:
        out["rounds"] = [
            {k: r.get(k) for k in ("round", "n_new", "total", "gain", "S_alpha_prime", "verified", "streak")}
            if isinstance(r, dict) else r
            for r in rounds
        ]
    out["reworks"] = len(data.get("rework_events") or [])
    out["leaks"] = data.get("leak_hits") or data.get("leak_hits_total")
    return out


def main():
    r14 = load(os.path.join(HERE, "..", "..", "..", "runs-s5-sm-gpu.json"))
    a14 = analyze("r14-final", r14)

    lines = []
    ap = lines.append
    ap("# r14 校准分析（structural test 修正版）\n")
    ap(f"> origin: cc-experimentalist · 2026-11-12 · 数据源: `runs-s5-sm-gpu.json` (DONE: {a14['n_nodes']} nodes, state={r14.get('final_state')}, leaks={a14['leaks']}, reworks={a14['reworks']})\n")

    ap("\n## 1. 总量\n")
    ap(f"- 节点数: **{a14['n_nodes']}** (r13 基线 70 → r14 中间 r2 ckpt 59 → r14 final {a14['n_nodes']})")
    ap(f"- 轮数: {len(r14.get('rounds', []))} (max_depth=4 hit 后停)")
    ap(f"- leaks: {a14['leaks']} | rework events: {a14['reworks']}")

    ap("\n## 2. Level 分布\n")
    ap("| level | nodes |\n|---|---|\n")
    for lv in sorted(a14["by_level"], key=lambda x: int(str(x).lstrip("L"))):
        ap(f"| {lv} | {a14['by_level'][lv]} |\n")

    ap("\n## 3. Edge 类型分布（核心指标：r13 quotient 90% 被 hack）\n")
    tot = max(a14["n_nodes"], 1)
    ap("| edge | nodes | % |\n|---|---|---|\n")
    for et in ("cartesian", "quotient", "stochastic"):
        v = a14["by_edge"].get(et, 0)
        ap(f"| {et} | {v} | {100*v/tot:.1f}% |\n")
    other = {k: v for k, v in a14["by_edge"].items() if k not in ("cartesian", "quotient", "stochastic")}
    for k, v in other.items():
        ap(f"| {k} | {v} | {100*v/tot:.1f}% |\n")

    ap("\n### 3a. Level × Edge 交叉表\n")
    ap("| level \\ edge | cartesian | quotient | stochastic |\n|---|---|---|---|\n")
    levels = sorted({k.split("|")[0] for k in a14["level_x_edge"]}, key=lambda x: int(str(x).lstrip("L")))
    for lv in levels:
        row = [a14["level_x_edge"].get(f"{lv}|{et}", 0) for et in ("cartesian", "quotient", "stochastic")]
        ap(f"| {lv} | {row[0]} | {row[1]} | {row[2]} |\n")

    ap("\n## 4. Status 分布（degraded 率是优化信号）\n")
    ap("| status | nodes | % |\n|---|---|---|\n")
    for st, v in sorted(a14["by_status"].items(), key=lambda kv: -kv[1]):
        ap(f"| {st} | {v} | {100*v/tot:.1f}% |\n")

    ap("\n### 4a. Level × Status\n")
    ap("| level \\ status | verified | degraded | pending | failed |\n|---|---|---|---|---|\n")
    for lv in levels:
        row = [a14["level_x_status"].get(f"{lv}|{st}", 0) for st in ("verified", "degraded", "pending", "failed")]
        ap(f"| {lv} | {row[0]} | {row[1]} | {row[2]} | {row[3]} |\n")

    ap("\n## 5. Source 分布\n")
    ap("| source | nodes |\n|---|---|\n")
    for s, v in sorted(a14["by_source"].items(), key=lambda kv: -kv[1]):
        ap(f"| {s} | {v} |\n")

    ap("\n## 6. 逐轮轨迹\n")
    if a14.get("rounds"):
        ap("| round | n_new | total | gain | S_α' | verified/n_new | streak |\n|---|---|---|---|---|---|---|\n")
        for r in a14["rounds"]:
            if isinstance(r, dict):
                ver = r.get("verified")
                nn = r.get("n_new") or 0
                ap(f"| {r.get('round')} | {nn} | {r.get('total')} | {r.get('gain')} | {r.get('S_alpha_prime')} | {ver}/{nn} | {r.get('streak')} |\n")

    ap("\n## 7. Rebuild 检查：rework 事件抽样\n")
    evs = r14.get("rework_events") or []
    ap(f"共 {len(evs)} 条 rework 事件。前 8 条：\n")
    for e in evs[:8]:
        ap(f"- N? {e.get('node_id')} attempt={e.get('attempt')} :: {str(e.get('claim',''))[:50]} — {str(e.get('reason',''))[:60]}\n")

    ap("\n## 8. 判读（对照任务书阈值）\n")
    deg_pct = 100 * a14["by_status"].get("degraded", 0) / tot
    quo_pct = 100 * a14["by_edge"].get("quotient", 0) / tot
    ap(f"- degraded 率 = {deg_pct:.1f}% （任务书警戒线 >40%）→ {'⚠️ 超线，需诊断' if deg_pct > 40 else '✅ 未超线'}")
    ap(f"- quotient 占比 = {quo_pct:.1f}% （r13 为 90%，方向已反转）")
    ap(f"- max_depth=4 即停：树在深度 4 处截断——是机制生效还是提前封顶？见 §9。\n")

    ap("\n## 9. 待 Lead 判断的问题\n")
    ap("1. **state=rework 终止**：run 结束时状态是 rework 而非 STOP——是 max_depth 触发的正常退出路径吗？（代码里 max_depth hit 直接 break，state 停在当时值）")
    ap("2. **reworks=91 偏高**：91 次 rework 事件 / 137 节点 ≈ 每 1.5 节点一次返工。是核验过严（verify_threshold 0.6），还是检索通道（arXiv DDG）对 gpu 题命中率低？需要看 rework 失败原因分布（§7 只抽了前 8 条）。")
    ap("3. **max_depth=4 是否够**：gpu 题的 TCO/微架构下钻按 Decision 8 至少需要 L4-L5；当前 depth cap 可能系统性砍掉叶子层证据。调 max_depth 属于参数改动，走三问提案。")

    out_path = os.path.join(HERE, "r14-calibration-analysis.md")
    with open(out_path, "w") as f:
        f.write("".join(lines))
    print(f"wrote {out_path}")
    # stdout 摘要
    print(json.dumps({k: a14[k] for k in ("n_nodes", "by_level", "by_edge", "by_status", "reworks", "leaks")}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()