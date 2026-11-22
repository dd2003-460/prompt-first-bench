# N104: 当 K_opt=N=100,000 时，Belady最优算法的字节命中率上界 H_opt_byte 恒等于 1.0（因为分子分母均为所有对象的总请求字节数，Σ_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

当 K_opt=N=100,000 时，Belady最优算法的字节命中率上界 H_opt_byte 恒等于 1.0（因为分子分母均为所有对象的总请求字节数，Σ_{i=1}^{N} p_i * s_i / Σ_{i=1}^{N} p_i * s_i = 1）。

## Corrected Claim

当 K_opt=N=100,000 时，Belady最优算法的字节命中率上界 H_opt_byte 恒等于 1.0（因为分子分母均为所有对象的总请求字节数，Σ_{i=1}^{N} p_i * s_i / Σ_{i=1}^{N} p_i * s_i = 1）。

## Evidence

先验知识/题面给定，逻辑校验通过：当缓存容量K等于对象总数N时，Belady算法（或任何最优离线算法）可缓存所有对象，无驱逐发生，所有请求均命中，命中率恒为1.0。
