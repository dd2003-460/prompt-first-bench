#!/usr/bin/env python3
"""assert-audit8-erratum.py — AUDIT-report erratum 防漂移断言（RV3G6-audit8-erratum）

校验 bench/rubric-v3/AUDIT-report.md 的 2026-10-30 erratum 已正确落地且不再回漂：
  ① 修正值定点断言（L108/L109/L172/L252/§8 表的 8 个新值存在）
  ② 旧错误 token 黑名单全文扫描零命中（含「可优于 W3-orig」语义句）
  ③ gmr-criterion-freeze.md §4 byte-exact 块 == AUDIT §8 实际文本（diff 空）
  ④ 定性关键词仍在（勘误不得误伤定性结论）
exit 0 = 全部 PASS, exit 1 = 存在 FAIL
"""
import re, sys

AUDIT = "bench/rubric-v3/AUDIT-report.md"
FREEZE = "bench/rubric-v3/gmr-criterion-freeze.md"

audit = open(AUDIT).read()
freeze = open(FREEZE).read()

passed = failed = 0
def check(name, ok, detail=""):
    global passed, failed
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail and not ok else ""))
    passed += bool(ok)
    failed += (not ok)

# ① 修正值定点断言（每值在 AUDIT 中至少出现 1 次；区间串要求完整形态）
required = [
    ("E1a W1 范围", "[8.60, 12.40]"),
    ("E1b W2-orig 范围", "[8.20, 8.40]"),
    ("E1c W2-new 范围", "[8.80, 10.20]"),
    ("E1d W3/W4-new 范围", "[7.40, 7.60]"),
    ("E2a orig 侧 W1 id-order", "W1=10.2、W2=8.2、W3=W4=5.4"),
    ("E2b new 侧 id-order", "new judge 侧 W1=10.2、W2=9.8、W3=W4=7.6"),
    ("E3 正确结论句", "仍劣于 W3-orig（5.40, 0-based）"),
    ("E5 引用模板", "10.2（0-based，落盘顺序 tie-break；精确范围 [8.60, 12.40]"),
    ("Erratum 节存在", "## Erratum（2026-10-30 · RV3G6-audit8-erratum）"),
]
for name, token in required:
    check(f"① {name}", token in audit, f"未找到: {token!r}")

# ② 旧错误 token 黑名单（全文零命中）
blacklist = [
    "[2.60, 6.40]",
    "[7.80, 8.00]",
    "[5.20, 6.60]",
    "[6.80, 7.00]",
    "可优于 W3-orig",
    "W1=9.8",
]
for token in blacklist:
    # Erratum 节的修正清单表内允许引用原值（带「错」标注的溯源用途）——排除 Erratum 节后扫描正文
    body = audit.split("## Erratum（2026-10-30")[0]
    hits = [m.start() for m in re.finditer(re.escape(token), body)]
    check(f"② 黑名单零命中 {token!r}（正文区）", not hits, f"命中 {len(hits)} 处")

# ③ freeze doc §4 byte-exact 块 == AUDIT §8 实际文本
def extract_section(text, start_marker, end_marker):
    i = text.index(start_marker)
    j = text.index(end_marker, i)
    return text[i:j].rstrip("\n")

audit_s8 = extract_section(audit, "## §8 (e) Tie-sensitivity 引用规则", "\n---")
freeze_block = extract_section(
    freeze,
    "<!-- BEGIN BYTE-EXACT QUOTE: AUDIT-report.md §8",
    "<!-- END BYTE-EXACT QUOTE -->",
).strip()
# 块内首行是抄录起始 HTML 注释，去掉后应与 AUDIT §8 逐字一致
freeze_block = re.sub(r"^<!-- BEGIN BYTE-EXACT QUOTE:[^\n]*\n", "", freeze_block)
check("③ byte-exact 块 == AUDIT §8 文本", freeze_block == audit_s8,
      f"diff: block_len={len(freeze_block)} audit_len={len(audit_s8)}")

# ④ 定性关键词仍在（勘误不得误伤定性结论）
qualitative = [
    "tie-robust 单值",
    "对 tie-break 规则敏感",
    "禁止各方案取各自最优",
    "跨方案比较必须在预注册 tie-break 下进行",
    "W3-orig / W4-orig | 5.40",
]
for kw in qualitative:
    check(f"④ 定性关键词 {kw!r}", kw in audit)

print(f"\n=== {passed} PASS / {failed} FAIL ===")
sys.exit(1 if failed else 0)