# N306: 量化价格效应项 $Q_{sold} \cdot \Delta P$ 的绝对值：基于基线GMV $GMV_0 = P_0 Q_0$，若价格下降幅度 $\Delta

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N106

## Claim

量化价格效应项 $Q_{sold} \cdot \Delta P$ 的绝对值：基于基线GMV $GMV_0 = P_0 Q_0$，若价格下降幅度 $\Delta P/P_0 = -15\%$，则该项贡献为 $-0.15 GMV_0$。

## Corrected Claim

量化价格效应项 $Q_{sold} \cdot \Delta P$ 的绝对值：基于基线GMV $GMV_0 = P_0 Q_0$，若价格下降幅度 $\Delta P/P_0 = -15\%$，则该项贡献为 $-0.15 GMV_0$。

## Evidence

先验知识/题面给定，逻辑校验通过：根据定义，量化价格效应项 $Q_{sold} \cdot \Delta P$ 在基线条件下（$Q_{sold} \approx Q_0$）且价格变化率为 $-15\%$ 时，其值为 $Q_0 \cdot (-0.15 P_0) = -0.15 P_0 Q_0 = -0.15 GMV_0$，推导严谨且量纲一致。
