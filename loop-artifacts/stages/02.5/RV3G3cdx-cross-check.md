# 02.5 — RV3G3-threshold-crossdomain-reverify 核销轮 · 交叉核对

> goal: queue 队列卫生修复 + 核销验证 · 分支 ralph/rv3g3-threshold-crossdomain-reverify-close · 2026-10-30
> 定位：对 02 事实链做独立复核——不读 02 的结论，直接吃 git/文件系统原始证据；并锁定回归基线对照表。

## X1 — checkbox 状态三时点独立核验（不吃 02 F2 的转述）

| 时点 | 命令 | L? 行首 | 判定 |
|------|------|---------|------|
| r138+（446f4cc） | `git show 446f4cc:tasks/goal-queue.md \| grep -n crossdomain` | L22 `- [ ]` | 初始导出态 ✅ |
| r140 收口后（97d2adf） | `git show 97d2adf:tasks/goal-queue.md \| sed -n '23p' \| cut -c1-40` | `- [ ] RV3G3-threshold-crossdomain-reveri…` | **结果注记已写入但 checkbox 未翻** ✅（与 02 F2 一致） |
| 当前 main（c0eba3b） | Read tasks/goal-queue.md | L28 `- [ ]` | 仍未翻 ✅ |

三时点独立取证，与 02 F2 零 mismatch。

## X2 — 97d2adf diff 面精确核算

`git show 97d2adf --stat` = `tasks/goal-queue.md | 3 ++-`（2 insertions, 1 deletion）。逐 hunk 核对：唯一改动块 = 新导出候选区顶部，(i) 新增 batch2-arrival-closure 整行；(ii) crossdomain 行原位重写（追加结果注记，行首 `[ ]` 保留）。**无其他文件改动**（--stat 仅此一文件）→ 「漏翻」定性成立且范围封闭（不是「划到别处去了」——全文件 grep 该短名在 97d2adf 版本中仅此一行）。

## X3 — 回归基线对照表（04 实跑锚点，全部本轮从仓库根执行）

| 脚本 | 预期基线 | 来源 |
|------|----------|------|
| assert-goldrank-crossdomain.py | `[SIGNAL] blocked-on-external: batch2 data absent (等 batch2 数据落盘 bench/rubric-v3/ablation/batch2/ 后零改动接入)` + `[INFO] 预注册锚点: S1=['W3-new', 'W3-orig', 'W4-orig'], T_PASS=4, GOLD_DOMAIN1=['N-2.1', 'N-3.2.2', 'N-2', 'N-4', 'N-1.3']`，exit 0 | r140 docstring L7 预注册语义 + 本轮 od -c byte-exact 捕获（两行均以 `\n` 结尾，无 stderr） |
| assert-o3-claim-list.py | exit 0，`=== 4/4 检查组 PASS · 0 明细项 FAIL ===` | r142/r143 基线 |
| assert-gmr-recompute.py | exit 0，`=== 11 PASS / 0 FAIL ===` | r142/r143 基线 |
| assert-kappa-receipt.py | exit 1，`RESULT: FAIL (1 checks failed)`（kappa-receipt.json 不存在 = 常态，不伪造转绿） | r136 语义 / r142-r143 基线 |
| assert-o3-claim-rejudge.py | exit 0，`[SIGNAL] blocked-on-external: rejudge-results.json absent …` | r141 语义 / r142-r143 基线 |
| assert-goldrank-threshold.py | exit 0，`SUMMARY: 31 PASS / 0 FAIL` | r138+ 基线 |
| assert-w3w4-recompute.py | exit 0，`SIGNAL: W0-W4 × 8 run 合计 0 mismatch` | r116 基线 |

X3 备注：assert-gmr-recompute.py 输出含 11 条 `[PASS]` 明细行 + 汇总行 `11 PASS / 0 FAIL`（grep -c PASS = 12 系把汇总行也计入，非 12 项检查——以汇总行为准，与 r142/r143 工件记载一致）。

## X4 — 核销动作的影响面封闭性

翻转 L28 checkbox + 追加核销注记 + 底部追加新候选，全部落在 `tasks/goal-queue.md` 单文件；loop-artifacts 只增不改。**不触碰任何冻结件、任何脚本、任何既有 queue 行的状态位**（batch2-arrival-closure 保持 `[ ]` blocked-on-external 不变）。影响面 = {goal-queue.md, current-goal.md, stages/{02,02.5,03,04,04.5}/}。

## X5 — 风险声明

1. 若 04 实跑 crossdomain 输出与 X3 第一行不一致 → 触发失败降级（停止核销，登记基线漂移）。
2. 「漏翻」的归因（97d2adf 执行遗漏 vs 有意保留）不可从 git 证据区分——按 message 声称「划掉」采信为执行遗漏；即使属有意保留，补翻 + 注记也是净改善（消除 message 与状态的矛盾），无下行风险。