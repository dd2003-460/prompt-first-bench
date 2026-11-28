# N128: 边界条件：当KV heads < TP size (4)时，vLLM采用复制策略而非切分，单卡KV占用变为 5KB (而非1.25KB)，总显存需求翻倍，需调整

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N39

## Claim

边界条件：当KV heads < TP size (4)时，vLLM采用复制策略而非切分，单卡KV占用变为 5KB (而非1.25KB)，总显存需求翻倍，需调整TP=2或启用GQA压缩

## Corrected Claim

边界条件：当KV heads < TP size (4)时，vLLM采用复制策略而非切分，单卡KV占用变为 5KB (而非1.25KB)，总显存需求翻倍，需调整TP=2或启用GQA压缩

## Evidence

先验知识/题面给定，逻辑校验通过：当KV头数小于TP大小时，无法进一步切分，必须复制KV Cache到所有GPU，导致单卡KV占用从 N/TP 变为 N，即 1.25KB * 4 = 5KB，总显存需求确实翻倍。
