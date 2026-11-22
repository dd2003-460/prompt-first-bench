# N9: LRU 稳态字节命中率下界的经典公式：H_byte_LRU ≥ 1 - (C / W_eff)，其中 C 是缓存容量，W_eff 是有效工作集大小；在 Pare

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

LRU 稳态字节命中率下界的经典公式：H_byte_LRU ≥ 1 - (C / W_eff)，其中 C 是缓存容量，W_eff 是有效工作集大小；在 Pareto 负载下，W_eff 由累积字节数达到 C 时的对象排名 K 决定：Σ_{k=1}^{K} S_k = C，且命中率近似为 Σ_{k=1}^{K} R_k / Σ_{k=1}^{N} R_k

## Corrected Claim

LRU 稳态字节命中率下界的经典公式：H_byte_LRU ≥ 1 - (C / W_eff)，其中 C 是缓存容量，W_eff 是有效工作集大小；在 Pareto 负载下，W_eff 由累积字节数达到 C 时的对象排名 K 决定：Σ_{k=1}^{K} S_k = C，且命中率近似为 Σ_{k=1}^{K} R_k / Σ_{k=1}^{N} R_k

## Evidence

父节点级核验未通过：不完备（父节点包含两个核心数学组件：1) 基础命中率公式 H >= 1 - C/W_eff；2) Pareto 负载下 W_eff 的具体计算逻辑（基于累积字节数 C 确定排名 K，进而计算命中率）。子节点仅聚焦于 W_eff 的定义修正和验证，完全缺失了父节点中关于 Pareto 负载下如何通过对象排名 K 和累积字节数 ΣS_k 来确定 W_eff 或计算命中率的关键推导过程。因此，子节点未能覆盖父节点的所有关键方面，完备性不足。）

## Search Query

LRU cache hit rate lower bound Pareto distribution
