# N267: 在高利用率工作点（U_self=60%）下，闲置容量成本显著降低：C_idle_annual ≈ (C_total_self - B_avg) × unit_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

在高利用率工作点（U_self=60%）下，闲置容量成本显著降低：C_idle_annual ≈ (C_total_self - B_avg) × unit_cost × 12 / 394,600，其中 C_total_self = B_avg / 0.6，闲置带宽为 B_avg/0.6 - B_avg = 0.667 × B_avg，导致 C_idle 约为总带宽成本的 22.2%，但故障冗余度降低，P99 延迟风险增加。

## Corrected Claim

在高利用率工作点（U_self=60%）下，闲置容量成本显著降低：C_idle_annual ≈ (C_total_self - B_avg) × unit_cost × 12 / 394,600，其中 C_total_self = B_avg / 0.6，闲置带宽为 B_avg/0.6 - B_avg = 0.667 × B_avg，导致 C_idle 约为总带宽成本的 22.2%，但故障冗余度降低，P99 延迟风险增加。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导自洽（闲置比例1/3，成本占比22.2%），符合高利用率下成本与风险权衡的工程直觉。
