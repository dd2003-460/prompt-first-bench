# N132: 每个选定 POP 点（如广州 POP）所覆盖的服务区域集合 $R_k$ 及其对应的流量权重 $W_k = \sum_{i \in R_k} P_i$，用于后续计

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

每个选定 POP 点（如广州 POP）所覆盖的服务区域集合 $R_k$ 及其对应的流量权重 $W_k = \sum_{i \in R_k} P_i$，用于后续计算各 POP 点的独立负载率 λ_k 和带宽需求 B_k，确保单点负载不超过容量上限（如 80% 利用率）。

## Corrected Claim

每个选定 POP 点（如广州 POP）所覆盖的服务区域集合 $R_k$ 及其对应的流量权重 $W_k = \sum_{i \in R_k} P_i$，用于后续计算各 POP 点的独立负载率 λ_k 和带宽需求 B_k，确保单点负载不超过容量上限（如 80% 利用率）。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述定义了基于区域流量加权的负载计算模型，数学逻辑自洽，且80%利用率作为容量上限阈值符合工程惯例。
