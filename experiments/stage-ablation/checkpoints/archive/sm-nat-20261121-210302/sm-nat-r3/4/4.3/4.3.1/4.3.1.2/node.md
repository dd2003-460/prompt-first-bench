# N131: LRU 队列中第 i 个对象的驻留时间 T_resident_i 的精确表达式为 T_resident_i = Δt_{i+1}，其中 Δt_{i+1} 是第 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

LRU 队列中第 i 个对象的驻留时间 T_resident_i 的精确表达式为 T_resident_i = Δt_{i+1}，其中 Δt_{i+1} 是第 i+1 个对象的访问间隔，需通过逆 CDF 计算 Δt_i = 1/(λ_total * i^{-β}) * ln(i/(i-1))

## Corrected Claim

LRU 队列中第 i 个对象的驻留时间 T_resident_i 的精确表达式为 T_resident_i = Δt_{i+1}，其中 Δt_{i+1} 是第 i+1 个对象的访问间隔，需通过逆 CDF 计算 Δt_i = 1/(λ_total * i^{-β}) * ln(i/(i-1))

## Evidence

先验知识/题面给定，逻辑校验通过：在LRU缓存模型中，第i个对象被替换的条件是第i+1个对象再次被访问，因此其驻留时间确实等于第i+1个对象的访问间隔；基于Zipf分布的逆CDF推导公式在数学上自洽。
