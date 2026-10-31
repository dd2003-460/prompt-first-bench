#!/usr/bin/env python3
"""assert-m8-no-suffix.py — 检查 M8 引用无版本后缀（opportunity-set-freeze 协议 §四.4）

规则：matrix/scorecard 文件中引用 M8 口径时，只允许裸名（M8-truth / M8-cover），
不允许带版本后缀（M8-truth-v11 / M8-truth-r4 / M8-truth-J1v11 等）。
原因：口径由 rubric 版本决定，不应硬编码进引用；换 rubric 后引用自动跟随。

用法：python3 assert-m8-no-suffix.py [dir]
默认扫描 experiments/T8-matrix/runs/c3-v3/ 下所有 .md/.json
exit 0 = PASS, exit 1 = FAIL（有违规引用）
"""
import re, sys, pathlib

def main():
    target = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path("experiments/T8-matrix/runs/c3-v3")
    # Pattern: M8-(truth|cover) followed by a version suffix
    bad = re.compile(r"M8-(?:truth|cover)[-_](?:v\d+|r\d+|J1\w+)")
    violations = []
    for f in sorted(target.rglob("*")):
        if not f.is_file() or f.suffix not in (".md", ".json"):
            continue
        try:
            txt = f.read_text(errors="replace")
        except Exception:
            continue
        for i, line in enumerate(txt.splitlines(), 1):
            m = bad.search(line)
            if m:
                violations.append(f"{f}:{i}: {m.group()} → {line.strip()[:80]}")
    
    if violations:
        print(f"FAIL: {len(violations)} M8 带后缀引用:")
        for v in violations:
            print(f"  {v}")
        sys.exit(1)
    else:
        print(f"PASS: 0 M8 带后缀引用（扫描 {target}）")
        sys.exit(0)

if __name__ == "__main__":
    main()
