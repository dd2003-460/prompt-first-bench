# N16: 卖家动机：最大化利润 Π_seller = (P_ask - C_cost) × q_sold - C_listing，其中 C_listing 为固定成本（≈

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

卖家动机：最大化利润 Π_seller = (P_ask - C_cost) × q_sold - C_listing，其中 C_listing 为固定成本（≈ 0），q_sold 为成交概率；卖家初始高挂价源于损失厌恶（λ ≈ 2.25）导致 C_cost 被高估 15%-25%，而快速成交降低机会成本，使 Π_seller 在 15-25% 溢价区间内达到局部最优。

## Corrected Claim

卖家动机：最大化利润 Π_seller = (P_ask - C_cost) × q_sold - C_listing，其中 C_listing 为固定成本（≈ 0），q_sold 为成交概率；卖家初始高挂价源于损失厌恶（λ ≈ 2.25）导致 C_cost 被高估 15%-25%，而快速成交降低机会成本，使 Π_seller 在 15-25% 溢价区间内达到局部最优。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的关键变量（C_cost, 行为偏差机制, q_sold, 机会成本/时间价值），彼此独立且无重复，共同构成了卖家定价决策的完整逻辑闭环。）

## Search Query

seller profit maximization loss aversion listing price used goods market
