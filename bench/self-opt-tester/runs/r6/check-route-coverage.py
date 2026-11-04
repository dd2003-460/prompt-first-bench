#!/usr/bin/env python3
"""R6 · 阶段路由漏载检测器（漏载失效模式 R/A/G/X 的机检实现）

背景：R6 把「全量注入 7 个 loop 文件」改成「INDEX.md 路由 + 阶段包」。
削减规则负载的前提是**被切掉的文件确实不需要**。若某个规则文件里点名要求读另一个文件，
而路由表没把它排进该阶段包，agent 就会静默漏读 —— 这类缺口必须机检，不能靠人肉 review。

四类断言（对应 loop-artifacts/stages/01/R6-01-decomp.md 的正交分解）：
  R-miss  规则缺载：阶段包成员集合为空 / 少于 2 个（结构自检）
  X-miss  路由缺载：规则文件 A 引用了文件 B，但 B 不在 route(stage(A)) 里
          （distinguish: dangling = 被引用的文件根本不存在）
  A-miss  产出缺载：规则要求读上游 loop-artifacts/stages/<N>/，但该目录无产出
  G-miss  门禁缺载：已存在的 stage 目录里没有 verdict 判定行

用法：
  python3 check-route-coverage.py                     # 默认检查仓库内 INDEX.md
  python3 check-route-coverage.py --index /tmp/a.md   # 检查另一版路由表（回归用）
  python3 check-route-coverage.py --json              # 机器可读
退出码：0 = 无 X-miss 且无 dangling；1 = 有缺口；2 = 路由表解析失败
无网络依赖；不写任何文件（纯只读检查）。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
LOOP = REPO / "loop" / "prompt-first"
ARTIFACTS = REPO / "loop-artifacts" / "stages"

CORE = [
    "00-common-review.md",
    "01-goal-decomposition.md",
    "02-information-research.md",
    "02.5-cross-check.md",
    "03-action-decomposition.md",
    "04-execution-verification.md",
    "04.5-final-review.md",
]
# 规则文件名 -> 阶段号（00 为全阶段共用）
FILE_STAGE = {name: name.split("-")[0] for name in CORE}
FILE_STAGE["00-common-review.md"] = "00"

REF_PAT = re.compile(r"(examples/[0-9][\w.\-]*\.md|[0-9][0-9.]*-[a-z\-]+\.md|INDEX\.md)")


def parse_index(path: Path) -> dict[str, set[str]]:
    """解析 INDEX.md 的 markdown 表格 -> {stage: {文件名}}。"""
    routes: dict[str, set[str]] = {}
    row = re.compile(r"^\|\s*([0-9][0-9.]*)[^|]*\|(.+)\|\s*$")
    for line in path.read_text(encoding="utf-8").splitlines():
        m = row.match(line.strip())
        if not m:
            continue
        stage, cells = m.group(1).strip(), m.group(2)
        if stage == "当前阶段" or "阶段" in stage:
            continue
        names = set(re.findall(r"(?:examples/)?[0-9][\w.\-]*\.md", cells))
        if names:
            routes[stage] = names
    return routes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--index", default=str(LOOP / "INDEX.md"))
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    idx = Path(args.index)
    if not idx.exists():
        print(f"FATAL: index not found: {idx}", file=sys.stderr)
        return 2
    routes = parse_index(idx)
    if len(routes) < 6:
        print(f"FATAL: parsed only {len(routes)} stages from {idx}: {sorted(routes)}", file=sys.stderr)
        return 2

    routed_all = {f for fs in routes.values() for f in fs}

    # ---- R-miss：结构自检 ----
    r_miss = [{"stage": s, "size": len(fs)} for s, fs in sorted(routes.items()) if len(fs) < 2]

    # ---- X-miss：引用未覆盖 ----
    x_miss, dangling = [], []
    for name in CORE:
        src = LOOP / name
        if not src.exists():
            continue
        own = FILE_STAGE[name]
        stages = sorted(routes) if own == "00" else [own]
        for lineno, line in enumerate(src.read_text(encoding="utf-8").splitlines(), 1):
            for ref in REF_PAT.findall(line):
                if ref in {name, "INDEX.md"}:
                    continue
                target = (LOOP / ref) if not ref.startswith("examples/") else (LOOP / ref)
                if not target.exists():
                    dangling.append({"src": name, "line": lineno, "ref": ref})
                    continue
                missing = [s for s in stages if ref not in routes.get(s, set())]
                if missing:
                    x_miss.append({"src": name, "line": lineno, "ref": ref, "missing_in_stages": missing})

    # ---- A-miss / G-miss：产出与门禁 ----
    a_miss, g_miss = [], []
    for stage in sorted(routes):
        d = ARTIFACTS / stage
        files = sorted(p.name for p in d.glob("R6-*.md")) if d.is_dir() else []
        if not files:
            a_miss.append({"stage": stage, "reason": "no R6-*.md under loop-artifacts/stages/" + stage})
            continue
        text = "".join((d / f).read_text(encoding="utf-8") for f in files)
        if "verdict" not in text.lower():
            g_miss.append({"stage": stage, "reason": "no verdict line"})

    ok = not x_miss and not dangling and not r_miss
    report = {
        "checker": "check-route-coverage.py",
        "index": str(idx.relative_to(REPO)) if idx.is_relative_to(REPO) else str(idx),
        "stages_parsed": len(routes),
        "routed_files_total": len({f for f in routed_all if not f.startswith("examples/")}),
        "routed_examples_total": len({f for f in routed_all if f.startswith("examples/")}),
        "core_files_total": len(CORE),
        "r_miss": r_miss,
        "x_miss": x_miss,
        "dangling": dangling,
        "a_miss": a_miss,
        "g_miss": g_miss,
        "exit": 0 if ok else 1,
    }

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"index: {report['index']}  stages={len(routes)}  routed_files={report['routed_files_total']}/{len(CORE)}  examples={report['routed_examples_total']}")
        print(f"R-miss (stage bundle < 2 files): {len(r_miss)}")
        print(f"X-miss (rule refs not in route): {len(x_miss)}")
        for r in x_miss:
            print(f"  - {r['src']}:{r['line']} -> {r['ref']}  missing in {r['missing_in_stages']}")
        print(f"dangling (ref target absent):    {len(dangling)}")
        for r in dangling:
            print(f"  - {r['src']}:{r['line']} -> {r['ref']}")
        print(f"A-miss (no artifact for stage):  {len(a_miss)}")
        for r in a_miss:
            print(f"  - stage {r['stage']}: {r['reason']}")
        print(f"G-miss (artifact w/o verdict):   {len(g_miss)}")
        for r in g_miss:
            print(f"  - stage {r['stage']}: {r['reason']}")
        print(f"\nRESULT: {'PASS' if ok else 'FAIL'} (exit {report['exit']})")
    return report["exit"]


if __name__ == "__main__":
    sys.exit(main())
