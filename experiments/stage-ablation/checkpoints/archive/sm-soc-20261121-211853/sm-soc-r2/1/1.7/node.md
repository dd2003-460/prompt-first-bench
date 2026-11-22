# N12: 卖家的效用函数为：卖家收益 = (成交价 - 保留价) * 成交概率 / 成交周期；卖家有动机维持高挂价，因为高挂价提升单次成交收益，且短周期抵消了时间成本，量

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

卖家的效用函数为：卖家收益 = (成交价 - 保留价) * 成交概率 / 成交周期；卖家有动机维持高挂价，因为高挂价提升单次成交收益，且短周期抵消了时间成本，量化为：卖家对降价的边际收益 = 成交概率提升 * 降价损失，当降价损失 > 成交概率提升时，卖家不降价。

## Corrected Claim

卖家通常有动机在保留价之上维持较高挂价以获取单次成交的高收益，但需权衡成交概率与时间成本；当降价带来的成交概率提升不足以弥补价格损失时，卖家倾向于不降价。

## Evidence

父节点级核验失败（LLM 错误）：Invalid \escape: line 5 column 165 (char 231)

## Search Query

seller pricing strategy utility function second hand market
