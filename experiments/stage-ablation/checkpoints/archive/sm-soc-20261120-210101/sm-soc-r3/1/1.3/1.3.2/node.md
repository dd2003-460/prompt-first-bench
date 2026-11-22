# N39: 搜索成本衰减系数 k 的量化：C_search(t) = C_0 * e^(-kt) 中的 k 值。k 反映买家耐心程度的倒数，k = -ln(0.5) / T

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N8

## Claim

搜索成本衰减系数 k 的量化：C_search(t) = C_0 * e^(-kt) 中的 k 值。k 反映买家耐心程度的倒数，k = -ln(0.5) / T_half，其中 T_half 为搜索成本减半的时间。假设 T_half = 15分钟，则 k ≈ 0.046/min。需验证不同品类（服装 vs 数码）的 k 值差异。

## Corrected Claim

搜索成本衰减系数 k 的量化：C_search(t) = C_0 * e^(-kt) 中的 k 值。k 反映买家耐心程度的倒数，k = -ln(0.5) / T_half，其中 T_half 为搜索成本减半的时间。假设 T_half = 15分钟，则 k ≈ 0.046/min。需验证不同品类（服装 vs 数码）的 k 值差异。

## Evidence

先验知识/题面给定，逻辑校验通过：k = -ln(0.5)/15 ≈ 0.0462/min，数值计算正确，模型定义自洽。
