# N332: 组间差异>10%的显著性检验需具体化：计算p_<5%与p_>15%的差值Δp，其标准误SE(Δp) = sqrt(p1(1-p1)/n1 + p2(1-p2)/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95, N96, N97

## Claim

组间差异>10%的显著性检验需具体化：计算p_<5%与p_>15%的差值Δp，其标准误SE(Δp) = sqrt(p1(1-p1)/n1 + p2(1-p2)/n2)，若Δp > 1.96 * SE(Δp)，则差异显著，需按组加权修正原始60%数据，修正公式为 p_corrected = Σ(p_group * w_group)，其中w_group为各组样本量占比。

## Corrected Claim

组间差异>10%的显著性检验需具体化：计算p_<5%与p_>15%的差值Δp，其标准误SE(Δp) = sqrt(p1(1-p1)/n1 + p2(1-p2)/n2)，若Δp > 1.96 * SE(Δp)，则差异显著，需按组加权修正原始60%数据，修正公式为 p_corrected = Σ(p_group * w_group)，其中w_group为各组样本量占比。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合双比例差异显著性检验（Z检验）及加权平均的标准统计学定义，量纲与逻辑自洽。
