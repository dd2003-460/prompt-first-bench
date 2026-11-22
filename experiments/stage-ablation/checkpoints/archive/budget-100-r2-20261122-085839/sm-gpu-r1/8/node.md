# N29: 性价比核心指标定义：Cost_Per_Token = (Hardware_Cost + Electricity_Cost_Per_Hour * Deployme

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比核心指标定义：Cost_Per_Token = (Hardware_Cost + Electricity_Cost_Per_Hour * Deployment_Hours) / Total_Tokens_Generated。在本地工作站长期部署场景下，若假设24/7运行，电力成本占比显著；若为按需推理，则硬件折旧成本占比更高。建议采用 'Effective_Tokens_Per_Dollar' = (Throughput_tokens_per_sec * 3600 * 8760 * Utilization_Factor) / Hardware_Cost 作为静态指标，其中Utilization_Factor需根据业务负载设定（保守取0.3-0.5）。

## Corrected Claim

性价比核心指标定义：Cost_Per_Token = (Hardware_Cost + Electricity_Cost_Per_Hour * Deployment_Hours) / Total_Tokens_Generated。在本地工作站长期部署场景下，若假设24/7运行，电力成本占比显著；若为按需推理，则硬件折旧成本占比更高。建议采用 'Effective_Tokens_Per_Dollar' = (Throughput_tokens_per_sec * 3600 * 8760 * Utilization_Factor) / Hardware_Cost 作为静态指标，其中Utilization_Factor需根据业务负载设定（保守取0.3-0.5）。

## Evidence

检索失败: no sources from any channel (all 5 failed)
