# N233: 共享随机源：P(IgnoreLabel) 的估计模型为 P(IgnoreLabel) = 1 - P(ReadLabel)，其中 P(ReadLabel) 由 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N71

## Claim

共享随机源：P(IgnoreLabel) 的估计模型为 P(IgnoreLabel) = 1 - P(ReadLabel)，其中 P(ReadLabel) 由 N116 定义的曝光率与疲劳率决定；该值在 N71 公式中作为负向调节项，其不确定性直接传导至 ΔQ 的置信区间。

## Corrected Claim

共享随机源：P(IgnoreLabel) 的估计模型为 P(IgnoreLabel) = 1 - P(ReadLabel)，其中 P(ReadLabel) 由 N116 定义的曝光率与疲劳率决定；该值在 N71 公式中作为负向调节项，其不确定性直接传导至 ΔQ 的置信区间。

## Evidence

先验知识/题面给定，逻辑校验通过：P(IgnoreLabel) 与 P(ReadLabel) 构成互补事件，概率和为1，逻辑自洽；作为负向调节项影响置信区间符合统计推断直觉。

## Search Query

label ignore probability model user behavior logging
