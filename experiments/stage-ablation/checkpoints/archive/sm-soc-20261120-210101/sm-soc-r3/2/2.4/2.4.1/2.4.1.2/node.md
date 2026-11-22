# N202: 买家侧策略噪声投影：买家搜索阈值 θ_buyer 的随机扰动 δ_θ ~ U(-δ_θ_max, δ_θ_max)，其中 δ_θ_max = ε_max * β

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N55

## Claim

买家侧策略噪声投影：买家搜索阈值 θ_buyer 的随机扰动 δ_θ ~ U(-δ_θ_max, δ_θ_max)，其中 δ_θ_max = ε_max * β_buyer，β_buyer 为买家对噪声的敏感度系数，假设值为 0.5。

## Corrected Claim

买家侧策略噪声投影：买家搜索阈值 θ_buyer 的随机扰动 δ_θ ~ U(-δ_θ_max, δ_θ_max)，其中 δ_θ_max = ε_max * β_buyer，β_buyer 为买家对噪声的敏感度系数，假设值为 0.5。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

buyer search threshold stochastic perturbation sensitivity coefficient
