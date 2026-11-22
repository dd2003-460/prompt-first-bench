# N223: ΔH_max 的解析上界推导：ΔH_max = H_LFU - H_LRU ≤ ∫_{h_th}^{∞} (P_f_lfu(h) - P_f_lru(h)) *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N80

## Claim

ΔH_max 的解析上界推导：ΔH_max = H_LFU - H_LRU ≤ ∫_{h_th}^{∞} (P_f_lfu(h) - P_f_lru(h)) * s(h) * f_H(h) dh / E[S]，其中 P_f_lfu(h) - P_f_lru(h) 仅在 LRU 因时间局部性淘汰高频对象时为正；在稳态且访问分布平稳时，LRU 堆栈深度与频率单调相关，故 ΔH_max ≈ 0，除非存在突发访问模式打破时间局部性。

## Corrected Claim

ΔH_max 的解析上界推导：ΔH_max = H_LFU - H_LRU ≤ ∫_{h_th}^{∞} (P_f_lfu(h) - P_f_lru(h)) * s(h) * f_H(h) dh / E[S]，其中 P_f_lfu(h) - P_f_lru(h) 仅在 LRU 因时间局部性淘汰高频对象时为正；在稳态且访问分布平稳时，LRU 堆栈深度与频率单调相关，故 ΔH_max ≈ 0，除非存在突发访问模式打破时间局部性。

## Evidence

先验知识/题面给定，逻辑校验通过
