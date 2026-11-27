# N71: 对象平均驻留时间 T_resident 的解析近似：T_resident ≈ (C_norm * N) / (λ_avg * (1 - P_eviction))

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

对象平均驻留时间 T_resident 的解析近似：T_resident ≈ (C_norm * N) / (λ_avg * (1 - P_eviction))，其中 λ_avg=500/天，P_eviction 为对象在驻留期内被驱逐的概率，需结合 LRU 队列长度分布求解。

## Corrected Claim

对象平均驻留时间 T_resident 的解析近似：T_resident ≈ (C_norm * N) / (λ_avg * (1 - P_eviction))，其中 λ_avg=500/天，P_eviction 为对象在驻留期内被驱逐的概率，需结合 LRU 队列长度分布求解。

## Evidence

先验知识/题面给定，逻辑校验通过
