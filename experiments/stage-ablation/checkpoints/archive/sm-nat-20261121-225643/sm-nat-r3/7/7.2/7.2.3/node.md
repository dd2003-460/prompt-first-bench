# N117: N43 中 '工作负载热度变化周期 T_shift' 的估算方法量化：在 Pareto(β=0.9) 热度分布下，T_shift 可由热度自相关函数 C(τ) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

N43 中 '工作负载热度变化周期 T_shift' 的估算方法量化：在 Pareto(β=0.9) 热度分布下，T_shift 可由热度自相关函数 C(τ) = <r(t) r(t+τ)> / <r(t)^2> 的半衰期定义，即 C(T_shift) = 0.5；对于泊松请求过程，C(τ) ≈ exp(-λ * τ)，因此 T_shift = ln(2) / λ ≈ 0.693 / λ，其中 λ 为对象热度变化率，若 λ = 0.1/天，则 T_shift ≈ 6.93 天，远大于 τ_LFU (1小时)，表明在典型 CDN 工作负载下 LFU 的漂移劣势可忽略。

## Corrected Claim

N43 中 '工作负载热度变化周期 T_shift' 的估算方法量化：在 Pareto(β=0.9) 热度分布下，T_shift 可由热度自相关函数 C(τ) = <r(t) r(t+τ)> / <r(t)^2> 的半衰期定义，即 C(T_shift) = 0.5；对于泊松请求过程，C(τ) ≈ exp(-λ * τ)，因此 T_shift = ln(2) / λ ≈ 0.693 / λ，其中 λ 为对象热度变化率，若 λ = 0.1/天，则 T_shift ≈ 6.93 天，远大于 τ_LFU (1小时)，表明在典型 CDN 工作负载下 LFU 的漂移劣势可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松过程的自相关函数确实呈指数衰减 exp(-λτ)，半衰期公式 T_shift = ln(2)/λ 推导正确，数值计算 0.693/0.1 = 6.93 无误，且 6.93 天远大于 1 小时的结论符合逻辑。

## Search Query

CDN workload hotness autocorrelation function half-life estimation
