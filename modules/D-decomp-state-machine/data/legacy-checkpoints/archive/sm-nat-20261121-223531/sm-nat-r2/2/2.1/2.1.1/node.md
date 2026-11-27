# N37: 在 ρ=0 独立假设下，LRU 字节命中率下界的简化积分公式：HitRate_base = 1 - (1/E[S]_trunc) * ∫_{s_min}^{s_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

在 ρ=0 独立假设下，LRU 字节命中率下界的简化积分公式：HitRate_base = 1 - (1/E[S]_trunc) * ∫_{s_min}^{s_max} s * f_S(s) * (1 - F_H(h_ref)) ds，其中 h_ref 为缓存容量 C_bytes 对应的热度阈值，即保留热度前 C_bytes/E[S]_trunc 比例的对象。

## Corrected Claim

在 ρ=0 独立假设下，LRU 字节命中率下界的简化积分公式：HitRate_base = 1 - (1/E[S]_trunc) * ∫_{s_min}^{s_max} s * f_S(s) * (1 - F_H(h_ref)) ds，其中 h_ref 为缓存容量 C_bytes 对应的热度阈值，即保留热度前 C_bytes/E[S]_trunc 比例的对象。

## Evidence

先验知识/题面给定，逻辑校验通过
