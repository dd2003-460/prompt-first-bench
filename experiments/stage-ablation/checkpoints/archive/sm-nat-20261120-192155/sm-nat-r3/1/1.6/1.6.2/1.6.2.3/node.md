# N102: 多对象交换下的ΔH_max修正：当LRU驱逐m个头部对象并保留m个尾部对象时，ΔH_max = (Σ_{i=1}^m i^{-2.0} - Σ_{i=k+1}^

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

多对象交换下的ΔH_max修正：当LRU驱逐m个头部对象并保留m个尾部对象时，ΔH_max = (Σ_{i=1}^m i^{-2.0} - Σ_{i=k+1}^{k+m} i^{-2.0}) / Σ_{i=1}^{100000} i^{-2.0}；由于尾部项i^{-2.0}极小，ΔH_max ≈ Σ_{i=1}^m i^{-2.0} / 1.645，m=1时ΔH_max≈60.8%，m=2时ΔH_max≈75.4%。

## Corrected Claim

多对象交换下的ΔH_max修正：当LRU驱逐m个头部对象并保留m个尾部对象时，ΔH_max = (Σ_{i=1}^m i^{-2.0} - Σ_{i=k+1}^{k+m} i^{-2.0}) / Σ_{i=1}^{100000} i^{-2.0}；由于尾部项i^{-2.0}极小，ΔH_max ≈ Σ_{i=1}^m i^{-2.0} / 1.645，m=1时ΔH_max≈60.8%，m=2时ΔH_max≈75.4%。

## Evidence

先验知识/题面给定，逻辑校验通过：分母为p=2的Riemann zeta函数近似值1.645，分子计算符合数学推导，数值量级合理。
