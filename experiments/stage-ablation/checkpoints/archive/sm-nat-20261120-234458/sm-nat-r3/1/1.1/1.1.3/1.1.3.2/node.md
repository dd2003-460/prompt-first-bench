# N73: 容量受限下的 LRU 稳态字节命中率下界 H_LRU_lower 需通过积分计算：H_LRU_lower = (Σ_{i∈Top_K} q_i * s_i) /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

容量受限下的 LRU 稳态字节命中率下界 H_LRU_lower 需通过积分计算：H_LRU_lower = (Σ_{i∈Top_K} q_i * s_i) / (Σ_{i=1}^{N} q_i * s_i)，其中 Top_K 为 LRU 保留的 K 个对象（通常近似为频率最高的 K 个），K=17,650，具体数值需数值积分求解。

## Corrected Claim

容量受限下的 LRU 稳态字节命中率下界 H_LRU_lower 需通过积分计算：H_LRU_lower = (Σ_{i∈Top_K} q_i * s_i) / (Σ_{i=1}^{N} q_i * s_i)，其中 Top_K 为 LRU 保留的 K 个对象（通常近似为频率最高的 K 个），K=17,650，具体数值需数值积分求解。

## Evidence

先验知识/题面给定，逻辑校验通过
