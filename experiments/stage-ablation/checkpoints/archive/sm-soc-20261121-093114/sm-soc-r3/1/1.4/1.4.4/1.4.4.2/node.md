# N119: 挂价上升速度 v_ask 量化为 v_ask = ΔP_ask / Δt，其中 ΔP_ask 为卖家调整挂价的幅度，Δt 为调整间隔，需与 P_market 的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

挂价上升速度 v_ask 量化为 v_ask = ΔP_ask / Δt，其中 ΔP_ask 为卖家调整挂价的幅度，Δt 为调整间隔，需与 P_market 的更新速度 v_market = λ_lag * (P_deal_avg - P_market) 进行对比，若 v_ask > v_market 则系统处于不稳定均衡。

## Corrected Claim

挂价上升速度 v_ask 量化为 v_ask = ΔP_ask / Δt，其中 ΔP_ask 为卖家调整挂价的幅度，Δt 为调整间隔，需与 P_market 的更新速度 v_market = λ_lag * (P_deal_avg - P_market) 进行对比，若 v_ask > v_market 则系统处于不稳定均衡。

## Evidence

先验知识/题面给定，逻辑校验通过
