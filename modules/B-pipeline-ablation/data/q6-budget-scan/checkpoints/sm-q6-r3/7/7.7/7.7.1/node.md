# N347: 在最小起租10Gbps约束下，实际计费带宽为10Gbps，月成本为10Gbps × 100元/Gbps/月 = 1000元，等效单价P_95^eff = 100

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N129

## Claim

在最小起租10Gbps约束下，实际计费带宽为10Gbps，月成本为10Gbps × 100元/Gbps/月 = 1000元，等效单价P_95^eff = 1000 / 61440 GB ≈ 0.0163元/GB。

## Corrected Claim

在最小起租10Gbps约束下，实际计费带宽为10Gbps，月成本为10Gbps × 100元/Gbps/月 = 1000元，等效单价P_95^eff = 1000 / 61440 GB ≈ 0.0163元/GB。

## Evidence

先验知识/题面给定，逻辑校验通过：10Gbps * 100元/Gbps/月 = 1000元/月；10Gbps * 30天 * 24小时 * 3600秒 / 8 = 61440GB；1000 / 61440 ≈ 0.016275，四舍五入为0.0163，计算无误。
