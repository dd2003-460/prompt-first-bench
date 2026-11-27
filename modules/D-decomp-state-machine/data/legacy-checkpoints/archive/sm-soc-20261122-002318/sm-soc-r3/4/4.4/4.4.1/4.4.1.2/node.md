# N185: 工作点B（中等成交量弹性/中等价格弹性）：假设成交量弹性 ε_V = 1.0，价格弹性 ε_P = -1.0。在干预导致平均价格下降5%的场景下，成交量上升5%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N64

## Claim

工作点B（中等成交量弹性/中等价格弹性）：假设成交量弹性 ε_V = 1.0，价格弹性 ε_P = -1.0。在干预导致平均价格下降5%的场景下，成交量上升5%，ΔGMV = (1.05*V_old - V_old)*P_old*0.95 + V_old*(-0.05*P_old) = 0.05*V_old*P_old*0.95 - 0.05*V_old*P_old = -0.0025*GMV_old，即GMV净减0.25%（近似中性）。

## Corrected Claim

工作点B（中等成交量弹性/中等价格弹性）：假设成交量弹性 ε_V = 1.0，价格弹性 ε_P = -1.0。在干预导致平均价格下降5%的场景下，成交量上升5%，ΔGMV = (1.05*V_old - V_old)*P_old*0.95 + V_old*(-0.05*P_old) = 0.05*V_old*P_old*0.95 - 0.05*V_old*P_old = -0.0025*GMV_old，即GMV净减0.25%（近似中性）。

## Evidence

先验知识/题面给定，逻辑校验通过：GMV变化率 = (1+ΔP)(1+ΔV)-1 = 0.95*1.05-1 = -0.0025，即-0.25%，计算无误。

## Search Query

neutral GMV impact elasticity balance second hand market
