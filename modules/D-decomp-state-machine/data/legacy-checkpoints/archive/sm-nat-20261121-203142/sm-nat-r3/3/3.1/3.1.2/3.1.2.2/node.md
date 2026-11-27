# N120: 数值积分计算 ΔH：对 ∫ [f_R(r|s)_LFU - f_R(r|s)_LRU] × f_S(s) ds 进行离散化求和，步长 Δs 取对象大小分位数的 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N45

## Claim

数值积分计算 ΔH：对 ∫ [f_R(r|s)_LFU - f_R(r|s)_LRU] × f_S(s) ds 进行离散化求和，步长 Δs 取对象大小分位数的 1%，积分结果即为 LFU 相对 LRU 的字节命中率增益上限，需排除容量开销影响

## Corrected Claim

数值积分计算 ΔH：对 ∫ [f_R(r|s)_LFU - f_R(r|s)_LRU] × f_S(s) ds 进行离散化求和，步长 Δs 取对象大小分位数的 1%，积分结果即为 LFU 相对 LRU 的字节命中率增益上限，需排除容量开销影响

## Evidence

先验知识/题面给定，逻辑校验通过
