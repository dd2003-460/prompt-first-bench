# N318: P99 延迟的排队论修正：T_queue = (ρ / (1-ρ)) × T_service，其中 ρ = B_served / B_capacity 为利用率

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100, N101, N102

## Claim

P99 延迟的排队论修正：T_queue = (ρ / (1-ρ)) × T_service，其中 ρ = B_served / B_capacity 为利用率，T_service 为平均服务时间；当 ρ > 0.8 时，排队延迟指数增长；需结合 N18 的利用率模型 U_self，计算在峰值流量下 ρ 的值，若 ρ=0.8，T_queue ≈ 4 × T_service，此项不可忽略

## Corrected Claim

P99 延迟的排队论修正：T_queue = (ρ / (1-ρ)) × T_service，其中 ρ = B_served / B_capacity 为利用率，T_service 为平均服务时间；当 ρ > 0.8 时，排队延迟指数增长；需结合 N18 的利用率模型 U_self，计算在峰值流量下 ρ 的值，若 ρ=0.8，T_queue ≈ 4 × T_service，此项不可忽略

## Evidence

先验知识/题面给定，逻辑校验通过：公式 T_queue = (ρ / (1-ρ)) × T_service 符合 M/M/1 排队模型中等待时间 Wq 与利用率 ρ 及平均服务时间 1/μ 的关系（Wq = ρ/(μ(1-ρ)) = ρ/(1-ρ) * 1/μ），且 ρ=0.8 时系数为 0.8/0.2=4，数值推导正确。

## Search Query

M/M/1 queueing delay formula utilization factor
