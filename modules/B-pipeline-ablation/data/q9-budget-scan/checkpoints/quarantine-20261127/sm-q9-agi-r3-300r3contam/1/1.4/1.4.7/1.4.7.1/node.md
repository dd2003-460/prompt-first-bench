# N128: 资源预估 Cost_est 的计算公式：Cost_est = T_est * C_unit + M_peak * C_storage，其中 T_est 为基于历

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

资源预估 Cost_est 的计算公式：Cost_est = T_est * C_unit + M_peak * C_storage，其中 T_est 为基于历史相似任务耗时的预测值（取 P90 分位），C_unit 为每单位时间/算力的标准化成本系数（$0.005/query 或 $/hr），M_peak 为峰值显存占用预测值（GB）。

## Corrected Claim

资源预估 Cost_est 的计算公式：Cost_est = T_est * C_unit + M_peak * C_storage，其中 T_est 为基于历史相似任务耗时的预测值（取 P90 分位），C_unit 为每单位时间/算力的标准化成本系数（$0.005/query 或 $/hr），M_peak 为峰值显存占用预测值（GB）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM agent resource estimation cost model formula
