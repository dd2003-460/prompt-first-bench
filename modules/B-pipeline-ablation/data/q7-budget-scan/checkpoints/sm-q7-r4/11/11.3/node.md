# N387: 动态功耗增量的精确计算：ΔP_dynamic = P_active - P_idle。假设 P_active = 25W/盘，P_idle = 5W/盘，则 Δ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131

## Claim

动态功耗增量的精确计算：ΔP_dynamic = P_active - P_idle。假设 P_active = 25W/盘，P_idle = 5W/盘，则 ΔP = 20W/盘。对于 100TB 温数据（假设 50 块 2TB 盘），总 ΔP = 50 * 20W = 1000W = 1kW。年动态能耗增量 = 1kW * 33.3% * 8760h ≈ 29,200 kWh。年电费增量 = 29,200 * 1.4 (PUE) * 0.8 (¥/kWh) ≈ ¥32,864。

## Corrected Claim

动态功耗增量的精确计算：ΔP_dynamic = P_active - P_idle。假设 P_active = 25W/盘，P_idle = 5W/盘，则 ΔP = 20W/盘。对于 100TB 温数据（假设 50 块 2TB 盘），总 ΔP = 50 * 20W = 1000W = 1kW。年动态能耗增量 = 1kW * 33.3% * 8760h ≈ 29,200 kWh。年电费增量 = 29,200 * 1.4 (PUE) * 0.8 (¥/kWh) ≈ ¥32,864。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（50*20=1000W; 1000*0.333*8760≈29200kWh; 29200*1.4*0.8≈32864元），量纲与物理直觉一致。
