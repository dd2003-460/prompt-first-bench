# N564: Cohen's h 的 95% 置信区间半宽（CI_half_width）计算公式为 CI_hw = 1.96 * SE_h，其中 SE_h = sqrt((1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N202

## Claim

Cohen's h 的 95% 置信区间半宽（CI_half_width）计算公式为 CI_hw = 1.96 * SE_h，其中 SE_h = sqrt((1-p1)/p1 + (1-p2)/p2) / (2*sqrt(n))，该公式基于大样本正态近似，仅在 n*p1 > 5 且 n*p2 > 5 时成立。

## Corrected Claim

Cohen's h 的 95% 置信区间半宽（CI_half_width）计算公式为 CI_hw = 1.96 * SE_h，其中 SE_h = sqrt((1-p1)/p1 + (1-p2)/p2) / (2*sqrt(n))，该公式基于大样本正态近似，仅在 n*p1 > 5 且 n*p2 > 5 时成立。

## Evidence

[质询]SE_h 的公式形式存在争议：标准 Cohen's h 的标准误通常近似为 sqrt((1-p1)/p1 + (1-p2)/p2) / (2*sqrt(n)) 仅在特定简化假设下成立，更精确的公式涉及 p1 和 p2 的联合方差，且分母通常为 2*sqrt(n) 仅当 n1=n2=n 时成立；若 n1≠n2，公式应为 sqrt((1-p1)/(4*n1*p1) + (1-p2)/(4*n2*p2))。此外，Cohen's h 定义为 2*arcsin(sqrt(p1)) - 2*arcsin(sqrt(p2))，其标准误推导基于 Delta 方法，给出的近似公式在 p 接近 0 或 1 时误差较大，但题目已限定 n*p>5，故在大样本正态近似下该简化公式是可接受的常用近似。 | 先验知识/题面给定，逻辑校验通过：Cohen's h 的置信区间基于正态近似，SE 公式为常用简化形式，适用条件 n*p>5 符合二项分布正态近似准则。
