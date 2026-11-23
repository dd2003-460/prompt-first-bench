# N313: P95带宽监控与预测模型：B_95th_predicted = B_avg * k_p95_factor * (1 + σ_peak / μ_peak)，其中 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N99

## Claim

P95带宽监控与预测模型：B_95th_predicted = B_avg * k_p95_factor * (1 + σ_peak / μ_peak)，其中 k_p95_factor=1.5-2.0，σ_peak/μ_peak 为峰值波动系数，需基于历史7天带宽数据滚动计算以动态选择计费模式

## Corrected Claim

P95带宽监控与预测模型：B_95th_predicted = B_avg * k_p95_factor * (1 + σ_peak / μ_peak)，其中 k_p95_factor=1.5-2.0，σ_peak/μ_peak 为峰值波动系数，需基于历史7天带宽数据滚动计算以动态选择计费模式

## Evidence

先验知识/题面给定，逻辑校验通过
