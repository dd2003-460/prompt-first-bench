# N324: Consistency_Index 的分子 Correlation(ΔP_ask, ΔT_close) 的计算需基于配对样本数据，其中 ΔP_ask 定义为 (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N112

## Claim

Consistency_Index 的分子 Correlation(ΔP_ask, ΔT_close) 的计算需基于配对样本数据，其中 ΔP_ask 定义为 (P_ask - P_market)/P_market，ΔT_close 定义为 T_close - E[T_close|P_market]，需明确时间窗口（如7天）及样本筛选条件（排除异常值）。

## Corrected Claim

Consistency_Index 的分子 Correlation(ΔP_ask, ΔT_close) 的计算需基于配对样本数据，其中 ΔP_ask 定义为 (P_ask - P_market)/P_market，ΔT_close 定义为 T_close - E[T_close|P_market]，需明确时间窗口（如7天）及样本筛选条件（排除异常值）。

## Evidence

先验知识/题面给定，逻辑校验通过
