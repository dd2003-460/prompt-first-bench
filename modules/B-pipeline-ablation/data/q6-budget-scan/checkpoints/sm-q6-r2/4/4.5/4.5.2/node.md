# N141: 混合策略中公有云流量基数 $V_{tail}$ 的计算：$V_{tail} = V_{total} \cdot (1 - \eta_{coverage})$，其

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

混合策略中公有云流量基数 $V_{tail}$ 的计算：$V_{tail} = V_{total} \cdot (1 - \eta_{coverage})$，其中 $V_{total} = 60 \text{ TB/month}$（N18），若 $\eta_{coverage} = 80\%$，则 $V_{tail} = 12 \text{ TB/month}$，该值直接代入 N39 的 $C_{bandwidth}^{pub}$ 计算。

## Corrected Claim

混合策略中公有云流量基数 $V_{tail}$ 的计算：$V_{tail} = V_{total} \cdot (1 - \eta_{coverage})$，其中 $V_{total} = 60 \text{ TB/month}$（N18），若 $\eta_{coverage} = 80\%$，则 $V_{tail} = 12 \text{ TB/month}$，该值直接代入 N39 的 $C_{bandwidth}^{pub}$ 计算。

## Evidence

先验知识/题面给定，逻辑校验通过：60 * (1 - 0.8) = 12，计算无误且量纲一致
