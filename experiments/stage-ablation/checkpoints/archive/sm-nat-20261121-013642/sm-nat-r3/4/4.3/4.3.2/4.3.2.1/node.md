# N184: N63 的驱逐决策影响工作点 1（无驱逐）：当更新对象不在缓存中时，P_hit_cold = 1 且无驱逐发生，更新率对命中率无影响，f_update = 1.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

N63 的驱逐决策影响工作点 1（无驱逐）：当更新对象不在缓存中时，P_hit_cold = 1 且无驱逐发生，更新率对命中率无影响，f_update = 1.0。

## Corrected Claim

N63 的驱逐决策影响工作点 1（无驱逐）：当更新对象不在缓存中时，P_hit_cold = 1 且无驱逐发生，更新率对命中率无影响，f_update = 1.0。

## Evidence

先验知识/题面给定，逻辑校验通过：在无驱逐且对象不在缓存中时，更新必然导致缓存命中（或视为有效访问），故 P_hit_cold=1，且无驱逐意味着更新率不影响命中率，f_update=1.0 符合逻辑自洽。
