# N102: 动态更新导致的缓存失效概率 P_invalid(i)：P_invalid(i) = 1 - exp(-λ_update * W_LRU(i))，其中 W_LRU

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

动态更新导致的缓存失效概率 P_invalid(i)：P_invalid(i) = 1 - exp(-λ_update * W_LRU(i))，其中 W_LRU(i) 为对象 i 在缓存中的驻留时间；当 λ_update * W_LRU(i) << 1 时，P_invalid(i) ≈ λ_update * W_LRU(i)。

## Corrected Claim

动态更新导致的缓存失效概率 P_invalid(i)：P_invalid(i) = 1 - exp(-λ_update * W_LRU(i))，其中 W_LRU(i) 为对象 i 在缓存中的驻留时间；当 λ_update * W_LRU(i) << 1 时，P_invalid(i) ≈ λ_update * W_LRU(i)。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式基于泊松过程假设（更新事件服从指数分布），P_invalid = 1 - exp(-λt) 是标准推导，且当 λt << 1 时利用泰勒展开 exp(-x) ≈ 1-x 得到近似式，数学逻辑自洽。
