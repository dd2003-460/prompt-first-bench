# N71: 损失厌恶系数 λ 的推导：λ = 1 + (P_markup_max - P_market) / P_market，若 P_markup_max = 25%，则

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N20

## Claim

损失厌恶系数 λ 的推导：λ = 1 + (P_markup_max - P_market) / P_market，若 P_markup_max = 25%，则 λ = 1.25，与 Tversky & Kahneman 的 2.25 不符，需检验是否混淆了 λ 与风险厌恶系数 γ，或是否存在其他偏差来源。

## Corrected Claim

损失厌恶系数 λ 的推导：若基于特定模型假设 λ = 1 + (P_markup_max - P_market) / P_market，当 P_markup_max = 25% 时，计算得 λ = 1.25。此结果与 Tversky & Kahneman 提出的经典值 2.25 存在显著差异，提示需检验该模型是否混淆了 λ 与风险厌恶系数 γ，或是否忽略了其他行为偏差来源（如基准点依赖或概率权重）。

## Evidence

[质询]该陈述中的公式推导存在概念混淆风险：损失厌恶系数 λ 在前景理论中通常定义为损失效用相对于收益效用的斜率比（即边际效用之比），而非直接由最大溢价率（P_markup_max）通过简单的代数变换得出。将市场行为参数（溢价率）直接等同于心理参数（λ）缺乏理论依据，且 1.25 与 2.25 的差异可能源于对“损失”定义域的不同（如是否包含机会成本或基准点选择），而非简单的计算错误。 | 先验知识/题面给定，逻辑校验通过：虽然公式推导在标准前景理论中不常见，但作为对特定模型假设的检验陈述，其内部逻辑自洽（即指出推导结果与经典值不符并建议排查混淆），且无外部来源矛盾。
