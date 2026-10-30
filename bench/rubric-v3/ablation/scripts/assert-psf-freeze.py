#!/usr/bin/env python3
"""assert-psf-freeze.py — RV3B1-prompt-side-freeze 冻结断言（R-09 部分落地机判防护）

三组检查：
① loop/prompt-first/02.5-cross-check.md 附录区 D2 副本 == DRAFT v2 L155-L160 正文 6 行（byte-exact）
② §3.2 变体矩阵含 V3-sham 行，且既有六变体行文本不变（对照 batch1 收口 commit 61416b4 快照）
③ §4.4 存在 + 代码块内正文行数 = 6 + 总字符数与 D2 正文偏差 ≤10% + 黑名单 token 零命中

用法：python3 assert-psf-freeze.py → exit 0 = 全部通过；exit 1 = FAIL（打印失败项）
变异测试：见 04 执行日志（逐项破坏后脚本必须 FAIL）。
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DRAFT = ROOT / "bench/rubric-v3/DRAFT-rubric-v3-v2.md"
STAGE_025 = ROOT / "loop/prompt-first/02.5-cross-check.md"
FROZEN_COMMIT = "61416b43f80e28d9785137f320003bf8e121d306"  # batch1 收口 commit（revision-log「回填状态」节登记）

BLACKLIST = [
    "边界类型", "数学/理论边界", "实操边界", "信息边界",
    "research_required", "OPEN/矛盾条目", "未完成追问",
    "候选集", "搜索预算", "分区 a/b/c/d",
]

failures = []


def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail and not ok else ""))
    if not ok:
        failures.append(name)


draft_lines = DRAFT.read_text(encoding="utf-8").split("\n")
s025 = STAGE_025.read_text(encoding="utf-8")

# ---- 定位 D2 正文 6 行（按内容锚定，不依赖行号——防未来行号漂移）----
start = next((i for i, l in enumerate(draft_lines) if l.startswith("【边界类型声明】（硬性，不许跳过）")), None)
if start is None:
    check("D2 anchor in DRAFT v2", False, "未找到【边界类型声明】标题行")
    sys.exit(1)
d2_body = draft_lines[start:start + 6]
check("D2 body = 6 lines ending at 终止注记 line",
      d2_body[-1].startswith("未声明边界类型的终止注记视为未完成追问。"),
      f"got tail: {d2_body[-1]!r}")

# ---- 检查①：02.5 附录区 byte-exact ----
m = re.search(r"## 附录 · 冻结件：D2 边界类型声明段.*?```\n(.*?)\n```", s025, re.S)
check("① 02.5 appendix section exists", m is not None)
if m:
    copy = m.group(1).split("\n")
    check("① 02.5 D2 copy byte-exact vs DRAFT v2 L155-L160", copy == d2_body,
          f"diff: {[(a, b) for a, b in zip(copy, d2_body) if a != b]} len {len(copy)} vs {len(d2_body)}")

# ---- 检查②：§3.2 变体矩阵 ----
matrix_rows = [l for l in draft_lines if re.match(r"\| V\d?-?\w*-?\w* \|", l)]
variant_names = [re.match(r"\|\s*([\w-]+)\s*\|", l).group(1) for l in matrix_rows]
check("② V3-sham row present in §3.2 matrix", "V3-sham" in variant_names, f"rows: {variant_names}")
v3sham_row = next((l for l in matrix_rows if l.startswith("| V3-sham |")), "")
check("② V3-sham row references §4.4", "§4.4" in v3sham_row and "R-09" in v3sham_row)

try:
    frozen = subprocess.run(
        ["git", "show", f"{FROZEN_COMMIT}:bench/rubric-v3/DRAFT-rubric-v3-v2.md"],
        capture_output=True, text=True, cwd=ROOT, check=True).stdout.split("\n")
    frozen_rows = [l for l in frozen if re.match(r"\| V\d?-?\w*-?\w* \|", l)]
    six = {"V0-baseline", "V1-full", "V1-align", "V2-nocoverage", "V3-noboundary", "V-sham"}
    now_map = {re.match(r"\|\s*([\w-]+)\s*\|", l).group(1): l for l in matrix_rows}
    same = all(now_map.get(n, "<missing>") == fr for fr, n in
               [(fr, re.match(r"\|\s*([\w-]+)\s*\|", fr).group(1)) for fr in frozen_rows])
    check("② existing six variant rows unchanged vs frozen commit",
          set(now_map) >= six and same,
          f"changed: {[n for n in six if now_map.get(n) != next((fr for fr in frozen_rows if n in fr), '<missing>')]}")
except subprocess.CalledProcessError as e:
    check("② frozen commit snapshot retrievable", False, str(e))

# ---- 检查③：§4.4 sham 段 ----
m44 = re.search(r"### 4\.4 V3-sham 替换段.*?\n```\n(.*?)\n```", DRAFT.read_text(encoding="utf-8"), re.S)
check("③ §4.4 section + code block exist", m44 is not None)
if m44:
    body44 = m44.group(1).split("\n")
    chars44 = sum(len(l) for l in body44)
    chars_d2 = sum(len(l) for l in d2_body)
    dev = abs(chars44 - chars_d2) / chars_d2 * 100
    check("③ §4.4 body line count = 6", len(body44) == 6, f"got {len(body44)}")
    check("③ §4.4 char deviation ≤10%", dev <= 10.0, f"{chars44} vs {chars_d2} = {dev:.1f}%")
    hits = [t for t in BLACKLIST if t in m44.group(1)]
    check("③ §4.4 blacklist tokens zero hit", not hits, f"hits: {hits}")

print()
if failures:
    print(f"RESULT: FAIL ({len(failures)} checks failed)")
    sys.exit(1)
print("RESULT: PASS (all checks green)")
sys.exit(0)