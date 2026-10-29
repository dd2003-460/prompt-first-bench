# 阶段 01：目标分解 — RUBRIC-V3-FULL-AUDIT / G4 漏洞对照

> goal: rubric-v3-audit-g4 · 分支 ralph/rubric-v3-audit-g4 · 2026-10-30
> 上游任务书: tasks/RUBRIC-V3-FULL-AUDIT-task-brief.md（队首大 goal，G1-G6 串联）
> 前置: G1（矛盾清单 C1-C4）、G2（根因 = 双源 p̃ 偏差 + 判据极严）、G3（W3/W4 敏感性分级 + O1/O2/O3 决策矩阵）。本 goal 消费 gap-analysis Q2 与前三环证据。

## 因素分解

任务书 G4 = 「gap-analysis Q2 五条结构性解释逐条对照我们的协议，标『已规避/未规避/部分规避』+ 证据」。拆成四个正交因素：

### F1 · 材料定位与口径界定
- gap-analysis 原文不在 main 工作树（`receipts/rubric-v3-gap-analysis.md` 只在 `origin/rubric-v3` / `research/deepresearch-bench-survey` 等分支），用 `git show aea3d6b:receipts/rubric-v3-gap-analysis.md` 取——Q2 节含**五条编号的结构性解释**（S1-S5）+ 一段「ResearcherBench 和 RACE 为什么没继续到结构节点×意外性权重」的补充分析。
- 「我们的协议」口径：rubric-v3 **草案协议**（DRAFT-rubric-v3.md，origin/rubric-v3）+ **消融实现协议**（TASK-ablation.md 实际执行 + 冻结数据文件）。两者要分开标——草案写了但消融没做的，算「未规避（实现层）」还是「部分规避」需要显式规则：**判定对象 = 当前可运行的完整链条（草案 + 已执行消融）**；草案条款若从未被执行过，其防护效力按「纸面存在、实证缺失」计入。
- 判定三值定义：已规避 = 协议有明确机制且该机制在本仓有执行痕迹或数据支撑；部分规避 = 有机制但不完整/未经检验/只覆盖一部分暴露面；未规避 = 无对应机制或机制被证无效。

### F2 · 五条解释逐条对照（核心交付）
- S1 构念错配（短答案任务强加研究树测错构念）→ 对照点：rubric-v3 适用域声明（§3.1 域选择）+ 第二格设计。
- S2 唯一 gold 路径偏置（构造唯一树造成路径偏置/漏标/reference 依赖）→ 对照点：gold-tree 单源构建、O2「新深层矛盾不计分」、adversarial-check Q1-blocker-2 的同源依赖发现、R5.2-third-scorer 挂起状态。
- S3 细粒度标注/judge 可靠性成本 → 对照点：p̃ 获取协议（≥3 LLM 盲生成）vs 实际执行（单 judge 自评 + 一次同族盲测）、judge 门禁（κ≥0.6 换位双判）的执行状态、G1/G2 发现的同族偏差。
- S4 单一终点可比性 vs p̃ 数据集/版本依赖 → 对照点：O3 分数跨域可比性、p̃ 冻结纪律（prior-estimates.json source_baseline_commit）、O1 候选集扩展指令的域特定性（硬件老卡分区）。
- S5 surprisal 统计/构念风险（稀有不等于重要）→ 对照点：这是 G1-G3 的主战场——C4（3/5↔1/5 翻转）、G2 根因、G3 分级直接就是对本条的实证回答。
- 每条输出：解释原文摘要 + 我们协议的暴露面 + 判定（三值）+ evidence（file:line / JSON path / 前序 loop 工件引用）。

### F3 · 交叉引用去重
- gap-analysis 是 2026-10-29 写的，早于 blindtest（G1/G2/G3 的证据）。凡 Q2 里「需验证 p̃ 估计稳定」类的前瞻警告，已被后续 loop 证实/证伪的，标注「已被 G1/G2/G3 闭环」并引具体工件，不重复推导。
- adversarial-check-rubric-v3.json（origin/rubric-v3）的 28 条 findings 中涉及同源/泄漏/机械可判性的条目，作为 S2/S3 的补充证据源（它是独立 arena 会话的对抗核验，比本 runner 的自查外部性更强）。

### F4 · 交付物结构
- g4-vulnerability-crosscheck.md：S1-S5 五节（每节 = 解释摘要 + 暴露面 + 判定 + evidence）+ 判定汇总表 + 负面结果声明（哪些「我们以为规避了」的判断被推翻）+ 给 G5/G6 的导出（未规避项 = G5 优化清单的输入；部分规避项 = G6 定稿时的保留条件）。
- 边界：不改冻结文件、不动 gold set、不实施任何修复、不重新跑消融。

## 空缺清单

| # | 空缺 | 类型 | 影响 |
|---|------|------|------|
| G1 | T17 第二格域的实际执行记录 | 仓库内不存在（adversarial-check Q6-minor 已指出本仓无 T17 文件） | S1/S4 判定只能基于草案设计，不能基于实测 |
| G2 | ≥3 LLM 盲生成 p̃ 协议的执行记录 | 从未执行（消融实际用单 judge 自评） | S3 判定的关键事实，需从 TASK-ablation.md Step 2 与实际 prior-estimates.json 的差异确认 |
| G3 | κ≥0.6 门禁在消融评分中的执行回执 | 未见回执文件 | S3 判定需登记「门禁执行状态 unverified」 |

## 阶段 02 研究入口

- 仓库内材料足够：gap-analysis 用 git show 取；DRAFT/TASK/gold-tree/冻结 JSON/adversarial-check receipt 全部可查；G1-G3 工件在 main。
- web-llm 强制步骤预期三 provider 仍失效 → 记录失败回执后继续，不阻塞。

## 判定

分解完成：四个叶子因素（F1 口径 / F2 五条对照 / F3 交叉引用 / F4 交付结构）覆盖任务书 G4 全部要求；判定三值规则显式化避免「部分规避」滥用；空缺 G1-G3 均有处置路径（登记为判定限定语而非阻塞）。→ 进入 02。