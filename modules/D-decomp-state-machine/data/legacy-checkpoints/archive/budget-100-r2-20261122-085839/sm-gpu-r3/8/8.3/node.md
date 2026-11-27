# N105: Utilization_Factor（利用率系数）在本地工作站场景下，若为单用户交互式推理（Batch=1，突发请求），典型值为 0.2-0.4；若为后台批量处

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

Utilization_Factor（利用率系数）在本地工作站场景下，若为单用户交互式推理（Batch=1，突发请求），典型值为 0.2-0.4；若为后台批量处理（Batch>8，持续队列），典型值为 0.7-0.9。该系数直接线性影响 Effective_Tokens_Per_Dollar，0.3 与 0.8 的差异会导致性价比排名反转 [知识: 负载特征经验值]

## Corrected Claim

Utilization_Factor（利用率系数）在本地工作站场景下，若为单用户交互式推理（Batch=1，突发请求），典型值为 0.2-0.4；若为后台批量处理（Batch>8，持续队列），典型值为 0.7-0.9。该系数直接线性影响 Effective_Tokens_Per_Dollar，0.3 与 0.8 的差异会导致性价比排名反转 [知识: 负载特征经验值]

## Evidence

先验知识/题面给定，逻辑校验通过
