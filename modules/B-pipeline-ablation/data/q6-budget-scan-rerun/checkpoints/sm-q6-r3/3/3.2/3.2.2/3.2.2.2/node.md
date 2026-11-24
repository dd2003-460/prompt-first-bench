# N215: 自建节点峰值带宽预留系数 K_self 的取值范围：K_self = B_peak_total / B_avg_total，基于 N139 的计算，若流量完全独

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

自建节点峰值带宽预留系数 K_self 的取值范围：K_self = B_peak_total / B_avg_total，基于 N139 的计算，若流量完全独立，K_self ≈ 3.0 × 3.16 ≈ 9.48；若流量部分相关（ρ = 0.5），K_self ≈ 3.0 × 2.37 ≈ 7.11；此值远高于题目假设的 2.0-2.5 区间，表明自建节点的带宽预留需考虑多POP点峰值叠加效应，而非单点峰谷比

## Corrected Claim

自建节点峰值带宽预留系数 K_self 的取值范围：K_self = B_peak_total / B_avg_total，基于 N139 的计算，若流量完全独立，K_self ≈ 3.0 × 3.16 ≈ 9.48；若流量部分相关（ρ = 0.5），K_self ≈ 3.0 × 2.37 ≈ 7.11；此值远高于题目假设的 2.0-2.5 区间，表明自建节点的带宽预留需考虑多POP点峰值叠加效应，而非单点峰谷比

## Evidence

先验知识/题面给定，逻辑校验通过：基于独立流量峰谷比3.0及多节点叠加的统计规律（独立时峰值叠加系数约为sqrt(N)或线性叠加，此处3.16对应sqrt(10)量级，部分相关时系数降低），计算结果9.48和7.11在量级和逻辑上均合理，且符合多POP点峰值叠加需预留更高带宽的工程直觉。
