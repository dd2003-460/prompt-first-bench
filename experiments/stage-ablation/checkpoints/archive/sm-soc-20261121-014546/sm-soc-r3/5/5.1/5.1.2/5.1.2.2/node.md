# N315: 心理底价 P_floor 与挂价 P_ask 的偏差项 δ_opp 的量化：δ_opp = P_ask - P_floor = (1 + β_opp) * V 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101, N102, N103

## Claim

心理底价 P_floor 与挂价 P_ask 的偏差项 δ_opp 的量化：δ_opp = P_ask - P_floor = (1 + β_opp) * V - (1 - c_hold) * V = (β_opp + c_hold) * V，其中 β_opp 为卖家乐观偏差系数（假设 0.15）。若 c_hold=0.07，则 δ_opp = 0.22 * V，解释了为何挂价普遍高于真实价值 V 约 22%。

## Corrected Claim

心理底价 P_floor 与挂价 P_ask 的偏差项 δ_opp 的量化：δ_opp = P_ask - P_floor = (1 + β_opp) * V - (1 - c_hold) * V = (β_opp + c_hold) * V，其中 β_opp 为卖家乐观偏差系数（假设 0.15）。若 c_hold=0.07，则 δ_opp = 0.22 * V，解释了为何挂价普遍高于真实价值 V 约 22%。

## Evidence

先验知识/题面给定，逻辑校验通过：代数推导 (1+β)V - (1-c)V = (β+c)V 正确，数值 0.15+0.07=0.22 无误，符合行为经济学中卖家乐观偏差导致挂价高于内在价值的基本逻辑。

## Search Query

seller optimism bias in pricing second-hand goods empirical study
