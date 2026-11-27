# N109: 离散度项的截断修正：考虑到物理上热度 h 不能无限大，引入截断上限 h_max（例如 h_max = 10^4 * h_min），修正后的 CV_H^2_tru

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

离散度项的截断修正：考虑到物理上热度 h 不能无限大，引入截断上限 h_max（例如 h_max = 10^4 * h_min），修正后的 CV_H^2_trunc 将显著低于 801900，需计算 h_max/h_min 比值对 CV_H^2 的衰减因子，以找到线性近似失效的临界点。

## Corrected Claim

离散度项的截断修正：考虑到物理上热度 h 不能无限大，引入截断上限 h_max（例如 h_max = 10^4 * h_min），修正后的 CV_H^2_trunc 将显著低于 801900，需计算 h_max/h_min 比值对 CV_H^2 的衰减因子，以找到线性近似失效的临界点。

## Evidence

先验知识/题面给定，逻辑校验通过：引入截断上限 h_max 限制积分/求和范围，数学上必然导致方差及变异系数（CV）减小，且 h_max/h_min 比值越大衰减越显著，符合统计与物理直觉。

## Search Query

truncated Pareto distribution variance calculation
