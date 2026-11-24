# N393: 源站扩容需求公式 N_servers_new = ceil(N_servers_base * (1 - H_new) / (1 - H_base) / Redu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N130, N131, N132

## Claim

源站扩容需求公式 N_servers_new = ceil(N_servers_base * (1 - H_new) / (1 - H_base) / Redundancy_Factor)，其中 Redundancy_Factor 为源站冗余系数（通常 1.5-2.0）；当 H 从 90% 降至 72% 时，回源率从 10% 升至 28%，负载增加 2.8 倍，若 N_servers_base = 10，Redundancy_Factor = 1.5，则 N_servers_new = ceil(10 * 2.8 / 1.5) = ceil(18.67) = 19 台。

## Corrected Claim

源站扩容需求公式 N_servers_new = ceil(N_servers_base * (1 - H_new) / (1 - H_base) / Redundancy_Factor)，其中 Redundancy_Factor 为源站冗余系数（通常 1.5-2.0）；当 H 从 90% 降至 72% 时，回源率从 10% 升至 28%，负载增加 2.8 倍，若 N_servers_base = 10，Redundancy_Factor = 1.5，则 N_servers_new = ceil(10 * 2.8 / 1.5) = ceil(18.67) = 19 台。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合CDN回源负载线性关系，数值计算 ceil(10 * 0.28/0.10 / 1.5) = ceil(18.666...) = 19 正确。

## Search Query

CDN origin server scaling cache hit rate drop
