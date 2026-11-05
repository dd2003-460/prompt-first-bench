#!/usr/bin/env python3
"""assert-closure-checklist.py — 收口 commit 的 queue diff 机判门禁（RV3G3cdx-closure-checklist-assert）

用途：消费「收口 commit hash + 目标 goal 短名」，机判 commit message ↔ tasks/goal-queue.md
diff 的双向闭合，把 97d2adf 型漏翻（message 声称「划掉」而 checkbox 未翻转）的检测时点
从「事后 sweep」前移到「收口 commit 当下」。纯字符串机判，不做语义理解。

用法：python3 assert-closure-checklist.py <commit-hash> <goal-short-name>

三项检查（规则权威源 = r146 loop-artifacts/stages/02/RV3G3cdx-scan-execution.md
三列对照表 + stages/04.5 攻击 5 豁免子句）：
  (a) message 含划掉类关键词 ⇒ queue diff 必含目标行 `[ ]`→`[x]` 翻转；
      **豁免子句**：目标行在该 commit 之前不存在于 queue
      （git show <h>~1:tasks/goal-queue.md | grep -c <短名> = 0）⇒ 「首建即 [x]」合法形态，跳过 (a)。
  (b) message 含追加候选类关键词 ⇒ 每个提取出的候选短名 X 必出现在 diff 的 `+` 行中。
  (c) 双向闭合：diff 中每个含 checkbox 的行变更，其 goal 短名须在 message 中有对应声称
      （匹配规则 = r148 02.5 X4 修正版：diff 短名 ⊆ message，或 message 含该短名的
      连续子串且长度 ≥ min(8, len(短名))——兼容 message 用局部短称如「schema-lint」
      指代「batch2-schema-lint」）。

exit code：0 = 全通过 / 1 = 任一检查 FAIL（指名道姓输出）/ 2 = 输入不可解析
           （commit 不存在 / 该 commit 无 queue diff）。
"""
import re
import subprocess
import sys

QUEUE = "tasks/goal-queue.md"
FLIP_KW = ["划掉", "标记完成", "核销", "[ ]→[x]"]          # (a) 触发词（r148 02 S1 并集）
APPEND_KW = ["新导出候选", "追加候选", "导出候选"]            # (b) 触发词
CAND_RE = re.compile(r"(?:RV|R5\.)[\w.-]*")                 # 候选短名提取


def run(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def git_show_diff(h):
    r = run("git", "show", h, "--", QUEUE)
    if r.returncode != 0:
        return None
    lines = [l for l in r.stdout.splitlines()
             if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))]
    return lines or None


def main():
    if len(sys.argv) != 3:
        print(f"[ERROR] usage: {sys.argv[0]} <commit-hash> <goal-short-name>")
        sys.exit(2)
    h, name = sys.argv[1], sys.argv[2]

    r = run("git", "log", "-1", "--format=%s", h)
    if r.returncode != 0:
        print(f"[ERROR] commit not found: {h}")
        sys.exit(2)
    msg = r.stdout.strip()

    diff = git_show_diff(h)
    if diff is None:
        print(f"[ERROR] no queue diff in {h} (非 queue 收口 commit)")
        sys.exit(2)

    plus = [l[1:] for l in diff if l.startswith("+")]   # 已剥 diff 前缀，正则不再带 +/-
    minus = [l[1:] for l in diff if l.startswith("-")]
    fails = []

    # (a) 划掉声称 ⇒ 翻转或首建豁免
    if any(k in msg for k in FLIP_KW):
        flipped = any(re.match(rf"^- \[ \] {re.escape(name)}\b", m)
                      and re.match(rf"^- \[x\] {re.escape(name)}\b", p)
                      for m in minus for p in plus)
        exempt = False
        if not flipped:
            # 注：必须 shell=True——列表形式传 '|' 会被 git 当作字面路径参数（exit 128）
            prev = subprocess.run(
                f"git show {h}~1:{QUEUE} | grep -c {name}", shell=True,
                capture_output=True, text=True)
            cnt = int(prev.stdout.strip() or "0")
            created_as_done = cnt == 0 and any(
                re.match(rf"^- \[x\] {re.escape(name)}\b", p) for p in plus)
            exempt = created_as_done
        if flipped:
            print(f"[PASS] (a) 划掉声称 ↔ 既有行 [ ]→[x] 翻转")
        elif exempt:
            print(f"[PASS] (a) 豁免子句命中：{name} 在 {h}~1 不存在于 queue → 首建即 [x] 合法形态")
        else:
            fails.append("(a) message 声称划掉但 diff 无 [ ]→[x] 翻转且非首建豁免（97d2adf 型漏翻）")

    # (b) 追加候选声称 ⇒ 候选短名在 + 行
    if any(k in msg for k in APPEND_KW):
        cands = [c for c in CAND_RE.findall(msg) if c != name]
        # 去重保序
        seen, uniq = set(), []
        for c in cands:
            if c not in seen:
                seen.add(c)
                uniq.append(c)
        for c in uniq:
            if any(c in p for p in plus):
                print(f"[PASS] (b) 追加候选 {c} 在 diff + 行中找到")
            else:
                fails.append(f"(b) message 声称追加候选 {c} 但 diff 无对应插入行")
        if not uniq:
            print("[INFO] (b) 追加类关键词命中但未提取到候选短名（跳过）")

    # (c) 双向闭合：diff 中每个 checkbox 行变更的短名须被 message 提及
    for line in plus + minus:
        m = re.match(r"^[+-] \[[ x~]\] (\S+) ", line)
        if not m:
            continue
        dname = m.group(1)
        if dname == name or name in dname or dname in msg:
            continue
        # 子串双向匹配（02.5 X4 修正版）
        ok = any(len(s) >= min(8, len(dname)) and s in dname
                 for s in re.findall(r"[\w][\w.-]{7,}", msg))
        if not ok:
            fails.append(f"(c) diff 动了 {dname} 行但 message 未提及（双向闭合缺口）")

    if fails:
        for f in fails:
            print(f"[FAIL] {f}")
        print(f"SUMMARY: FAIL ({len(fails)} checks failed) — {h} {name}")
        sys.exit(1)
    print(f"SUMMARY: PASS — {h} {name} message↔queue diff 双向闭合")
    sys.exit(0)


if __name__ == "__main__":
    main()