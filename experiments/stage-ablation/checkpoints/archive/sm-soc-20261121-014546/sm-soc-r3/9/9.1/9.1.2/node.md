# N363: 成交概率 p_min 的均衡维持条件：p_min 需覆盖卖家的固定交易成本 C_fixed 和机会成本 C_opp，即 p_min * (P_ask - V) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N120

## Claim

成交概率 p_min 的均衡维持条件：p_min 需覆盖卖家的固定交易成本 C_fixed 和机会成本 C_opp，即 p_min * (P_ask - V) ≥ C_fixed + C_opp。若 C_fixed = 0.05V 且 C_opp = 0.03V，则 p_min = 0.08 / (P_ask/V - 1)。当 P_ask = 1.2V 时，p_min = 0.4，低于此值卖家将退出市场。

## Corrected Claim

成交概率 p_min 的均衡维持条件：p_min 需覆盖卖家的固定交易成本 C_fixed 和机会成本 C_opp，即 p_min * (P_ask - V) ≥ C_fixed + C_opp。若 C_fixed = 0.05V 且 C_opp = 0.03V，则 p_min = 0.08 / (P_ask/V - 1)。当 P_ask = 1.2V 时，p_min = 0.4，低于此值卖家将退出市场。

## Evidence

先验知识/题面给定，逻辑校验通过：代数推导 p_min = (C_fixed + C_opp) / (P_ask - V) 正确，代入数值 0.08V / 0.2V = 0.4 计算无误，经济直觉（覆盖成本以维持均衡）自洽。

## Search Query

minimum transaction probability equilibrium seller exit condition fixed opportunity cost
