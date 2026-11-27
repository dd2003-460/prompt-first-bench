# N7: 随机偏好噪声σ_noise的量化：σ_noise = sqrt(Var(P_listed | P_market))，在控制锚定效应后，剩余方差中60%来自卖家个

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

随机偏好噪声σ_noise的量化：σ_noise = sqrt(Var(P_listed | P_market))，在控制锚定效应后，剩余方差中60%来自卖家个体风险偏好差异（β_risk ~ N(0.3, 0.1)），40%来自信息不对称导致的估值误差（ε_info ~ N(0, 0.15)）。

## Corrected Claim

随机偏好噪声σ_noise的量化：σ_noise = sqrt(Var(P_listed | P_market))。在控制锚定效应后，剩余方差主要由卖家个体风险偏好差异和信息不对称导致的估值误差两部分构成，具体比例取决于市场微观结构及卖家群体特征，通常需通过实证数据拟合确定。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且互不重叠：节点1负责数学公式推导与参数代入，节点2和节点3分别独立验证两个核心随机变量（风险偏好和信息误差）的统计分布假设。虽然节点2和3结构相似，但它们针对不同变量，属于必要的并列证据，不构成冗余。父节点中的核心要素（公式、两个变量的分布及占比）均被覆盖。）

## Search Query

price setting noise variance decomposition risk preference information asymmetry
