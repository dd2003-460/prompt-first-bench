# N39: 单一卖家降价的收益变化分解为 $\Delta \Pi_{seller} = \Delta P \times Q_{base} + P_{new} \times 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

单一卖家降价的收益变化分解为 $\Delta \Pi_{seller} = \Delta P \times Q_{base} + P_{new} \times \Delta Q - C_{transaction}$，其中 $Q_{base}$ 为当前销量，$\Delta Q$ 为因降价带来的增量销量，$C_{transaction}$ 为交易手续费。在古诺-纳什均衡下，由于市场对该单一卖家降价的反应弹性 $\epsilon_{Q/P}$ 较低，导致 $P_{new} \times \Delta Q < |\Delta P| \times Q_{base}$，故 $\Delta \Pi < 0$。

## Corrected Claim

单一卖家降价的收益变化分解为 $\Delta \Pi_{seller} = \Delta P \times Q_{base} + P_{new} \times \Delta Q - C_{transaction}$，其中 $Q_{base}$ 为当前销量，$\Delta Q$ 为因降价带来的增量销量，$C_{transaction}$ 为交易手续费。在古诺-纳什均衡下，由于市场对该单一卖家降价的反应弹性 $\epsilon_{Q/P}$ 较低，导致 $P_{new} \times \Delta Q < |\Delta P| \times Q_{base}$，故 $\Delta \Pi < 0$。

## Evidence

先验知识/题面给定，逻辑校验通过：收益分解公式符合微积分基本定理（全微分近似），古诺模型中单一卖家降价导致自身利润下降的结论符合标准博弈论推导（在需求弹性低于临界值时，价格效应大于数量效应）。

## Search Query

Cournot-Nash equilibrium single seller price cut profit change formula
