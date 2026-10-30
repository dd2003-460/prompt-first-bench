#!/usr/bin/env python3
"""assert-leak-triage.py — 罕见 token 泄题扫描（主数字+罕见随机判断）

动机：hit-matrix 的 h 值由 judge 判「是否命中 gold」，但 judge 可能把「模型恰好写出
gold 里的具体数值」误当命中。本脚本做独立机判：从 gold-tree.md 提取「罕见数值 token」
（小数 x 倍数 + ≥3位整数，排除任务书 prompt-V0.txt 里已有的），扫全部 run 的 evidence，
任何命中即 FAIL——说明该 cell 的「命中」可能来自答案泄漏而非真实推理。

白名单（合法引用，非泄漏）：
  - 公开硬件型号（3090）：候选集调研必然出现
  - 公式换算常数（3600 = 秒/时）：λ_raw=3600/t_task 自带

exit code: 0 = 无泄漏 / 1 = 存在泄漏 cell。
"""
import json, re, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
GOLD = BASE / "gold-tree.md"
PROMPT = BASE / "prompt-V0.txt"
MATRIX = BASE / "hit-matrix.json"

KNOWN_PUBLIC = {"3090", "3600"}


def rare_tokens() -> list[str]:
    gold = GOLD.read_text(encoding="utf-8")
    toks = set(re.findall(r"\d+\.\d+x\b", gold)) | {t for t in re.findall(r"\b\d{3,}\b", gold)}
    prompt = PROMPT.read_text(encoding="utf-8")
    return sorted(toks - {t for t in toks if t in prompt} - KNOWN_PUBLIC)


def main() -> int:
    toks = rare_tokens()
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    leaks = {}
    for rk, cells in matrix.items():
        for node, cell in cells.items():
            ev = str(cell.get("evidence") or "")
            found = [t for t in toks if t in ev]
            if found:
                leaks.setdefault(rk, {})[node] = found
    total = sum(len(v) for v in leaks.values())
    print(f"[rare-token-scan] tokens={len(toks)} leak_cells={total}")
    for rk, nodes in leaks.items():
        for n, ts in nodes.items():
            print(f"[LEAK] {rk}/{n}: {ts}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
