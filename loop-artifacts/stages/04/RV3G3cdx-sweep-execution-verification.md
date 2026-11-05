# 04 — RV3G3cdx-queue-hygiene-sweep · 执行验证

> goal: queue 卫生例行扫描 · 分支 ralph/rv3g3cdx-queue-hygiene-sweep · 2026-10-30
> 输入：03 行动分解 A1-A4。本文件记录 A1/A2 实跑证据；A3（queue 更新）与 A4（04.5）见收口 commit 与 stages/04.5/。

## A1 — 回归基线 spot check ✅（7/7 与 r145 X3 基线一致）

仓库根执行（`python3 bench/rubric-v3/ablation/scripts/<s>`，2>&1 合并捕获），r146 时点 vs r145 A1 表逐格比对：

| 脚本 | exit | 关键输出（本轮实跑） | r145 基线 | 判定 |
|------|------|---------------------|-----------|------|
| assert-goldrank-crossdomain.py | 0 | `[SIGNAL] blocked-on-external: batch2 data absent (等 batch2 数据落盘 bench/rubric-v3/ablation/batch2/ 后零改动接入)` + `[INFO] 预注册锚点: S1=['W3-new', 'W3-orig', 'W4-orig'], T_PASS=4, GOLD_DOMAIN1=['N-2.1', 'N-3.2.2', 'N-2', 'N-4', 'N-1.3']` | 同左 | ✅ 逐字一致 |
| assert-o3-claim-list.py | 0 | `=== 4/4 检查组 PASS · 0 明细项 FAIL ===` | 同左 | ✅ |
| assert-gmr-recompute.py | 0 | `=== 11 PASS / 0 FAIL ===` | 同左 | ✅ |
| assert-kappa-receipt.py | 1 | `RESULT: FAIL (1 checks failed)`（kappa-receipt.json 不存在——常态，不伪造转绿） | 同左 | ✅ |
| assert-o3-claim-rejudge.py | 0 | `[SIGNAL] blocked-on-external: rejudge-results.json absent (…)` | 同左 | ✅ |
| assert-goldrank-threshold.py | 0 | `SUMMARY: 31 PASS / 0 FAIL` | 同左 | ✅ |
| assert-w3w4-recompute.py | 0 | `SIGNAL: W0-W4 × 8 run 合计 0 mismatch` | 同左 | ✅ |

exit codes 序列 = [0, 0, 0, 1, 0, 0, 0]，与 r145 04.5 前置节独立重跑序列**完全一致**。失败降级触发条件（任一偏离预注册语义）**未触发**。

执行环境注记（如实登记）：首轮误从 scripts/ 目录内执行，o3-claim-list/gmr/threshold 三脚本因相对路径 FileNotFoundError 报 exit 1——系 CWD 错误非脚本缺陷，改回仓库根重跑全部恢复上表基线态。该现象本身佐证脚本对 CWD 的依赖是既有设计（路径硬编码为仓库相对路径），非本轮引入。

## A2 — 冻结面零修改 ✅

`git diff main --stat -- bench/rubric-v3/hit-matrix.json bench/rubric-v3/prior-estimates.json bench/rubric-v3/gold-tree.md 'bench/runs-C0-*'` = **0 行**。
全量 `git diff main --stat` 改动面 = {stages/02/*, stages/02.5/*, stages/03/*, tasks/current-goal.md}（+ 本文件 + 待做的 goal-queue.md）⊆ current-goal 验收标准第 4 条允许集。**冻结面零触碰。**

## A3 — queue 收口更新（随收口 commit 落地）

- L28 本 goal 行：`[ ]`→`[x]` + `(2026-10-30, r146: <hash>, ralph/rv3g3cdx-queue-hygiene-sweep)` + 结果注记（17 收口 commit 三列对照全 ✓ / D1 已修复复核 / 零新增未修复异常 / 七脚本基线 7/7）。
- 新导出候选追加 ≥1（见下）。

### A3 新导出候选（2 条）

1. `RV3G3cdx-closure-checklist-assert` —— 收口 commit 的 queue diff 机判门禁：写轻量 assert 脚本消费「收口 commit hash + 目标 goal 短名」，机判三项——(a) message 含「划掉/标记完成」⇒ diff 必含对应行 `[ ]`→`[x]` 翻转；(b) message 声称「追加候选 X」⇒ diff 必含 X 完整条目插入；(c) diff 中每个 checkbox 位翻转在 message 中有对应声称（双向闭合）。97d2adf 型漏翻（message 说划掉、diff 无翻转）将被 (a) 直接拦截。**规则细化（r146 04.5 攻击 5 处置）**：(a) 须含豁免子句——目标行在该 commit 之前不存在于 queue（`git show <h>~1:tasks/goal-queue.md | grep -c <短名>` = 0，A13/404ba7e 实证此检测可用）⇒ 「首建即 [x]」为合法形态，跳过 (a)。纯仓库内 ~5 回合（规则 = 本 sweep 02 表的机械化，零新增设计）。产投比依据：本 goal 实证了人工抽查的滞后性（D1 跨四轮无人发现），机判门禁把检测时点从「事后 sweep」前移到「收口 commit 当下」。
2. `RV3G3cdx-queue-dedup-lint` —— queue 结构 lint：机判检查 goal-queue.md 的 (a) 同一 goal 短名重复行（历史先例 r105c/r102c 两次人工去重）；(b) 「已完成」区出现 `[ ]` 行或「待办」区出现带完整结果注记却仍 `[ ]` 的行（97d2adf 型的静态形态）；(c) 行格式五段完整性（短名/一句话/产投比依据分隔符）。纯仓库内 ~3 回合。产投比依据：r105c/r102c 证明重复行会自然发生，且当前仅靠人工发现；与本 sweep 的时序抽查互补（本 sweep 查 message↔状态动态一致性，lint 查静态结构）。

## A4 — 04.5 反方复核

见 `loop-artifacts/stages/04.5/RV3G3cdx-hygiene-final-review.md`。