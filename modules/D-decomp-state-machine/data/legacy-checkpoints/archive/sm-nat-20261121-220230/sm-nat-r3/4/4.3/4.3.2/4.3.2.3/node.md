# N203: K_diff 的核心贡献项来自‘高频但大’对象，其数量 K_high_freq_large 可通过积分估算：K_high_freq_large ≈ ∫_{f >

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

K_diff 的核心贡献项来自‘高频但大’对象，其数量 K_high_freq_large 可通过积分估算：K_high_freq_large ≈ ∫_{f > f_th} P(S > s_min | f) N(f) df，其中 s_min 为 LRU 驱逐边界对应的大小，需结合 β=0.9 和 α=1.1 的联合分布计算。

## Corrected Claim

K_diff 的核心贡献项来自‘高频但大’对象，其数量 K_high_freq_large 可通过积分估算：K_high_freq_large ≈ ∫_{f > f_th} P(S > s_min | f) N(f) df，其中 s_min 为 LRU 驱逐边界对应的大小，需结合 β=0.9 和 α=1.1 的联合分布计算。

## Evidence

先验知识/题面给定，逻辑校验通过
