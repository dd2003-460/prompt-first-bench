# N34: 最小请求率 r_min 的解析确定式 r_min = (50,000,000 / N) * (N / (N^(1/β) - 1))^(1/β)，该公式由离散 P

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

最小请求率 r_min 的解析确定式 r_min = (50,000,000 / N) * (N / (N^(1/β) - 1))^(1/β)，该公式由离散 Pareto 分布的归一化条件 Σr_i = R_total 推导得出，用于消除 r_min 的自由度。

## Corrected Claim

最小请求率 r_min 的解析确定式 r_min = (50,000,000 / N) * (N / (N^(1/β) - 1))^(1/β)，该公式由离散 Pareto 分布的归一化条件 Σr_i = R_total 推导得出，用于消除 r_min 的自由度。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合离散Pareto分布归一化条件推导出的最小值解析式结构，量纲与逻辑自洽。
