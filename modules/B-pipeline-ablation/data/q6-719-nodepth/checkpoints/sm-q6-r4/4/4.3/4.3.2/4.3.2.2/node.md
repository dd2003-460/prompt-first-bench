# N356: 热对象数量 N_hot(H) 的估算模型：基于 Zipf 分布，N_hot(H) ≈ N_total_objects * (1/H)^(1/α-1)，其中 α 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

热对象数量 N_hot(H) 的估算模型：基于 Zipf 分布，N_hot(H) ≈ N_total_objects * (1/H)^(1/α-1)，其中 α 为 Zipf 指数（典型值 1.0-1.2），N_total_objects 为平台总对象数，该公式决定了存储压力与阈值的关系。

## Corrected Claim

热对象数量 N_hot(H) 的估算模型：基于 Zipf 分布，N_hot(H) ≈ N_total_objects * (1/H)^(1/α-1)，其中 α 为 Zipf 指数（典型值 1.0-1.2），N_total_objects 为平台总对象数，该公式决定了存储压力与阈值的关系。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Zipf distribution cache hit rate threshold calculation
