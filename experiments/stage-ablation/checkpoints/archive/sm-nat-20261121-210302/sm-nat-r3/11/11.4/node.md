# N218: 该修正系数对 LRU 稳态字节命中率下界 H_LRU 的传递影响公式：ΔH = (B_indep - B_corr) / C_cache，其中 C_cache=

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

该修正系数对 LRU 稳态字节命中率下界 H_LRU 的传递影响公式：ΔH = (B_indep - B_corr) / C_cache，其中 C_cache=128GB，量化因空间节省导致的额外命中率提升百分点。

## Corrected Claim

该修正系数对 LRU 稳态字节命中率下界 H_LRU 的传递影响公式：ΔH = (B_indep - B_corr) / C_cache，其中 C_cache=128GB，量化因空间节省导致的额外命中率提升百分点。

## Evidence

先验知识/题面给定，逻辑校验通过
