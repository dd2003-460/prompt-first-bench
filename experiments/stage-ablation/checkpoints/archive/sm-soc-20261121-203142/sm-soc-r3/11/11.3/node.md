# N300: 计算 β_low 的 95% 置信区间 [0.3, 0.7] 所需的样本量 n，基于标准误 SE = 0.2（由CI宽度推导），假设 β_low 的标准差 σ_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

计算 β_low 的 95% 置信区间 [0.3, 0.7] 所需的样本量 n，基于标准误 SE = 0.2（由CI宽度推导），假设 β_low 的标准差 σ_β ≈ 0.15，则 n = (1.96 * 0.15 / 0.2)^2 ≈ 2.2，表明该区间可能基于极小样本或先验分布，需核验数据来源是否满足大数定律条件。

## Corrected Claim

计算 β_low 的 95% 置信区间 [0.3, 0.7] 所需的样本量 n，基于标准误 SE = 0.2（由CI宽度推导），假设 β_low 的标准差 σ_β ≈ 0.15，则 n = (1.96 * 0.15 / 0.2)^2 ≈ 2.2，表明该区间可能基于极小样本或先验分布，需核验数据来源是否满足大数定律条件。

## Evidence

先验知识/题面给定，逻辑校验通过：根据公式 n = (z * σ / SE)^2，代入 z=1.96, σ=0.15, SE=0.2，计算得 n ≈ 2.2，数值量级与推导逻辑自洽。

## Search Query

sample size required for confidence interval width 0.4 for parameter beta
