#!/usr/bin/env python3
"""T-PUB-1 题集自检脚本.

从 tasks/T-PUB-1-result.md 中抽出所有 ```json 的 spec 块，机械校验：
  1) 10 题、id 唯一、domain/type 计数符合任务书（5 GPU full + 2 math/phys + 3 rank-deficient）
  2) 每题 checkpoint 数 ∈ [3,5]
  3) kind=calc 的 gold 能被 sympy.sympify 解析为实数（可 eval）
  4) kind=fact 的 source 是 https:// URL 或显式推导链
  5) type=rank-deficient 必须含 missing_fact，且至少 1 个 bool + 1 个 fact checkpoint
  6) kind=bool 的 gold ∈ {0,1}

用法: python3 tasks/T-PUB-1-verify.py [-v]
退出码 0 = 全部通过。
"""
import json
import re
import sys
from pathlib import Path

import sympy
from sympy import floor, sympify  # noqa: F401  (floor 供 gold 表达式使用)

HERE = Path(__file__).resolve().parent
MD = HERE / "T-PUB-1-result.md"
VERBOSE = "-v" in sys.argv

fails: list[str] = []
passes: list[str] = []


def ok(msg: str) -> None:
    passes.append(msg)
    if VERBOSE:
        print(f"PASS {msg}")


def bad(msg: str) -> None:
    fails.append(msg)
    print(f"FAIL {msg}")


def main() -> int:
    if not MD.exists():
        print(f"FAIL 缺少 {MD}")
        return 1

    specs = [json.loads(b) for b in re.findall(r"```json\n(.*?)```", MD.read_text(), re.S)]
    print(f"spec blocks found: {len(specs)}  (sympy {sympy.__version__})")

    # 1) 数量与分布
    if len(specs) != 10:
        bad(f"题目数量 {len(specs)} != 10")
    else:
        ok("10 个 spec 块")

    ids = [s["id"] for s in specs]
    if len(set(ids)) != len(ids):
        bad(f"id 重复: {ids}")
    else:
        ok("id 唯一")

    dom = {}
    typ = {}
    for s in specs:
        dom[s["domain"]] = dom.get(s["domain"], 0) + 1
        typ[s["type"]] = typ.get(s["type"], 0) + 1

    if dom.get("gpu") == 8 and dom.get("math") == 1 and dom.get("physics") == 1:
        ok(f"domain 分布 {dom}")
    else:
        bad(f"domain 分布不符: {dom}")
    if typ.get("full") == 7 and typ.get("rank-deficient") == 3:
        ok(f"type 分布 {typ}")
    else:
        bad(f"type 分布不符: {typ}")

    # 2) 逐题检查
    for s in specs:
        qid = s["id"]
        cps = s["checkpoints"]
        if not 3 <= len(cps) <= 5:
            bad(f"{qid}: checkpoint 数 {len(cps)} 不在 [3,5]")
        kinds = {}
        for c in cps:
            kinds[c["kind"]] = kinds.get(c["kind"], 0) + 1
            if c["kind"] == "calc":
                try:
                    v = sympify(str(c["gold"]), locals={"floor": floor, "pi": sympy.pi})
                    fv = float(v.evalf())
                    if fv != fv:  # NaN
                        raise ValueError("NaN")
                    if VERBOSE:
                        print(f"     {qid}/{c['id']} calc gold -> {fv:.6f}")
                except Exception as e:  # noqa: BLE001
                    bad(f"{qid}/{c['id']}: calc gold 不可 eval ({c['gold']!r}): {e}")
            elif c["kind"] == "bool":
                if c["gold"] not in (0, 1):
                    bad(f"{qid}/{c['id']}: bool gold 必须是 0/1")
            elif c["kind"] == "fact":
                src = str(c.get("source", ""))
                if not (src.startswith("https://") or "datasheet" in src):
                    bad(f"{qid}/{c['id']}: fact 缺可访问 URL/datasheet 来源")
            else:
                bad(f"{qid}/{c['id']}: 未知 kind {c['kind']!r}")
        if not {"calc", "fact", "bool"} & set(kinds):
            bad(f"{qid}: 无有效 checkpoint")
        if s["type"] == "rank-deficient":
            if "missing_fact" not in s:
                bad(f"{qid}: rank-deficient 缺 missing_fact 字段")
            if kinds.get("bool", 0) < 1 or kinds.get("fact", 0) < 1:
                bad(f"{qid}: rank-deficient 需 >=1 bool + >=1 fact，实得 {kinds}")
    ok("逐题 checkpoint 检查完成")

    # 3) 汇总
    n_calc = sum(1 for s in specs for c in s["checkpoints"] if c["kind"] == "calc")
    n_fact = sum(1 for s in specs for c in s["checkpoints"] if c["kind"] == "fact")
    n_bool = sum(1 for s in specs for c in s["checkpoints"] if c["kind"] == "bool")
    print(f"\ncheckpoints: total={n_calc + n_fact + n_bool} calc={n_calc} fact={n_fact} bool={n_bool}")
    print(f"passes={len(passes)} fails={len(fails)}")
    if fails:
        for f in fails:
            print(f"  - {f}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
