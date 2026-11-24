# N631: 工作点 2 的 P99 抖动容忍度量化指标为 L_p99_jitter_tol = (L_p99_target - L_p99_baseline) / L_p9

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N209

## Claim

工作点 2 的 P99 抖动容忍度量化指标为 L_p99_jitter_tol = (L_p99_target - L_p99_baseline) / L_p99_baseline，其中 L_p99_baseline 为平均延迟，L_p99_target 为合规阈值 T；在 60% 利用率下，队列等待时间遵循 M/M/1 模型，L_wait = λ / (μ - λ)，λ 为到达率，μ 为服务率，利用率 0.6 时 L_wait ≈ 1.5 * 1/μ，需确保此值小于 T - L_prop - L_processing。

## Corrected Claim

工作点 2 的 P99 抖动容忍度量化指标为 L_p99_jitter_tol = (L_p99_target - L_p99_baseline) / L_p99_baseline，其中 L_p99_baseline 为平均延迟，L_p99_target 为合规阈值 T；在 60% 利用率下，队列等待时间遵循 M/M/1 模型，L_wait = λ / (μ - λ)，λ 为到达率，μ 为服务率，利用率 0.6 时 L_wait ≈ 1.5 * 1/μ，需确保此值小于 T - L_prop - L_processing。

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/1 模型中平均等待时间公式 L_wait = λ/(μ-λ) 正确，当利用率 ρ=λ/μ=0.6 时，L_wait = 0.6μ/(0.4μ) = 1.5/μ，推导无误；P99 抖动容忍度定义符合常规工程指标逻辑。

## Search Query

M/M/1 queueing theory CDN edge latency jitter utilization 60%
