# N85: 收敛性边界条件：若 Delta_Error 在连续 2 次迭代中 < 1%（即陷入局部最优或震荡），则强制终止循环并标记为 'Unresolved'，防止无限循

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

收敛性边界条件：若 Delta_Error 在连续 2 次迭代中 < 1%（即陷入局部最优或震荡），则强制终止循环并标记为 'Unresolved'，防止无限循环消耗算力，此时需人工介入或切换云端更强模型。

## Corrected Claim

收敛性边界条件：若 Delta_Error 在连续 2 次迭代中 < 1%（即陷入局部最优或震荡），则强制终止循环并标记为 'Unresolved'，防止无限循环消耗算力，此时需人工介入或切换云端更强模型。

## Evidence

先验知识/题面给定，逻辑校验通过
