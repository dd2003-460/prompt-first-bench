# N300: 字节命中率 H_byte_lower 的数值估算：H_byte_lower = Num_Hit / Denom_Total，基于 N107 和 N108 的结果

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N103

## Claim

字节命中率 H_byte_lower 的数值估算：H_byte_lower = Num_Hit / Denom_Total，基于 N107 和 N108 的结果，预计值在 10%-15% 区间，需对比 N100 中的 0.120 基准值，并量化负相关 ρ=-0.3 对分子项的提升系数（即小对象高热度导致的命中率增益 Δρ_H ≈ 2-5% 的绝对值贡献）。

## Corrected Claim

字节命中率 H_byte_lower 的数值估算：H_byte_lower = Num_Hit / Denom_Total，基于 N107 和 N108 的结果，预计值在 10%-15% 区间，需对比 N100 中的 0.120 基准值，并量化负相关 ρ=-0.3 对分子项的提升系数（即小对象高热度导致的命中率增益 Δρ_H ≈ 2-5% 的绝对值贡献）。

## Evidence

先验知识/题面给定，逻辑校验通过
