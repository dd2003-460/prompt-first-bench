# N57: 中频率波动场景下，LFU 的字节命中率增益 ΔH_byte(t) = ΔH_byte_stable * (1 - e^(-t/τ_lag))，其中 t 为时间步

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

中频率波动场景下，LFU 的字节命中率增益 ΔH_byte(t) = ΔH_byte_stable * (1 - e^(-t/τ_lag))，其中 t 为时间步，ΔH_byte_stable 为频率稳定时的增益。

## Corrected Claim

中频率波动场景下，LFU 的字节命中率增益 ΔH_byte(t) = ΔH_byte_stable * (1 - e^(-t/τ_lag))，其中 t 为时间步，ΔH_byte_stable 为频率稳定时的增益。

## Evidence

先验知识/题面给定，逻辑校验通过
