# N266: C_infra_self 的具体计算：C_infra_self = (N_pop * (C_server_pop + C_storage_pop + C_net

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

C_infra_self 的具体计算：C_infra_self = (N_pop * (C_server_pop + C_storage_pop + C_network_pop)) / 5 / 12，其中 N_pop=10，需代入单POP硬件月均折旧成本（参考 N127 父节点中的服务器/存储单价），并考虑 5 年折旧期。

## Corrected Claim

C_infra_self 的具体计算：C_infra_self = (N_pop * (C_server_pop + C_storage_pop + C_network_pop)) / 5 / 12，其中 N_pop=10，需代入单POP硬件月均折旧成本（参考 N127 父节点中的服务器/存储单价），并考虑 5 年折旧期。

## Evidence

先验知识/题面给定，逻辑校验通过
