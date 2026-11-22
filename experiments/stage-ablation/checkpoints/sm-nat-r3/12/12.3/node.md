# N302: ε_update 的量化定义：ε_update = (Σ_{i∈S_LRU} r_i * S_i * P_invalid(i)) / (Σ_{i∈S_LRU} 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N107

## Claim

ε_update 的量化定义：ε_update = (Σ_{i∈S_LRU} r_i * S_i * P_invalid(i)) / (Σ_{i∈S_LRU} r_i * S_i)，其中 P_invalid(i) = 1 - exp(-λ_update * T_res(i))，T_res(i) 为对象 i 在 LRU 中的驻留时间，需结合 N71/N72 的失效概率公式进行加权计算。

## Corrected Claim

ε_update 的量化定义：ε_update = (Σ_{i∈S_LRU} r_i * S_i * P_invalid(i)) / (Σ_{i∈S_LRU} r_i * S_i)，其中 P_invalid(i) = 1 - exp(-λ_update * T_res(i))，T_res(i) 为对象 i 在 LRU 中的驻留时间，需结合 N71/N72 的失效概率公式进行加权计算。

## Evidence

先验知识/题面给定，逻辑校验通过
