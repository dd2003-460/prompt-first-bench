#!/usr/bin/env python3
"""assert-prior-source.py — RV3G4-prior-source-assert（G4 强制机械化候选落地）

SIGNAL ONLY: provenance metadata check, NOT a family-independence verdict.
校验 prior-estimates.json 的 p_tilde_provenance 元数据块：
① p_tilde_provenance 顶层对象存在 + independent_sources 为非空列表
② 每条 source：judge_id 非空字符串 + artifact 相对 ROOT 可解析且 is_file()
   + role="blind-reestimate" 条目的 judge_id 与 judge-blindtest-r1.json:judge byte-exact
③ judge_id 去重数 ≥ N_MIN（独立生成源下限；≥3 异族标准见 rubric-v3 遗留 #1，不在本脚本范围）

用法：python3 assert-prior-source.py → exit 0 = PASS；exit 1 = FAIL（打印失败项）
家族隔离说明：两源同属 Qwen 家族的事实登记于 prior-estimates.json:p_tilde_provenance.note
（family-independent: false），跨家族闭环待 rubric-v3 遗留 #1 另开 goal。
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PRIOR = ROOT / "bench/rubric-v3/ablation/prior-estimates.json"
BLINDTEST = ROOT / "bench/rubric-v3/ablation/judge-blindtest-r1.json"
N_MIN = 2  # G4 导出「≥N」最小落地值；≥3 异族 = rubric-v3 遗留 #1（另开 goal）

failures = []


def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail and not ok else ""))
    if not ok:
        failures.append(name)


print("SIGNAL ONLY: provenance metadata check, NOT a family-independence verdict")

prior = json.loads(PRIOR.read_text(encoding="utf-8"))
blind = json.loads(BLINDTEST.read_text(encoding="utf-8"))

# ---- 检查①：provenance 对象存在 ----
prov = prior.get("p_tilde_provenance")
check("① p_tilde_provenance top-level object exists", isinstance(prov, dict),
      f"type={type(prov).__name__}")
sources = prov.get("independent_sources") if isinstance(prov, dict) else None
check("① independent_sources is non-empty list",
      isinstance(sources, list) and len(sources) > 0,
      f"type={type(sources).__name__} len={len(sources) if hasattr(sources, '__len__') else 'n/a'}")

if isinstance(sources, list):
    # ---- 检查②：逐条 source 结构 ----
    for i, s in enumerate(sources):
        prefix = f"② source[{i}] ({s.get('role', '?')})"
        jid = s.get("judge_id")
        check(f"{prefix} judge_id non-empty str", isinstance(jid, str) and len(jid.strip()) > 0,
              f"got {jid!r}")
        art = s.get("artifact")
        ok_art = isinstance(art, str) and (ROOT / art).is_file()
        check(f"{prefix} artifact resolvable under ROOT", ok_art, f"got {art!r}")
        if s.get("role") == "blind-reestimate":
            ref = blind.get("judge")
            check("② blind-reestimate judge_id byte-exact vs judge-blindtest-r1.json:judge",
                  jid == ref, f"registered={jid!r} actual={ref!r}")

    # ---- 检查③：独立性下限（judge_id 去重数）----
    distinct = {s.get("judge_id") for s in sources if isinstance(s.get("judge_id"), str)}
    check(f"③ distinct judge_id count >= N_MIN={N_MIN}", len(distinct) >= N_MIN,
          f"distinct={sorted(d for d in distinct if d)}")

print()
if failures:
    print(f"RESULT: FAIL ({len(failures)} checks failed)")
    sys.exit(1)
print("RESULT: PASS (all checks green; metadata gate — NOT a family-independence verdict, see header)")
sys.exit(0)
