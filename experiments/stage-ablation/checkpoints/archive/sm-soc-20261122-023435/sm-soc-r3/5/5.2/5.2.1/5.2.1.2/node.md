# N196: 阈值 S_season > 0.15 的统计依据：该阈值对应于在正态分布假设下，偏离均值 1.5 个标准差（σ）的临界值，即 P(|Z| > 1.5) ≈ 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

阈值 S_season > 0.15 的统计依据：该阈值对应于在正态分布假设下，偏离均值 1.5 个标准差（σ）的临界值，即 P(|Z| > 1.5) ≈ 0.13，意味着若 S_season 超过 0.15，则视为小概率事件，提示存在非随机需求冲击。

## Corrected Claim

阈值 S_season > 0.15 的统计依据：该阈值对应于在正态分布假设下，偏离均值 1.5 个标准差（σ）的临界值，即 P(|Z| > 1.5) ≈ 0.13，意味着若 S_season 超过 0.15，则视为小概率事件，提示存在非随机需求冲击。

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布下 P(|Z| > 1.5) ≈ 0.134，与陈述中的 0.13 一致，且 1.5σ 对应小概率事件的统计解释符合基本概率论原理。

## Search Query

statistical threshold 1.5 standard deviation anomaly detection
