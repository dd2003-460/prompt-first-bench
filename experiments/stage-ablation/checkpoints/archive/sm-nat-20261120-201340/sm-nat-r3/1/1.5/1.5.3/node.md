# N44: LRU 稳态字节命中率下界 H_byte_LRU_lower = (R_total * H_req(k) * E[S | Rank_r ≤ k]) / (R_t

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

LRU 稳态字节命中率下界 H_byte_LRU_lower = (R_total * H_req(k) * E[S | Rank_r ≤ k]) / (R_total * E[S]) = H_req(k) * (E[S | Rank_r ≤ k] / E[S])，其中 H_req(k) 由 N11 给出，E[S | Rank_r ≤ k] / E[S] 由 N29 给出的修正系数决定；该公式将命中率分解为请求覆盖率和大小加权因子两部分。

## Corrected Claim

LRU 稳态字节命中率下界 H_byte_LRU_lower = (R_total * H_req(k) * E[S | Rank_r ≤ k]) / (R_total * E[S]) = H_req(k) * (E[S | Rank_r ≤ k] / E[S])，其中 H_req(k) 由 N11 给出，E[S | Rank_r ≤ k] / E[S] 由 N29 给出的修正系数决定；该公式将命中率分解为请求覆盖率和大小加权因子两部分。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合概率论全期望公式及命中率定义，量纲一致，分解逻辑自洽。
