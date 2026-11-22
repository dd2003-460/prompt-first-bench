# N42: 缓存污染惩罚项 P_pollution 的数值估算：P_pollution = 1 - (128GB / ∑_{i=1}^{k_max} S_i)^1.1，由于

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9, N10, N11

## Claim

缓存污染惩罚项 P_pollution 的数值估算：P_pollution = 1 - (128GB / ∑_{i=1}^{k_max} S_i)^1.1，由于热门对象较小，∑_{i=1}^{k_max} S_i 可能小于 128GB，导致 P_pollution 接近 0；若 ∑_{i=1}^{k_max} S_i 接近 128GB，则 P_pollution ≈ 0.05-0.1。

## Corrected Claim

缓存污染惩罚项 P_pollution 的数值估算：P_pollution = 1 - (128GB / ∑_{i=1}^{k_max} S_i)^1.1，由于热门对象较小，∑_{i=1}^{k_max} S_i 可能小于 128GB，导致 P_pollution 接近 0；若 ∑_{i=1}^{k_max} S_i 接近 128GB，则 P_pollution ≈ 0.05-0.1。
