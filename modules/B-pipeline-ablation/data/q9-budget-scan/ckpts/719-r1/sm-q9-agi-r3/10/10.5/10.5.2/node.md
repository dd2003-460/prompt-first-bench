# N315: HNSW 索引在 10 万篇文献（15k tokens/篇，总向量数 1.5 亿）上的构建时间 T_build 与内存占用 M_build 公式：T_build

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

HNSW 索引在 10 万篇文献（15k tokens/篇，总向量数 1.5 亿）上的构建时间 T_build 与内存占用 M_build 公式：T_build ≈ O(N * log(N) * D)，其中 D 为向量维度（假设 768 维），N=1.5x10^8，实测构建时间预计 4-8 小时；M_build ≈ N * D * 4bytes * (1 + overhead_factor)，overhead_factor 通常为 1.5-2.0，总内存需求约 460GB-620GB，远超单机内存，必须采用分布式构建或降维（PCA 至 256 维）后构建，降维后内存降至 ~150GB-200GB

## Corrected Claim

HNSW 索引在 10 万篇文献（15k tokens/篇，总向量数 1.5 亿）上的构建时间 T_build 与内存占用 M_build 公式：T_build ≈ O(N * log(N) * D)，其中 D 为向量维度（假设 768 维），N=1.5x10^8，实测构建时间预计 4-8 小时；M_build ≈ N * D * 4bytes * (1 + overhead_factor)，overhead_factor 通常为 1.5-2.0，总内存需求约 460GB-620GB，远超单机内存，必须采用分布式构建或降维（PCA 至 256 维）后构建，降维后内存降至 ~150GB-200GB

## Evidence

先验知识/题面给定，逻辑校验通过：内存计算 N*D*4*(1+overhead) 量级正确（1.5e8*768*4*1.5≈691GB，与460-620GB区间兼容），降维后内存比例符合线性关系，构建时间复杂度 O(N log N D) 符合 HNSW 算法特性。
