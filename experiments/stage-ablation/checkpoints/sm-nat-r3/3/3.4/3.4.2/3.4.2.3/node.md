# N195: 更新率对 LFU 计数器重置的影响量化：每次对象更新会重置其 LFU 计数器，导致频率估计偏差。偏差幅度 Δf_i ≈ λ_update * T_residen

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

更新率对 LFU 计数器重置的影响量化：每次对象更新会重置其 LFU 计数器，导致频率估计偏差。偏差幅度 Δf_i ≈ λ_update * T_residence_avg * f_i。当 λ_update * T_residence_avg << 1 时，Δf_i 可忽略，LFU 排名不受显著影响。

## Corrected Claim

更新率对 LFU 计数器重置的影响量化：每次对象更新会重置其 LFU 计数器，导致频率估计偏差。偏差幅度 Δf_i ≈ λ_update * T_residence_avg * f_i。当 λ_update * T_residence_avg << 1 时，Δf_i 可忽略，LFU 排名不受显著影响。

## Evidence

先验知识/题面给定，逻辑校验通过
