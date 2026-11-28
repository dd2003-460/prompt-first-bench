# N29: 知识更新冲突检测机制：新知识与现有知识相似度 > 0.95 时触发冲突检测，计算逻辑一致性得分 C = 1 - |P(new) - P(old)|，若 C < 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

知识更新冲突检测机制：新知识与现有知识相似度 > 0.95 时触发冲突检测，计算逻辑一致性得分 C = 1 - |P(new) - P(old)|，若 C < 0.5 则标记为矛盾并启动人工审核队列，否则自动合并（权重 w_new = 0.7, w_old = 0.3）

## Corrected Claim

知识更新冲突检测机制：新知识与现有知识相似度 > 0.95 时触发冲突检测，计算逻辑一致性得分 C = 1 - |P(new) - P(old)|，若 C < 0.5 则标记为矛盾并启动人工审核队列，否则自动合并（权重 w_new = 0.7, w_old = 0.3）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

knowledge base conflict detection logical consistency score update mechanism
