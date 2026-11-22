# N59: 稳态命中率 H_steady 的下界：在容量 K > N 且无更新时，H_steady = 1 - (N_miss / N_total)，其中 N_miss 为

- **status**: verified
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

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache hit rate lower bound full capacity no updates
