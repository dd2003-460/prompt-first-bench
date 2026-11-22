# N44: 缓存内对象热度分布：缓存内对象的平均请求频率 E[r_i|Cache] 显著高于全局平均，需计算 E[r_i | s_i < s_threshold]，其中 s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

缓存内对象热度分布：缓存内对象的平均请求频率 E[r_i|Cache] 显著高于全局平均，需计算 E[r_i | s_i < s_threshold]，其中 s_threshold 为容量约束下可容纳的对象大小阈值。

## Corrected Claim

缓存内对象热度分布：缓存内对象的平均请求频率 E[r_i|Cache] 显著高于全局平均，需计算 E[r_i | s_i < s_threshold]，其中 s_threshold 为容量约束下可容纳的对象大小阈值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

conditional expectation frequency given size cache constraint
