# N528: 混合策略放弃临界点 P_core_critical 的计算公式：P_core_critical = (C_fixed_self + C_ops_self - C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N174

## Claim

混合策略放弃临界点 P_core_critical 的计算公式：P_core_critical = (C_fixed_self + C_ops_self - C_bandwidth_delta) / (C_bandwidth_public - C_bandwidth_self)，其中 C_bandwidth_delta 为混合策略相比全自建节省的带宽成本，该值决定了地理分布分散程度导致混合策略失效的边界。

## Corrected Claim

混合策略放弃临界点 P_core_critical 的计算公式：P_core_critical = (C_fixed_self + C_ops_self - C_bandwidth_delta) / (C_bandwidth_public - C_bandwidth_self)，其中 C_bandwidth_delta 为混合策略相比全自建节省的带宽成本，该值决定了地理分布分散程度导致混合策略失效的边界。

## Evidence

先验知识/题面给定，逻辑校验通过
