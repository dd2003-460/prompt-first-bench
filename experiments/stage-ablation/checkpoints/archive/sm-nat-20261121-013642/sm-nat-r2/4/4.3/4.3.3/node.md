# N64: P_hit_cold 的中间工作点估算：假设 50% 更新为内容变更 (P=0)，50% 为元数据刷新 (P=1)，则 P_hit_cold ≈ 0.5。此时 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

P_hit_cold 的中间工作点估算：假设 50% 更新为内容变更 (P=0)，50% 为元数据刷新 (P=1)，则 P_hit_cold ≈ 0.5。此时 δ = 1 - 0.5 * C_steady，用于量化部分失效场景下的折损。

## Corrected Claim

P_hit_cold 的中间工作点估算：假设 50% 更新为内容变更 (P=0)，50% 为元数据刷新 (P=1)，则 P_hit_cold ≈ 0.5。此时 δ = 1 - 0.5 * C_steady，用于量化部分失效场景下的折损。

## Evidence

先验知识/题面给定，逻辑校验通过：P_hit_cold 作为概率加权平均，在 50/50 混合且 P 分别为 0 和 1 时，期望值确为 0.5，公式推导自洽。
