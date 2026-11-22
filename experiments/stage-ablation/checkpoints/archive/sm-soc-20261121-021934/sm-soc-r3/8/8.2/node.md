# N135: 信息获取成本 C_info 的量化表达式为 C_info = T_att * W_time，其中 T_att 为买家处理价格变化所需的平均注意力时间（秒），W_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

信息获取成本 C_info 的量化表达式为 C_info = T_att * W_time，其中 T_att 为买家处理价格变化所需的平均注意力时间（秒），W_time 为买家单位时间机会成本（元/秒），该成本与降价幅度 ΔP 存在非线性关系：当 ΔP < σ_perception 时，C_info 趋近于 ∞，导致咨询率 Change_Rate ≈ 0。

## Corrected Claim

信息获取成本 C_info 的量化表达式为 C_info = T_att * W_time，其中 T_att 为买家处理价格变化所需的平均注意力时间（秒），W_time 为买家单位时间机会成本（元/秒），该成本与降价幅度 ΔP 存在非线性关系：当 ΔP < σ_perception 时，C_info 趋近于 ∞，导致咨询率 Change_Rate ≈ 0。

## Evidence

先验知识/题面给定，逻辑校验通过
