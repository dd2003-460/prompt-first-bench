#!/usr/bin/env python3
"""T-JUDGE-1 J1+J2: gold 事实清单解析 + checkpoint 树读取（原型验证）

首跑范围 = gpu only:
  gold: Q1.md 事实清单（表格行/编号误读/bullet 结论/bullet 缺口 → 各 1 单元）
  checkpoint: checkpoints/sm-gpu-r{N}/ 树形目录（node.json 的 claim 字段）
输出统一 schema: [{unit_id, depth, text, parent_id}]
"""
import json, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
PFB_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
GOLD = os.path.join(PFB_ROOT, "experiments/stage-ablation/gold/Q1.md")
CKPT = os.path.join(PFB_ROOT, "experiments/stage-ablation/checkpoints")


def parse_gold_q1(path):
    """Q1 事实清单 → 单元列表。规则:
    - 表格行（| 开头, 非表头/分隔行, 在'关键规格'节）→ spec 单元
    - 编号项（1. 2. 3. 4. 在'常见误读'节）→ misread 单元（含缩进续行）
    - bullet（- 开头, 在'正确结论'/'应识别的缺口'节）→ conclusion/gap 单元
    """
    units = []
    section = None
    lines = open(path, encoding="utf-8").read().splitlines()
    i = 0
    while i < len(lines):
        ln = lines[i]
        m = re.match(r"^##\s+(.*)", ln)
        if m:
            section = m.group(1).strip()
            i += 1
            continue
        # 表格行
        if section and "关键规格" in section and ln.startswith("|"):
            cells = [c.strip() for c in ln.strip("|").split("|")]
            if len(cells) >= 2 and not set(cells[0]) <= set("- ") and cells[0] != "项":
                units.append({"unit_id": f"SPEC-{len([u for u in units if u['unit_id'].startswith('SPEC')])+1}",
                              "depth": 1, "text": " | ".join(cells), "parent_id": "N-0", "kind": "spec"})
            i += 1
            continue
        # 编号项（含缩进续行）
        m = re.match(r"^(\d+)\.\s+(.*)", ln)
        if m and section and "误读" in section:
            text = m.group(2)
            j = i + 1
            while j < len(lines) and (lines[j].startswith("   ") or lines[j].startswith("\t")):
                text += " " + lines[j].strip()
                j += 1
            units.append({"unit_id": f"MIS-{m.group(1)}", "depth": 1, "text": text,
                          "parent_id": "N-0", "kind": "misread"})
            i = j
            continue
        # bullet
        m = re.match(r"^- (.*)", ln)
        if m and section and ("结论" in section or "缺口" in section):
            kind = "conclusion" if "结论" in section else "gap"
            units.append({"unit_id": f"{kind.upper()[:3]}-{len([u for u in units if u['kind']==kind])+1}",
                          "depth": 1, "text": m.group(1), "parent_id": "N-0", "kind": kind})
        i += 1
    return units


def parse_gold_flat(qid, items):
    """s8b_pilot.GOLD 平铺要点清单（nat/soc）→ 单元列表（与 Q1 同构, kind=point）"""
    return [{"unit_id": f"P-{i+1}", "depth": 1, "text": t, "parent_id": "N-0", "kind": "point"}
            for i, t in enumerate(items)]


def load_gold(qid):
    """按 qid 取 gold 单元: gpu → Q1.md 事实清单(16, 更权威); nat/soc → s8b_pilot.GOLD 平铺清单"""
    if qid == "gpu":
        return parse_gold_q1(GOLD)
    sys.path.insert(0, os.path.join(PFB_ROOT, "experiments", "stage-ablation"))
    from s8b_pilot import GOLD as FLAT_GOLD
    return parse_gold_flat(qid, FLAT_GOLD[qid])


def parse_checkpoint(ckpt_dir):
    """树形目录 checkpoints/sm-{qid}-r{N}/ → 单元列表。
    目录名 '1', '1.1', '1.1.3' 编码层级；node.json 含 id/claim。
    """
    units = []
    node_files = glob.glob(os.path.join(ckpt_dir, "**", "node.json"), recursive=True)
    for nf in node_files:
        d = json.load(open(nf, encoding="utf-8"))
        rel = os.path.relpath(os.path.dirname(nf), ckpt_dir)  # e.g. '1/1.1'
        depth = rel.count(os.sep) + 1
        units.append({"unit_id": d.get("id", rel), "depth": depth,
                      "text": d.get("claim", ""), "parent_id": None, "kind": "node"})
    units.sort(key=lambda u: u["unit_id"])
    return units


if __name__ == "__main__":
    g = parse_gold_q1(GOLD)
    print(f"gold Q1 单元: {len(g)}")
    from collections import Counter
    print("  按类型:", dict(Counter(u["kind"] for u in g)))
    for u in g[:3]:
        print(f"  [{u['unit_id']}] {u['text'][:60]}...")
    print()
    for ck in sorted(glob.glob(os.path.join(CKPT, "sm-gpu-r*"))):
        if os.path.isdir(ck):
            c = parse_checkpoint(ck)
            meta_f = os.path.join(ck, "meta.json")
            meta_n = json.load(open(meta_f)).get("n_nodes") if os.path.exists(meta_f) else "?"
            print(f"{os.path.basename(ck)}: 解析 {len(c)} 节点 (meta n_nodes={meta_n}) "
                  f"depth max={max(u['depth'] for u in c) if c else 0}")
            if c:
                print(f"  样例: [{c[0]['unit_id']} d{c[0]['depth']}] {c[0]['text'][:60]}...")
