# N92: 低频大对象带宽占比 B_tail 的数值计算：B_tail = (Σ_{i: f_i < f_threshold, S_i > C/K} f_i * S_i) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

低频大对象带宽占比 B_tail 的数值计算：B_tail = (Σ_{i: f_i < f_threshold, S_i > C/K} f_i * S_i) / (Σ_{all} f_i * S_i)；其中 f_threshold 为累计请求频率 95% 对应的频率值，C/K 为平均缓存对象大小；计算该比值，量化 LRU 因驱逐低频大对象而损失的潜在命中率上限。

## Corrected Claim

低频大对象带宽占比 B_tail 的数值计算：B_tail = (Σ_{i: f_i < f_threshold, S_i > C/K} f_i * S_i) / (Σ_{all} f_i * S_i)；其中 f_threshold 为累计请求频率 95% 对应的频率值，C/K 为平均缓存对象大小；计算该比值，量化 LRU 因驱逐低频大对象而损失的潜在命中率上限。

## Evidence

先验知识/题面给定，逻辑校验通过
