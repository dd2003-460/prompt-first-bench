# N89: W2模式下的云端 Token 消耗量 Tokens_cloud 由路由阈值决定：若本地 Self-Consistency 失败概率 P_fail = 0.3 (

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

W2模式下的云端 Token 消耗量 Tokens_cloud 由路由阈值决定：若本地 Self-Consistency 失败概率 P_fail = 0.3 (基于 N23 的 H(p)>0.5 bits 阈值)，且每次云端调用平均消耗 5k tokens，则 Tokens_cloud = P_fail * Avg_Tokens_per_Call * Iterations

## Corrected Claim

W2模式下的云端 Token 消耗量 Tokens_cloud 由路由阈值决定：若本地 Self-Consistency 失败概率 P_fail = 0.3 (基于 N23 的 H(p)>0.5 bits 阈值)，且每次云端调用平均消耗 5k tokens，则 Tokens_cloud = P_fail * Avg_Tokens_per_Call * Iterations

## Evidence

检索失败: no sources from any channel (all 5 failed)
