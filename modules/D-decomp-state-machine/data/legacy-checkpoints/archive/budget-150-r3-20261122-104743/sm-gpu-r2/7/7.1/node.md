# N180: 3年总生成Token数 (Total_Tokens) 的计算公式为：Throughput_Tokens_per_s × 3600 (s/h) × 24 (h/d

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

3年总生成Token数 (Total_Tokens) 的计算公式为：Throughput_Tokens_per_s × 3600 (s/h) × 24 (h/day) × 365 (days/year) × 3 (years) × Utilization_Factor，其中 Throughput 取自 N36 的实测数据，Utilization_Factor 需根据业务负载曲线确定（本地工作站典型值 0.2-0.5，数据中心典型值 0.6-0.9）

## Corrected Claim

3年总生成Token数 (Total_Tokens) 的计算公式为：Throughput_Tokens_per_s × 3600 (s/h) × 24 (h/day) × 365 (days/year) × 3 (years) × Utilization_Factor，其中 Throughput 取自 N36 的实测数据，Utilization_Factor 需根据业务负载曲线确定（本地工作站典型值 0.2-0.5，数据中心典型值 0.6-0.9）

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（Tokens/s * s = Tokens），时间换算系数（3600*24*365*3）符合3年总时长的定义，利用率系数范围符合工程常识。
