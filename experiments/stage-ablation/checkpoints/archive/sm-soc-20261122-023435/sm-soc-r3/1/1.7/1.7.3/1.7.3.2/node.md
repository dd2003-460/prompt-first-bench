# N135: 默认缺陷概率 P_defect_expected 的跳跃机制：当 δ_anchor 超过 θ_trust 时，P_defect_expected 并非线性增加，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45

## Claim

默认缺陷概率 P_defect_expected 的跳跃机制：当 δ_anchor 超过 θ_trust 时，P_defect_expected 并非线性增加，而是遵循逻辑斯蒂函数 P_defect_expected = 1 / (1 + exp(-γ * (δ_anchor - θ_trust)))，其中 γ ≈ 5-8 为陡峭度参数，确保在阈值附近概率从 <0.2 迅速跃升至 >0.4。

## Corrected Claim

默认缺陷概率 P_defect_expected 的跳跃机制：当 δ_anchor 超过 θ_trust 时，P_defect_expected 遵循逻辑斯蒂函数 P_defect_expected = 1 / (1 + exp(-γ * (δ_anchor - θ_trust)))，其中 γ 为陡峭度参数，确保在阈值附近概率迅速跃升。

## Evidence

[质询]该陈述包含具体的经验参数（γ ≈ 5-8）和特定的函数形式（逻辑斯蒂），属于经验事实/模型设定，无法从第一性原理严格推导，且缺乏来源支持其具体数值范围。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

logistic function jump in perceived defect probability price threshold
