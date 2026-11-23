# N207: 源站并发实例数 K_origin 的部署策略：K_origin 取决于源站架构（单体 vs 集群），若为集群，K_origin 为总处理能力单元数；通常源站配置

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

源站并发实例数 K_origin 的部署策略：K_origin 取决于源站架构（单体 vs 集群），若为集群，K_origin 为总处理能力单元数；通常源站配置 2-5 台高配服务器（每台 16-32 核），故 K_origin ∈ [2, 5] 或按核心数折算的等效并发度

## Corrected Claim

源站并发实例数 K_origin 的部署策略：K_origin 取决于源站架构（单体 vs 集群），若为集群，K_origin 为总处理能力单元数；通常源站配置 2-5 台高配服务器（每台 16-32 核），故 K_origin ∈ [2, 5] 或按核心数折算的等效并发度

## Evidence

先验知识/题面给定，逻辑校验通过
