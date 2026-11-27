# N266: 交易公平感 $F_{fair}$ 提升幅度的量化：定义为 $\Delta F_{fair} = f(P_{ref}, P_{ask}, \sigma_{pric

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N88

## Claim

交易公平感 $F_{fair}$ 提升幅度的量化：定义为 $\Delta F_{fair} = f(P_{ref}, P_{ask}, \sigma_{price})$。需计算在强制显示 $P_{ref}$ 后，买家感知到的'价格偏差'方差减小量。假设原偏差方差为 $\sigma_{dev}^2$，显示后方差降至 $\sigma_{dev, new}^2$，则 $\Delta F_{fair}$ 对应于公平感量表（如 Likert 5点）的提升分值，需通过 A/B 测试中的问卷数据校准。

## Corrected Claim

交易公平感 $F_{fair}$ 的提升幅度可能与价格偏差方差的减小相关，具体量化关系需通过实证研究（如A/B测试）确定。

## Evidence

[质询]该陈述将公平感提升量化为价格偏差方差的减小，并声称需通过A/B测试校准，但缺乏具体的函数形式或实证数据支持，属于未经验证的经验性假设。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

impact of price transparency on perceived fairness in online marketplaces survey data
