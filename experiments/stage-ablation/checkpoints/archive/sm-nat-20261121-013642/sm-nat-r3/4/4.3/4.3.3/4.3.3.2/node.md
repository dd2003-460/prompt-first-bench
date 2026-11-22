# N188: 工作点B（元数据刷新主导）：假设更新中 10% 为内容变更 (P_hit_cold=0)，90% 为元数据刷新 (P_hit_cold=1)，则 P_hit_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

工作点B（元数据刷新主导）：假设更新中 10% 为内容变更 (P_hit_cold=0)，90% 为元数据刷新 (P_hit_cold=1)，则 P_hit_cold = 0.9。此时 δ = 1 - 0.9 * C_steady，在 T_cold=50天、C_steady=0.393 条件下，δ ≈ 0.646，折损显著。

## Corrected Claim

工作点B（元数据刷新主导）：假设更新中 10% 为内容变更 (P_hit_cold=0)，90% 为元数据刷新 (P_hit_cold=1)，则 P_hit_cold = 0.9。此时 δ = 1 - 0.9 * C_steady，在 T_cold=50天、C_steady=0.393 条件下，δ ≈ 0.646，折损显著。

## Evidence

先验知识/题面给定，逻辑校验通过：P_hit_cold = 0.9 * 1 + 0.1 * 0 = 0.9；δ = 1 - 0.9 * 0.393 = 1 - 0.3537 = 0.6463 ≈ 0.646，计算无误。
