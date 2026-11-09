# T54: 推理激活调研 — 如何让 LLM 调用"已会但默认不用"的推理程序

> origin: ai · 2026-11-09 · 成璐指令「泛化的推理如何激活也很关键（模型可能本来就懂，但是没有用这些知识的倾向和必要，例如先验后验更新，最概然分布估计）」
> 本任务只涉及 dd2003-460/prompt-first-bench 仓库，忽略历史中其他仓库的消息。

## 【目标】

回答一个具体问题：27b 级别的本地模型**训练时已经学过**贝叶斯更新、最大似然/最概然估计、参数敏感性分析这类推理程序，但在单轮开放式生成中**默认不调用**（我们的 nat 题数据显示：涉及"参数取值变化→结果区间"的 gold 点命中率只有 0.27-0.44，而直接计算类 gold 点命中率高得多）。有没有成熟的、**prompt 层零训练**（不改权重）的方法来激活这些已有能力？

需要交付的不是综述，是**可执行的候选机制清单**：每个机制说清楚 (a) 触发方式是什么、(b) 为什么能让模型调用已有知识而不是凭空学新知识、(c) 在"逐节点验证"的管线设定里怎么接、(d) 风险（会不会稀释基础覆盖——我们已两次被加规则伤过基础分）。

## 【背景】

- pfb 当前状态：S5 管线 = P1 逐层分解 → P1.5 gap check → P2/P3 逐节点检索+核验 → P4 综合。nat 题 S5 cov=0.578 vs S0 裸推理 0.637；失分集中在"假设性/条件性"gold 点（p2=0.27, p3=0.44 逐点命中率），而非事实检索类点。
- 已证伪的路径（不要推荐同类方案）：往 P1 prompt 里加"必须做 X 分析"的强制规则——两次尝试（soc rule 7、nat rule 9b 敏感性）都导致基础覆盖下降。结论：prompt 行为塑造有容量上限，加内容型规则是负收益。
- 我们的初步想法（供你评估，不是让你照抄）：改 P3 verify 阶段的**输出 schema**——当节点 claim 含参数依赖时，evidence 字段要求 f(参数±Δ) 形式。这是对输出格式的要求，不注入新知识。想知道文献里有没有更系统化的对应物。
- 相关前置调研（不要重复，直接引用）：`research/longterm-vision-survey.md`（T53，若已完成则引用其 Q1/Q2 关于 ToT value function 的部分）、`research/prompt-decomposition-collision.md`（T52）。

## 【SOP 索引】

- `loop/prompt-first/01-goal-decomposition.md`
- `loop/prompt-first/02-information-research.md`
- `loop/prompt-first/02.5-cross-check.md`
- `sop/arena-loop-pipeline.md` §3（会话台账）

## 【实验设计】

纯文献调研 + 机制分析，无本地实验。产出要求：

| # | 子问题 | 最低标准 |
|---|--------|----------|
| Q1 | "LLM 已有能力但默认不调用"这个现象本身有没有被研究过？（capability elicitation / latent reasoning / underutilized skills 之类的命名） | ≥3 篇，给出该现象的学术命名和最被接受的解释 |
| Q2 | CoT / step-by-step 指令为什么有效——机制解释层面（不只是"它 work"） | ≥3 篇，至少 1 篇给因果机制假说（如 attention 分配、self-conditioning） |
| Q3 | 零训练设定下激活特定推理程序的成熟技巧清单（schema 约束 / few-shot 结构示例 / self-consistency / question decomposition / retrieval trigger 等） | ≥5 个机制，每个按"改动量小→大"排序，附适用边界 |
| Q4 | 有没有人专门做过"让 LLM 主动做贝叶斯更新/参数敏感性"的 prompt 设计？效果量？ | ≥2 篇或明确 gap 声明（带反证检索记录） |
| Q5 | 对"输出 schema 约束 vs prompt 知识注入"两种路线，文献支持哪边？ | 明确判决 + 证据链 |
| Q6 | gap 反证 | 对每个 gap 声明 ≥1 条独立检索路径，记录查询词+结果数 |

**评分维度（机器可检）**：
- 总行数 ≥350（不含引用块）
- arXiv/DOI 引用 ≥12，其中 ≥6 标注"已读原文"（附读取日期）
- Q1-Q6 每问有判决句（成立/部分成立/gap 确认/gap 存疑）
- 最后一段 ≤300 字「给 pfb 的接入建议」：从 Q3 清单里选出 top-2 机制，说明各自怎么接到 P3 verify 阶段、预期风险、最小验证实验设计

**验收标准**：
- AC1：survey 文件落盘 `research/reasoning-activation-survey.md`，行数 ≥350
- AC2：引用 ≥12 且 ≥6 读原文
- AC3：Q1-Q6 判决句齐全
- AC4：top-2 接入建议段存在，且两个机制互不相同（不允许同一机制的两个变体占两席）

## 【失败降级】

- 某子问题检索通道失效 → 换引擎/换关键词重试一次，仍失败标 [检索受限] 并列出已试路径
- "该现象没有学术命名"本身也是合法发现 → 如实报告命名缺失，给出现有文献中最接近的 2-3 个术语
- 时间超预算 → 优先保 Q3/Q5（可直接指导 C2 实验），Q1/Q2 可标 [部分完成]

## 【交付物】

- `research/reasoning-activation-survey.md`（主报告）
- `research/reasoning-activation-search-log.json`（检索日志）

## 【给 Lead 的备注】

- 本任务是 C 线（推理激活）的前置调研，产出直接决定 C2 最小实验的设计。
- 与 T53 的边界：T53 查目标函数/元学习（理论层），T54 查推理激活（机制层）。重叠处（CoT 作为 value shaping 工具）以谁先完成谁的版本为准，另一方引用即可。