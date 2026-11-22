# N140: 筛选强度 S 的期望值表达式：E[S] = 1 - p_consult = 1 - Φ((V - P_ask)/σ)，表明 S 是 P_ask 的单调递增函数，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N42

## Claim

筛选强度 S 的期望值表达式：E[S] = 1 - p_consult = 1 - Φ((V - P_ask)/σ)，表明 S 是 P_ask 的单调递增函数，且当 P_ask 接近 V 时 S 趋近于 0.5。

## Corrected Claim

筛选强度 S 的期望值表达式：E[S] = 1 - p_consult = 1 - Φ((V - P_ask)/σ)，表明 S 是 P_ask 的单调递增函数，且当 P_ask 接近 V 时 S 趋近于 0.5。

## Evidence

先验知识/题面给定，逻辑校验通过：S=1-Φ((V-P_ask)/σ) 中，P_ask 增大导致 (V-P_ask)/σ 减小，Φ 值减小，故 S 单调递增；当 P_ask=V 时，Φ(0)=0.5，S=0.5，推导自洽。
