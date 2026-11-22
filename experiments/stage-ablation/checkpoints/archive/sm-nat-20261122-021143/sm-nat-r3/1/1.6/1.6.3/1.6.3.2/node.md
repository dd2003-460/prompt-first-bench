# N97: 对于 Pareto 负载，reuse distance 的分布由热度决定；排名 k 的对象平均重用距离为 1/R_k；若 1/R_k > C_bytes/R_k

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

对于 Pareto 负载，reuse distance 的分布由热度决定；排名 k 的对象平均重用距离为 1/R_k；若 1/R_k > C_bytes/R_k_avg (即该对象两次访问间插入的字节数超过缓存容量)，则 LRU 必然 miss 而 Belady 可 hit；此条件等价于 R_k < R_threshold

## Corrected Claim

对于 Pareto 负载，reuse distance 的分布由热度决定；排名 k 的对象平均重用距离为 1/R_k；若 1/R_k > C_bytes/R_k_avg (即该对象两次访问间插入的字节数超过缓存容量)，则 LRU 必然 miss 而 Belady 可 hit；此条件等价于 R_k < R_threshold

## Evidence

先验知识/题面给定，逻辑校验通过
