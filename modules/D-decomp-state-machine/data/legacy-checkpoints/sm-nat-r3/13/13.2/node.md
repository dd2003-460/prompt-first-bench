# N304: P_req_LFU 与 P_req_LRU 的精确计算：P_req_LFU = Σ_{i∈S_LFU} r_i / Σ_{all} r_i，P_req_LRU 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N108

## Claim

P_req_LFU 与 P_req_LRU 的精确计算：P_req_LFU = Σ_{i∈S_LFU} r_i / Σ_{all} r_i，P_req_LRU = Σ_{i∈S_LRU} r_i / Σ_{all} r_i，其中 r_i 服从 Pareto(β=0.9)；需分别计算两个集合的请求概率覆盖率差异。

## Corrected Claim

P_req_LFU 与 P_req_LRU 的精确计算：P_req_LFU = Σ_{i∈S_LFU} r_i / Σ_{all} r_i，P_req_LRU = Σ_{i∈S_LRU} r_i / Σ_{all} r_i，其中 r_i 服从 Pareto(β=0.9)；需分别计算两个集合的请求概率覆盖率差异。

## Evidence

先验知识/题面给定，逻辑校验通过
