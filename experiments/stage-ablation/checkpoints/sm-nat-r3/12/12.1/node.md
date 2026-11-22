# N300: LRU缓存对象集合 S_LRU 在128GB容量下的精确边界：设对象按热度降序排列，S_LRU = {i | Σ_{j=1}^i S_j ≤ 128GB}，其中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N107

## Claim

LRU缓存对象集合 S_LRU 在128GB容量下的精确边界：设对象按热度降序排列，S_LRU = {i | Σ_{j=1}^i S_j ≤ 128GB}，其中 S_j 为第 j 热门对象的大小；需通过数值积分计算满足该不等式的最大对象数 N_LRU，以确定 f_byte_cached 的分母基准。

## Corrected Claim

LRU缓存对象集合 S_LRU 在128GB容量下的精确边界：设对象按热度降序排列，S_LRU = {i | Σ_{j=1}^i S_j ≤ 128GB}，其中 S_j 为第 j 热门对象的大小；需通过数值积分计算满足该不等式的最大对象数 N_LRU，以确定 f_byte_cached 的分母基准。

## Evidence

先验知识/题面给定，逻辑校验通过
