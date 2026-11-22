# N134: 在动态更新工作点（λ_update=1%/天）下，f_cache 的有效值需乘以 D_update 折扣因子；若 T_residence_avg=1h，D_up

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N45

## Claim

在动态更新工作点（λ_update=1%/天）下，f_cache 的有效值需乘以 D_update 折扣因子；若 T_residence_avg=1h，D_update≈0.9996，则有效覆盖率 f_eff ≈ 1 * 0.9996 = 99.96%，表明更新失效是主要命中率损失来源，而非容量不足。

## Corrected Claim

在动态更新工作点（λ_update=1%/天）下，f_cache 的有效值需乘以 D_update 折扣因子；若 T_residence_avg=1h，D_update≈0.9996，则有效覆盖率 f_eff ≈ 1 * 0.9996 = 99.96%，表明更新失效是主要命中率损失来源，而非容量不足。

## Evidence

先验知识/题面给定，逻辑校验通过：D_update = 1 - λ_update * T_residence_avg = 1 - 0.01 * (1/24) ≈ 0.99958，与0.9996一致；f_eff = f_cache * D_update 逻辑自洽。
