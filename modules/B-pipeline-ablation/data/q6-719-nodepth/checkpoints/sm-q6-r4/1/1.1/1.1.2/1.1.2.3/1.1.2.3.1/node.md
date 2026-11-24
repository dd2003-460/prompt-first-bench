# N621: 公有云 CDN 在 T=100ms 约束下的总成本增幅因子 F_cost_public(T=100) 的计算公式：F_cost = 1 + (C_optimiz

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N204

## Claim

公有云 CDN 在 T=100ms 约束下的总成本增幅因子 F_cost_public(T=100) 的计算公式：F_cost = 1 + (C_optimization_T100 - C_optimization_T200) / C_base_public，其中 C_optimization_T100 为为满足 100ms P99 所需的额外优化成本（如更高规格实例或专线回源），C_base_public 为基准成本。

## Corrected Claim

公有云 CDN 在 T=100ms 约束下的总成本增幅因子 F_cost_public(T=100) 的计算公式：F_cost = 1 + (C_optimization_T100 - C_optimization_T200) / C_base_public，其中 C_optimization_T100 为为满足 100ms P99 所需的额外优化成本（如更高规格实例或专线回源），C_base_public 为基准成本。

## Evidence

先验知识/题面给定，逻辑校验通过
