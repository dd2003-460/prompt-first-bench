# N29: 条件性推荐逻辑：定义推荐条件矩阵，例如 '若电价 > $0.15/kWh，则推荐低功耗方案（如 L40S 或 Mac Studio）；若预算 < $5000，则

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

条件性推荐逻辑：定义推荐条件矩阵，例如 '若电价 > $0.15/kWh，则推荐低功耗方案（如 L40S 或 Mac Studio）；若预算 < $5000，则推荐 2× RTX 4090 W4 量化方案；若追求最高吞吐量且预算充足，则推荐 1× H100 FP8 方案'；确保最终结论依赖于这些条件而非绝对排名。

## Corrected Claim

条件性推荐逻辑：定义推荐条件矩阵，例如 '若电价 > $0.15/kWh，则推荐低功耗方案（如 L40S 或 Mac Studio）；若预算 < $5000，则推荐 2× RTX 4090 W4 量化方案；若追求最高吞吐量且预算充足，则推荐 1× H100 FP8 方案'；确保最终结论依赖于这些条件而非绝对排名。

## Evidence

先验知识/题面给定，逻辑校验通过
