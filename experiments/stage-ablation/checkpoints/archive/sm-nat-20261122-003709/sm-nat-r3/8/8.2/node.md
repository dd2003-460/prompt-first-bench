# N90: 代入T_res数值到M_invalidation ≈ 1 - exp(-λ_update * T_res)，计算一致性未命中率M_invalidation的具体

- **status**: pending
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

代入T_res数值到M_invalidation ≈ 1 - exp(-λ_update * T_res)，计算一致性未命中率M_invalidation的具体百分比，其中λ_update=0.01/day。

## Corrected Claim

代入T_res数值到M_invalidation ≈ 1 - exp(-λ_update * T_res)，计算一致性未命中率M_invalidation的具体百分比，其中λ_update=0.01/day。

## Evidence

父节点级核验未通过：不完备（子节点1侧重具体数值计算，子节点2侧重不同T_res区间下的近似分析与误差评估，两者在任务性质上正交（计算 vs 分析/近似）。然而，父节点明确要求“计算具体百分比”，这通常基于N103得出的特定T_res值。子节点2引入了“若T_res较小/较大”的假设性场景和近似分析，这超出了父节点“代入特定数值计算”的核心指令，且未明确N103得出的具体T_res值落在哪个区间，导致子节点2的分析可能偏离父节点意图。此外，父节点未要求分析非线性影响或误差范围，子节点2扩展了范围，但未覆盖“如何确定使用哪种公式”或“N103具体值是多少”这一关键前置条件，完备性不足。）
