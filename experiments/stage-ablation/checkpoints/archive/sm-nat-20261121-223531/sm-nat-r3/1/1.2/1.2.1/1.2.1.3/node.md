# N99: h_min 对热度分布长尾程度的影响：Pareto(β=0.9) 的尾指数固定，h_min 仅缩放整体热度，不改变相对长尾程度，但影响绝对请求数分配，h_min

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

h_min 对热度分布长尾程度的影响：Pareto(β=0.9) 的尾指数固定，h_min 仅缩放整体热度，不改变相对长尾程度，但影响绝对请求数分配，h_min 每增加 1%，总请求数增加 1% [待核验]。

## Corrected Claim

h_min 对热度分布长尾程度的影响：Pareto(β=0.9) 的尾指数固定，h_min 仅缩放整体热度，不改变相对长尾程度，但影响绝对请求数分配，h_min 每增加 1%，总请求数增加 1% [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布中尾指数β决定形状（长尾程度），h_min作为尺度参数仅线性缩放整体数值，不改变相对分布形态；总请求数与尺度参数成正比，故h_min增加1%导致总请求数增加1%。
