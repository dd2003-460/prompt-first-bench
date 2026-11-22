# N23: 缓存容量利用率约束：在 128GB 内存和 10 万对象规模下，需验证 K_max * E[S] ≤ C，若 K_max 由热度分布前缀决定（即缓存最热门的 K

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

缓存容量利用率约束：在 128GB 内存和 10 万对象规模下，需验证 K_max * E[S] ≤ C，若 K_max 由热度分布前缀决定（即缓存最热门的 K 个对象），则 K 需满足 ∑_{i=1}^K S_i ≤ 128GB，此约束决定了 LRU 实际能驻留的最大对象集合边界。

## Corrected Claim

缓存容量利用率约束：在 128GB 内存和 10 万对象规模下，需验证 K_max * E[S] ≤ C，若 K_max 由热度分布前缀决定（即缓存最热门的 K 个对象），则 K 需满足 ∑_{i=1}^K S_i ≤ 128GB，此约束决定了 LRU 实际能驻留的最大对象集合边界。

## Evidence

父节点级核验未通过：不完备（子节点1正确验证了约束的非绑定性（边界条件），子节点2基于此结论推导对命中率下界的影响（后果/修正），两者逻辑上正交且互补。但父节点核心是‘约束本身的定义与验证’，子节点2过度延伸到了‘命中率公式修正’这一下游影响，超出了父节点‘约束验证’的范围，导致完备性覆盖偏差（未完整覆盖约束的一般性定义，而是直接跳到了特定参数下的后果）。）

## Search Query

LRU cache capacity constraint formula 128GB memory object size
