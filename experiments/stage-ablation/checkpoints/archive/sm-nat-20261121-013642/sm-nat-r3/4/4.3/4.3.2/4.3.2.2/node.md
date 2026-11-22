# N185: N63 的驱逐决策影响工作点 2（部分驱逐）：当 50% 更新对象在缓存中且被驱逐时，P_hit_cold = 1 但缓存容量被占用，f_update ≈ 1 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

N63 的驱逐决策影响工作点 2（部分驱逐）：当 50% 更新对象在缓存中且被驱逐时，P_hit_cold = 1 但缓存容量被占用，f_update ≈ 1 - 0.5 * (更新对象字节占比)，需计算更新对象的平均大小与缓存容量的比值。

## Corrected Claim

N63 的驱逐决策影响工作点 2（部分驱逐）：当 50% 更新对象在缓存中且被驱逐时，P_hit_cold = 1 但缓存容量被占用，f_update ≈ 1 - 0.5 * (更新对象字节占比)，需计算更新对象的平均大小与缓存容量的比值。

## Evidence

先验知识/题面给定，逻辑校验通过
