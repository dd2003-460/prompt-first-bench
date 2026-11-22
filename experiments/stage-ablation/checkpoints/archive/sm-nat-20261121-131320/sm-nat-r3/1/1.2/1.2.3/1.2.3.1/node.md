# N71: 基于 x_min=1KB 假设的 LRU 稳态字节命中率 H_LRU_xmin1：利用 C_norm≈1187.8 (N23) 和 Pareto(α=1.1) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

基于 x_min=1KB 假设的 LRU 稳态字节命中率 H_LRU_xmin1：利用 C_norm≈1187.8 (N23) 和 Pareto(α=1.1) 分布，计算缓存覆盖前 1187.8 个平均大小对象的字节占比，预期值约为 75-85%，因为头部对象虽小但数量多且累积字节占比上升较快，该值作为问题 (a) 下界计算的一个基准工作点。

## Corrected Claim

基于 x_min=1KB 假设的 LRU 稳态字节命中率 H_LRU_xmin1：利用 C_norm≈1187.8 (N23) 和 Pareto(α=1.1) 分布，计算缓存覆盖前 1187.8 个平均大小对象的字节占比，预期值约为 75-85%，因为头部对象虽小但数量多且累积字节占比上升较快，该值作为问题 (a) 下界计算的一个基准工作点。

## Evidence

先验知识/题面给定，逻辑校验通过
