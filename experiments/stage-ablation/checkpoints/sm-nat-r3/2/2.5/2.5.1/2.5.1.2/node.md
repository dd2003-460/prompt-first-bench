# N163: 128GB 容量对应的对象大小截断点 S_128 定义为满足 ∫_{x_min}^{S_128} f_S(s) ds = N_128 / N_total 的分位

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N56

## Claim

128GB 容量对应的对象大小截断点 S_128 定义为满足 ∫_{x_min}^{S_128} f_S(s) ds = N_128 / N_total 的分位数，其中 N_128 = 128GB / E[S]_truncated；若 E[S]_truncated ≈ 154KB（基于 x_max=1GB），则 N_128 ≈ 875,000，但 N_total=100,000，故 S_128 应取 x_max=1GB，Byte_Coverage_128 = 100%。

## Corrected Claim

128GB 容量对应的对象大小截断点 S_128 定义为满足 ∫_{x_min}^{S_128} f_S(s) ds = N_128 / N_total 的分位数，其中 N_128 = 128GB / E[S]_truncated；若 E[S]_truncated ≈ 154KB（基于 x_max=1GB），则 N_128 ≈ 875,000，但 N_total=100,000，故 S_128 应取 x_max=1GB，Byte_Coverage_128 = 100%。

## Evidence

先验知识/题面给定，逻辑校验通过：N_128 (875,000) 远大于 N_total (100,000)，意味着128GB容量足以覆盖所有对象，因此截断点 S_128 必然取最大值 x_max，覆盖率100%。
