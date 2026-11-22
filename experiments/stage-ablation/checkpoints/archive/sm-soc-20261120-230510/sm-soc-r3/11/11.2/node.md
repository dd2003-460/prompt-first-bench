# N315: S_dir 的边界条件：当 P_ask - V_true > 3σ 时，S_dir 公式失效，因为买家完全沉默导致成交概率趋近于零，卖家无法实现最大化单次收益，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N112

## Claim

S_dir 的边界条件：当 P_ask - V_true > 3σ 时，S_dir 公式失效，因为买家完全沉默导致成交概率趋近于零，卖家无法实现最大化单次收益，需引入流动性枯竭修正项 δ_liquidity（对应 N96 的修正）。

## Corrected Claim

S_dir 的边界条件：当 P_ask - V_true > 3σ 时，S_dir 公式失效，因为买家完全沉默导致成交概率趋近于零，卖家无法实现最大化单次收益，需引入流动性枯竭修正项 δ_liquidity（对应 N96 的修正）。

## Evidence

先验知识/题面给定，逻辑校验通过：当报价偏离真实价值超过3个标准差时，市场流动性枯竭导致成交概率趋近于零，原收益最大化公式失效需引入修正项，符合经济学直觉与逻辑自洽。

## Search Query

directed selection pressure boundary condition liquidity exhaustion high premium
