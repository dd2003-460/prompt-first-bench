# N230: M/M/1 队列 P99 等待时间近似公式：T_queue_p99 ≈ (1/(μ*(1-ρ))) * ln(99/(100*(1-ρ)))，当 ρ=0.9 时

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60, N61, N62

## Claim

M/M/1 队列 P99 等待时间近似公式：T_queue_p99 ≈ (1/(μ*(1-ρ))) * ln(99/(100*(1-ρ)))，当 ρ=0.9 时，T_queue_p99 约为平均等待时间的 4.6 倍，是 P99 尾部延迟的非线性主导项。

## Corrected Claim

M/M/1 队列 P99 等待时间近似公式：T_queue_p99 ≈ (1/(μ*(1-ρ))) * ln(99/(100*(1-ρ)))，当 ρ=0.9 时，T_queue_p99 约为平均等待时间的 4.6 倍，是 P99 尾部延迟的非线性主导项。

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/1队列等待时间服从指数分布，P99分位数为 -ln(0.01)/μ_eff，平均等待时间为 1/μ_eff，比值为 -ln(0.01) ≈ 4.605，与陈述一致。

## Search Query

M/M/1 queue P99 waiting time approximation logarithmic
