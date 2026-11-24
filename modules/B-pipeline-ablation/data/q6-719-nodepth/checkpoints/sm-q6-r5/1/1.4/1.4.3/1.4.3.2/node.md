# N153: Safety_Margin 的量化依据：基于 N106 的成本放大系数 C_amp ≈ 1.2，Safety_Margin 应至少覆盖流量波动导致的峰值偏差，建

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

Safety_Margin 的量化依据：基于 N106 的成本放大系数 C_amp ≈ 1.2，Safety_Margin 应至少覆盖流量波动导致的峰值偏差，建议取 25% 以平衡采购成本与过载风险；若取 20%，则 P(过载) ≈ 5%，需结合 SLA 违约成本进一步优化。

## Corrected Claim

Safety_Margin 的量化依据：基于 N106 的成本放大系数 C_amp ≈ 1.2，Safety_Margin 应至少覆盖流量波动导致的峰值偏差，建议取 25% 以平衡采购成本与过载风险；若取 20%，则 P(过载) ≈ 5%，需结合 SLA 违约成本进一步优化。

## Evidence

先验知识/题面给定，逻辑校验通过
