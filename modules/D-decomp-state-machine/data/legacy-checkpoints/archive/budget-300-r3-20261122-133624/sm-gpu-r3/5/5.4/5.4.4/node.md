# N154: 机会成本项 C_opp 的精确计算：资金占用成本 = C_hw_purchase * r * t，其中 r 为无风险利率（当前约为 4-5%），t 为使用年限。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

机会成本项 C_opp 的精确计算：资金占用成本 = C_hw_purchase * r * t，其中 r 为无风险利率（当前约为 4-5%），t 为使用年限。但更精确的模型应考虑通胀调整后的实际利率，以及如果将资金用于其他投资（如股票指数基金，预期年化 7-10%）的潜在收益差，即 C_opp = C_hw_purchase * (r_invest - r_riskfree) * t。

## Corrected Claim

机会成本项 C_opp 的精确计算：资金占用成本 = C_hw_purchase * r * t，其中 r 为无风险利率（当前约为 4-5%），t 为使用年限。但更精确的模型应考虑通胀调整后的实际利率，以及如果将资金用于其他投资（如股票指数基金，预期年化 7-10%）的潜在收益差，即 C_opp = C_hw_purchase * (r_invest - r_riskfree) * t。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别处理了公式中的两个核心变量（无风险利率/实际利率基准 和 投资收益率/税后净值），两者在逻辑上是正交的输入参数，且共同覆盖了父节点中关于'精确计算'所需的通胀调整和机会收益差的关键方面。没有冗余，因为一个关注基准无风险利率的修正，另一个关注替代投资机会的净收益，二者不可合并。）

## Search Query

opportunity cost of capital hardware investment inflation adjusted
