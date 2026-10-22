# Prompt-first 提升验证：公开证据与可执行实验方案

日期：2026-10-22（UTC）。范围：≤10 个公开来源的限额检索；非系统综述。**结论先行：公开证据不能证明完整 1-loop 提升成功率/质量，也不能估计组件边际或模型差异。** 论文显示特定规划系统在特定基准上有正向结果，同时存在反例；实现机制本身不等于因果证据。未执行模型对照实验。

## 核心结论（核心 6 行）

| 问题 | 结论 | 证据（来源 + 关键数字） | conf |
|---|---|---|---|
| Q1 拆解是否提高最终成功率？ | **公开证据不足以给 prompt-first 拆解的普遍因果效应量。** 特定任务上分解/规划系统有正向结果，但处理条件混杂且基准异质。 | Meta-Task Planning：TravelPlanner 约40% vs baseline 2.92%，API-Bank 约+14%（检索摘要，可能并非只差拆解）；ACONIC SATBench Claude 49.3→58.1%、LLaMA 21.5→36.5%；反例 PDDL agentic 20% vs direct 50%。https://arxiv.org/abs/2405.16510 ; https://arxiv.org/abs/2510.07772 ; https://arxiv.org/abs/2603.06064 | 中低：多项方向线索，数字未逐表复核/不能横向比较 |
| Q2 正交+完备及交叉验证、落盘门禁、反方复核各有何边际？ | **公开证据不足；没有找到隔离这些要求的消融。** 不能把框架整体收益归因于某一环节。 | LangChain Plan-and-Execute 与 AutoGen Task Decomposition 展示 planner/executor 或分解机制，不提供组件因果效应。https://www.langchain.com/blog/planning-agents ; https://microsoft.github.io/autogen/0.2/docs/topics/task_decomposition/ | 高（对“本次检索未找到直接消融”）；组件效果未知 |
| Q3 强/中/弱模型收益差异？ | **公开证据不足。** 有论文跨模型报告表现，但任务、提示、训练与执行机制不同，无法识别“强模型不拆解也更好/弱模型更依赖拆解”的交互。 | ACONIC摘要中 Claude 与 LLaMA 分解后分别+8.8pp、+15.0pp；不是匹配的强弱模型因果交互。https://arxiv.org/abs/2510.07772 | 中低 |

> 数字来自公开搜索结果/摘要，未逐表核正文；应视为检索线索而非本报告独立复算。开源框架证据仅证明实现模式存在。总计 6 个来源；未实际调用多模型交叉审阅。

## 小型对照实验方案（证据不足分支，可执行）

### 条件与因果对照
- **V0**：裸 prompt，只给题目与交付格式，不要求拆解、引用、复核或阶段门禁。
- **V1a**：普通任务拆解；列子任务即可，不要求正交、完备或递归原子化。
- **V1b**：prompt-first 01 目标分解（正交+覆盖+递归到原子）——与 V1a 的差识别“正交/完备”附加要求。
- **完整流程**：按任务要求 V1 走 01–04.5。若要拆分要求，依序加臂：V2=加 02 来源/conf；V3=加 02.5 ≥2 独立来源/交叉验证；V4=加 04.5 反方复核；V5=再加逐阶段落盘与 pass 门禁。逐项边际用相邻变体差；该顺序估计的是此顺序下的条件边际，不能假定要求间无交互。
- 每题×变体×模型 **≥3 runs**（满足下限而非充分功效）；按模型内配对、交错随机运行。固定模型版本、工具权限、温度/采样配置、上下文及输出上限；日志记录实际可控参数。若平台不支持固定，则注明限制。

### 模型、任务与判分
- 模型：强/中/弱各至少 1 个，依据实验前公开能力榜单/基准选定并冻结；若 Arena 无法选模型，只用“arena 默认模型”，模型维度 N/A，不事后分强弱。不得声称本会话已经访问或运行这些模型。
- 固定任务集（来自 `rubric/scoring.md`）：(1) Shannon 1948 核心贡献；(2) Bell 1948 与 Shannon 分工/先后；(3) 量子纠错阈值定理数值、提出者、年份；(4) LMArena agent mode vs browser mode 执行层差异（≥2 源）；(5) 开放题：预先指定领域，完整搜集里程碑并选高置信方向。任务 4 易变，运行时冻结查询日期与可用来源。
- 按仓库 rubric D1 正确性40、D2完备性25、D3结构正交20、D4来源/conf 15，总分100；≥80 success，60–79 partial，<60 fail。**任务书另称“18分制”，与 `rubric/scoring.md` 的100分制不一致**；开跑前须由任务负责人澄清/冻结一种换算，当前方案按现存评分文件执行且不伪称18分制。
- 盲评：匿名随机输出；至少两名独立评审，不知变体；预先冻结标准答案/关键事实清单，分歧裁决留痕。执行者自评只能探索性，不能作为主要结论。报告每组成功率、平均分、原始分布及配对差/不确定性；n小不做强显著性或等效性宣称。

## 反方复核、风险与限制

- 内部背景数字不一致：C0 σ=.45、C9 σ=1.53 的**标准差比约3.4**，但方差比是 (1.53/.45)²≈11.6；若“方差低3.4倍”指标准差须修正称谓。n=5 vs 3 极小，均值15.2 vs 15.3不能证明稳定性因果；仅作假设，本报告未据此定结论。
- 分解可能增加无效步骤、token/时延，并可能因子任务边界错误损害答案；规划研究系统常伴随额外训练、工具、反馈，不能归因纯 prompt。
- 每格3 runs、5题样本很小；结论只适用于这组任务和被测模型。要判断稳定性需更多重复与任务，报告方差/区间并预注册分析。
- `ralph`、`ego-browser` 在执行环境未安装；网页 LLM 线索调用失败为环境限制，未循环重试。无法在本会话让其他 Arena 模型各自回答；没有伪造多模型 cross-check 或实际实验结果。

## 来源清单（全部公开 URL）
1. Meta-Task Planning for Language Agents, arXiv:2405.16510 — https://arxiv.org/abs/2405.16510
2. Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks, arXiv:2503.09572 — https://arxiv.org/abs/2503.09572
3. An Approach for Systematic Decomposition of Complex LLM Tasks (ACONIC), arXiv:2510.07772 — https://arxiv.org/abs/2510.07772
4. Agentic LLM Planning via Step-Wise PDDL Simulation, arXiv:2603.06064 — https://arxiv.org/abs/2603.06064
5. LangChain, Plan-and-Execute Agents — https://www.langchain.com/blog/planning-agents
6. Microsoft AutoGen Task Decomposition — https://microsoft.github.io/autogen/0.2/docs/topics/task_decomposition/ （repo：https://github.com/microsoft/autogen）

## 交接
阶段工件：`loop-artifacts/stages/{01,02,02.5,03,04,04.5}/`。外部 Ralph Reviewer 与 Arena 多模型对战不可用，阶段 PASS 是按通用质检标准自检记录，**不是伪造的 Reviewer 回执**。建议下一步：澄清18/100分制；冻结任务5领域与答案清单；确定可控模型；预注册并执行配对 runs；匿名双盲评分后更新本报告。