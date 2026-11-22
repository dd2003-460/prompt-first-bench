# N62: 需求函数 Q(P) 的具体形式：在二手市场中，Q(P) = Q_0 * exp(-ε_p * (P - P_market)/P_market)，其中 ε_p 为

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

需求函数 Q(P) 的具体形式：在二手市场中，Q(P) = Q_0 * exp(-ε_p * (P - P_market)/P_market)，其中 ε_p 为价格弹性系数（通常 ε_p ≈ 1.5-2.5）；需量化在 P_list = 1.2 * P_market 时，Q 相对于 Q_market 的下降比例（通常为 10%-20%）。

## Corrected Claim

在二手市场中，若采用指数需求函数 Q(P) = Q_0 * exp(-ε_p * (P - P_market)/P_market)，当 P_list = 1.2 * P_market 时，Q 相对于 Q_market 的下降比例取决于价格弹性系数 ε_p。若 ε_p ≈ 1.5-2.5，下降比例约为 26%-39%；若下降比例仅为 10%-20%，则隐含的 ε_p 约为 0.5-0.8。具体数值需根据实际市场数据校准。

## Evidence

[质询]该陈述包含具体的经验参数（弹性系数 1.5-2.5 和下降比例 10%-20%），这些数值并非数学公理或第一性原理可推导的必然结果，而是依赖于特定市场环境的经验估计。参考来源仅提供了需求函数的一般定义和性质（单调递减），未提供具体的函数形式或参数范围，因此无法通过外部来源直接验证这些具体数值。 | 逻辑校验通过：根据给定的指数需求函数 Q(P) = Q_0 * exp(-ε_p * (P - P_market)/P_market)，当 P_list = 1.2 * P_market 时，价格相对变化为 0.2。若 ε_p 在 1.5-2.5 之间，则指数项为 -0.3 到 -0.5，Q/Q_market = exp(-0.3) ≈ 0.74 到 exp(-0.5) ≈ 0.61，即下降比例约为 26%-39%。这与陈述中声称的“通常为 10%-20%”存在数值上的不一致（陈述中的下降比例偏小，或者隐含的弹性系数需更小，约 0.5-0.8 才能得出 10%-20% 的下降）。然而，考虑到二手市场可能具有较低的价格弹性（非标准化商品），或者陈述中的“通常”指代的是更宽泛的经验观察而非严格基于该公式的计算，逻辑上虽自洽（函数形式合理）但数值结论与公式推导有出入。由于来源 [1][2] 仅确认需求函数单调递减，未覆盖具体参数，且该事实属于经验事实（具体参数值），缺乏直接来源支持，故降级。

## Search Query

price elasticity of demand used goods second hand market empirical estimate

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E9%9C%80%E6%B1%82%E5%87%BD%E6%95%B0/3945374&rut=e513ea19768fb03a914292f0f7b4b2429a2dc428f43c708c5d7aa170ccc4804e', 'type': 'ddg', 'title': '需求函数_百度百科'}
- {'url': 'https://baike.baidu.com/item/%E9%9C%80%E6%B1%82%E6%9B%B2%E7%BA%BF/3351682&rut=eca09b76134ce2b79a838099ceafc4c530d7316be476b00e67aa315aa163e25b', 'type': 'ddg', 'title': '需求曲线_百度百科'}
