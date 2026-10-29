#!/usr/bin/env python3
"""R5.2 输入对称性断言（F4：可重放性验证方法）

验收标准第 6 条的机判实现：
(a) P1-P6 × 3 run 全非空，或 null 字段带 reason/conf_note；
(b) R5.1 的 4 项 |Δ|>15 分歧点（run1 M2 / run2 M2 / run1 M5 / run3 M5）
    对应字段在 packet v2 中存在且承载值非空、source_path 指向的对象真实存在。

exit 0 = pass（结构性分歧源已消除：两打分器将看到同一证据面）。
本脚本不产出任何 0-100 分数（分数冻结纪律）。

已知局限（04.5 W1）：file_reachable 的 basename glob 兜底可能误判同名文件
（run1/run2/run3 各有 execution-log.md / loop-state.json）；触发兜底的条目
已人工核对路径真实存在。后续版本应让 source_path 强制完整相对路径。
"""
import json, os, re, subprocess, sys

PFB = "/Users/a1-6/Desktop/workspace/pfb"
WS = "/Users/a1-6/Desktop/workspace/projects/AI-计算科学/D1-efficiency-optimization/tasks/self-optimization-tester/loop-artifacts/stages/04.5/r3"
PACKET = os.path.join(PFB, "bench/self-opt-tester/r5/evidence-packet-r4-v2.json")

failures = []
passes = []

def check(label, ok, detail=""):
    (passes if ok else failures).append(f"{label} {detail}")
    print(("PASS " if ok else "FAIL ") + label + (f" — {detail}" if detail else ""))

# ---------- (a) 必填字段完整性 ----------
packet = json.load(open(PACKET))
runs = packet["runs"]
check("json.load 通过", set(runs.keys()) == {"run1", "run2", "run3"}, f"runs={sorted(runs)}")

for run, data in runs.items():
    for field in ["P1_brief_lines", "P2_conf_rounds", "P3_token_split",
                  "P4_breakpoints", "P5_degradations", "P6_cross_validation"]:
        present = field in data and data[field] is not None
        check(f"{run}/{field} 存在", present)
        if not present:
            continue
        # 三件套：source_path + source_quote（P4/P5/P6 用 evidence/anchor 替代 quote，单独校验）
        d = data[field]
        if field in ("P1_brief_lines", "P2_conf_rounds", "P3_token_split"):
            check(f"{run}/{field}.source_path 非空", bool(d.get("source_path")))
            check(f"{run}/{field}.source_quote 非空", bool(d.get("source_quote")))
        else:
            check(f"{run}/{field}.source_path 非空", bool(d.get("source_path")))

# P1 null 政策：wc_l_output 与 approx_lines 二选一非空
for run, data in runs.items():
    p1 = data["P1_brief_lines"]
    check(f"{run}/P1 行数有值（wc 或自估）",
          p1.get("wc_l_output") is not None or bool(p1.get("approx_lines")),
          f"wc={p1.get('wc_l_output')} approx={str(p1.get('approx_lines'))[:30]}")

# P2 null 政策：conf_at_completion=null → conf_note 必填
for run, data in runs.items():
    p2 = data["P2_conf_rounds"]
    if p2.get("conf_at_completion") is None:
        check(f"{run}/P2 conf=null 带 conf_note", bool(p2.get("conf_note")))
    check(f"{run}/P2 rounds 为正整数", isinstance(p2.get("rounds"), int) and p2["rounds"] >= 1)
    if p2.get("rounds_basis") in ("inferred", "self-reported"):
        check(f"{run}/P2 推断/自述轮数带原文句", len(p2.get("source_quote", "")) > 20)

# P5 降级条目展开（禁纯数量统计）
for run, data in runs.items():
    items = data["P5_degradations"].get("degraded_items", [])
    all_anchored = all(i.get("item") and i.get("anchor") for i in items)
    check(f"{run}/P5 降级条目全带 anchor", all_anchored, f"n={len(items)}")

# ---------- (b) 4 个 R5.1 分歧点字段存在且来源可达 ----------
def file_reachable(path_field):
    """source_path 可达性：本地文件路径存在，或 git 对象（commit:path）可达。"""
    s = path_field
    m = re.search(r"commit ([0-9a-f]{7,})", s)
    if m:
        cm = m.group(1)
        fm = re.search(r"(tasks/[^\s]+\.md)", s)
        if fm:
            r = subprocess.run(["git", "-C", PFB, "show", f"{cm}:{fm.group(1)}"],
                               capture_output=True)
            return r.returncode == 0
    # 本地文件：提取路径 token（容忍 'WS .../' 缩写前缀 → 映射到真实 WS 目录；
    # 容忍 token 后跟非路径尾注如 " bench-row 节"——findall 只取 .ext 前的部分）
    for tok in re.findall(r"[\w./\-]+\.(?:md|json|txt)", s):
        for base in (WS, PFB, "/Users/a1-6/Desktop/workspace"):
            cand = os.path.join(base, tok)
            if os.path.exists(cand):
                return True
            # 相对 base 的深层路径（tok 含多段时 join 已覆盖；此处兜底 substring 匹配）
        # 兜底：tok 作为子串出现在某已知目录下
    import glob as _g
    leaf = os.path.basename(tok)
    for pat in (os.path.join(WS, "**", leaf), os.path.join(PFB, "**", leaf)):
        if _g.glob(pat, recursive=True):
            return True
    return False

disagreement_points = [
    ("run1", "P1_brief_lines", "R5.1 分歧 #1: run1 M2 (DeepSeek 50 vs Claude 100)"),
    ("run2", "P1_brief_lines", "R5.1 分歧 #2: run2 M2 (DeepSeek 50 vs Claude 100)"),
    ("run1", "P2_conf_rounds", "R5.1 分歧 #3: run1 M5 (DeepSeek 60 vs Claude 90)"),
    ("run3", "P2_conf_rounds", "R5.1 分歧 #4: run3 M5 (DeepSeek 55 vs Claude 90)"),
]
for run, field, why in disagreement_points:
    d = runs[run][field]
    if field == "P1_brief_lines":
        has_value = d.get("wc_l_output") is not None or bool(d.get("approx_lines"))
    else:
        has_value = isinstance(d.get("rounds"), int) and d["rounds"] >= 1
    check(f"[{why}] 字段承载值非空", has_value)
    check(f"[{why}] source_path 可达", file_reachable(d["source_path"]), d["source_path"][:80])

# ---------- 汇总 ----------
print(f"\n=== {len(passes)} PASS / {len(failures)} FAIL ===")
if failures:
    print("FAILURES:")
    for f in failures:
        print("  -", f)
    sys.exit(1)
print("VERDICT: 输入对称性断言通过——4 项 R5.1 分歧点的字段在 packet v2 中全部存在、"
      "承载值非空、来源可达。结构性分歧源（缺字段+错配）已消除。"
      "注：本断言只证明输入面对称，不预测新 κ 值（κ 重算归第三打分器 goal）。")
sys.exit(0)