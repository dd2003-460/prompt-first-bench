# N238: 观望效应导致的成交量下降幅度 ΔV_wait 的量化公式：ΔV_wait = -k_wait * (1 - e^(-λ_wait * ΔP_signal))，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

观望效应导致的成交量下降幅度 ΔV_wait 的量化公式：ΔV_wait = -k_wait * (1 - e^(-λ_wait * ΔP_signal))，其中 k_wait 为观望弹性系数，λ_wait 为买家对价格信号变化的敏感度参数，ΔP_signal 为价格信号重置的幅度（如中位价展示导致的预期价差）。

## Corrected Claim

观望效应导致的成交量下降幅度 ΔV_wait 的量化公式：ΔV_wait = -k_wait * (1 - e^(-λ_wait * ΔP_signal))，其中 k_wait 为观望弹性系数，λ_wait 为买家对价格信号变化的敏感度参数，ΔP_signal 为价格信号重置的幅度（如中位价展示导致的预期价差）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

wait-and-see effect volume decline formula price signal reset
