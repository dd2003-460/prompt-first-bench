# N11: LRU 工作点 1（高性低成）：假设 ρ=0（独立性），计算基准命中率 H_base = 1 - ∫_{s_min}^{s_max} (s/E[S]_trunc

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

LRU 工作点 1（高性低成）：假设 ρ=0（独立性），计算基准命中率 H_base = 1 - ∫_{s_min}^{s_max} (s/E[S]_trunc) * f_S(s) * (1 - F_H(h_median)) ds，其中 h_median 为热度中位数，此工作点提供命中率下界，计算复杂度低，误差范围 [待核验] ±5%。

## Corrected Claim

LRU 工作点 1（高性低成）：假设 ρ=0（独立性），计算基准命中率 H_base 的简化模型，该模型提供命中率下界，计算复杂度低，具体误差范围需根据实际负载分布进一步评估。

## Evidence

父节点级核验未通过：不完备（子节点在正交性上表现良好，分别关注参数计算、误差量化和模型偏差修正，无重复。但在完备性上存在缺失：父节点核心是计算 H_base 的积分公式，子节点 1 仅计算了 h_median 这一参数，子节点 2 和 3 仅讨论误差和偏差，完全缺失了如何执行积分计算（即被积函数的具体形式、数值积分方法或解析解推导）这一关键执行步骤。）

## Search Query

LRU cache hit rate independent size popularity pareto approximation
