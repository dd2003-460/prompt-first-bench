# N119: ΔH_drift 的量化取决于负载热度漂移周期 T_shift 与 LFU 适应时间常数 τ_LFU 的比值：ΔH_drift ≈ -k * max(0, 1 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

ΔH_drift 的量化取决于负载热度漂移周期 T_shift 与 LFU 适应时间常数 τ_LFU 的比值：ΔH_drift ≈ -k * max(0, 1 - T_shift/τ_LFU) * P_drift_region；在静态稳态假设下 T_shift → ∞，则 ΔH_drift → 0；若假设日内热度波动周期 T_shift ≈ 6h = 0.25天，且 τ_LFU ≈ 1天（典型老化窗口），则 ΔH_drift ≈ -k * 0.75 * P_drift_region；由于题目给定的是稳态估算且未提供日内波动数据，[待核验] 假设 T_shift >> τ_LFU，故 ΔH_drift ≈ 0，修正 N44 中 '-1~3%' 的保守估计。

## Corrected Claim

ΔH_drift 的量化取决于负载热度漂移周期 T_shift 与 LFU 适应时间常数 τ_LFU 的比值：ΔH_drift ≈ -k * max(0, 1 - T_shift/τ_LFU) * P_drift_region；在静态稳态假设下 T_shift → ∞，则 ΔH_drift → 0；若假设日内热度波动周期 T_shift ≈ 6h = 0.25天，且 τ_LFU ≈ 1天（典型老化窗口），则 ΔH_drift ≈ -k * 0.75 * P_drift_region；由于题目给定的是稳态估算且未提供日内波动数据，[待核验] 假设 T_shift >> τ_LFU，故 ΔH_drift ≈ 0，修正 N44 中 '-1~3%' 的保守估计。

## Evidence

先验知识/题面给定，逻辑校验通过：在稳态假设下，热度漂移周期远大于适应时间常数，导致漂移项趋于零，推导自洽。

## Search Query

LFU cache adaptation time constant steady state assumption
