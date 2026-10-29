#!/usr/bin/env python3
"""R5.2 输入对称性断言（F4：可重放性验证方法）

验收标准第 6 条的机判实现：
(a) P1-P6 × 3 run 全非空，或 null 字段带 reason/conf_note；
(b) R5.1 的 4 项 |Δ|>15 分歧点（run1 M2 / run2 M2 / run1 M5 / run3 M5）
    对应字段在 packet v2 中存在且承载值非空、source_path 指向的对象真实存在。

exit 0 = pass（结构性分歧源已消除：两打分器将看到同一证据面）。
本脚本不产出任何 0-100 分数（分数冻结纪律）。

source_path 可达性判定（R5.2-sourcepath-hardening · W1 收口，严格模式）：
- git 对象形式（"commit <hash>" + tasks/*.md）→ git show 可达即过；
- 本地文件：提取的全部路径 token 必须在某 base（WS/PFB/workspace 根）下
  join 命中——**全部命中才 PASS**（多文件 source_path 逐 token 独立判定）。
- 已删除 basename glob 兜底（原 W1 局限：同名文件跨 run 误判）。
  EXEMPT 豁免清单预留（预期永不使用）：条目必须带原因注释并在 stdout 明示。
- source_path 填写规范见 evidence-packet-template-v2.md（禁 `...` 缩写与裸 basename）。
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
# EXEMPT 豁免清单（R5.2-sourcepath-hardening A4 裁决：预期永不使用）。
# 条目格式 = (source_path 前缀, 原因)。命中豁免的 token 在 stdout 明示，不静默。
EXEMPT = []

def file_reachable(path_field):
    """source_path 严格可达性（W1 收口）：git 对象可达，或全部路径 token 在 base 下 join 命中。
    无 basename glob 兜底——同名文件跨 run 误判已消除。"""
    s = path_field
    m = re.search(r"commit ([0-9a-f]{7,})", s)
    if m:
        cm = m.group(1)
        fm = re.search(r"(tasks/[^\s]+\.md)", s)
        if fm:
            r = subprocess.run(["git", "-C", PFB, "show", f"{cm}:{fm.group(1)}"],
                               capture_output=True)
            return r.returncode == 0
    # 本地文件：提取全部路径 token（容忍 'WS .../' / 'pfb ...' 前缀；
    # 尾注如 " bench-row 节" 因无扩展名结尾不会被提取）
    toks = re.findall(r"[\w./\-]+\.(?:md|json|txt)", s)
    if not toks:
        return False
    for tok in toks:
        hit = any(os.path.exists(os.path.join(base, tok))
                  for base in (WS, PFB, "/Users/a1-6/Desktop/workspace"))
        if hit:
            continue
        # 查显式豁免（非 glob 兜底）
        exempted = next((reason for prefix, reason in EXEMPT if tok.startswith(prefix)), None)
        if exempted is None:
            print(f"  [EXEMPT-MISS] {tok} — 无 base join 命中且不在 EXEMPT 清单")
            return False
        print(f"  [EXEMPT] {tok} — {exempted}")
    return True

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