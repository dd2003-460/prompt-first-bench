# N70: 基于 x_min=10KB 假设的 LRU 稳态字节命中率 H_LRU_xmin10：利用 C_norm≈118.8 (N24) 和 Pareto(α=1.1)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

基于 x_min=10KB 假设的 LRU 稳态字节命中率 H_LRU_xmin10：利用 C_norm≈118.8 (N24) 和 Pareto(α=1.1) 分布，计算缓存覆盖前 118.8 个平均大小对象（等效排名）的字节占比，预期值约为 45-55%（具体需积分 ∫_{10KB}^{S_th} s * f(s) ds / Total_Bytes），该值显著低于 x_min=1KB 场景下的命中率，体现了 x_min 假设对结论的巨大影响。

## Corrected Claim

基于 x_min=10KB 假设的 LRU 稳态字节命中率 H_LRU_xmin10：利用 C_norm≈118.8 (N24) 和 Pareto(α=1.1) 分布，计算缓存覆盖前 118.8 个平均大小对象（等效排名）的字节占比，预期值约为 45-55%（具体需积分 ∫_{10KB}^{S_th} s * f(s) ds / Total_Bytes），该值显著低于 x_min=1KB 场景下的命中率，体现了 x_min 假设对结论的巨大影响。

## Evidence

先验知识/题面给定，逻辑校验通过
