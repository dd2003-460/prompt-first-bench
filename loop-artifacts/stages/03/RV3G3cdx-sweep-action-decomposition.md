# 03 — RV3G3cdx-queue-hygiene-sweep · 动作分解

> goal: queue 卫生例行扫描（近 20 轮收口 commit 的 message↔状态位一致性抽查）· 分支 ralph/rv3g3cdx-queue-hygiene-sweep · 2026-10-30
> 输入：02（三列对照表全 ✓ + D1 已修复 + 零新增未修复异常）+ 02.5（独立复核零 mismatch）。
> 注：stages/03/ 下既有 `RV3G3cdx-action-decomposition.md` 属 r145 核销轮（前缀撞名），本文件以 `-sweep` 后缀区分。

## 判定

02 S4 异常清单 = {D1（已修复，r145/9f48d94），D2（随 D1 闭环）}。**零新增未修复异常** → 按 current-goal 验收标准走「零新异常显式声明」路径，不触发失败降级（>2 个未修复异常才停止批量修复）。

## 行动分解

| # | 动作 | 对象 | 可验证产物 |
|---|------|------|-----------|
| A1 | 回归基线 spot check：实跑窗口内收口 commit 落盘的关键 assert 脚本，确认 r146 时点行为与各自收口时基线一致（防「核销的是历史而非活行为」——r145 先例口径） | `bench/rubric-v3/ablation/scripts/` 七脚本（crossdomain / o3-claim-list / gmr / kappa-receipt / rejudge / goldrank-threshold / w3w4） | exit codes + 关键行 grep，与 r145 X3 基线表逐格比对 |
| A2 | 冻结面零修改验证 | hit-matrix.json / prior-estimates.json / gold-tree.md / runs-C0-* 十件 | `git diff main --stat` = 0 行 |
| A3 | queue 收口更新：本 goal L28 `[ ]`→`[x]` + 日期 + 结果注记；追加新导出候选 ≥1 | tasks/goal-queue.md L28 + 尾部 | diff 面核算（预期 1+/1- + N 行追加） |
| A4 | 04.5 八攻击反方复核 | 本 goal 全部动作 | loop-artifacts/stages/04.5/RV3G3cdx-hygiene-final-review.md |

## 预注册边界（04.5 消费）

- B1：A1 的「基线一致」口径 = exit code + 关键输出行文案一致；SIGNAL 常态脚本（crossdomain/rejudge/kappa-receipt）预期维持 SIGNAL/FAIL 原态，**不要求转绿**。
- B2：A3 的新候选必须带产投比依据（queue 格式硬约束），且不得是 trivial 凑数。
- B3：改动面 ⊆ {goal-queue.md, stages/*}——current-goal 验收标准第 4 条。