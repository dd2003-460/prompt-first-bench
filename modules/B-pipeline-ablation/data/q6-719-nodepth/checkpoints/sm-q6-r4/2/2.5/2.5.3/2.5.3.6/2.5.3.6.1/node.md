# N626: 缓存扩容的边际成本 C_cache_upgrade 由新增存储硬件折旧与 IOPS 性能提升成本构成，公式为 C_cache_upgrade = (ΔN_sto

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N207

## Claim

缓存扩容的边际成本 C_cache_upgrade 由新增存储硬件折旧与 IOPS 性能提升成本构成，公式为 C_cache_upgrade = (ΔN_storage * C_storage_marginal) + (ΔIOPS_requirement / IOPS_per_node * C_node_perf)，其中 ΔN_storage 为热数据增量，C_storage_marginal ≈ ¥0.8/GB/月，IOPS 需求增量取决于对象大小 s_avg 的减少比例。

## Corrected Claim

缓存扩容的边际成本 C_cache_upgrade 由新增存储硬件折旧与 IOPS 性能提升成本构成，公式为 C_cache_upgrade = (ΔN_storage * C_storage_marginal) + (ΔIOPS_requirement / IOPS_per_node * C_node_perf)，其中 ΔN_storage 为热数据增量，C_storage_marginal ≈ ¥0.8/GB/月，IOPS 需求增量取决于对象大小 s_avg 的减少比例。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN cache expansion marginal cost storage IOPS pricing model
