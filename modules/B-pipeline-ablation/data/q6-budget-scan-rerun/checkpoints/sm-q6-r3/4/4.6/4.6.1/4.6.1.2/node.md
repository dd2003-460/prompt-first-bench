# N276: 工作点B（性价比平衡）：自建核心区域配置利用率目标 U_target=55%，闲置成本 C_idle_self_core_B = C_total_self_co

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N88

## Claim

工作点B（性价比平衡）：自建核心区域配置利用率目标 U_target=55%，闲置成本 C_idle_self_core_B = C_total_self_core_annual × (1 - 0.55) / (R_total_annual_core / 1000)，此点通常对应 P99 延迟合规边界附近的最低总成本工作点

## Corrected Claim

工作点B（性价比平衡）：自建核心区域配置利用率目标 U_target=55%，闲置成本 C_idle_self_core_B = C_total_self_core_annual × (1 - 0.55) / (R_total_annual_core / 1000)，此点通常对应 P99 延迟合规边界附近的最低总成本工作点

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合成本分摊逻辑，55%利用率作为平衡点在工程上合理
