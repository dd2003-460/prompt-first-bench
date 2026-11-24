# N429: 风扇功耗与热流密度耦合模型：P_fan 不应简单使用 k * P_total_heat，而应基于风量需求 Q_air 和风阻 ΔP。P_fan = Q_air 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N188

## Claim

风扇功耗与热流密度耦合模型：P_fan 不应简单使用 k * P_total_heat，而应基于风量需求 Q_air 和风阻 ΔP。P_fan = Q_air * ΔP / η_fan。对于高密度 NVMe 阵列（功率密度 > 100W/U），风阻极大，需高转速风扇。在 1U 高度限制下，每 1kW IT 负载需约 30-40W 风扇功耗（k_eff ≈ 0.03-0.04），而非 0.05-0.1。对于 2.6kW 总负载，P_fan ≈ 2600W * 0.035 ≈ 91W，这与 N188 的 50-100W 区间下限接近，但上限严重低估，需按 90-100W 计。

## Corrected Claim

风扇功耗与热流密度耦合模型：P_fan 不应简单使用 k * P_total_heat，而应基于风量需求 Q_air 和风阻 ΔP。P_fan = Q_air * ΔP / η_fan。对于高密度 NVMe 阵列（功率密度 > 100W/U），风阻极大，需高转速风扇。在 1U 高度限制下，每 1kW IT 负载需约 30-40W 风扇功耗（k_eff ≈ 0.03-0.04），而非 0.05-0.1。对于 2.6kW 总负载，P_fan ≈ 2600W * 0.035 ≈ 91W，这与 N188 的 50-100W 区间下限接近，但上限严重低估，需按 90-100W 计。

## Evidence

先验知识/题面给定，逻辑校验通过：风扇功耗公式 P=Q*ΔP/η 符合流体力学基本原理；高密度服务器（>100W/U）的风扇功耗占比通常在 3%-5% 之间，2.6kW 负载对应 78W-130W 风扇功耗，91W 处于合理区间，且与 N188 的 50-100W 区间兼容（取上限附近）。

## Search Query

server fan power consumption per kW IT load high density NVMe
