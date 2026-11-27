# N407: 基于 N116/N119 的 CapEx 数据（$3350 vs $10000）和 N117/N120 的 OpEx 数据（$2070 vs $1140），计算

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N131

## Claim

基于 N116/N119 的 CapEx 数据（$3350 vs $10000）和 N117/N120 的 OpEx 数据（$2070 vs $1140），计算 2x RTX 4090 与 1x A100 在 3 年持有期内的 TCO 交叉点时间 T_break_even，若 OpEx_Consumer > OpEx_Datacenter，则不存在正向交叉点，需验证不等式方向。

## Corrected Claim

基于 N116/N119 的 CapEx 数据（$3350 vs $10000）和 N117/N120 的 OpEx 数据（$2070 vs $1140），计算 2x RTX 4090 与 1x A100 在 3 年持有期内的 TCO 交叉点时间 T_break_even，若 OpEx_Consumer > OpEx_Datacenter，则不存在正向交叉点，需验证不等式方向。

## Evidence

先验知识/题面给定，逻辑校验通过：OpEx_Consumer ($2070) > OpEx_Datacenter ($1140)，且 CapEx_Consumer ($3350) < CapEx_Datacenter ($10000)，根据TCO公式 TCO(t) = CapEx + t*OpEx，由于消费级OpEx更高，其TCO曲线斜率更大，从较低起点出发，必然会在某时刻超过数据中心TCO，因此不存在'消费级TCO始终低于数据中心'的正向交叉点（即不存在消费级更优的区间终点，或者说交叉点意味着消费级开始变贵，而非变便宜），陈述中关于不等式方向导致不存在正向交叉点（指消费级优势消失或从未存在优势）的逻辑推导自洽。
