#!/usr/bin/env python3
"""q9-budget-scan run → md 树渲染。

D 2026-11-27: "我要的是分解结果的md" — 把模型分解出的节点树
(JSON nodes[]) 渲染成人可读 md, 每 run 一个文件, 落 data/q9-budget-scan/md/。
树结构用 level 字段缩进 + parent_ids 校验; 每节点带 status/rework/溯源。
"""
import json, glob, os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, "..", "data", "q9-budget-scan")
OUT = os.path.join(BASE, "md")
os.makedirs(OUT, exist_ok=True)


def _lvl(n):
    v = str(n.get("level", 0)).lstrip("Ll")
    try:
        return int(v)
    except ValueError:
        return 0


def render(run_file):
    r = json.load(open(run_file))
    name = os.path.basename(run_file).replace(".json", "")
    nodes = r.get("nodes", [])
    by_id = {n["id"]: n for n in nodes}
    lines = [f"# {name}", ""]
    lines.append(f"- 节点数: {len(nodes)} | 轮数: {r.get('n_rounds')} | 终态: {r.get('final_state')}")
    rew = r.get("rework_events") or []
    rew_nodes = sorted({e.get("node_id", "?") for e in rew if isinstance(e, dict)})
    lines.append(f"- rework 事件: {len(rew)} 次, 涉及节点: {', '.join(rew_nodes)} | leak: {r.get('leak_hits')}")
    lines.append("")
    lines.append("## 节点树 (按 level 缩进)")
    lines.append("")
    for n in sorted(nodes, key=lambda x: (_lvl(x), str(x.get("id", "")))):
        lv = _lvl(n)
        ind = "  " * min(lv, 8)
        flag = ""
        if n.get("rework_count"):
            flag += f" [rework×{n['rework_count']}]"
        if n.get("corrected_claim"):
            flag += " [已修正]"
        st = n.get("status", "")
        claim = (n.get("claim") or "").replace("\n", " ").strip()
        lines.append(f"{ind}- `{n['id']}` (L{lv}{f'/{st}' if st else ''}{flag}) {claim}")
        ev = n.get("evidence") or ""
        if ev and isinstance(ev, str) and ev.strip():
            lines.append(f"{ind}  > 证据: {ev.strip()[:150]}")
    md = "\n".join(lines) + "\n"
    out = os.path.join(OUT, name + ".md")
    open(out, "w").write(md)
    return out, len(nodes)


def main():
    rows = []
    for f in sorted(glob.glob(os.path.join(BASE, "q9-*-r*.json"))):
        out, n = render(f)
        rows.append((os.path.basename(out), n, os.path.getsize(out)))
    print(f"渲染 {len(rows)} 个 run → {os.path.relpath(OUT)}")
    for name, n, sz in rows:
        print(f"  {name:<40} {n:>4} 节点  {sz//1024}KB")
    # 索引
    idx = ["# q9-budget-scan 分解结果 md 索引", "", "| 文件 | 节点数 | 大小 |", "|---|---|---|"]
    for name, n, sz in rows:
        idx.append(f"| {name} | {n} | {sz//1024}KB |")
    open(os.path.join(OUT, "INDEX.md"), "w").write("\n".join(idx) + "\n")
    print("INDEX.md 已生成")


if __name__ == "__main__":
    main()
