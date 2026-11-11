#!/usr/bin/env python3
"""tree→report 组装器：把 s5_state_machine 的节点树渲染成 DRB judge 吃的研究报告。

设计（T53 night · Lead）：
- 输入: runs-s5-sm-{qid}.json（SMResult 落盘，含 nodes/rounds/objective/question 可选）
- 输出: experiments/stage-ablation/drb-pilot/answers/{qid}-report.md
- 原则: 纯机械组装，不改 claim 内容（claim 是 SM 已核验产物；evidence/corrected_claim 一并带上）。
  按 level 分节，L1 作报告骨架标题，子节点缩进挂在父下（parent_ids 反查），
  verified/degraded/failed 状态标注在条目后。开头附 objective（模型自估计目标函数）作为"研究范围声明"。
- 泄漏安全: 只写节点 claim/evidence，不写题目原文以外的元数据；DRB 题本身允许出现在报告里
  （judge 需要对照 prompt），但 SM 侧禁止的是把 bench 特征写进 prompt 规则——本脚本不碰 prompt。
"""
import argparse, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load_tree(path):
    with open(path) as f:
        return json.load(f)


def build_report(d, question=None):
    nodes = d.get("nodes", [])
    by_id = {n["id"]: n for n in nodes}
    children = {}
    for n in nodes:
        for p in (n.get("parent_ids") or []):
            children.setdefault(p, []).append(n["id"])
    roots = [n["id"] for n in nodes if not (n.get("parent_ids") or [])]

    status_mark = {"verified": "✓", "degraded": "△", "pending": "…", "failed": "✗"}

    lines = []
    if question:
        lines.append(f"# 研究报告：{question}\n")
    obj = d.get("objective")
    if obj:
        o = obj.get("objective") if isinstance(obj, dict) else str(obj)
        lines.append(f"**研究范围与合格判据**（模型自估计）：{o}\n")

    def emit(nid, depth, seen):
        if nid in seen:  # 防环：parent_ids 可能构成循环引用
            return
        n = by_id[nid]
        mark = status_mark.get(n.get("status"), "?")
        cc = (n.get("corrected_claim") or "").strip()
        ev = (n.get("evidence") or "").strip()
        title = cc or n.get("claim", "")
        indent = "  " * depth
        lines.append(f"{indent}- [{mark}] **{title}**")
        if ev and ev != title:
            ev_short = ev.replace("\n", " ")
            if len(ev_short) > 400:
                ev_short = ev_short[:400] + "…"
            lines.append(f"{indent}  - 依据: {ev_short}")
        for cid in sorted(children.get(nid, []), key=lambda x: int(str(x).lstrip("N"))):
            emit(cid, depth + 1, seen | {nid})

    for rid in sorted(roots, key=lambda x: int(str(x).lstrip("N"))):
        emit(rid, 0, set())
        lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, help="runs-s5-sm-{qid}.json 路径")
    ap.add_argument("--qid", required=True)
    ap.add_argument("--question", default=None, help="题目文本（可选，用于报告标题）")
    ap.add_argument("--out-dir", default=os.path.join(HERE, "answers"))
    args = ap.parse_args()
    d = load_tree(args.run)
    report = build_report(d, args.question)
    os.makedirs(args.out_dir, exist_ok=True)
    out = os.path.join(args.out_dir, f"{args.qid}-report.md")
    with open(out, "w") as f:
        f.write(report)
    print(f"[assemble] {len(d.get('nodes', []))} nodes → {out} ({len(report)} chars)")


if __name__ == "__main__":
    main()