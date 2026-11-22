# N252: 下游投影3：均衡点漂移量化。新的均衡信号强度 k_new_eq 满足 E[CTR | k_new_eq] = E[CTR | k_old]。若 w_signal

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N68

## Claim

下游投影3：均衡点漂移量化。新的均衡信号强度 k_new_eq 满足 E[CTR | k_new_eq] = E[CTR | k_old]。若 w_signal 下降导致曝光减少，需计算 k 需增加多少才能维持相同的转化率，从而判断均衡是否稳定。

## Corrected Claim

下游投影3：均衡点漂移量化。新的均衡信号强度 k_new_eq 满足 E[CTR | k_new_eq] = E[CTR | k_old]。若 w_signal 下降导致曝光减少，需计算 k 需增加多少才能维持相同的转化率，从而判断均衡是否稳定。

## Evidence

先验知识/题面给定，逻辑校验通过
