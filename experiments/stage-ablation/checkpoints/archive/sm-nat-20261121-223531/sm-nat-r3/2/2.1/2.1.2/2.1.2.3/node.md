# N122: 数值积分的离散化网格步长选择：在 1000x1000 网格下，lnS 和 lnH 的步长 ΔlnS = (ln(s_max) - ln(s_min)) / 99

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

数值积分的离散化网格步长选择：在 1000x1000 网格下，lnS 和 lnH 的步长 ΔlnS = (ln(s_max) - ln(s_min)) / 999，ΔlnH = (ln(h_max) - ln(h_min)) / 999。概率质量 P(s_i, h_j) 由二元正态 PDF 在网格点 (lnS_i, lnH_j) 的值乘以 Jacobian 行列式 ΔlnS * ΔlnH 得到，确保总和归一化为 1。

## Corrected Claim

数值积分的离散化网格步长选择：在 1000x1000 网格下，lnS 和 lnH 的步长 ΔlnS = (ln(s_max) - ln(s_min)) / 999，ΔlnH = (ln(h_max) - ln(h_min)) / 999。概率质量 P(s_i, h_j) 由二元正态 PDF 在网格点 (lnS_i, lnH_j) 的值乘以 Jacobian 行列式 ΔlnS * ΔlnH 得到，确保总和归一化为 1。

## Evidence

先验知识/题面给定，逻辑校验通过：数值积分中通过PDF乘以网格面积（Jacobian行列式）进行离散化是标准做法，且步长定义与网格点数（1000x1000，间隔999）逻辑自洽。
