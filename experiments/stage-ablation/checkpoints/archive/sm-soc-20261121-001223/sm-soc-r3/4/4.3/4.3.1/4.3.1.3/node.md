# N175: 反事实均值 E[Outcome | Treat=0] 的估计量公式：采用最近邻匹配 (Nearest Neighbor Matching) 时，E[Outcom

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

反事实均值 E[Outcome | Treat=0] 的估计量公式：采用最近邻匹配 (Nearest Neighbor Matching) 时，E[Outcome | Treat=0] ≈ (1/n_treat) * Σ_{i in Treat} Y_{j(i)}，其中 Y_{j(i)} 是与处理组个体 i 最匹配的对照组个体 j 的观测结果；需指定匹配比例 (k:1) 及距离度量方法（如欧氏距离）以量化估计偏差。

## Corrected Claim

反事实均值 E[Outcome | Treat=0] 的估计量公式：采用最近邻匹配 (Nearest Neighbor Matching) 时，E[Outcome | Treat=0] ≈ (1/n_treat) * Σ_{i in Treat} Y_{j(i)}，其中 Y_{j(i)} 是与处理组个体 i 最匹配的对照组个体 j 的观测结果；需指定匹配比例 (k:1) 及距离度量方法（如欧氏距离）以量化估计偏差。

## Evidence

先验知识/题面给定，逻辑校验通过
