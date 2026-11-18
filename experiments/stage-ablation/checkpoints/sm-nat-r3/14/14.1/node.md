# N199: T_avg_residency 在稳态下近似为 C / (S_avg * R_miss)，其中 C=128GB，S_avg 为缓存内对象的平均大小（受 ρ=-0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

T_avg_residency 在稳态下近似为 C / (S_avg * R_miss)，其中 C=128GB，S_avg 为缓存内对象的平均大小（受 ρ=-0.3 影响，约为 9.35 KB），R_miss 为平均未命中请求率。

## Corrected Claim

T_avg_residency 在稳态下近似为 C / (S_avg * R_miss)，其中 C=128GB，S_avg 为缓存内对象的平均大小（受 ρ=-0.3 影响，约为 9.35 KB），R_miss 为平均未命中请求率。

## Evidence

先验知识/题面给定，逻辑校验通过
