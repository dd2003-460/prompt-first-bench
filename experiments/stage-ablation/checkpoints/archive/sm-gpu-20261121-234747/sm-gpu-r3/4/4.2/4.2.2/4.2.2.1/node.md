# N296: 硬件价格参数（如RTX 4090, L40S）的'重大更新'量化阈值定义为：|P_current - P_baseline| / P_baseline > 10

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

硬件价格参数（如RTX 4090, L40S）的'重大更新'量化阈值定义为：|P_current - P_baseline| / P_baseline > 10%，其中P_baseline为2024Q4季度均价，P_current为查询日实时均价；若触发该条件，置信度降为'低'。

## Corrected Claim

硬件价格参数（如RTX 4090, L40S）的'重大更新'量化阈值定义为：|P_current - P_baseline| / P_baseline > 10%，其中P_baseline为2024Q4季度均价，P_current为查询日实时均价；若触发该条件，置信度降为'低'。

## Evidence

先验知识/题面给定，逻辑校验通过
