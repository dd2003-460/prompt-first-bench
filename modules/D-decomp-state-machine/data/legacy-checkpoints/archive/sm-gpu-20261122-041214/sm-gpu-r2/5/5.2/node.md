# N41: 功耗数据来源不确定性：GPU TDP（如 4090 450W, A100 400W）为官方标称值，实际峰值功耗可能高出 10-20%。机房 PUE（Power 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

功耗数据来源不确定性：GPU TDP（如 4090 450W, A100 400W）为官方标称值，实际峰值功耗可能高出 10-20%。机房 PUE（Power Usage Effectiveness）通常为 1.2-1.5，电力成本计算需乘以 PUE 系数。若 PUE 未知，按 1.3 估算，误差范围 ±0.2。

## Corrected Claim

功耗数据来源不确定性：GPU TDP（如 4090 450W, A100 400W）为官方标称值，实际峰值功耗可能高出 10-20%。机房 PUE（Power Usage Effectiveness）通常为 1.2-1.5，电力成本计算需乘以 PUE 系数。若 PUE 未知，按 1.3 估算，误差范围 ±0.2。

## Evidence

先验知识/题面给定，逻辑校验通过：GPU TDP 为标称值且实际峰值略高符合工程常识，PUE 1.2-1.5 为行业典型范围，1.3 为合理估算中值，数值量级与逻辑均自洽。

## Search Query

data center PUE average 2024
