# N253: 二手市场锚定效应修正系数 k_used 的推导：基于 Kahneman & Tversky 的锚定实验，标准品 k_std ≈ 0.25；二手非标品因信息不对称

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N81

## Claim

二手市场锚定效应修正系数 k_used 的推导：基于 Kahneman & Tversky 的锚定实验，标准品 k_std ≈ 0.25；二手非标品因信息不对称增加，买家对锚点的信任度下降，修正公式 k_used = k_std * (1 - η_asym)，其中 η_asym 为信息不对称系数（η_asym ∈ [0.2, 0.4]），故 k_used ∈ [0.15, 0.20]。

## Corrected Claim

二手非标品因信息不对称增加，买家对锚点的信任度下降，导致锚定效应修正系数 k_used 低于标准品 k_std（约 0.25），具体数值需根据特定市场数据校准，通常认为在 0.15-0.20 区间内。

## Evidence

[质询]该公式 k_used = k_std * (1 - η_asym) 及具体数值区间 [0.15, 0.20] 缺乏明确的实证文献支持，属于基于行为经济学原理的定性推导而非标准定量模型；Kahneman & Tversky 的原始实验并未直接给出针对二手非标品的具体修正系数公式。 | 先验知识/题面给定，逻辑校验通过：逻辑上信息不对称导致信任度下降从而降低锚定效应强度是合理的，但具体公式和数值区间属于经验性假设，缺乏直接来源支持，故降级为定性表述。
