#!/usr/bin/env python3
"""assert-o3-claim-list.py — O3 原子 claim 清单结构完整性断言（RV3G6-o3-claim-list）

验证 bench/rubric-v3/o3-claim-list.md：
  ① 31 节点 ID 全出现且各对应非空 claim 行（§2.2 表）
  ② claim 文本不含 gold-tree.md 专有数值（防答案泄漏 R1；结构性数字豁免见 GOLD_NUM_EXEMPT）
  ③ 映射一致性基线值从 hit-matrix.json 独立复算，与 o3-claim-list.md §3.2 声明一致
     （M1 全量 248/248 / M1 gold strict 40/40 / M2 8/8，identity-baseline 标签存在）
  ④ DRAFT-rubric-v3-v2.md L71 旧判据措辞已替换（「节点 ID 对得上」全文消失 + claim 引用存在）
exit 0 = 全部 PASS, exit 1 = 存在 FAIL
"""
import json, re, sys

BASE = "bench/rubric-v3"
CLAIM_FILE = f"{BASE}/o3-claim-list.md"
GOLD_TREE = f"{BASE}/ablation/gold-tree.md"
HIT_MATRIX = f"{BASE}/ablation/hit-matrix.json"
DRAFT_V2 = f"{BASE}/DRAFT-rubric-v3-v2.md"

GOLD_STRICT = ["N-2.1", "N-3.2.2", "N-2", "N-4", "N-1.3"]

# 结构性数字豁免：claim 中允许出现的数字（汉字数字不触发本检查，仅阿拉伯数字）
# '0'/'1' = 二值判定记法 h_v∈{0,1}（判据机制用语，非 gold 答案数值）；定稿 claim 零其他数值
GOLD_NUM_EXEMPT = {"0", "1"}

# 黑名单噪声豁免（04.5 W5 二次修复配套）：gold-tree 节点行里的**节点 ID 自身数字**
# （N-2.1 → '2','1'；N-3.2.2 → '3','2'）与树形结构计数（主干深度 4 / 叶子 13 / 31 个节点）。
# 这些不是「专有数值」（judge 看到 '2' 无法反推任何 gold 结论），若入黑名单则所有含
# 层级指称的 claim（如 N-3.2.2「属于第三层」）必然误报。真正的专有数值（42.8%、774 GB/s、
# 14/27/54 GB、8.00x 等）全部保留在黑名单内。
def _noise_exempt():
    ids, _, _ = node_ids()
    ex = set(GOLD_NUM_EXEMPT)
    for nid in ids:
        parts = nid[2:].split(".")
        ex |= set(parts)                                   # ID 分段：'1','1','1'（整数 token）
        ex.add(".".join(parts[:2]))                        # 一级前缀：'1.1'/'3.2'（层级指称，非数值）
    ex |= {"31", "4", "13"}                                # 树形结构计数（31 节点/深度 4/叶子 13）
    return ex


def node_ids():
    """31 个 gold 节点 ID（以 hit-matrix 为权威全集，与 gold-tree 交叉核对）。"""
    hm = json.load(open(HIT_MATRIX))
    runs = sorted(hm.keys())
    ids = set(hm[runs[0]].keys())
    for r in runs[1:]:
        assert set(hm[r].keys()) == ids, f"run {r} 节点集不一致"
    # gold-tree 交叉核对：树中每个 N-x.y 标记都必须在 hit-matrix 里
    tree = open(GOLD_TREE).read()
    tree_ids = set(re.findall(r"\bN-\d+(?:\.\d+)*\b", tree))
    missing_in_hm = tree_ids - ids
    extra_in_hm = ids - tree_ids
    return sorted(ids), missing_in_hm, extra_in_hm


def claim_section():
    """§2 正文（'## 2.' 到 '## 3.' 之间）。用 find 切片——str.split('## 2.') 在本环境行为异常（返回截断片段），find 已验证可靠。"""
    text = open(CLAIM_FILE).read()
    i = text.find("## 2.")
    j = text.find("## 3.")
    assert i != -1 and j != -1 and j > i, "o3-claim-list.md 缺少 §2/§3 节标记"
    return text[i + len("## 2."):j]


def claim_row(section, nid):
    """取 §2.2 表中 node 行的完整文本（贪婪到行尾，claim 内含 | 符号安全）。"""
    m = re.search(rf"^\|\s*{re.escape(nid)}\s*\|.*$", section, flags=re.M)
    return m.group(0) if m else None


def check_1_coverage():
    """① 31 节点全覆盖 + claim 非空。"""
    ids, miss, extra = node_ids()
    ok_count = len(ids) == 31 and not miss and not extra
    print(f"[{'PASS' if ok_count else 'FAIL'}] 节点全集 = 31（hit-matrix ∩ gold-tree 一致；miss={sorted(miss)} extra={sorted(extra)}）")
    section = claim_section()
    failed = 0
    for nid in ids:
        row = claim_row(section, nid)
        if not row or len(row) < 40:
            print(f"[FAIL] {nid}: claim 行缺失或过短")
            failed += 1
    ok = failed == 0
    print(f"[{'PASS' if ok else 'FAIL'}] 31 条 claim 行均存在且非空（{31 - failed}/31）")
    return ok and ok_count, (failed + (0 if ok_count else 1))


def gold_numbers_per_node():
    """gold-tree.md 每节点行的数值 token（防泄漏黑名单来源）。

    04.5 W5 二次修复：旧版用 re.match(r'^\\s*[-*]?...') 按行首锚定——但 gold-tree 的树体是
    box-drawing 缩进（├─/│ 前缀），节点 ID 从不在行首，导致只匹配到 OC-1 卡片区的 N-0 一行
    （31 节点里 30 个黑名单为空 → 检查形同虚设）。改为全文件 findall 定位节点 ID 所在行。
    """
    tree = open(GOLD_TREE).read()
    out = {}
    for line in tree.splitlines():
        ids_in_line = re.findall(r"\bN-\d+(?:\.\d+)*\b", line)
        if not ids_in_line:
            continue
        toks = set(re.findall(r"\d+(?:\.\d+)?", line))
        for nid in ids_in_line:
            out.setdefault(nid, set()).update(toks)
    return out


def check_2_no_leak():
    """② claim 文本不含 gold-tree 专有数值（04.5 W5：黑名单 = 全部 31 节点 gold 行数值的并集，防跨节点泄漏）。

    04.5 W5 二次修复：黑名单提取正则从「行首锚定」（只匹配到 OC-1 卡片区 N-0 一行，检查形同虚设）
    改为全文件 findall 定位节点 ID 所在行；同时豁免节点 ID 自身数字与树形结构计数（见 _noise_exempt），
    防止层级指称类 claim 误报。真正的 gold 专有数值（42.8/774/14/27/54/8.00x…）仍在黑名单内。
    """
    section = claim_section()
    gold_nums = gold_numbers_per_node()
    ids, _, _ = node_ids()
    all_gold_nums = set().union(*gold_nums.values())
    noise = _noise_exempt()
    blacklist = all_gold_nums - noise
    failed = 0
    for nid in ids:
        row = claim_row(section, nid)
        if not row:
            continue  # 缺失已由 ① 报 FAIL
        claim_nums = set(re.findall(r"\d+(?:\.\d+)?", row))
        leaked = claim_nums & blacklist
        if leaked:
            print(f"[FAIL] {nid}: claim 含 gold-tree 专有数值 {sorted(leaked)}")
            failed += 1
    ok = failed == 0
    print(f"[{'PASS' if ok else 'FAIL'}] 31 条 claim 零 gold 专有数值泄漏（黑名单={len(blacklist)} 个 token（全节点并集 {len(all_gold_nums)} − 噪声豁免 {len(noise & all_gold_nums)}）；噪声豁免={sorted(noise)}）")
    return ok, failed


def check_3_baseline():
    """③ M1/M2 基线值从 hit-matrix 独立复算 + identity-baseline 标签存在。"""
    hm = json.load(open(HIT_MATRIX))
    runs = sorted(hm.keys())
    nodes = sorted(hm[runs[0]].keys())
    n_cells = len(runs) * len(nodes)
    h1_total = sum(1 for r in runs for n in nodes if hm[r][n]["h"] == 1)
    # identity baseline: h_claim := h_id → 一致 cell = 全部 cell
    m1_full = f"{n_cells}/{n_cells}"
    gold_cells = len(GOLD_STRICT) * len(runs)
    m1_gold = f"{gold_cells}/{gold_cells}"
    m2 = f"{len(runs)}/{len(runs)}"
    text = open(CLAIM_FILE).read()
    checks = [
        ("M1 全量基线", m1_full, f"M1 全量 | {m1_full}"),
        ("M1 gold strict 切片", m1_gold, f"M1 gold strict 切片 | {m1_gold}"),
        ("M2 run 级", m2, f"M2 | {m2}"),
    ]
    failed = 0
    for label, computed, declared in checks:
        ok = declared in text
        print(f"[{'PASS' if ok else 'FAIL'}] {label}: 复算={computed} 声明于 §3.2={'是' if ok else '否'}")
        failed += (not ok)
    tag_ok = "identity-baseline" in text
    print(f"[{'PASS' if tag_ok else 'FAIL'}] identity-baseline (degenerate, pre-execution) 标签存在")
    failed += (not tag_ok)
    # 附带信息：h=1 实际分布（供报告，不参与 PASS/FAIL）
    print(f"[info] h=1 cells = {h1_total}/{n_cells}；gold strict h=1 = {sum(1 for r in runs for g in GOLD_STRICT if hm[r][g]['h'] == 1)}/{gold_cells}")
    return failed == 0, failed


def check_4_draft():
    """④ DRAFT v2 旧判据措辞已替换 + claim 引用存在。"""
    draft = open(DRAFT_V2).read()
    old_gone = "节点 ID 对得上" not in draft
    new_ref = "o3-claim-list" in draft
    hv_kept = "h_v" in draft
    ok = old_gone and new_ref and hv_kept
    print(f"[{'PASS' if ok else 'FAIL'}] DRAFT v2: 旧判据措辞消失={old_gone} · claim 引用存在={new_ref} · h_v 符号保留={hv_kept}")
    return ok, (0 if ok else 1)


def main():
    results = [check_1_coverage(), check_2_no_leak(), check_3_baseline(), check_4_draft()]
    passed = sum(1 for ok, _ in results if ok)
    failed_checks = sum(1 for ok, _ in results if not ok)
    detail_fails = sum(f for _, f in results)
    print(f"\n=== {passed}/4 检查组 PASS · {detail_fails} 明细项 FAIL ===")
    sys.exit(1 if (failed_checks or detail_fails) else 0)


if __name__ == "__main__":
    main()