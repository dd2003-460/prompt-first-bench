# N167: 在 Top 1% 对象工作点，阈值 S_1% 计算为 S_min * (1-0.01)^(1/(1-1.1)) ≈ 1KB * 0.99^(-10) ≈ 1.1

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

在 Top 1% 对象工作点，阈值 S_1% 计算为 S_min * (1-0.01)^(1/(1-1.1)) ≈ 1KB * 0.99^(-10) ≈ 1.1KB，由于 Pareto 长尾特性，B_top_1% 可能占据总字节数的 80-90%，具体值需数值积分验证

## Corrected Claim

在 Top 1% 对象工作点，若假设 S_min=1KB 且分布指数为 1.1，则阈值 S_1% 计算约为 1.1KB；基于 Pareto 长尾特性，B_top_1% 预计占据总字节数的较大比例（如 80-90%），具体数值需结合实际分布参数进行数值积分验证。

## Evidence

[质询]该陈述包含具体的工程/系统参数（S_min=1KB, 指数1.1, 占比80-90%），属于经验事实或特定模型假设，无法从第一性原理严格推出；且参考来源[2]仅讨论Pareto分布中alpha参数的推导，未提供针对该特定阈值计算及字节占比的具体数值支持。 | 逻辑推导自洽（0.99^-10 ≈ 1.1046），但参考来源[2]仅涉及Pareto分布理论，未直接支持具体的1KB阈值及80-90%占比结论，属于经验事实缺直接来源支持。

## Search Query

Pareto alpha 1.1 top 1 percent byte share calculation

## Retrieval Sources

- {'url': 'https://corporatefinanceinstitute.com/resources/capital_markets/alpha/&rut=c149f5382a3a159856a35baf166d8d9af5c8d39bfd366ae7cdc261a6fd54ba38', 'type': 'ddg', 'title': 'Alpha - Learn How to Calculate and Use Alpha in Investing'}
- {'url': 'https://stats.stackexchange.com/questions/88394/how-to-derive-the-alpha-for-the-pareto-rule&rut=fd327cf289cc0c9a69b6f4c8762177b65afdd6f919a1e5ab4c24ab17e4feb307', 'type': 'ddg', 'title': 'How to derive the $\\\\alpha$ for the Pareto rule - Cross Validated'}
- {'url': 'https://stockalpha.ai/alpha-learning/understanding-alpha-and-beta-measuring-investment-performance-and-risk&rut=aadf7c9b350e0a495e7295e13e3f80e9e07057363275d69a143ff3a97938b7c9', 'type': 'ddg', 'title': 'Alpha and Beta: Measuring Investment Performance and Risk'}
