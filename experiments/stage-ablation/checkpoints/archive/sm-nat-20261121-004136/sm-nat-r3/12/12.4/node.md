# N184: LFU 相对于 LRU 在更新场景下的增益来源量化：增益并非来自抵抗更新，而是来自静态命中率差异。在容量充足（H_static=1）且更新率相同的情况下，H_L

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

LFU 相对于 LRU 在更新场景下的增益来源量化：增益并非来自抵抗更新，而是来自静态命中率差异。在容量充足（H_static=1）且更新率相同的情况下，H_LFU_eff ≈ H_LRU_eff，增益趋近于 0。若考虑‘更新导致热度分布漂移’，LFU 的频率老化机制（如衰减因子 λ_decay）可能导致其滞后于热度变化，反而降低命中率。量化：Δ_H_update = H_LFU_eff - H_LRU_eff ≈ 0，前提是两者对更新的响应速度相同。

## Corrected Claim

LFU 相对于 LRU 在更新场景下的增益来源量化：增益并非来自抵抗更新，而是来自静态命中率差异。在容量充足（H_static=1）且更新率相同的情况下，H_LFU_eff ≈ H_LRU_eff，增益趋近于 0。若考虑‘更新导致热度分布漂移’，LFU 的频率老化机制（如衰减因子 λ_decay）可能导致其滞后于热度变化，反而降低命中率。量化：Δ_H_update = H_LFU_eff - H_LRU_eff ≈ 0，前提是两者对更新的响应速度相同。

## Evidence

先验知识/题面给定，逻辑校验通过：在静态命中率相同且更新响应速度一致的假设下，LFU与LRU的有效命中率差异趋近于0符合缓存替换算法的基本理论推导。
