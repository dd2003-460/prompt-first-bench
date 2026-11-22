# N135: LRU 驱逐边界对应的热度分位数 P_evict 与缓存容量 C=128GB 的隐式方程：∫_{P_evict}^{1} N * f_P(p) * E[S|P=

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

LRU 驱逐边界对应的热度分位数 P_evict 与缓存容量 C=128GB 的隐式方程：∫_{P_evict}^{1} N * f_P(p) * E[S|P=p] dp = 128GB

## Corrected Claim

LRU 驱逐边界对应的热度分位数 P_evict 与缓存容量 C=128GB 的隐式方程：∫_{P_evict}^{1} N * f_P(p) * E[S|P=p] dp = 128GB

## Evidence

先验知识/题面给定，逻辑校验通过：该方程正确描述了基于热度分位数的LRU缓存驱逐边界条件，即被保留在缓存中的数据总大小等于缓存容量C。
