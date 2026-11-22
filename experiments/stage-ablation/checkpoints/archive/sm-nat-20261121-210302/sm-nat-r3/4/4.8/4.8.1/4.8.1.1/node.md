# N186: T_evict 在低缓存占用率下的工作点（N_cap/N_total ≈ 0.1）：假设 N_cap 约为 10,000 个对象（基于平均大小估算），代入公式 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

T_evict 在低缓存占用率下的工作点（N_cap/N_total ≈ 0.1）：假设 N_cap 约为 10,000 个对象（基于平均大小估算），代入公式 T_evict ≈ 1 / (1 + 0.01 * 0.1) ≈ 0.999 天，此时驱逐周期接近更新周期，更新对驱逐的影响可忽略。

## Corrected Claim

T_evict 在低缓存占用率下的工作点（N_cap/N_total ≈ 0.1）：假设 N_cap 约为 10,000 个对象（基于平均大小估算），代入公式 T_evict ≈ 1 / (1 + 0.01 * 0.1) ≈ 0.999 天，此时驱逐周期接近更新周期，更新对驱逐的影响可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 T_evict ≈ 1 / (1 + 0.01 * 0.1) 计算结果为 1/1.001 ≈ 0.999，数值量级与结论（驱逐周期接近更新周期，影响可忽略）在逻辑上自洽。
