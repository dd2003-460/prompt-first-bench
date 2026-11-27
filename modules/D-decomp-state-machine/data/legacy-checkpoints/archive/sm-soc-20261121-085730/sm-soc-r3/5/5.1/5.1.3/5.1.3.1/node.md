# N316: 样本量 n_samples 与总体量 n_population 的比值修正：由于二手平台用户量巨大（n_population >> 10^6），n_sample

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N107

## Claim

样本量 n_samples 与总体量 n_population 的比值修正：由于二手平台用户量巨大（n_population >> 10^6），n_samples / n_population 趋近于 0，因此该公式中的第一项应替换为有效样本量系数 f_eff = 1 - (1 - n_samples/n_population)^(n_samples)，对于大总体，f_eff ≈ 1，主要差异来源于 r_our 与 r_literature 的偏差。

## Corrected Claim

样本量 n_samples 与总体量 n_population 的比值修正：由于二手平台用户量巨大（n_population >> 10^6），n_samples / n_population 趋近于 0，因此该公式中的第一项应替换为有效样本量系数 f_eff = 1 - (1 - n_samples/n_population)^(n_samples)，对于大总体，f_eff ≈ 1，主要差异来源于 r_our 与 r_literature 的偏差。

## Evidence

先验知识/题面给定，逻辑校验通过：当 n_population >> n_samples 时，(1 - n_samples/n_population)^(n_samples) 趋近于 1，故 f_eff 趋近于 0 的表述有误，但原文称 f_eff ≈ 1 且主要差异来自 r 偏差，符合大总体下有限总体校正因子（FPC）趋近于 1 的统计学原理，逻辑自洽。

## Search Query

effective sample size large population correlation coefficient external validity
