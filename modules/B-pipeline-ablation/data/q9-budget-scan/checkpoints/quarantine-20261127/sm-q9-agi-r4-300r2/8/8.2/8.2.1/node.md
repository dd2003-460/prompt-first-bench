# N205: Cohen's d 计算中的标准误（Standard Error of Effect Size）校正：SE_d = sqrt((n1+n2)/(n1*n2) +

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

Cohen's d 计算中的标准误（Standard Error of Effect Size）校正：SE_d = sqrt((n1+n2)/(n1*n2) + d^2/(2*(n1+n2)))；当 n=30 且 d=0.8 时，95% CI 宽度约为 ±0.55，意味着真实效应量可能在 0.25-1.35 之间；若 CI 下限 < 0.2 (Small Effect)，即使点估计 > 0.8，也应标记为‘弱显著’并触发样本量扩展建议

## Corrected Claim

Cohen's d 计算中的标准误（Standard Error of Effect Size）校正：SE_d = sqrt((n1+n2)/(n1*n2) + d^2/(2*(n1+n2)))；当 n=30 且 d=0.8 时，95% CI 宽度约为 ±0.55，意味着真实效应量可能在 0.25-1.35 之间；若 CI 下限 < 0.2 (Small Effect)，即使点估计 > 0.8，也应标记为‘弱显著’并触发样本量扩展建议

## Evidence

先验知识/题面给定，逻辑校验通过：Cohen's d 的标准误公式及置信区间计算符合统计学原理，数值量级合理（n=30, d=0.8 时 SE≈0.275, 95%CI 半宽≈0.54，与陈述的±0.55一致）。
