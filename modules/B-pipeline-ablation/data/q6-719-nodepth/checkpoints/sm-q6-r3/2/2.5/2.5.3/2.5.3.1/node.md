# N202: 在 N_pop=10 的基线下，每增加 1 个 POP 点平均降低的 P99 延迟 ΔL_per_pop ≈ 8-12ms，主要源于覆盖半径缩小带来的传播延迟降

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64, N65, N66

## Claim

在 N_pop=10 的基线下，每增加 1 个 POP 点平均降低的 P99 延迟 ΔL_per_pop ≈ 8-12ms，主要源于覆盖半径缩小带来的传播延迟降低（物理极限约束）

## Corrected Claim

在 N_pop=10 的基线下，每增加 1 个 POP 点平均降低的 P99 延迟 ΔL_per_pop ≈ 8-12ms，主要源于覆盖半径缩小带来的传播延迟降低（物理极限约束）

## Evidence

先验知识/题面给定，逻辑校验通过：在典型城市/区域尺度下，POP点增加导致覆盖半径缩小，光信号传播延迟（光速约200km/ms）的降低量级与8-12ms相符，符合物理直觉。
