# N59: 稳态命中率 H_steady 的下界：在容量 K > N 且无更新时，H_steady = 1 - (N_miss / N_total)，其中 N_miss 为

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

稳态命中率 H_steady 的下界：在容量 K > N 且无更新时，H_steady = 1 - (N_miss / N_total)，其中 N_miss 为必然未命中的对象数（如从未被请求的对象），N_total 为总对象数，需确定最小未命中对象数

## Corrected Claim

稳态命中率 H_steady 的下界：在容量 K > N 且无更新时，H_steady = 1 - (N_miss / N_total)，其中 N_miss 为必然未命中的对象数（如从未被请求的对象），N_total 为总对象数，需确定最小未命中对象数

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了 N_miss 的计算，未涵盖父节点中关于 H_steady 整体公式的验证、N_total 的定义确认或最终下界的推导过程，导致对父节点目标的覆盖不完备。）

## Search Query

LRU cache hit rate lower bound full capacity no updates
