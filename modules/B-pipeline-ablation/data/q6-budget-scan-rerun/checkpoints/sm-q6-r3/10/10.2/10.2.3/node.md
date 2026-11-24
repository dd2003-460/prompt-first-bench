# N393: 冷启动P99延迟降低幅度ΔT = T_miss_penalty - T_hit，基于N148和N149的中值计算：ΔT = (80+170)/2 - (16+4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N136

## Claim

冷启动P99延迟降低幅度ΔT = T_miss_penalty - T_hit，基于N148和N149的中值计算：ΔT = (80+170)/2 - (16+40)/2 = 125 - 28 = 97ms，降低比例 = 97/125 = 77.6%

## Corrected Claim

冷启动P99延迟降低幅度ΔT = T_miss_penalty - T_hit，基于N148和N149的中值计算：ΔT = (80+170)/2 - (16+40)/2 = 125 - 28 = 97ms，降低比例 = 97/125 = 77.6%

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (80+170)/2=125, (16+40)/2=28, 125-28=97, 97/125=0.776 均正确，且符合冷启动延迟降低的定义逻辑。
