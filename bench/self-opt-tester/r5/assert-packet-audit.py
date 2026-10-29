#!/usr/bin/env python3
"""R5.2-audit 原 r4 packet 单行摘要全字段审计——机判脚本

审计对象：r4/independent-scoring-deepseek.json → evidence_packet 字段（v1 单行摘要）。
对照 packet-audit-r4-v1.md 的 12+1 条原子断言，对**可机械核验**的断言自动比对原始证据。

exit 0 语义 = 所有 confirmed 断言复核通过 **且** 所有已知 mismatch 断言按预期复现
（即"该错配确实存在于 v1 packet"也被机判确认）。
SKIP 项：C4 (unverified，本地无计时源) / C12 (形式性文本判断，人工裁决) —— 不参与 exit code。

本脚本不产出任何 0-100 分数（分数冻结纪律）。
"""
import json, os, re, subprocess, sys

PFB = "/Users/a1-6/Desktop/workspace/pfb"
WS = "/Users/a1-6/Desktop/workspace/projects/AI-计算科学/D1-efficiency-optimization/tasks/self-optimization-tester/loop-artifacts/stages/04.5/r3"
PACKET_V1 = os.path.join(PFB, "bench/self-opt-tester/r4/independent-scoring-deepseek.json")

failures = []
passes = []
skips = []

def check(label, ok, detail=""):
    (passes if ok else failures).append(f"{label} {detail}")
    print(("PASS " if ok else "FAIL ") + label + (f" — {detail}" if detail else ""))

def skip(label, reason):
    skips.append(label)
    print(f"SKIP {label} — {reason}")

def jload(p):
    with open(p) as f:
        return json.load(f)

# ---------- 读取审计对象与原始证据 ----------
packet_v1 = jload(PACKET_V1)["evidence_packet"]
check("v1 packet 字段可读", isinstance(packet_v1, str) and len(packet_v1) > 50, f"len={len(packet_v1)}")

run1_state = jload(os.path.join(WS, "run1/loop-state.json"))
run1_r1 = jload(os.path.join(WS, "run1/loop-state-r1.json"))
run2_state = jload(os.path.join(WS, "run2/loop-state.json"))
run3_state = jload(os.path.join(WS, "run3/loop-state.json"))
token_ledger = jload(os.path.join(WS, "run1/token-ledger.json"))
token_counts = open(os.path.join(WS, "run2/token-counts.txt")).read()
review3 = open(os.path.join(WS, "run3/03-review.md")).read()

# ---------- confirmed 断言（应复核通过） ----------
# C1 run1 7锚点
check("C1 run1 '7锚点' anchors_count=7", run1_state.get("anchors_count") == 7,
      f"actual={run1_state.get('anchors_count')}")

# C2 run1 5.11M累计未切分（数值 ±1% + scope_note 含"切分"声明）
cum = token_ledger.get("input_tokens_cumulative", 0)
check("C2a run1 5.11M input_tokens_cumulative≈5.11M(±1%)",
      abs(cum - 5_110_000) / 5_110_000 <= 0.01, f"actual={cum}")
note = token_ledger.get("run1_scope_note", "")
check("C2b run1 scope_note 声明未切分到 run 级", "切分" in note and "待 R3.5" in note,
      f"note[:40]={note[:40]}")

# C5 run2 10锚点
check("C5 run2 '10锚点' anchors_count=10", run2_state.get("anchors_count") == 10,
      f"actual={run2_state.get('anchors_count')}")

# C6 run2 12,086 o200k（RULE LOAD TOTAL 行）
m = re.search(r"^TOTAL\s+\d+B\so200k=(\d+)", token_counts, re.M)
check("C6 run2 '12,086 o200k' RULE LOAD TOTAL o200k=12086", m is not None and m.group(1) == "12086",
      f"actual={m.group(1) if m else 'NOT FOUND'}")

# C7 run2 2降级
deg2 = run2_state.get("degraded", [])
check("C7 run2 '2降级' degraded 数组长度=2", len(deg2) == 2, f"actual={len(deg2)}")

# C8 run3 7锚点
check("C8 run3 '7锚点' anchors_count=7", run3_state.get("anchors_count") == 7,
      f"actual={run3_state.get('anchors_count')}")

# C9 run3 无网络（execution-log M6 行 + token-split run3.note 双源 grep）
execlog3 = open(os.path.join(WS, "run3/execution-log.md")).read()
split = jload(os.path.join(PFB, "bench/self-opt-tester/r4/token-split.json"))
check("C9 run3 '无网络' execution-log M6 标注", "无网络" in execlog3)
check("C9b run3 '无网络' token-split run3.note", "无网络" in split["runs"]["run3"].get("note", ""))

# C10 run3 3模板缺陷（^## 缺陷 标题计数）
n_defects = len(re.findall(r"^## 缺陷", review3, re.M))
check("C10 run3 '3模板缺陷' 03-review.md 缺陷标题数=3", n_defects == 3, f"actual={n_defects}")

# ---------- mismatch 断言（应按预期复现 = PASS） ----------
# C3/X4 run1 "无降级" vs degraded[3]
deg1 = run1_r1.get("degraded", [])
check("C3/X4 run1 '无降级' 错配复现（degraded 非空）", len(deg1) >= 1,
      f"degraded 实际={len(deg1)} 项 → packet '无降级' 字面为假")

# C11/X2 run3 "任务书25行"：25 实为 run2 task-brief 实测值
wc2 = subprocess.run(["wc", "-l", os.path.join(PFB, "bench/self-opt-tester/run2-arena/task-brief.md")],
                     capture_output=True, text=True).stdout.split()[0]
check("C11/X2 run3 '任务书25行' 错配复现（25=run2 实测值）", wc2 == "25",
      f"run2 task-brief wc -l={wc2}；run3 无落盘文件（自估 ~45）→ 张冠李戴成立")

# X6 adjudication-step2 inputs "49/25/25"：run1 实测 24 ≠ 49
step2 = jload(os.path.join(PFB, "bench/self-opt-tester/r4/adjudication-step2.json"))
inputs = step2.get("inputs", "")
check("X6a step2 inputs 含 '49/25/25' 主张", "49/25/25" in inputs)
r = subprocess.run(["git", "-C", PFB, "show", "d96f5db:tasks/003-self-optimization-tester.md"],
                   capture_output=True, text=True)
lines_run1 = r.stdout.count("\n") + (0 if r.stdout.endswith("\n") else 1) if r.returncode == 0 else None
check("X6b run1 任务书实测行数≠49（X3 冻结值 24）", lines_run1 == 24,
      f"git show d96f5db wc -l={lines_run1} → '49' 无出处，错配成立")
check("X6c step2 run1_M2 裁决理由引用了 49", "49 行" in step2["adjudications"]["run1_M2"]["reason"],
      f"reason={step2['adjudications']['run1_M2']['reason']}")

# ---------- SKIP 项（不参与 exit code） ----------
skip("C4 run2 '14m27s'", "unverified——原始计时源为 arena 网页会话（外部），本地无账本可重建（X5）")
skip("C12 'M1-M6 定义+' 句", "形式性 mismatch（声称-内容不符），人工裁决见审计表（X7）")

# ---------- 汇总 ----------
print(f"\n=== {len(passes)} PASS / {len(failures)} FAIL / {len(skips)} SKIP ===")
if failures:
    print("FAILURES:")
    for f in failures:
        print("  -", f)
    sys.exit(1)
print("VERDICT: 原 v1 packet 单行摘要机判审计通过——8 条 confirmed 断言全部复核成立；"
      "3 条 mismatch（C3/X4、C11/X2、X6）按预期复现（错配确实存在，已登记）；"
      "1 条 unverified（C4/X5）+ 1 条形式性（C12/X7）SKIP 留人工结论。"
      "本脚本不改任何分数值（分数冻结纪律）。")
sys.exit(0)