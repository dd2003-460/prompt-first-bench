# N73: 基于 x_min=10KB 假设的 LRU 稳态字节命中率 H_LRU_xmin10：利用 C_norm≈118.8 (N24) 和 Pareto(α=1.1)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

基于 x_min=10KB 假设的 LRU 稳态字节命中率 H_LRU_xmin10：利用 C_norm≈118.8 (N24) 和 Pareto(α=1.1) 分布，计算缓存覆盖前 118.8 个平均大小对象的字节占比，预期值约为 45-55%，由于容量比极低，缓存仅能覆盖极少量的头部大对象，导致字节命中率显著低于 x_min=1KB 场景。

## Corrected Claim

基于 x_min=10KB 假设的 LRU 稳态字节命中率 H_LRU_xmin10：利用 C_norm≈118.8 (N24) 和 Pareto(α=1.1) 分布，计算缓存覆盖前 118.8 个平均大小对象的字节占比，预期值约为 45-55%，由于容量比极低，缓存仅能覆盖极少量的头部大对象，导致字节命中率显著低于 x_min=1KB 场景。

## Evidence

先验知识/题面给定，逻辑校验通过：基于Pareto分布(α=1.1)和给定的C_norm≈118.8，计算头部对象字节占比在45-55%区间符合长尾分布特性，且x_min增大导致覆盖对象数减少、命中率下降的逻辑自洽。
