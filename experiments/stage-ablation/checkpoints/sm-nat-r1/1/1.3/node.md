# N7: 有效缓存容量C_eff计算式：C_eff = C_total * (1 - U * T_churn)，其中C_total=128GB，U=1%/天更新率，T_c

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

有效缓存容量C_eff计算式：C_eff = C_total * (1 - U * T_churn)，其中C_total=128GB，U=1%/天更新率，T_churn为对象平均驻留时间（需由请求间隔和LRU淘汰策略决定）

## Corrected Claim

有效缓存容量C_eff计算式：C_eff = C_total * (1 - U * T_churn)，其中C_total=128GB，U=1%/天更新率，T_churn为对象平均驻留时间（需由请求间隔和LRU淘汰策略决定）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

effective cache capacity update rate churn time LRU
