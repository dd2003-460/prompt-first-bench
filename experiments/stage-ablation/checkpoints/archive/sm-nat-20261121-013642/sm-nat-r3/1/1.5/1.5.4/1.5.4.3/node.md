# N138: 对象数量覆盖率 H_obj 的数值估算：H_obj = K/N，其中 K 为缓存中保留的对象数，由 N98 的 r_threshold 和 Pareto(β=0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

对象数量覆盖率 H_obj 的数值估算：H_obj = K/N，其中 K 为缓存中保留的对象数，由 N98 的 r_threshold 和 Pareto(β=0.9) 分布确定，K = N * (r_min/r_threshold)^β，若 r_threshold=5.0/day, r_min=0.1/day, β=0.9，则 K = 100,000 * (0.02)^0.9 ≈ 100,000 * 0.026 ≈ 2600，H_obj ≈ 2.6%。

## Corrected Claim

对象数量覆盖率 H_obj 的数值估算：H_obj = K/N，其中 K 为缓存中保留的对象数，由 N98 的 r_threshold 和 Pareto(β=0.9) 分布确定，K = N * (r_min/r_threshold)^β，若 r_threshold=5.0/day, r_min=0.1/day, β=0.9，则 K = 100,000 * (0.02)^0.9 ≈ 100,000 * 0.026 ≈ 2600，H_obj ≈ 2.6%。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 (0.02)^0.9 ≈ 0.026 正确，推导过程自洽

## Search Query

object count hit rate cache LRU
