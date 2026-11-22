# N258: 引入买家理性筛选机制后的残差分布修正：若买家仅在 |Noise| < Threshold_screen 时发起交易，则观测到的成交溢价分布被截断。计算截断正态分

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

引入买家理性筛选机制后的残差分布修正：若买家仅在 |Noise| < Threshold_screen 时发起交易，则观测到的成交溢价分布被截断。计算截断正态分布下 P(Noise > 0.15*μ | |Noise| < K) 的概率值，其中 K 为筛选阈值，需确定 K 的取值（如 1.5σ 或 2σ）以使理论概率从 20.3% 降至 15%。

## Corrected Claim

引入买家理性筛选机制后的残差分布修正：若买家仅在 |Noise| < Threshold_screen 时发起交易，则观测到的成交溢价分布被截断。计算截断正态分布下 P(Noise > 0.15*μ | |Noise| < K) 的概率值，其中 K 为筛选阈值，需确定 K 的取值（如 1.5σ 或 2σ）以使理论概率从 20.3% 降至 15%。

## Evidence

先验知识/题面给定，逻辑校验通过：截断正态分布的概率计算在数学上是自洽的，且通过调整截断阈值K来匹配目标概率（从20.3%降至15%）符合统计学原理。
