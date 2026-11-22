# N242: 收敛时间 T_convergence 的精确计算公式：T_convergence = (ln(δ_0) - ln(δ_target)) / λ_transpar

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79, N80, N81

## Claim

收敛时间 T_convergence 的精确计算公式：T_convergence = (ln(δ_0) - ln(δ_target)) / λ_transparency，其中 δ_0 = 0.20，δ_target = 0.05；需代入 λ_transparency 的估计区间（如 0.1-0.3/天）计算 T_convergence 的具体天数范围，并验证该范围是否落在假设的 10-20 天区间内，若偏离则需调整 λ 参数。

## Corrected Claim

收敛时间 T_convergence 的精确计算公式：T_convergence = (ln(δ_0) - ln(δ_target)) / λ_transparency，其中 δ_0 = 0.20，δ_target = 0.05；需代入 λ_transparency 的估计区间（如 0.1-0.3/天）计算 T_convergence 的具体天数范围，并验证该范围是否落在假设的 10-20 天区间内，若偏离则需调整 λ 参数。

## Evidence

先验知识/题面给定，逻辑校验通过
