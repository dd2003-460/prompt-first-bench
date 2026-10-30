# Goal: RV3G3cdx-queue-hygiene-sweep — queue 卫生例行扫描（r146）

> 创建：2026-10-30 · ralph loop runner（queue 消费——r145 核销轮导出项，纯仓库内 grep/git show 工作）
> 依据：r145 实证实例 = 97d2adf message 声称「queue 划掉」而 checkbox 仍 `[ ]`，跨 r141-r144 四轮无人发现。本 goal = 对近 20 轮收口 commit 做 message↔状态位一致性抽查，封死该缺陷类复发路径。
> 范围上限（04.5 攻击 6 处置）：**近 20 轮收口 commit 对应的 queue 行**，非全量历史；单轮成本封顶 ~3 回合。

## 【目标】
逐收口 commit 核对：commit message 声称的 queue 动作（划掉/转 [~]/追加候选）vs 该 commit 实际 queue diff vs 当前 main 状态位；输出对照表 + 异常清单（预期 = 零异常或仅已修复项）。

## 【阶段】
01（本文件）→ 02 扫描执行（收口 commit 枚举 + 逐条 queue diff 提取 + 三列对照）→ 02.5 交叉核对（独立重跑关键 git show 命令复核对照表）→ 03 动作分解 → 04 执行验证（异常处置/零异常声明 + 回归基线 spot check）→ 04.5 反方复核 → 收口（queue 更新 + merge main）

## 【SOP 索引】
- `tasks/ralph-loop-runner.md` 阶段 B/C
- 被检对象（只读）：`tasks/goal-queue.md` 当前版 + 近 20 轮收口 commit 的 `git show <h> -- tasks/goal-queue.md`
- 缺陷实例锚点：97d2adf（r140，message「划掉」vs 实际 `[ ]` 保留）——r145 已修复，本轮应作为「已修复项」出现在对照表中

## 【验收标准】
- [ ] 收口 commit 枚举完整（近 20 轮内全部含 queue 改动的收口 commit，逐条列出 hash + message 摘要）
- [ ] 三列对照表（message 声称 / 实际 diff / 当前状态位）覆盖全部枚举项，每格有 git 证据
- [ ] 异常处置：新发现异常 → 修复或如实登记 + 导出候选；零新异常 → 显式声明
- [ ] 冻结面零修改（改动面 ⊆ {goal-queue.md, current-goal.md, stages/*}）
- [ ] 04.5 verdict pass；queue 更新（本 goal `[x]` + 结果注记 + 新候选 ≥1）

## 【失败降级】
- 若发现 >2 个未修复异常 → 停止批量修复，逐个登记为独立候选（防单轮改动面失控），本 goal 收口为「审计完成 + N 候选导出」
- 若某收口 commit 的 queue diff 无法解析（rebase/merge 干扰）→ 该行标注 unverified 并继续，不阻塞