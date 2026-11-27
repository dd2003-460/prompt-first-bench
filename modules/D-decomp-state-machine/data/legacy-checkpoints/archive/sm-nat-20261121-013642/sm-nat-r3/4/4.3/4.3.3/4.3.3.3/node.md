# N189: 工作点C（均匀混合）：假设更新中 50% 为内容变更，50% 为元数据刷新，则 P_hit_cold = 0.5。此时 δ = 1 - 0.5 * C_stea

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

工作点C（均匀混合）：假设更新中 50% 为内容变更，50% 为元数据刷新，则 P_hit_cold = 0.5。此时 δ = 1 - 0.5 * C_steady，在 T_cold=50天、C_steady=0.393 条件下，δ ≈ 0.804，为中性基准。

## Corrected Claim

工作点C（均匀混合）：假设更新中 50% 为内容变更，50% 为元数据刷新，则 P_hit_cold = 0.5。此时 δ = 1 - 0.5 * C_steady，在 T_cold=50天、C_steady=0.393 条件下，δ ≈ 0.804，为中性基准。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 1 - 0.5 * 0.393 = 1 - 0.1965 = 0.8035 ≈ 0.804，数值准确，逻辑自洽。
