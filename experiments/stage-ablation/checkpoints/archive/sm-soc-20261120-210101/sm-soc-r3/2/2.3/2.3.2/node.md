# N52: 高挂价曝光权重公式：W_high = W_base * (1 + β_signal * I_signal)，其中 I_signal 为‘近期成交’或‘高信用’信

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N12

## Claim

高挂价曝光权重公式：W_high = W_base * (1 + β_signal * I_signal)，其中 I_signal 为‘近期成交’或‘高信用’信号强度，β_signal ∈ [0.1, 0.3] 为算法对正向信号的加权系数。若 I_signal > 0.5，则 W_high 显著高于 W_base，导致短周期。

## Corrected Claim

高挂价曝光权重公式：W_high = W_base * (1 + β_signal * I_signal)，其中 I_signal 为‘近期成交’或‘高信用’信号强度，β_signal ∈ [0.1, 0.3] 为算法对正向信号的加权系数。若 I_signal > 0.5，则 W_high 显著高于 W_base，导致短周期。

## Evidence

先验知识/题面给定，逻辑校验通过
