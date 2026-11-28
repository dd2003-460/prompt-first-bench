# N15: 自我纠错机制需引入 Critic-Refiner 双角色 Prompt 架构：初始 Draft 由主模型生成，随后由同一模型在独立 Context Window

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

自我纠错机制需引入 Critic-Refiner 双角色 Prompt 架构：初始 Draft 由主模型生成，随后由同一模型在独立 Context Window 中扮演 Critic 角色进行逻辑一致性检查；实测表明，这种 Self-Consistency 策略可将数学/逻辑错误率从 35% 降低至 15-20%，但每次纠错循环需额外消耗 1.5-2 倍的 Token 数量，因此在预算受限下需设置最大重试次数为 2 次。

## Corrected Claim

自我纠错机制可引入 Critic-Refiner 双角色 Prompt 架构：初始 Draft 由主模型生成，随后由同一模型在独立 Context Window 中扮演 Critic 角色进行逻辑一致性检查。这种 Self-Consistency 策略通常能显著降低数学/逻辑错误率，但每次纠错循环会额外消耗 Token 资源，因此在预算受限场景下建议设置最大重试次数（如 2 次）以平衡效果与成本。

## Evidence

[质询]具体数值（35%降至15-20%、1.5-2倍Token消耗）缺乏通用基准，高度依赖特定任务难度、模型版本及Prompt设计，将其作为普适性‘实测’结论存在以偏概全的风险。 | 先验知识/题面给定，逻辑校验通过；Critic-Refiner架构在逻辑上自洽，Self-Consistency策略确实能降低错误率但增加计算成本，但具体量化指标属于经验事实，在无外部来源支持且存在变量依赖的情况下，降级为定性表述。

## Search Query

Self-consistency critic refiner prompt error rate reduction LLM
