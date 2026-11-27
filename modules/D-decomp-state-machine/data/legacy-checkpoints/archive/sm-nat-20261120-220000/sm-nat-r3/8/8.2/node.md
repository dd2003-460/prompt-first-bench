# N56: 逻辑失效与物理失效的区分量化：逻辑失效（内容哈希变更但ID不变）导致缓存行标记为 stale，需重新验证，折损系数为 (1 - p_invalid * P_ve

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

逻辑失效与物理失效的区分量化：逻辑失效（内容哈希变更但ID不变）导致缓存行标记为 stale，需重新验证，折损系数为 (1 - p_invalid * P_verify_miss)，其中 P_verify_miss 为验证请求未命中的概率，通常约为 0.1；物理失效（对象ID变更）导致缓存行直接删除，折损系数为 (1 - p_invalid * P_hit_on_updated)，其中 P_hit_on_updated 约为 0.005，因此物理失效折损约为 0.99995，逻辑失效折损约为 0.999。

## Corrected Claim

逻辑失效与物理失效的区分量化：逻辑失效（内容哈希变更但ID不变）导致缓存行标记为 stale，需重新验证，折损系数为 (1 - p_invalid * P_verify_miss)，其中 P_verify_miss 为验证请求未命中的概率，通常约为 0.1；物理失效（对象ID变更）导致缓存行直接删除，折损系数为 (1 - p_invalid * P_hit_on_updated)，其中 P_hit_on_updated 约为 0.005，因此物理失效折损约为 0.99995，逻辑失效折损约为 0.999。

## Evidence

父节点级核验未通过：非正交（子节点之间存在严重的逻辑矛盾和事实错误。1. 矛盾：父节点定义物理失效折损系数为 (1 - p_invalid * P_hit_on_updated) 且 P_hit_on_updated ≈ 0.005，得出结果约为 0.99995；而子节点2声称 P_hit_on_updated = H_LRU(C) ≈ 0.95，得出结果 0.9905。两者在定义和数值上完全冲突。2. 事实错误：子节点3基于错误的子节点2数据（0.9905 vs 0.9995）得出‘物理失效更显著’的结论，这与父节点中物理失效影响极小（0.99995 vs 0.999）的结论相反，导致整体逻辑链断裂。）
