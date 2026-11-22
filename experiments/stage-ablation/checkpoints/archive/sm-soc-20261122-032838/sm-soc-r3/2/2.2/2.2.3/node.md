# N56: 买家对高价商品的价格敏感度弹性 $\epsilon_{price}$ 计算：$\epsilon_{price} = \frac{\Delta \% P_{buy

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11, N12, N13

## Claim

买家对高价商品的价格敏感度弹性 $\epsilon_{price}$ 计算：$\epsilon_{price} = \frac{\Delta \% P_{buy}}{\Delta \% U_b}$。在存在质量信号推断时，$\epsilon_{price}$ 随 $P_{ask}$ 相对 $P_{ref}$ 的溢价幅度呈非线性下降，具体函数需通过A/B测试或历史数据回归确定，当前假设下 $\epsilon_{price} < 0.5$ 当溢价 > 15%。

## Corrected Claim

买家对高价商品的价格敏感度弹性 $\epsilon_{price}$ 计算：$\epsilon_{price} = \frac{\Delta \% P_{buy}}{\Delta \% U_b}$。在存在质量信号推断时，$\epsilon_{price}$ 随 $P_{ask}$ 相对 $P_{ref}$ 的溢价幅度呈非线性下降，具体函数需通过A/B测试或历史数据回归确定，当前假设下 $\epsilon_{price} < 0.5$ 当溢价 > 15%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

price sensitivity elasticity quality signal premium consumer behavior
