# N245: 故障率与负载强度的非线性关系系数：GPU 故障率并非恒定，而是随工作负载强度（如显存占用率 >90% 或核心温度 >85°C）呈指数增长；需建立 P_fail 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

故障率与负载强度的非线性关系系数：GPU 故障率并非恒定，而是随工作负载强度（如显存占用率 >90% 或核心温度 >85°C）呈指数增长；需建立 P_fail = P_base * exp(k * (T_core - T_threshold)) 的修正模型，其中 k 为温度敏感系数，需通过加速老化实验数据拟合。

## Corrected Claim

故障率与负载强度的非线性关系系数：GPU 故障率并非恒定，而是随工作负载强度（如显存占用率 >90% 或核心温度 >85°C）呈指数增长；需建立 P_fail = P_base * exp(k * (T_core - T_threshold)) 的修正模型，其中 k 为温度敏感系数，需通过加速老化实验数据拟合。

## Evidence

先验知识/题面给定，逻辑校验通过
