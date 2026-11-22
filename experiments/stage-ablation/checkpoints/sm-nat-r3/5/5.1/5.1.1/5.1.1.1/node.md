# N216: 周期性负载下 LRU 命中率的修正项 ε_periodic = (1 - cos(2πT_access/T_cycle)) / 2，其中 T_access 为对

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N76

## Claim

周期性负载下 LRU 命中率的修正项 ε_periodic = (1 - cos(2πT_access/T_cycle)) / 2，其中 T_access 为对象平均访问间隔，T_cycle 为负载周期（如 24 小时）；若 T_access = 1h，T_cycle = 24h，则 ε_periodic = (1 - cos(π/12)) / 2 ≈ 0.0034，表明周期性负载导致命中率下降约 0.34%。

## Corrected Claim

周期性负载下 LRU 命中率的修正项 ε_periodic = (1 - cos(2πT_access/T_cycle)) / 2，其中 T_access 为对象平均访问间隔，T_cycle 为负载周期（如 24 小时）；若 T_access = 1h，T_cycle = 24h，则 ε_periodic = (1 - cos(π/12)) / 2 ≈ 0.0171，表明周期性负载导致命中率下降约 1.71%。

## Evidence

[质询]该公式缺乏通用的理论或工程依据，属于特定模型假设下的经验拟合或虚构公式；LRU命中率受缓存大小、访问分布（如Zipf指数）等多因素影响，仅凭访问间隔与周期的余弦关系无法直接推导，且0.34%的下降幅度在典型周期性负载下可能偏小或偏大，取决于具体场景。 | 先验知识/题面给定，逻辑校验通过（数值计算正确：cos(π/12)≈0.9659，(1-0.9659)/2≈0.017？等等，重新计算：cos(π/12) = cos(15°) ≈ 0.9659。 (1 - 0.9659) / 2 = 0.0341 / 2 = 0.01705。 题目中声称 ≈ 0.0034。 0.01705 与 0.0034 相差约5倍。 存在硬逻辑/计算错误。
