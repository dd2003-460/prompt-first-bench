# #10 分解树 v2 核验回执（2026-11-24）

> 核验对象：commit b8f7a3691:tasks/decomposition.md（#10 五件套 1-loop 01 分解树 v2）
> 核验依据：tasks/10-decomposition/TASK.md（任务书 281a1322d）
> 核验方式：文档 vs 规格完整性对照（两文件全文已读，非长读/batch，Lead 直接核）
> 背景：原核验 subagent（deleg_82f8a870）502 挂掉，本回执为替代核验。

## 结论：内容完整性 PASS，2 个 issue 需处理

### 任务书要求逐条核（全过）
| 要求 | 状态 | 证据 |
|---|---|---|
| 7 正交子项（系统/净增益/终点/题面/#53/发表/风险） | ✓ | S1-S7 全在 |
| 正交性核对（重叠度） | ✓ | 量化表，无 >50% 配对，可并行度 4 |
| 缺口标注 [待核验] | ✓ | S1-S7 每子项都有 |
| 任务表（步骤+机器可查验收+耗时） | ✓ | T10-1~8，含依赖图 |
| 中文 | ✓ | — |
| 每条结论标 conf(0-1) | ✓ | S1 0.85…S7 0.8，总树 0.8 |
| 不确定标未验证 | ✓ | [待核验] 多处 |
| 核心 ≤50 行 | ✓ | 核心 50 行内，过程论证在附录 A |
| 回执含 repo+branch+sha | ✓ | repo=dd2003-460/prompt-first-bench / branch=arena/f8477718-prompt-first-bench / sha=b8f7a3691 |

### Issue 1（需处理）：交付物在 arena 分支，未合入主工作分支
- b8f7a3691 只在 `origin/arena/f8477718-prompt-first-bench`，**不在**当前主分支 `tmp-lit-snowball`。
- 任务书说"commit 到当前分支"——subagent 的"当前分支"是它工作的 arena 分支，内容合规，但主工作树里没有这个文件。
- **处置**：cherry-pick b8f7a3691 到主分支（或后续合 arena 分支），让 tasks/decomposition.md 进主工作树。

### Issue 2（可关闭）：S5 的 #53 原始数据 [待核验] 其实可解
- 交付物 S5/附录 A 写"#53 负结果原始数据 commit 5fa9dfe8b 不在本分支，未验证原始数据"。
- **核验事实**：5fa9dfe8b **在**主分支 `tmp-lit-snowball` 历史里（`git merge-base --is-ancestor 5fa9dfe8b HEAD` = YES）。
- 即 subagent 在 arena 分支上看到的"不可达"是分支视角局限；主分支上有这份数据。
- **处置**：T10-5（#53 模块执行）可直接指向主分支 5fa9dfe8b 的数据落盘，该 [待核验] 关闭。

### 次要 note（不阻塞）
- 来源给的是 arXiv ID（2510.17109 / 2601.23163）非完整 https URL；任务书要"来源 URL"。但撞车结论声明"复用 IDEA-review 81be67cb9 不重查"，完整 URL 在 tasks/IDEA-review/result.md。可接受，T10 执行时引用该文件即可。

## 下一步（Lead 编排）
1. cherry-pick b8f7a3691 → 主分支（解 Issue 1）
2. T10-5 数据源改指主分支 5fa9dfe8b（解 Issue 2）
3. 分解树 v2 作为 #10 主线 1-loop 01 阶段交付物冻结，进入 02 信息调研
