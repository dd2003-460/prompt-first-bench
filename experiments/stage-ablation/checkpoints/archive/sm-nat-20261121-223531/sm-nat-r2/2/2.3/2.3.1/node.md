# N43: 在 N22 确定的场景下（缓存容量 1.26M 对象 > 10万对象总数），LRU 稳态字节命中率 H_LRU_base = 100%（忽略更新失效），因为所有

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

在 N22 确定的场景下（缓存容量 1.26M 对象 > 10万对象总数），LRU 稳态字节命中率 H_LRU_base = 100%（忽略更新失效），因为所有对象均驻留内存，不存在容量导致的淘汰。

## Corrected Claim

在 N22 确定的场景下（缓存容量 1.26M 对象 > 10万对象总数），LRU 稳态字节命中率 H_LRU_base = 100%（忽略更新失效），因为所有对象均驻留内存，不存在容量导致的淘汰。

## Evidence

先验知识/题面给定，逻辑校验通过：缓存容量（1.26M）远大于工作集大小（10万），且忽略更新失效，LRU 必然无淘汰，命中率 100%。
