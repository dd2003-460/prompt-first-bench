# N216: 工作点 A（快速筛查）：使用 GPT-4o-mini 作为裁判，单次调用成本 $0.0001，延迟 <1s，在逻辑连贯性任务上与 GPT-4o 的相关系数为 0

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N76

## Claim

工作点 A（快速筛查）：使用 GPT-4o-mini 作为裁判，单次调用成本 $0.0001，延迟 <1s，在逻辑连贯性任务上与 GPT-4o 的相关系数为 0.85，适用于迭代过程中的实时反馈，阈值设为 0.75。

## Corrected Claim

工作点 A（快速筛查）：使用 GPT-4o-mini 作为裁判，具有较低的单次调用成本和亚秒级延迟，在逻辑连贯性任务上与 GPT-4o 表现出较高的相关性（通常 >0.8），适用于迭代过程中的实时反馈，建议阈值设为 0.75。

## Evidence

[质询]具体数值（$0.0001成本、<1s延迟、0.85相关系数）属于经验事实，缺乏实时市场数据或特定实验报告支持，且不同任务下相关系数波动较大，0.85仅为特定条件下的估计值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

GPT-4o-mini vs GPT-4o logic consistency evaluation correlation cost
