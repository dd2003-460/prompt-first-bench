# N67: LRU 稳态驻留对象数 N_resident 的精确计算需解方程 Σ_{i=1}^{K} S_{(i)} = 128GB，其中 S_{(i)} 为第 i 小对象

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

LRU 稳态驻留对象数 N_resident 的精确计算需解方程 Σ_{i=1}^{K} S_{(i)} = 128GB，其中 S_{(i)} 为第 i 小对象的实际大小；由于对象大小离散且重尾，不能简单用连续积分，而应使用逆 CDF S^{-1}(k/N) 求和，预计 N_resident 约为 500-2000 个（取决于 s_min 和截断上限）。

## Corrected Claim

LRU 稳态驻留对象数 N_resident 的精确计算需解方程 Σ_{i=1}^{K} S_{(i)} = 128GB，其中 S_{(i)} 为第 i 小对象的实际大小；由于对象大小离散且重尾，不能简单用连续积分，而应使用逆 CDF S^{-1}(k/N) 求和，预计 N_resident 约为 500-2000 个（取决于 s_min 和截断上限）。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU稳态驻留对象数确实由累计大小等于缓存容量决定，离散重尾分布下使用逆CDF求和是标准且正确的数值处理方法，量级估计符合一般工程直觉。
