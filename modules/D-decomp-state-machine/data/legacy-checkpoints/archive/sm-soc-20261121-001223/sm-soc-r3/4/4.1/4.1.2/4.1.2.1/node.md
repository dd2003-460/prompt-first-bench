# N162: 二手市场损失厌恶系数 λ_loss 的校准值：基于二手交易情境的实证数据，λ_loss 通常介于 1.5-2.0 之间，低于标准前景理论的 2.5，因为二手卖家

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

二手市场损失厌恶系数 λ_loss 的校准值：基于二手交易情境的实证数据，λ_loss 通常介于 1.5-2.0 之间，低于标准前景理论的 2.5，因为二手卖家多为处置闲置资产而非核心资产，损失感知强度较弱，需引用特定情境下的回归系数。

## Corrected Claim

在二手交易情境中，由于卖家多为处置闲置资产，其损失厌恶系数 λ_loss 可能低于标准前景理论参数（如 2.5），具体数值需依据特定情境下的实证回归结果确定，通常认为其强度较弱。

## Evidence

[质询]该陈述声称基于二手交易情境的实证数据，λ_loss 通常介于 1.5-2.0 之间，且低于标准前景理论的 2.5。然而，参考来源 [2] 和 [3] 仅讨论了损失厌恶参数的一般测量方法和不同市场/情境下的差异性，并未提供针对“二手交易”这一特定情境的具体回归系数或数值范围（1.5-2.0）。此外，标准前景理论中 λ 的典型值通常引用为 2.25 或 2.5，但将其与二手市场特定值进行直接对比并给出精确区间属于具体的经验事实，现有来源未直接支持该特定数值区间。 | 逻辑上，二手卖家处置闲置资产导致损失感知减弱从而降低 λ 值符合行为经济学直觉，量级合理；但参考来源 [1]-[3] 仅涵盖前景理论通用框架及一般实证方法，未提供二手市场特定情境下 λ_loss 为 1.5-2.0 的直接数据支持，属于经验事实且缺乏特定来源直接佐证。

## Search Query

loss aversion coefficient second-hand sellers empirical study

## Retrieval Sources

- {'url': 'https://blog.csdn.net/q1w3e5r7t9y/article/details/155682298&rut=cbfa23f9ae01963c38264255173b48df8c5033157157876cfb7f72d6ed922702', 'type': 'ddg', 'title': '前景理论实战解析：如何用Python量化人类决策偏差？（中英双语）-CSDN博客'}
- {'url': 'https://www.zhangqiaokeyan.com/academic-degree-domestic_mphd_thesis/020314662139.html&rut=9a42ccfc5089577d3c4a4e4548943c8192e9f494f2fbe13ec57c85d5bebed58e', 'type': 'ddg', 'title': '基于实验方法的损失厌恶参数测量及实证研究 - 掌桥科研'}
- {'url': 'https://max.book118.com/html/2026/0513/5144240302013212.shtm&rut=13de587be8fcdf944e283ee4ed0fb99152a366c0f0455fbd03f763ba1ae196b7', 'type': 'ddg', 'title': '前景理论中损失厌恶系数的实证测算.docx - 原创力文档'}
