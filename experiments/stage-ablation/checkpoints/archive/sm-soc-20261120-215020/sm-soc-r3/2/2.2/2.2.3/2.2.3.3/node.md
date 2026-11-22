# N99: 交易成本 $C_{transaction}$ 的固定与变动部分分解：$C_{transaction} = C_{fixed} + C_{variable} \t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

交易成本 $C_{transaction}$ 的固定与变动部分分解：$C_{transaction} = C_{fixed} + C_{variable} \times P_{paid}$，其中 $C_{fixed}$ 为支付手续费基础费（如 2 元），$C_{variable}$ 为比例费率（如 1%）。量化：对于 $P_{paid}=5000$ 元的商品，$C_{transaction} = 2 + 50 = 52$ 元（1.04%）；对于 $P_{paid}=500$ 元的商品，$C_{transaction} = 2 + 5 = 7$ 元（1.4%）。此比例特性导致低价商品的有效交易成本率更高，从而抑制低价商品的流动性，间接支持高挂价策略（因为高挂价商品通常单价较高，交易成本率较低）。

## Corrected Claim

交易成本 $C_{transaction}$ 的固定与变动部分分解：$C_{transaction} = C_{fixed} + C_{variable} \times P_{paid}$，其中 $C_{fixed}$ 为支付手续费基础费（如 2 元），$C_{variable}$ 为比例费率（如 1%）。量化：对于 $P_{paid}=5000$ 元的商品，$C_{transaction} = 2 + 50 = 52$ 元（1.04%）；对于 $P_{paid}=500$ 元的商品，$C_{transaction} = 2 + 5 = 7$ 元（1.4%）。此比例特性导致低价商品的有效交易成本率更高，从而抑制低价商品的流动性，间接支持高挂价策略（因为高挂价商品通常单价较高，交易成本率较低）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（2+50=52, 2+5=7），比例关系推导符合数学逻辑，且符合交易成本理论的基本直觉。

## Search Query

transaction cost structure fixed vs variable components in e-commerce platforms
