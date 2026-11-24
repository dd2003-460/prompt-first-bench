# N41: D2 成本排序判据为每千请求的总成本 C_total_per_1000req = (C_infra + C_bandwidth + C_ops) / Q_tot

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

D2 成本排序判据为每千请求的总成本 C_total_per_1000req = (C_infra + C_bandwidth + C_ops) / Q_total * 1000，其中 C_infra 为基础设施成本，C_bandwidth 为带宽成本，C_ops 为运维成本。

## Corrected Claim

D2 成本排序判据为每千请求的总成本 C_total_per_1000req = (C_infra + C_bandwidth + C_ops) / Q_total * 1000，其中 C_infra 为基础设施成本，C_bandwidth 为带宽成本，C_ops 为运维成本。

## Evidence

先验知识/题面给定，逻辑校验通过
