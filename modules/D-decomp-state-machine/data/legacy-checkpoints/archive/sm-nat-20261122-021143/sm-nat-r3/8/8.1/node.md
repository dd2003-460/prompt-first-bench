# N150: Belady 最优算法在字节命中率下的理论上限 H_opt 计算：H_opt = (Σ_{k=1}^{K} R_k * S_k) / (Σ_{k=1}^{N} 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59, N60

## Claim

Belady 最优算法在字节命中率下的理论上限 H_opt 计算：H_opt = (Σ_{k=1}^{K} R_k * S_k) / (Σ_{k=1}^{N} R_k * S_k)，其中 K 由缓存容量 C=128GB 和对象大小分布 S_k ∝ k^{-0.1} 决定（K≈32000），需计算该比值以作为 LFU 增益的基准上限

## Corrected Claim

Belady 最优算法在字节命中率下的理论上限 H_opt 计算：H_opt = (Σ_{k=1}^{K} R_k * S_k) / (Σ_{k=1}^{N} R_k * S_k)，其中 K 由缓存容量 C=128GB 和对象大小分布 S_k ∝ k^{-0.1} 决定（K≈32000），需计算该比值以作为 LFU 增益的基准上限

## Evidence

先验知识/题面给定，逻辑校验通过：Belady最优算法（OPT）在字节命中率下的理论上限公式定义正确，且K值由缓存容量与对象大小分布推导符合逻辑。
