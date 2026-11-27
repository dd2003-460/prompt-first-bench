# N9: 工作点1（高性低成）：假设对象大小独立于热度（ρ=0），计算纯热度驱动的 LRU 命中率下界 H_LRU_independent = ∫_0^{C/S_avg}

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

工作点1（高性低成）：假设对象大小独立于热度（ρ=0），计算纯热度驱动的 LRU 命中率下界 H_LRU_independent = ∫_0^{C/S_avg} f_rank(r) dr，其中 C/S_avg 为可缓存对象数量上限。

## Corrected Claim

工作点1（高性低成）：假设对象大小独立于热度（ρ=0），计算纯热度驱动的 LRU 命中率下界 H_LRU_independent = ∫_0^{C/S_avg} f_rank(r) dr，其中 C/S_avg 为可缓存对象数量上限。

## Evidence

先验知识/题面给定，逻辑校验通过
