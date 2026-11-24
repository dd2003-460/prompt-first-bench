# N294: Patch_Validation_Cost = (Patch_Cycles_Per_Month × 10_Pops) × (Validation_Hours_P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

Patch_Validation_Cost = (Patch_Cycles_Per_Month × 10_Pops) × (Validation_Hours_Per_Patch × Hourly_Ops_Cost + Rollback_Probability × Rollback_Cost)，其中 Patch_Cycles 通常为 2-4 次/月（安全补丁），Validation_Hours 取决于自动化程度，手动验证约 4h/POP/次，自动化约 0.5h/POP/次。

## Corrected Claim

Patch_Validation_Cost = (Patch_Cycles_Per_Month × 10_Pops) × (Validation_Hours_Per_Patch × Hourly_Ops_Cost + Rollback_Probability × Rollback_Cost)，其中 Patch_Cycles 通常为 2-4 次/月（安全补丁），Validation_Hours 取决于自动化程度，手动验证约 4h/POP/次，自动化约 0.5h/POP/次。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

software patch management cost validation hours per node
