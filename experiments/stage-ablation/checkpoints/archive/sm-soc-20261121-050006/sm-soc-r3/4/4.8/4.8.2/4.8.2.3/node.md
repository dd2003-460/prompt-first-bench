# N295: 柠檬效应负面修正项的具体量化：-γ_defect * ΔP 中，γ_defect 为买家对降价商品存在质量瑕疵的后验概率，在 C2C 场景中通常估计为 0.2-

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N93

## Claim

柠檬效应负面修正项的具体量化：-γ_defect * ΔP 中，γ_defect 为买家对降价商品存在质量瑕疵的后验概率，在 C2C 场景中通常估计为 0.2-0.4（基于二手市场信息不对称程度），ΔP 为降价幅度比例；当 ΔP > 10% 时，该修正项导致净咨询率提升率下降 5-15 个百分点。

## Corrected Claim

在 C2C 场景中，柠檬效应负面修正项 -γ_defect * ΔP 中，γ_defect 代表买家对降价商品存在质量瑕疵的后验概率，通常随信息不对称程度增加而升高；当降价幅度 ΔP 超过一定阈值（如 10%）时，该修正项会显著抵消价格优势，导致净咨询率提升率下降。

## Evidence

[质询]该陈述包含具体的经验性数值参数（γ_defect 0.2-0.4，影响幅度 5-15 个百分点），这些并非第一性原理可推导的数学或物理常数，而是依赖于特定市场环境和统计模型的估计值，缺乏通用性且易受具体品类、平台规则影响，存在将特定模型拟合结果泛化为普遍规律的风险。 | source=knowledge，逻辑自洽（负向修正项随降价幅度增加而增大符合直觉），但具体数值区间属于经验估计，无外部来源直接支持，依据经验事实排除条款降级。

## Search Query

lemon market effect price drop signal quality risk C2C transactions
