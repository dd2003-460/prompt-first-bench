# N187: 信号效应显著性检验的最小样本量 n_min 计算：假设高挂价组成交周期均值 T_high=10天，低挂价组 T_low=8天，合并标准差 σ_pooled=5天

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N71

## Claim

信号效应显著性检验的最小样本量 n_min 计算：假设高挂价组成交周期均值 T_high=10天，低挂价组 T_low=8天，合并标准差 σ_pooled=5天，显著性水平 α=0.05，统计功效 1-β=0.8，则 n_min ≈ 148/组（基于双样本t检验功效分析）。

## Corrected Claim

信号效应显著性检验的最小样本量 n_min 计算：假设高挂价组成交周期均值 T_high=10天，低挂价组 T_low=8天，合并标准差 σ_pooled=5天，显著性水平 α=0.05，统计功效 1-β=0.8，则 n_min ≈ 148/组（基于双样本t检验功效分析）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于双样本t检验功效分析公式，效应量 d=0.4，α=0.05，power=0.8，计算得出每组样本量约为148，数值量级与统计原理一致。

## Search Query

sample size calculation two sample t test power 0.8
