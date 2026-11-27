# N37: 未实现损失规避的心理账户阈值：卖家设定挂价 $P_{list} = P_{ref} \times (1 + \pi)$ 的最低阈值由 $P_{min} = P_

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N6

## Claim

未实现损失规避的心理账户阈值：卖家设定挂价 $P_{list} = P_{ref} \times (1 + \pi)$ 的最低阈值由 $P_{min} = P_{ref} \times (1 + \frac{1}{\lambda})$ 决定，低于此价格的预期收益在心理账户中被视为‘损失’，导致卖家拒绝成交，该阈值解释了为何溢价下限约为15%（对应 $\lambda \approx 2.25$ 时的 $1/\lambda \approx 0.44$ 的倒数逻辑需修正，此处指溢价下限与 $\lambda$ 的函数关系）。

## Corrected Claim

未实现损失规避的心理账户阈值：卖家设定挂价 $P_{list} = P_{ref} \times (1 + \pi)$ 的最低阈值由 $P_{min} = P_{ref} \times (1 + \frac{1}{\lambda})$ 决定。若溢价下限约为15%，则对应 $\lambda \approx 6.67$（即 $1/\lambda \approx 0.15$），而非 $\lambda \approx 2.25$。

## Evidence

[质询]陈述内部存在严重的数学逻辑矛盾：若 $P_{min} = P_{ref} \times (1 + \frac{1}{\lambda})$，则溢价下限为 $1/\lambda$。当 $\lambda \approx 2.25$ 时，$1/\lambda \approx 0.44$（即44%），这与陈述中声称的“溢价下限约为15%”严重不符。若要得到15%的溢价，需 $1/\lambda \approx 0.15$，即 $\lambda \approx 6.67$。陈述中关于“倒数逻辑需修正”的模糊表述掩盖了数值与结论之间的硬性冲突。 | 先验知识/题面给定，但逻辑校验发现数值推导与结论矛盾（$1/2.25 \neq 0.15$），无法自洽。

## Search Query

psychological account threshold for unrealized loss avoidance in seller pricing
