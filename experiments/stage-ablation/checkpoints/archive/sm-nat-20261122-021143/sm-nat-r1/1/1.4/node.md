# N9: LRU 稳态字节命中率下界的经典公式：H_byte_LRU ≥ 1 - (C / W_eff)，其中 C 是缓存容量，W_eff 是有效工作集大小；在 Pare

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LRU 稳态字节命中率下界的经典公式：H_byte_LRU ≥ 1 - (C / W_eff)，其中 C 是缓存容量，W_eff 是有效工作集大小；在 Pareto 负载下，W_eff 由累积字节数达到 C 时的对象排名 K 决定：Σ_{k=1}^{K} S_k = C，且命中率近似为 Σ_{k=1}^{K} R_k / Σ_{k=1}^{N} R_k

## Corrected Claim

LRU 稳态字节命中率下界的经典公式：H_byte_LRU ≥ 1 - (C / W_eff)，其中 C 是缓存容量，W_eff 是有效工作集大小；在 Pareto 负载下，W_eff 由累积字节数达到 C 时的对象排名 K 决定：Σ_{k=1}^{K} S_k = C，且命中率近似为 Σ_{k=1}^{K} R_k / Σ_{k=1}^{N} R_k

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache hit rate lower bound Pareto distribution
