#!/usr/bin/env python3
"""assert-queue-lint.py — goal-queue.md 静态结构 lint（RV3G3cdx-queue-dedup-lint, r149）

用途：对 tasks/goal-queue.md 做三项纯静态结构机判，把 r102c/r105c 两次人工去重
与 97d2adf 型漏翻的静态形态检查从「事后人工发现」变为「可重复机判」。
与 assert-closure-checklist.py（动态 message↔diff 一致性，r148）互补：本脚本只查文件当下状态。

用法：python3 assert-queue-lint.py [path]   （默认 tasks/goal-queue.md；参数化供负样例沙盒消费）

行解析式：`^- [ <state> ] (body)$`，其中 state ∈ {空格, x, ~} → (状态位, 行体)；区归属 = 该行之前最近的 `## ` 标题。
短名提取（X4 裁定）：行体首空白前 token → 剥全部 `~~` → 截断至首个全角/半角左括号。

三项检查（判定语义 byte-stable，权威源 = stages/02.5/RV3G3cdx-qlint-crosscheck.md 末节）：
  (a) 短名重复：按短名分组——
      同区出现 >1 次 ⇒ FAIL（列出全部行号）【r102c/r105c 先例形态】；
      跨区出现 >1 次且所有相关行均不含「吸收」⇒ FAIL（真失控形态）；
      跨区出现 >1 次且 ≥1 行含「吸收」⇒ SIGNAL（吸收登记行合法形态，报告不拦截）。
  (b) 状态位异常：「已完成」区出现 `[ ]` 行 ⇒ FAIL；任意区 `[ ]` 行含 `**结果**`
      裸子串标记（04.5 W2 修复：覆盖 '**结果：'/'**结果**：'/'**结果**:' 全部变体）
      ⇒ FAIL（97d2adf 静态形态：声称完成却未翻转 checkbox）。`[~]` 行不参与 (b)
      （设计内终态：材料已备待裁定、message 明言不划掉——r146 sweep 逐行确认）。
  (c) 行格式完整性：每个 `- [<state>]` 行（三区全查，含 `[~]`）——短名 token 为空，
      或行体既无 `|` 也无 `—` 分隔符 ⇒ FAIL；其余 PASS（「可解析即过、不可解析才
      FAIL」最小规则，X2 裁定：em-dash 简写行 15 行实证存在，不设 pipe 计数下限）。

exit code：0 = 无 FAIL（SIGNAL 不影响 exit，stdout 带 `[SIGNAL]` 前缀）
           / 1 = ≥1 FAIL（逐条指名道姓：检查项+行号+短名）
           / 2 = 输入不可解析（文件缺失 / 空 / 无任何 goal 行）。

注：前序会话草稿版（(a) 一律 SIGNAL + C2-only 可解析性）被本轮 02.5 X1/X2 裁定取代——
(a) 三分支区分先例形态与失控形态；(c) 补「无分隔符」FAIL 出口（草稿版该出口不可达，
负样例矩阵无法构造 (c) FAIL）。
"""
import re
import sys

LINE_RE = re.compile(r"^- \[( |x|~)\] (.*)$")
SEC_RE = re.compile(r"^## (.+)$")


def parse(path):
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except OSError as e:
        print(f"[ERROR] cannot read {path}: {e}")
        sys.exit(2)
    if not any(LINE_RE.match(l) for l in lines):
        print(f"[ERROR] no goal lines (`- [ ]/[x]/[~]`) found in {path}")
        sys.exit(2)
    rows, sec = [], None
    for i, l in enumerate(lines, 1):
        m = SEC_RE.match(l)
        if m:
            sec = m.group(1).strip()
            continue
        m = LINE_RE.match(l)
        if m:
            body = m.group(2)
            name = re.sub(r"~~", "", body.split()[0])
            name = re.split(r"[（(]", name)[0].strip()
            rows.append({"line": i, "sec": sec or "(top)", "state": m.group(1),
                         "name": name, "body": body})
    return rows


def check_a(rows):
    """(a) 短名重复：同区 >1 = FAIL / 跨区无吸收声明 = FAIL / 跨区带吸收声明 = SIGNAL"""
    out, groups = [], {}
    for r in rows:
        groups.setdefault(r["name"], []).append(r)
    for name, rs in sorted(groups.items()):
        if len(rs) < 2:
            continue
        locs = ", ".join(f"L{r['line']}({r['sec']})" for r in rs)
        zones = {r["sec"] for r in rs}
        marked = any("吸收" in r["body"] for r in rs)
        if len(zones) == 1:
            out.append(("FAIL", f"(a) 同区重复短名「{name}」×{len(rs)} @ {locs}"))
        elif marked:
            out.append(("SIGNAL", f"(a) 跨区重复短名「{name}」@ {locs}（含「吸收」声明，合法形态）"))
        else:
            out.append(("FAIL", f"(a) 跨区重复短名「{name}」@ {locs}（无「吸收」声明）"))
    return out


def check_b(rows):
    """(b) 状态位异常：已完成区 [ ] / 任意区 [ ] + **结果**标记（04.5 W2 修复：裸子串，
    覆盖 '**结果：'/'**结果**：'/'**结果**:' 全部既有及可预见变体）"""
    out = []
    for r in rows:
        if r["state"] != " ":
            continue
        if r["sec"] == "已完成":
            out.append(("FAIL", f"(b) 「已完成」区出现未勾选行 L{r['line']} [{r['name']}]"))
        if "**结果**" in r["body"]:
            out.append(("FAIL", f"(b) 带结果注记却仍 [ ] L{r['line']} [{r['name']}]（97d2adf 静态形态）"))
    return out


def check_c(rows):
    """(c) 行格式完整性：短名非空 + 行体含 | 或 — 分隔符（三区全查含 [~]）"""
    out = []
    for r in rows:
        if not r["name"]:
            out.append(("FAIL", f"(c) 短名 token 为空 L{r['line']}"))
        elif "|" not in r["body"] and "—" not in r["body"]:
            out.append(("FAIL", f"(c) 无可识别分隔符(|/—) L{r['line']} [{r['name']}]"))
    return out


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "tasks/goal-queue.md"
    rows = parse(path)
    results = [("PASS", f"解析 goal 行 {len(rows)} 行")]
    for fn in (check_a, check_b, check_c):
        results.extend(fn(rows))
    fails = [d for s, d in results if s == "FAIL"]
    signals = [d for s, d in results if s == "SIGNAL"]
    for s, d in results:
        prefix = "[SIGNAL]" if s == "SIGNAL" else f"[{s}]"
        print(f"{prefix} {d}")
    print(f"== queue-lint: {len(rows)} 行 / {len(results) - 1} 检查项 / "
          f"{sum(1 for s, _ in results if s == 'PASS')} PASS / {len(fails)} FAIL / {len(signals)} SIGNAL ==")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()