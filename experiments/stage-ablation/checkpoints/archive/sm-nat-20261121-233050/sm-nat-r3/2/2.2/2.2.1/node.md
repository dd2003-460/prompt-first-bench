# N36: K 值的精确计算：K 不是由 Sum S_i <= 128GB 直接确定，而是由 LRU 的“热度-大小”权衡决定。在 ρ=-0.3 下，最热的 K 个对象的总

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

K 值的精确计算：K 不是由 Sum S_i <= 128GB 直接确定，而是由 LRU 的“热度-大小”权衡决定。在 ρ=-0.3 下，最热的 K 个对象的总大小 Sum_{i=1}^K S_i 随 K 增长缓慢（因热门对象小），因此 K 可远大于 128GB / E[S|hot]，需解方程 Sum_{i=1}^K S_i(rank by F) = 128GB。

## Corrected Claim

K 值的精确计算：K 不是由 Sum S_i <= 128GB 直接确定，而是由 LRU 的“热度-大小”权衡决定。在 ρ=-0.3 下，最热的 K 个对象的总大小 Sum_{i=1}^K S_i 随 K 增长缓慢（因热门对象小），因此 K 可远大于 128GB / E[S|hot]，需解方程 Sum_{i=1}^K S_i(rank by F) = 128GB。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU缓存容量约束下，K值确实由累积大小等于容量决定，而非简单除法，且负相关系数下热门对象小导致K值偏大的逻辑自洽。
