#!/usr/bin/env python3
"""assert-kappa-receipt.py — RV3G4-kappa-receipt-assert（G4 强制机械化候选 C2 落地）

门禁语义：DRAFT-rubric-v3-v2.md §0 原则 4 / §3.3 R5 —— 换位双判 + κ≥0.6 + 长度去偏，
评分前不过门禁不开评。本脚本机判「门禁执行回执」的存在性与格式，消除
g4-vulnerability-crosscheck S3「κ 门禁无执行回执 → unverified」状态。

SIGNAL ONLY 边界（同 assert-prior-source.py 判据）：本脚本验证的是**回执元数据**
（存在性 + schema），不是打分过程合规性（是否真的独立、真的换位）——后者不可机判
（AUDIT-report finding #15）。回执缺失/格式错 = FAIL（评分无效声明可机判）；
κ 数值低于阈值 = SIGNAL（阈值裁决留人工，脚本只暴露数值）。

最小 schema 提案（g5-optimization-list C2「schema 不存在，需最小 schema 提案」交付物；
相对 g5 四字段 gate_passed/kappa_value/method/judges 的改动及理由见
loop-artifacts/stages/01/RV3G4kra-stages01-03.md F1）：

  kappa-receipt.json = {
    "gate": "role-swap-dual-judge",   # str，固定值（防其他方法名混用）
    "kappa_value": <float -1..1>,      # 条目层二值 Cohen's κ（DRAFT v2 R-02 口径；
                                       #   理论界 [-1,1]，负值 = 一致性差于随机，合法记录值）
    "method": <str 非空>,             # κ 计算说明（含 n_items）
    "judges": [<str>, <str>],         # 恰两个非空 ID（换位双判 = 两 judge；
                                      #   ≥3 judge Fleiss'κ 属 R5.2-third-scorer 范围）
    "length_debias_check": "pass" | "na",  # R5 第三要件；"na" 必须配 note
    "length_debias_note": <str>,       # length_debias_check="na" 时必填（如实登记缺口）
    "scored_artifact": <str 相对 ROOT 可解析>  # 被门禁保护的评分文件（防张冠李戴）
  }
  注：不设 gate_passed 布尔——它是 kappa_value >= KAPPA_MIN 的派生量，双写 = 漂移源；
  阈值判断由本脚本现场执行（KAPPA_MIN = 0.6，DRAFT v2 R5）。

用法：python3 assert-kappa-receipt.py [评分目录]
  默认目录 = bench/rubric-v3/ablation（当前消融评分面）。
exit 0 = 回执存在且 schema 合法（κ<0.6 时输出 SIGNAL 但仍 exit 0）
exit 1 = 回执缺失/不可读/schema 违例（FAIL，打印失败项）
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DEFAULT_DIR = ROOT / "bench/rubric-v3/ablation"
KAPPA_MIN = 0.6  # DRAFT-rubric-v3-v2.md R5 门禁阈值
GATE_NAME = "role-swap-dual-judge"

failures = []


def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail and not ok else ""))
    if not ok:
        failures.append(name)


target_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DIR
receipt_path = target_dir / "kappa-receipt.json"

print(f"target dir : {target_dir}")
print(f"receipt    : {receipt_path}")
print("NOTE: receipt metadata check — NOT a scoring-process compliance verdict (finding #15)")

if not target_dir.is_dir():
    print(f"ERROR target dir does not exist: {target_dir}（区别于回执缺失——目录本身不存在，无法判定门禁状态）")
    sys.exit(1)

# ---- 分支①：存在性 ----
if not receipt_path.is_file():
    check("① kappa-receipt.json exists", False, f"not found at {receipt_path} → 评分无效（R5 门禁无执行回执）")
    print()
    print(f"RESULT: FAIL ({len(failures)} checks failed)")
    sys.exit(1)

try:
    r = json.loads(receipt_path.read_text(encoding="utf-8"))
    check("① kappa-receipt.json readable as JSON", True)
except Exception as e:
    check("① kappa-receipt.json readable as JSON", False, str(e))
    print()
    print(f"RESULT: FAIL ({len(failures)} checks failed)")
    sys.exit(1)

if not isinstance(r, dict):
    check("① top-level is object", False, f"type={type(r).__name__}")
    print()
    print(f"RESULT: FAIL ({len(failures)} checks failed)")
    sys.exit(1)

# ---- 分支②：schema 逐字段 ----
check("② gate == 'role-swap-dual-judge'", r.get("gate") == GATE_NAME, f"got {r.get('gate')!r}")

kv = r.get("kappa_value")
check("② kappa_value is number in [-1,1]",
      isinstance(kv, (int, float)) and not isinstance(kv, bool) and -1.0 <= kv <= 1.0,
      f"got {kv!r}")

check("② method non-empty str", isinstance(r.get("method"), str) and len(r["method"].strip()) > 0,
      f"got {r.get('method')!r}")

jd = r.get("judges")
check("② judges is list of exactly 2 non-empty str",
      isinstance(jd, list) and len(jd) == 2 and all(isinstance(j, str) and j.strip() for j in jd),
      f"got {jd!r}")

ldc = r.get("length_debias_check")
check("② length_debias_check in {'pass','na'}", ldc in ("pass", "na"), f"got {ldc!r}")
if ldc == "na":
    note = r.get("length_debias_note")
    check("② length_debias_note required when check='na'",
          isinstance(note, str) and len(note.strip()) > 0, f"got {note!r}")

art = r.get("scored_artifact")
ok_art = isinstance(art, str) and (ROOT / art).is_file()
check("② scored_artifact resolvable under ROOT", ok_art, f"got {art!r}")

# ---- 分支③：阈值 SIGNAL（不参与 exit code；schema FAIL 时不输出——避免陈旧值 SIGNAL 与 FAIL 同屏误导） ----
if not failures and isinstance(kv, (int, float)) and not isinstance(kv, bool):
    if kv < KAPPA_MIN:
        print(f"SIGNAL kappa_value={kv} < KAPPA_MIN={KAPPA_MIN} → 门禁阈值未达 [人工裁决，脚本不代判]")
    else:
        print(f"SIGNAL kappa_value={kv} >= KAPPA_MIN={KAPPA_MIN} → 门禁阈值达标")

print()
if failures:
    print(f"RESULT: FAIL ({len(failures)} checks failed)")
    sys.exit(1)
print("RESULT: PASS (receipt present + schema valid; metadata check only — see header)")
sys.exit(0)