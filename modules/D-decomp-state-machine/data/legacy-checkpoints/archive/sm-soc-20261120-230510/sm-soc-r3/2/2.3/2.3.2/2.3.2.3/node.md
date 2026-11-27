# N171: 通讯/心理摩擦成本 c_communication 的量化：c_communication = ψ_uncertainty * P_ambiguity，其中 ψ

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

通讯/心理摩擦成本 c_communication 的量化：c_communication = ψ_uncertainty * P_ambiguity，其中 ψ_uncertainty 为不确定性厌恶系数（典型值 0.5-2.0 元），P_ambiguity 为商品描述模糊度（0-1），反映买家因信息不透明产生的心理成本。

## Corrected Claim

通讯/心理摩擦成本 c_communication 可建模为不确定性厌恶系数与商品描述模糊度的乘积，具体系数取值需依据特定市场或实验数据确定。

## Evidence

[质询]该公式及具体参数（ψ_uncertainty 典型值 0.5-2.0 元）属于特定模型或假设下的经验性量化定义，并非通用的经济学或心理学第一性原理推导结果，且参考来源中未包含此特定公式或数值范围，存在来源缺失风险。 | 逻辑上量纲自洽（系数*概率=成本），但参考来源[1][2]仅讨论沟通成本的一般量化方法，[3]讨论算法通信成本，均未直接支持该特定心理摩擦成本公式及数值范围，属于经验事实且缺来源直接支持。

## Search Query

ambiguity aversion cost quantification online shopping psychological friction

## Retrieval Sources

- {'url': 'https://docs.pingcode.com/insights/w8fgth9pljuu1i9o7741tsnq&rut=7fed391d56b486ba8bce4bc69899d6a1b28b526b29b568ed2030245d35df27c2', 'type': 'ddg', 'title': '沟通成本无法量化怎么量化沟通成本？问题分析'}
- {'url': 'https://fastercapital.com/content/Cost-of-Communication--How-to-Calculate-and-Improve-Communication-Costs.html&rut=bab9c90050aef79dc81f68fbf55a5e131e067971ea3fae337084aaff41816f0c', 'type': 'ddg', 'title': 'Cost of Communication: How to Calculate and Improve Communication Costs'}
- {'url': 'https://solomonik.cs.illinois.edu/teaching/cs598_fall2016/lectures/lec1.pdf&rut=8c379e84dd9b09e2dda9a8305972a4f61381d6886fc80d2598b632e27716f8ea', 'type': 'ddg', 'title': 'PDF CS 598: Communication Cost Analysis of Algorithms'}
