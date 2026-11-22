# N148: 工作点1（高频小对象主导，高信度/低字节贡献）：在 β=0.9 下，f_threshold 设为总请求量的 90% 分位（即 top 10% 对象），P(fre

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

工作点1（高频小对象主导，高信度/低字节贡献）：在 β=0.9 下，f_threshold 设为总请求量的 90% 分位（即 top 10% 对象），P(freq > f_threshold) = 0.1，E[size | freq > f_threshold] ≈ 0.8 * E[size]（因 ρ=-0.3），则 B_LFU_only ≈ 0.1 * N_total * 0.8 * E[size] * r_avg_high，此工作点量化了 LFU 保留的‘高频但非最近’对象中，小对象占主导导致的字节量低估。

## Corrected Claim

工作点1（高频小对象主导，高信度/低字节贡献）：在 β=0.9 下，f_threshold 设为总请求量的 90% 分位（即 top 10% 对象），P(freq > f_threshold) = 0.1，E[size | freq > f_threshold] ≈ 0.8 * E[size]（因 ρ=-0.3），则 B_LFU_only ≈ 0.1 * N_total * 0.8 * E[size] * r_avg_high，此工作点量化了 LFU 保留的‘高频但非最近’对象中，小对象占主导导致的字节量低估。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合概率期望定义，数值量级（0.1 * 0.8）合理，无内部矛盾。
