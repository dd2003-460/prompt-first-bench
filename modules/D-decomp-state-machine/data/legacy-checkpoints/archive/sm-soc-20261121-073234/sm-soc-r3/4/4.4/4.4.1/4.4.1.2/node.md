# N271: 曝光量 Exposure 的基线值 E_0 及其与 Price Ratio 的交互效应：Exposure = E_0 * exp(β_exposure * (P

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N89

## Claim

曝光量 Exposure 的基线值 E_0 及其与 Price Ratio 的交互效应：Exposure = E_0 * exp(β_exposure * (Price_Ratio - 1))，其中 β_exposure 需通过回归分析估计

## Corrected Claim

曝光量 Exposure 通常被建模为基线值 E_0 与 Price Ratio 的函数，具体形式（如指数形式）及参数 β_exposure 需通过特定数据集的回归分析估计，不同模型设定可能不同。

## Evidence

[质询]该陈述包含具体的数学模型形式（指数函数）和参数估计方法（回归分析），属于经验性建模假设或特定研究结论，无法从第一性原理直接推导。参考来源均未提供该特定公式或证实该特定交互效应形式，存在模型设定任意性的风险。 | 逻辑自洽（量纲合理，Price_Ratio-1无量纲，exp结果无量纲，E_0为基线曝光量），但参考来源[1]仅讨论曝光定价敏感性的一般概念，[2][3]讨论统计交互效应但未涉及此具体公式，属于经验事实且缺乏直接来源支持。

## Search Query

product exposure baseline price ratio interaction effect regression analysis

## Retrieval Sources

- {'url': 'https://umbrex.com/resources/industry-analyses/how-to-analyze-a-property-casualty-insurance/exposure-based-pricing-sensitivity-analysis/&rut=f00ea1ad545cc941035fac9ab6373825c38bf2853c71f25e11dc2a3dc76a3e77', 'type': 'ddg', 'title': 'Exposure-Based Pricing Sensitivity Analysis | Umbrex'}
- {'url': 'https://www.sciencedirect.com/science/article/pii/S0895435621000810&rut=169066aa9cdb856fa6fbf5c57f1757ea6e402ca9d1d70f286ffbd2f8777afabc', 'type': 'ddg', 'title': 'Effect Modifiers and Statistical Tests for Interaction in Randomized ...'}
- {'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC1475799/&rut=552a604995e288986204019c9eade26a6517f83b9acdb60543246782e48595ed', 'type': 'ddg', 'title': 'Measuring additive interaction using odds ratios - PMC'}
