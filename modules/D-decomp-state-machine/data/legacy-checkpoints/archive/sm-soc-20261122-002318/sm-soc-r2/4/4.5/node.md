# N25: 最小干预定义：使总剩余恢复至 Pareto 最优所需的最低信息熵减操作。具体量化为：向买家展示‘同类商品90天中位成交价’的提示，该操作的信息价值 (Value

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N4

## Claim

最小干预定义：使总剩余恢复至 Pareto 最优所需的最低信息熵减操作。具体量化为：向买家展示‘同类商品90天中位成交价’的提示，该操作的信息价值 (Value of Information) 需大于买家当前因信号噪声产生的决策误差成本，即 VOI > 0.5 * σ_noise^2 / (2 * RiskAversionCoeff)。

## Corrected Claim

最小干预定义：使总剩余恢复至 Pareto 最优所需的最低信息熵减操作。其核心原则是干预的信息价值 (VOI) 需大于买家因信号噪声产生的决策误差成本，具体量化形式取决于风险偏好系数与噪声方差的函数关系，而非固定的 0.5 * σ_noise^2 / (2 * RiskAversionCoeff) 公式。

## Evidence

[质询]公式中的系数 0.5 和分母中的 2 缺乏明确的理论推导依据或标准定义，属于任意设定的经验参数，且将‘最小干预’直接等同于‘展示90天中位价’这一具体操作在逻辑上过于狭隘，未涵盖其他可能的低熵减干预手段。 | 先验知识/题面给定，逻辑校验通过（量纲与基本VOI概念自洽），但具体量化公式缺乏通用理论支持，且来源缺失，故降级为定性表述。

## Search Query

value of information in price signaling markets
