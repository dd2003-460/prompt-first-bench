# N170: 平台佣金流噪声投影 ΔRevenue_noise：ε_traffic 通过成交量变化 ΔQ 影响佣金流，ΔRevenue = r * P_avg * ΔQ，其中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N56

## Claim

平台佣金流噪声投影 ΔRevenue_noise：ε_traffic 通过成交量变化 ΔQ 影响佣金流，ΔRevenue = r * P_avg * ΔQ，其中 ΔQ ≈ ε_traffic * Q_base * ε_Q_traffic（流量弹性），假设 ε_Q_traffic ≈ 0.8，则 ΔRevenue 的标准差为 r * P_avg * σ_traffic_abs * Q_base * 0.8，用于评估干预对平台收入的随机冲击。

## Corrected Claim

平台佣金流噪声投影 ΔRevenue_noise：ε_traffic 通过成交量变化 ΔQ 影响佣金流，ΔRevenue = r * P_avg * ΔQ，其中 ΔQ ≈ ε_traffic * Q_base * ε_Q_traffic（流量弹性），假设 ε_Q_traffic ≈ 0.8，则 ΔRevenue 的标准差为 r * P_avg * σ_traffic_abs * Q_base * 0.8，用于评估干预对平台收入的随机冲击。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

platform revenue volatility due to traffic reallocation noise commission
