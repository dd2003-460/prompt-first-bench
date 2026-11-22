# N218: 成交概率 Q 的定价弹性系数 ε_QP = ∂lnQ/∂lnP_deal：需通过历史交易数据回归估计，以量化价格变动对成交概率的非线性影响，通常假设 ε_QP 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N72

## Claim

成交概率 Q 的定价弹性系数 ε_QP = ∂lnQ/∂lnP_deal：需通过历史交易数据回归估计，以量化价格变动对成交概率的非线性影响，通常假设 ε_QP ∈ [-2, -1]。

## Corrected Claim

成交概率 Q 的定价弹性系数 ε_QP = ∂lnQ/∂lnP_deal：需通过历史交易数据回归估计，以量化价格变动对成交概率的非线性影响。具体数值范围取决于市场微观结构及资产特性，需根据实证数据确定，而非固定假设在 [-2, -1] 区间。

## Evidence

[质询]陈述中给出的具体数值区间 ε_QP ∈ [-2, -1] 属于经验性参数假设，缺乏普遍适用的理论推导或广泛共识支持，不同市场、资产类别及微观结构下该弹性系数可能显著偏离此范围，且参考来源未提供该具体数值区间的实证依据。 | 来源[1]和[2]确认了成交概率估计及其对价格等因素的敏感性（间接支持逻辑框架），但未提供具体的弹性系数数值区间，该数值属于经验事实且缺乏直接来源支持。

## Search Query

price elasticity of transaction probability second hand goods

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/594792008&rut=ecd3615dc3ea2ba366266309ddcd918f6434737d090addd099dc71f14c644cee', 'type': 'ddg', 'title': '用深度学习方法来估计限价订单簿中的成交概率 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/407719696&rut=cfbcccacb8b10b319400e1c361630ff72604d9bd7385ea17bf2bfff9d6c4db9f', 'type': 'ddg', 'title': '限价单成交概率的估计与分析 - 知乎'}
