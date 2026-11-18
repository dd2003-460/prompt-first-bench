# N188: 字节命中率下界的修正项：N82 的公式 H_byte ≈ 1 - (K/N)^{1-β} 假设所有缓存对象大小相同。修正公式应引入大小加权因子：H_byte_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

字节命中率下界的修正项：N82 的公式 H_byte ≈ 1 - (K/N)^{1-β} 假设所有缓存对象大小相同。修正公式应引入大小加权因子：H_byte_corrected ≈ Σ_{i=1}^{K} (h_i * s_i) / Σ_{i=1}^{N} (h_i * s_i)。利用 N67 的结论，分子分母均需按 i^{-(α+β)} 积分。

## Corrected Claim

字节命中率下界的修正项：N82 的公式 H_byte ≈ 1 - (K/N)^{1-β} 假设所有缓存对象大小相同。修正公式应引入大小加权因子：H_byte_corrected ≈ Σ_{i=1}^{K} (h_i * s_i) / Σ_{i=1}^{N} (h_i * s_i)。利用 N67 的结论，分子分母均需按 i^{-(α+β)} 积分。

## Evidence

先验知识/题面给定，逻辑校验通过
