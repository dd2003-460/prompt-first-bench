#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_j3a_factors.py — J3a S1：从 gold-tree.md + calc.py 确定性提取层级因素树 + c_pass 参数 → JSON
# origin: ai · 2026-11-26 · 载体修正：纯机械提取不该派 reasoning sub（27b reasoning 在"想"阶段烧光输出预算，
#   J3a 家族 4 次同死因），改用确定性脚本。本脚本是复用工具，输出落盘不进任何上下文。
# 用法: python3 extract_j3a_factors.py  （在 pfb-thinkmech 根目录跑）
# 产出: tasks/think-trigger/exp-results/j3a-factors.json
"""
import json, re, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
TREE = os.path.join(ROOT, "bench/rubric-v3/ablation/gold-tree.md")
CALC = os.path.join(ROOT, "bench/rubric-v3/tasks/T0-local-27b/reference/calc.py")
OUT  = os.path.join(ROOT, "tasks/think-trigger/exp-results/j3a-factors.json")

NODE_RE = re.compile(r"N-(\d+(?:\.\d+)*)")

def level_of(nid):
    # nid 形如 "0","1","1.1","3.1.3.1"
    if nid == "0":
        return 0
    return nid.count(".") + 1

def parse_tree(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    # 只取第一个 ``` 围栏块（主树）；后面的围栏是 OC-1 卡片样例，含重复 ID
    fence_lines = []
    seen_open = False
    for ln in lines:
        if ln.strip().startswith("```"):
            if not seen_open:
                seen_open = True
                continue
            else:
                break  # 第一个块结束
        if seen_open:
            fence_lines.append(ln)
    nodes = []
    gaps = []
    for i, ln in enumerate(fence_lines):
        stripped = re.sub(r"^[│├└─\s]+", "", ln)
        # 跳过括号引用行（如 "(并发数 n → 由 N-5 决定, S-c, SHARED)"）和非节点行
        if stripped.startswith("(") or stripped.startswith(">") or stripped.startswith("**"):
            continue
        m = NODE_RE.search(ln)
        if not m:
            continue
        nid = m.group(1)
        tail = ln[m.end():]
        # name: 第一个中文串
        nm = re.search(r"[\u4e00-\u9fff]+", tail)
        name = nm.group(0) if nm else ""
        # param: 第一个小数 share 之前的最后一个标识符 token（黑名单 leaf/split/S/N）
        # 处理: snake_case(gpu_price) / 单词(resid,elec) / 单大写字母(H)；
        #       "prefill 计算量 prefill_flops" 取最后的 prefill_flops；无小数时取 leaf/split 关键词前
        param = None
        dec_pos = re.search(r"\.\d+", tail)
        kw_pos = re.search(r"\b(leaf|split)\b", tail)
        cut = min([p.start() for p in (dec_pos, kw_pos) if p], default=len(tail))
        seg = tail[:cut]
        idents = re.findall(r"[A-Za-z][A-Za-z0-9_]*", seg)
        bl = {"leaf", "split", "S", "N"}
        idents = [x for x in idents if x not in bl and not x.startswith("N-")]
        if idents:
            param = idents[-1]
        # share: 小数（含 SHARE 前缀 / % 后缀 / 纯小数）
        sm = re.search(r"(?:SHARE\s+)?(\d+\.?\d*)\s*(?:%|x)?(?=\s|$)", tail)
        share = sm.group(1) if sm else None
        # bound: Nx
        bm = re.search(r"(\d+\.?\d*)x", tail)
        bound = bm.group(1) + "x" if bm else None
        # blackbox: B\d+
        bbm = re.search(r"\b(B\d+)\b", tail)
        blackbox = bbm.group(1) if bbm else None
        # type: leaf|split
        tm = re.search(r"\b(leaf|split)\b", tail)
        ntype = tm.group(1) if tm else None
        # stop basis: S-a/b/c
        sbm = re.search(r"\b(S-[abc])\b", tail)
        stop = sbm.group(1) if sbm else None
        # shared ref
        shm = re.search(r"SHARED\s*→\s*(N-\d+(?:\.\d+)*)", tail)
        shared_ref = shm.group(1) if shm else None
        # 公式行：紧随其后的以 '=' 开头的行
        formula = None
        for j in range(i+1, min(i+3, len(fence_lines))):
            nxt = fence_lines[j].strip()
            if "=" in nxt and not NODE_RE.search(nxt):
                formula = nxt.lstrip("│├└─ ").strip()
                break
        nodes.append({
            "id": "N-"+nid, "level": level_of(nid), "name": name,
            "param": param, "share": share, "bound": bound,
            "blackbox": blackbox, "type": ntype, "stop_basis": stop,
            "shared_ref": shared_ref, "formula": formula,
            "src": f"gold-tree.md fence L{i+1}",
        })
        # 完整性 flag：叶子却没 param 且不是纯结构节点
        if ntype == "leaf" and param is None and name not in ("可行域",):
            gaps.append(f"{nodes[-1]['id']} 叶子无 param（可能纯约束节点，需 S2 核）")
    return nodes, gaps

def parse_calc(path):
    src = open(path, encoding="utf-8").read()
    gaps = []
    # HARDWARE dict
    hw_block = re.search(r"HARDWARE\s*=\s*\{(.*?)\n\}", src, re.S)
    hardware = {}
    if hw_block:
        for cm in re.finditer(r'"(\w+)"\s*:\s*dict\((.*?)\)', hw_block.group(1)):
            card = cm.group(1)
            fields = {}
            for fm in re.finditer(r"(\w+)\s*=\s*([\d.eE]+)", cm.group(2)):
                fields[fm.group(1)] = float(fm.group(2))
            hardware[card] = fields
    # 顶层常数
    const_names = ["HOST_PRICE","RESID","H_HOURS","P_FAIL","PREFILL_FLOPS","OUT_TOK","TP_EFF","KV_PER_STREAM"]
    constants = {}
    for cn in const_names:
        cm = re.search(rf"^{cn}\s*=\s*([\d.eE]+)", src, re.M)
        if cm:
            constants[cn] = float(cm.group(1))
        else:
            gaps.append(f"常数 {cn} 未匹配")
    # 黑盒中位数 U,G,ELEC,MFU,ETA_BW
    um = re.search(r"^U,\s*G,\s*ELEC,\s*MFU,\s*ETA_BW\s*=\s*([\d.,\s]+)", src, re.M)
    if um:
        vals = [float(x) for x in um.group(1).split(",")]
        for k,v in zip(["U","G","ELEC","MFU","ETA_BW"], vals):
            constants[k] = v
    else:
        gaps.append("黑盒中位数行 U,G,ELEC,MFU,ETA_BW 未匹配")
    # W_BYTES
    wb = re.search(r"W_BYTES\s*=\s*(\{.*?\})", src)
    w_bytes = {}
    if wb:
        for wm in re.finditer(r'"(W\d+)"\s*:\s*([\d.]+)', wb.group(1)):
            w_bytes[wm.group(1)] = float(wm.group(2))
    # c_pass 公式
    fm = re.search(r"c_pass\s*=\s*c_hour\s*/\s*\(\s*u\s*×\s*λ_raw\s*×\s*G_pass\s*\)", src)
    formula = "c_pass = c_hour / (u × λ_raw × G_pass)" if fm else None
    if not formula:
        gaps.append("c_pass 公式串未在 calc.py 命中（用 gold-tree 版）")
    return hardware, constants, w_bytes, formula, gaps

def main():
    tree_nodes, tree_gaps = parse_tree(TREE)
    hardware, constants, w_bytes, formula, calc_gaps = parse_calc(CALC)
    # 层级聚合
    levels = {}
    for n in tree_nodes:
        levels.setdefault(n["level"], []).append(n["id"])
    doc = {
        "meta": {"source_tree": "gold-tree.md", "source_calc": "calc.py",
                 "header_declares": "37 节点 / 主干深度 5 / 叶子 17（gold-tree.md L3）",
                 "extracted_nodes": len(tree_nodes),
                 "max_level": max(levels) if levels else 0},
        "layers": [{"level": lv, "node_ids": ids} for lv, ids in sorted(levels.items())],
        "nodes": tree_nodes,
        "c_pass_formula": {"equation": formula,
                            "hardware": hardware, "constants": constants,
                            "w_bytes": w_bytes},
        "gaps": tree_gaps + calc_gaps,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    print(f"OK nodes={len(tree_nodes)} levels={sorted(levels)} hw_cards={list(hardware)} consts={len(constants)} gaps={len(doc['gaps'])}")

if __name__ == "__main__":
    main()
