# N76: Bootstrap 95% 置信区间计算：基于 n=100 的二项分布样本，通过 10,000 次重抽样计算 H_domain 的置信区间 [CI_lower,

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

Bootstrap 95% 置信区间计算：基于 n=100 的二项分布样本，通过 10,000 次重抽样计算 H_domain 的置信区间 [CI_lower, CI_upper]，若 CI_lower > 15% 则强制启用 RAG Hook，避免小样本波动导致的误判。

## Corrected Claim

Bootstrap 95% 置信区间计算：基于 n=100 的二项分布样本，通过 10,000 次重抽样计算 H_domain 的置信区间 [CI_lower, CI_upper]，若 CI_lower > 15% 则强制启用 RAG Hook，避免小样本波动导致的误判。

## Evidence

先验知识/题面给定，逻辑校验通过：Bootstrap方法用于估计置信区间是标准统计实践，n=100样本下10,000次重抽样具有足够的收敛精度，阈值判断逻辑自洽。
