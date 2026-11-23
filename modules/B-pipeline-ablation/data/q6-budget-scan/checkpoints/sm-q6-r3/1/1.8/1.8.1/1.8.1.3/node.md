# N233: 核心区域 T_queue_P99(j) 的排队论模型：T_queue_P99(j) = (λ_j / (μ_j - λ_j)) * T_service_avg，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

核心区域 T_queue_P99(j) 的排队论模型：T_queue_P99(j) = (λ_j / (μ_j - λ_j)) * T_service_avg，其中 λ_j 为到达率，μ_j 为服务率，T_service_avg 为平均服务时间；当负载率 ρ_j = λ_j/μ_j > 0.8 时，P99 排队延迟急剧上升，需通过压测确定临界负载率（通常 0.7-0.85）

## Corrected Claim

核心区域 T_queue_P99(j) 的排队论模型：T_queue_P99(j) = (λ_j / (μ_j - λ_j)) * T_service_avg，其中 λ_j 为到达率，μ_j 为服务率，T_service_avg 为平均服务时间；当负载率 ρ_j = λ_j/μ_j > 0.8 时，P99 排队延迟急剧上升，需通过压测确定临界负载率（通常 0.7-0.85）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

M/M/1 queue P99 latency load factor threshold
