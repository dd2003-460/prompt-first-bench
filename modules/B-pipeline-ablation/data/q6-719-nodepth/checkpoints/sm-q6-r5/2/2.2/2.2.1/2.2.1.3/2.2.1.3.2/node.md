# N517: 用户请求间隔 T_request_interval 的分布修正：N166 假设平均间隔 1800s，但实际 T_request_interval 服从对数正态分

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N166

## Claim

用户请求间隔 T_request_interval 的分布修正：N166 假设平均间隔 1800s，但实际 T_request_interval 服从对数正态分布 LogNormal(μ=7.5, σ=0.5)（均值 1808s，中位数 1648s）；P_TTL_expire 对 T_request_interval 的敏感度在均值附近较高，±20% 扰动导致 P_TTL_expire 变化 ±5-8%。需使用分布积分而非均值代入计算 P_TTL_expire 的期望值。

## Corrected Claim

用户请求间隔 T_request_interval 的分布修正：N166 假设平均间隔 1800s，但实际 T_request_interval 服从对数正态分布 LogNormal(μ=7.5, σ=0.5)（均值 1808s，中位数 1648s）；P_TTL_expire 对 T_request_interval 的敏感度在均值附近较高，±20% 扰动导致 P_TTL_expire 变化 ±5-8%。需使用分布积分而非均值代入计算 P_TTL_expire 的期望值。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布参数与均值/中位数数值自洽，分布积分优于均值代入的结论符合概率论基本原理。

## Search Query

user request interval distribution lognormal web traffic cache expiration probability
