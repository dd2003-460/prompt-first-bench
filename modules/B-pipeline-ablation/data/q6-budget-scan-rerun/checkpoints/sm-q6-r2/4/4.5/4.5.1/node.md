# N85: 全自建策略闲置容量成本 C_idle 的量化公式：C_idle_annual = (C_total_self - B_avg) × unit_cost_per_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

全自建策略闲置容量成本 C_idle 的量化公式：C_idle_annual = (C_total_self - B_avg) × unit_cost_per_Mbps_month × 12 / (Total_Annual_Requests / 1000)，其中 C_total_self = 10 × C_pop，C_pop 需根据单点峰值流量 B_peak_pop 和利用率目标 U_self_target (40%-60%) 反推：C_pop = B_peak_pop / U_self_target

## Corrected Claim

全自建策略闲置容量成本 C_idle 的量化公式：C_idle_annual = (C_total_self - B_avg) × unit_cost_per_Mbps_month × 12 / (Total_Annual_Requests / 1000)，其中 C_total_self = 10 × C_pop，C_pop 需根据单点峰值流量 B_peak_pop 和利用率目标 U_self_target (40%-60%) 反推：C_pop = B_peak_pop / U_self_target

## Evidence

先验知识/题面给定，逻辑校验通过
