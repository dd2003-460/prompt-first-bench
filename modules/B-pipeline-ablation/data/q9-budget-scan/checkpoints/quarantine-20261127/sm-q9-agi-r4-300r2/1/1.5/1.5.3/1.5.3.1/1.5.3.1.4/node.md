# N290: ReAct 单步 Token 消耗精确分解：T_Action_Prompt 固定开销为 JSON 结构头尾 + 工具名 ≈ 15-25 tokens；T_Obs

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N115, N116, N117

## Claim

ReAct 单步 Token 消耗精确分解：T_Action_Prompt 固定开销为 JSON 结构头尾 + 工具名 ≈ 15-25 tokens；T_Observation_Return 取决于工具类型，代码执行返回 stdout/stderr 通常截断至 512 tokens (P95)，Web 检索返回摘要平均 256-384 tokens；相比 CoT 纯思维链平均 80-120 tokens/步，ReAct 单步 Token 膨胀率 Ratio_Expansion = (15+512) / 100 ≈ 5.27x (保守估计，若观察返回较短则降至 2-3x)。

## Corrected Claim

ReAct 单步 Token 消耗显著高于 CoT。T_Action_Prompt 固定开销较小（约 15-25 tokens）；T_Observation_Return 高度依赖工具类型及返回内容长度，代码执行和 Web 检索通常返回数百 tokens 的内容（具体数值依实现而定，常见截断限制在 256-1024 tokens 之间）。相比 CoT 纯思维链平均 80-120 tokens/步，ReAct 单步 Token 膨胀率通常在 2x 到 5x 以上，具体取决于观察返回的长度。

## Evidence

[质询]数值量级缺乏普适性：'512 tokens'作为代码执行返回的P95截断值以及'256-384 tokens'作为Web检索摘要的平均值属于特定实现的经验参数，不同框架（如LangChain, AutoGen）或工具配置下差异巨大，不能视为ReAct范式的固有属性。 | 经验事实，逻辑自洽但缺来源支持；具体Token数值为特定场景下的经验估算，非第一性原理可推导的恒定值。

## Search Query

ReAct agent token consumption analysis observation length truncation cost comparison chain of thought
