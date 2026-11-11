#!/usr/bin/env python3
"""tree→report 组装器：把 s5_state_machine 的节点树渲染成 DRB judge 吃的研究报告。

设计（T53 night · Lead）：
- 输入: runs-s5-sm-{qid}.json（SMResult 落盘，含 nodes/rounds/objective/question 可选）
- 输出: experiments/stage-ablation/drb-pilot/answers/{qid}-report.md
- 原则: 纯机械组装，不改 claim 内容（claim 是 SM 已核验产物；evidence/corrected_claim 一并带上）。
  按 level 分节平铺（C3 修订：旧版按 parent_ids 递归缩进，但 r14 及更早的树里
  parent_ids = 同轮 frontier batch（兄弟共享），且存在跨 level 撞号——递归会指数爆炸
  或丢节点；level 平铺 + 状态标注对 DRB 四维判分已足够）。
- 来源回填: SM 落盘不含检索 URL（evidence 是 P3 judge 的文字判断），.research-cache
  按 query(=claim) 存了完整 sources，按 claim 精确匹配回填（DRB instruction_following
  维度需要"引用了哪些来源"）。
- 泄漏安全: 只写节点 claim/evidence/sources，不写题目原文以外的元数据；DRB 题本身允许
  出现在报告里（judge 需要对照 prompt），但 SM 侧禁止的是把 bench 特征写进 prompt 规则——本脚本不碰 prompt。
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(HERE, "..", ".research-cache")


def load_tree(path):
    with open(path) as f:
        return json.load(f)


def _norm(s):
    return re.sub(r"\s+", "", s or "")


def build_cache_index():
    idx = {}
    if not os.path.isdir(CACHE_DIR):
        return idx
    for fn in os.listdir(CACHE_DIR):
        if not fn.endswith(".json"):
            continue
        try:
            e = json.load(open(os.path.join(CACHE_DIR, fn)))
        except Exception:
            continue
        q = e.get("question", "")
        if q and e.get("sources"):
            idx[_norm(q)] = e["sources"]
    return idx


def render_sources(srcs):
    lines = []
    for i, s in enumerate(srcs[:5], 1):
        t = (s.get("title") or "?")[:80]
        u = s.get("url") or "?"
        snip = (s.get("snippet") or "")[:200].replace("\n", " ")
        lines.append(f"{i}. {t} — <{u}>　{snip}")
    return "\n".join(lines)


def build_report(d, question=None):
    nodes = d.get("nodes", [])
    cache_idx = build_cache_index()
    n_backfilled = 0

    status_mark = {"verified": "✓", "degraded": "△", "pending": "…", "failed": "✗"}
    lines = []
    # E15: 终盘自带 question/objective 时优先用（r14 前旧文件缺字段，--question-file 兜底）
    question = question or d.get("question")
    if question:
        lines.append(f"# 研究报告：{question}\n")
    obj = d.get("objective")
    if obj:
        o = obj.get("objective") if isinstance(obj, dict) else str(obj)
        lines.append(f"**研究范围与合格判据**（模型自估计）：{o}\n")

    def emit_record(n):
        nonlocal n_backfilled
        mark = status_mark.get(n.get("status"), "?")
        cc = (n.get("corrected_claim") or "").strip()
        ev = (n.get("evidence") or "").strip()
        title = cc or n.get("claim", "")
        lines.append(f"- [{mark}] **{title}**")
        if ev and ev != title:
            ev_short = ev.replace("\n", " ")
            if len(ev_short) > 400:
                ev_short = ev_short[:400] + "…"
            lines.append(f"  - 依据: {ev_short}")
        if n.get("source") == "search":
            srcs = cache_idx.get(_norm(n.get("claim", "")))
            if srcs:
                n_backfilled += 1
                lines.append("  - 检索来源:\n" +
                             "\n".join(f"    {l}" for l in render_sources(srcs).splitlines()))

    max_lv = max((int(str(n.get("level", "L0")).lstrip("L")) for n in nodes), default=0)
    for lv in range(1, max_lv + 1):
        recs = [n for n in nodes if int(str(n.get("level", "L0")).lstrip("L")) == lv]
        if not recs:
            continue
        lines.append(f"\n## L{lv}\n")
        for n in recs:
            emit_record(n)

    print(f"[assemble] source backfill: {n_backfilled} search nodes matched in cache")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, help="runs-s5-sm-{qid}.json 路径")
    ap.add_argument("--qid", required=True)
    ap.add_argument("--question", default=None, help="题目文本（可选，用于报告标题）")
    ap.add_argument("--query-file", default=None, help="DRB query json（含 prompt 字段），--question 缺省时用")
    ap.add_argument("--out-dir", default=os.path.join(HERE, "answers"))
    args = ap.parse_args()
    d = load_tree(args.run)
    question = args.question
    if not question and args.query_file:
        try:
            question = json.load(open(args.query_file))["prompt"]
        except Exception:
            pass
    report = build_report(d, question)
    os.makedirs(args.out_dir, exist_ok=True)
    out = os.path.join(args.out_dir, f"{args.qid}-report.md")
    with open(out, "w") as f:
        f.write(report)
    print(f"[assemble] {len(d.get('nodes', []))} nodes → {out} ({len(report)} chars)")


if __name__ == "__main__":
    main()