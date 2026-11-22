# N91: 若缓存容量足以容纳所有对象（k_max=N），则 N_byte = D_byte，H_byte = 100%。但若存在超大对象导致部分对象无法缓存，需剔除这些对

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

若缓存容量足以容纳所有对象（k_max=N），则 N_byte = D_byte，H_byte = 100%。但若存在超大对象导致部分对象无法缓存，需剔除这些对象。假设 1% 的对象（最大）占据了 50% 的字节流量，则 H_byte ≤ 1 - 0.5 * (1 - hit_rate_of_large_objects)。

## Corrected Claim

若缓存容量足以容纳所有对象（k_max=N），则 N_byte = D_byte，H_byte = 100%。但若存在超大对象导致部分对象无法缓存，需剔除这些对象。假设 1% 的对象（最大）占据了 50% 的字节流量，则 H_byte ≤ 1 - 0.5 * (1 - hit_rate_of_large_objects)。

## Evidence

父节点级核验未通过：非正交, 不完备（子节点与父节点存在严重逻辑错位。父节点讨论的是静态容量限制下的字节命中率上限（H_byte），而子节点1引入了动态失效（时间维度），子节点2讨论的是剔除冷对象后的命中率，两者均未直接回应父节点中关于'超大对象导致无法缓存需剔除'这一特定场景的推导。此外，子节点1（更新失效）与父节点（容量/对象大小）属于不同维度的约束，强行并列导致正交性破裂。）
