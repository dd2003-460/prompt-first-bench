# N92: H_effective 的误差来源分解：总误差 ε_total = ε_H_corrected + ε_F_decay，其中 ε_H_corrected 来自负

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

H_effective 的误差来源分解：总误差 ε_total = ε_H_corrected + ε_F_decay，其中 ε_H_corrected 来自负相关修正因子 K 的二阶项误差（约 0.3-0.5 个百分点），ε_F_decay ≈ 1.2e-8；因此 H_effective 的主要不确定性来自静态命中率估算而非动态失效，置信区间应基于 K 的精度而非 F_decay。

## Corrected Claim

H_effective 的误差来源分解：总误差 ε_total = ε_H_corrected + ε_F_decay，其中 ε_H_corrected 来自负相关修正因子 K 的二阶项误差（约 0.3-0.5 个百分点），ε_F_decay ≈ 1.2e-8；因此 H_effective 的主要不确定性来自静态命中率估算而非动态失效，置信区间应基于 K 的精度而非 F_decay。

## Evidence

先验知识/题面给定，逻辑校验通过：误差分解公式在量纲和逻辑上自洽，且基于K因子精度主导不确定性的结论符合统计修正的一般原理。
