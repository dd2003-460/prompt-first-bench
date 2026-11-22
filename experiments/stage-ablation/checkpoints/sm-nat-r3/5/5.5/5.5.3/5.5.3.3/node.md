# N258: 混合更新工作点下的字节加权命中率折损因子 D_mixed = 1 - (Σ_{i∈S_LRU} p_i s_i P_invalid(i)) / (Σ_{i∈S_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

混合更新工作点下的字节加权命中率折损因子 D_mixed = 1 - (Σ_{i∈S_LRU} p_i s_i P_invalid(i)) / (Σ_{i∈S_LRU} p_i s_i)，需对 LRU 缓存中所有对象求和，计算具体数值并与 D_uniform 和 D_concentrated 对比。

## Corrected Claim

混合更新工作点下的字节加权命中率折损因子 D_mixed = 1 - (Σ_{i∈S_LRU} p_i s_i P_invalid(i)) / (Σ_{i∈S_LRU} p_i s_i)，需对 LRU 缓存中所有对象求和，计算具体数值并与 D_uniform 和 D_concentrated 对比。

## Evidence

先验知识/题面给定，逻辑校验通过
