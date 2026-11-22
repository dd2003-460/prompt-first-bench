# N32: 在 Pareto(β=0.9) 热度分布下，第 i 热对象的请求频率 R_i 的解析表达式为 R_i = r_min * (N/i)^0.9，其中 N=1000

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

在 Pareto(β=0.9) 热度分布下，第 i 热对象的请求频率 R_i 的解析表达式为 R_i = r_min * (N/i)^0.9，其中 N=100000，r_min 由归一化条件确定，此表达式用于计算前 K 个最热对象的累积请求占比

## Corrected Claim

在 Pareto(β=0.9) 热度分布下，第 i 热对象的请求频率 R_i 的解析表达式为 R_i = r_min * (N/i)^0.9，其中 N=100000，r_min 由归一化条件确定，此表达式用于计算前 K 个最热对象的累积请求占比

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Zipf law Pareto distribution rank frequency formula
