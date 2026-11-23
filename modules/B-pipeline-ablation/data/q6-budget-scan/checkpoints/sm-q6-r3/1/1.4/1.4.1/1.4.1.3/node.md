# N144: 混合策略中DNS路由切换的P99延迟贡献 ΔP99_dns = P_switch * t_lookup_p99，其中 P_switch 为单位请求内发生DNS切

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

混合策略中DNS路由切换的P99延迟贡献 ΔP99_dns = P_switch * t_lookup_p99，其中 P_switch 为单位请求内发生DNS切换的概率，t_lookup_p99 为DNS递归查询P99耗时（基准值 20-50ms），若 P_switch < 0.01，则 ΔP99_dns < 0.5ms，可忽略。

## Corrected Claim

混合策略中DNS路由切换的P99延迟贡献 ΔP99_dns = P_switch * t_lookup_p99，其中 P_switch 为单位请求内发生DNS切换的概率，t_lookup_p99 为DNS递归查询P99耗时（基准值 20-50ms），若 P_switch < 0.01，则 ΔP99_dns < 0.5ms，可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导正确（0.01 * 50ms = 0.5ms），符合概率加权延迟贡献的基本原理。
