# N6: 损失厌恶系数 (Loss Aversion Coefficient, $\lambda$) 的量化值为 2.0-2.5，即卖家对‘低于心理锚点成交’的痛感是‘高

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

损失厌恶系数 (Loss Aversion Coefficient, $\lambda$) 的量化值为 2.0-2.5，即卖家对‘低于心理锚点成交’的痛感是‘高于锚点未成交’的 2-2.5 倍，导致其定价策略系统性偏离边际成本，形成 $P_{listing} = P_{market} \times (1 + \lambda_{anchor})$ 的非理性溢价基础。

## Corrected Claim

损失厌恶效应（系数λ≈2.25）使得卖家对低于心理锚点的损失赋予更高权重，这可能导致其定价策略偏离边际成本，产生非理性溢价，但溢价幅度并非固定为λ倍，而是受市场供需、竞争程度等多重因素影响的复杂结果。

## Evidence

[质询]将行为经济学中通用的损失厌恶系数（λ≈2.25）直接等同于特定交易场景（卖家定价）中的‘锚点偏离溢价系数’（λ_anchor），属于概念混淆。损失厌恶描述的是效用函数的非线性，而定价溢价是市场均衡或策略结果，二者之间不存在直接的恒等换算关系，且2.0-2.5倍的溢价在实际市场中极少作为系统性基础存在。 | 先验知识/题面给定，逻辑校验通过。虽然损失厌恶系数λ≈2.25是Kahneman & Tversky的经典结论，但将其直接映射为定价公式中的乘数因子缺乏严格的经济学推导支持，属于经验性假设而非必然逻辑结果，故降级为定性表述。

## Search Query

loss aversion coefficient Kahneman Tversky 2.5 behavioral economics pricing
