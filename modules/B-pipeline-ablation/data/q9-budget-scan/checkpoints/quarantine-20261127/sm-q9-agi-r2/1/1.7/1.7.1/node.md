# N51: Reproducibility 的量化操作定义为：在相同随机种子集 (N_seeds=5) 下，独立重跑分析脚本产生的关键统计量（如均值/回归系数）的变异系数 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

Reproducibility 的量化操作定义为：在相同随机种子集 (N_seeds=5) 下，独立重跑分析脚本产生的关键统计量（如均值/回归系数）的变异系数 CV = Std/Mean < 0.05，或定性结论的一致率 > 95%。

## Corrected Claim

Reproducibility 的量化操作定义为：在相同随机种子集 (N_seeds=5) 下，独立重跑分析脚本产生的关键统计量（如均值/回归系数）的变异系数 CV = Std/Mean < 0.05，或定性结论的一致率 > 95%。

## Evidence

先验知识/题面给定，逻辑校验通过
