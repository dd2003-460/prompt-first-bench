# N197: 降价后 λ_t 与基准 λ_base 的统计显著性检验：计算比率 R = λ_t / λ_base，构建置信区间 [R * exp(-1.96/√N), R *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72, N73, N74

## Claim

降价后 λ_t 与基准 λ_base 的统计显著性检验：计算比率 R = λ_t / λ_base，构建置信区间 [R * exp(-1.96/√N), R * exp(1.96/√N)]（N为样本量）；若 CI 不包含 1 且 R < 1，则确认降价导致咨询率显著下降，支持‘算法抑制’或‘锚定失效’假设。

## Corrected Claim

降价后 λ_t 与基准 λ_base 的统计显著性检验：计算比率 R = λ_t / λ_base，构建置信区间 [R * exp(-1.96/√N), R * exp(1.96/√N)]（N为样本量）；若 CI 不包含 1 且 R < 1，则确认降价导致咨询率显著下降，支持‘算法抑制’或‘锚定失效’假设。

## Evidence

先验知识/题面给定，逻辑校验通过：基于对数正态分布近似或Delta方法，比率R的置信区间构建公式在统计上自洽，且判定逻辑（CI不含1且R<1）符合假设检验标准。
