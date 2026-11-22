# N71: 信号效应的统计检验指标：通过比较高挂价组与低挂价组的成交周期 T_deal 差异，计算 t 统计量 t = (T_high - T_low) / (σ_pool

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

信号效应的统计检验指标：通过比较高挂价组与低挂价组的成交周期 T_deal 差异，计算 t 统计量 t = (T_high - T_low) / (σ_pooled / sqrt(n))，其中 σ_pooled 为合并标准差，n 为样本量；若 t > 1.96 (p<0.05)，则支持信号效应。

## Corrected Claim

信号效应的统计检验指标：通过比较高挂价组与低挂价组的成交周期 T_deal 差异，计算 t 统计量 t = (T_high - T_low) / (σ_pooled / sqrt(n))，其中 σ_pooled 为合并标准差，n 为样本量；若 t > 1.96 (p<0.05)，则支持信号效应。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述准确描述了双样本t检验的标准公式及显著性判断准则（t>1.96对应双侧p<0.05），符合统计学基本原理。
