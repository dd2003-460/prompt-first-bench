# N264: 交互项 β_interaction 的符号与大小判定：若高挂价（>20%）已隐含‘高价值/稀缺’信号，则额外稀缺标签的边际效用递减。量化模型为 ΔT_cycle

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95

## Claim

交互项 β_interaction 的符号与大小判定：若高挂价（>20%）已隐含‘高价值/稀缺’信号，则额外稀缺标签的边际效用递减。量化模型为 ΔT_cycle = β_price * Premium + β_scarcity * Signal + β_interaction * (Premium * Signal)。若 β_interaction < 0，表明两者存在替代效应（Substitution Effect）。需检索是否有研究量化过‘价格溢价’与‘稀缺文案’的交互系数，通常假设 β_interaction ≈ -0.5 * β_scarcity 作为保守估计。

## Corrected Claim

交互项 β_interaction 的符号判定：若高挂价已隐含稀缺信号，额外稀缺标签的边际效用可能递减，此时 β_interaction < 0 表明存在替代效应。具体数值（如 β_interaction ≈ -0.5 * β_scarcity）需根据具体数据集回归确定，不应作为通用保守估计直接引用。

## Evidence

[质询]陈述中声称“通常假设 β_interaction ≈ -0.5 * β_scarcity 作为保守估计”缺乏普遍公认的学术或行业共识支持，该具体数值比例（-0.5）属于特定模型设定或经验法则，而非通用标准，存在将特定案例泛化为通用假设的风险。 | source=knowledge，逻辑自洽（交互项为负代表替代效应在经济学上成立），但“通常假设...≈ -0.5”这一具体量化经验值缺乏广泛验证，属于特定情境下的经验参数，故降级。
