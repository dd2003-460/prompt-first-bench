# N142: 流式缓存 vs 存储缓存的边界条件：定义流式比 S_ratio = T_obj_life / T_res。若 S_ratio > 1000，缓存为纯流式，更新逻

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

流式缓存 vs 存储缓存的边界条件：定义流式比 S_ratio = T_obj_life / T_res。若 S_ratio > 1000，缓存为纯流式，更新逻辑可忽略；若 S_ratio < 10，缓存为存储型，更新逻辑至关重要。本题 S_ratio = 100天 / 0.0023天 ≈ 43,000 >> 1000，确认为纯流式。因此，ETag 机制的主要作用是防止跨节点一致性错误，而非本地缓存失效。

## Corrected Claim

流式缓存 vs 存储缓存的边界条件：定义流式比 S_ratio = T_obj_life / T_res。若 S_ratio > 1000，缓存为纯流式，更新逻辑可忽略；若 S_ratio < 10，缓存为存储型，更新逻辑至关重要。本题 S_ratio = 100天 / 0.0023天 ≈ 43,000 >> 1000，确认为纯流式。因此，ETag 机制的主要作用是防止跨节点一致性错误，而非本地缓存失效。

## Evidence

先验知识/题面给定，逻辑校验通过：S_ratio计算正确（100/0.0023≈43478），远大于1000，符合纯流式缓存定义，ETag用于跨节点一致性符合分布式缓存原理。
