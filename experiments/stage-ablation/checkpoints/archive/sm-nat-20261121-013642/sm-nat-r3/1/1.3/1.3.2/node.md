# N37: 条件期望修正项 E[size | freq > f_q] 的计算：对于热度分位数 f_q，计算条件期望大小，该值用于修正 LRU 缓存集合的期望字节覆盖率，公式

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

条件期望修正项 E[size | freq > f_q] 的计算：对于热度分位数 f_q，计算条件期望大小，该值用于修正 LRU 缓存集合的期望字节覆盖率，公式为 E[s|r>f_q] = ∫_{s_min}^{S_max} s * P(s|r>f_q) ds，需数值积分求解。

## Corrected Claim

条件期望修正项 E[size | freq > f_q] 的计算：对于热度分位数 f_q，计算条件期望大小，该值用于修正 LRU 缓存集合的期望字节覆盖率，公式为 E[s|r>f_q] = ∫_{s_min}^{S_max} s * P(s|r>f_q) ds，需数值积分求解。

## Evidence

先验知识/题面给定，逻辑校验通过：条件期望的定义即为随机变量在特定条件下的积分形式，公式 E[s|r>f_q] = ∫ s * P(s|r>f_q) ds 符合概率论基本定义，且对于非解析分布需数值积分求解符合工程实践。
