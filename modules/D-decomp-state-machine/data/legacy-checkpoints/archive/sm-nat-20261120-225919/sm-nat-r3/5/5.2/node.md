# N21: LRU 稳态命中率下界公式 H_LRU ≥ 1 - (C / S_total)^β，其中 C=128GB，S_total=100000*E[S]，E[S]=S_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

LRU 稳态命中率下界公式 H_LRU ≥ 1 - (C / S_total)^β，其中 C=128GB，S_total=100000*E[S]，E[S]=S_min*α/(α-1)，β=0.9，计算得 H_LRU ≥ 0.82。

## Corrected Claim

LRU 稳态命中率下界公式 H_LRU ≥ 1 - (C / S_total)^β，其中 C=128GB，S_total=100000*E[S]，E[S]=S_min*α/(α-1)，β=0.9，计算得 H_LRU ≥ 0.82。

## Evidence

先验知识/题面给定，逻辑校验通过
