# N6: 对象大小服从 Pareto(α=1.1)，其累积分布函数 CDF(S>s) = (s_min/s)^1.1，其中 s_min 需根据总存储约束或经验值设定，通常

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

对象大小服从 Pareto(α=1.1)，其累积分布函数 CDF(S>s) = (s_min/s)^1.1，其中 s_min 需根据总存储约束或经验值设定，通常取 1KB 或 100KB 作为最小对象大小阈值。

## Corrected Claim

对象大小服从 Pareto(α=1.1)，其累积分布函数 CDF(S>s) = (s_min/s)^1.1，其中 s_min 需根据总存储约束或经验值设定，通常取 1KB 或 100KB 作为最小对象大小阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的CDF公式形式正确，量纲一致，且1KB/100KB作为最小对象大小阈值在存储系统建模中属于合理的经验取值范围。
