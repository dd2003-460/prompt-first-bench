# N137: P_rec_7d 的计算公式：P_rec_7d = Σ_{i∈S_7d} (P_i * w_sim_i) / Σ_{i∈S_7d} w_sim_i，其中 S_7

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N39

## Claim

P_rec_7d 的计算公式：P_rec_7d = Σ_{i∈S_7d} (P_i * w_sim_i) / Σ_{i∈S_7d} w_sim_i，其中 S_7d 为过去7天成交且相似度 sim(i, target) > 0.8 的商品集合，w_sim_i 基于 N70 定义的相似度函数

## Corrected Claim

P_rec_7d 的计算公式：P_rec_7d = Σ_{i∈S_7d} (P_i * w_sim_i) / Σ_{i∈S_7d} w_sim_i，其中 S_7d 为过去7天成交且相似度 sim(i, target) > 0.8 的商品集合，w_sim_i 基于 N70 定义的相似度函数

## Evidence

先验知识/题面给定，逻辑校验通过
