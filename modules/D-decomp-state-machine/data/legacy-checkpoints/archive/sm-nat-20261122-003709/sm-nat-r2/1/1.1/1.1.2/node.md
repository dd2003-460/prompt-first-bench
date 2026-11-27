# N31: Belady最优算法（Optimal）在缓存容量 C=128GB 下的理论字节命中率上界 H_opt_byte 计算公式为：H_opt_byte = (Σ_{i

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

Belady最优算法（Optimal）在缓存容量 C=128GB 下的理论字节命中率上界 H_opt_byte 计算公式为：H_opt_byte = (Σ_{i=1}^{K_opt} p_i * s_i) / (Σ_{i=1}^{N} p_i * s_i)，其中 K_opt 为缓存能容纳的最热对象数量，需通过积分 ∫_{s_min}^{s_K} f_S(s) ds = C 求解 K_opt。

## Corrected Claim

Belady最优算法（Optimal）在缓存容量 C=128GB 下的理论字节命中率上界 H_opt_byte 计算公式为：H_opt_byte = (Σ_{i=1}^{K_opt} p_i * s_i) / (Σ_{i=1}^{N} p_i * s_i)，其中 K_opt 为缓存能容纳的最热对象数量，需通过积分 ∫_{s_min}^{s_K} f_S(s) ds = C 求解 K_opt。

## Evidence

先验知识/题面给定，逻辑校验通过
