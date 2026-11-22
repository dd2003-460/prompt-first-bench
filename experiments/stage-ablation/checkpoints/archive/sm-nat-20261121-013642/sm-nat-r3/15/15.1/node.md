# N285: 修正前提错误：在 C < V_total 条件下，并非所有对象常驻。更新惩罚 f_update 不仅取决于 P(updated_before_access)，还

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N99

## Claim

修正前提错误：在 C < V_total 条件下，并非所有对象常驻。更新惩罚 f_update 不仅取决于 P(updated_before_access)，还取决于更新对象是否在缓存中。f_update = 1 - [P(updated) * P(in_cache) * P(miss_due_to_staleness)]。若更新导致对象失效，且该对象在缓存中，则命中转为未命中。

## Corrected Claim

修正前提错误：在 C < V_total 条件下，并非所有对象常驻。更新惩罚 f_update 不仅取决于 P(updated_before_access)，还取决于更新对象是否在缓存中。f_update = 1 - [P(updated) * P(in_cache) * P(miss_due_to_staleness)]。若更新导致对象失效，且该对象在缓存中，则命中转为未命中。

## Evidence

先验知识/题面给定，逻辑校验通过
