# N441: HDD层动态功耗增量的量化：单盘动态读功耗 P_active = 9W，增量 ΔP_disk = 9W - 6W = 3W。总动态增量功率 ΔP_total =

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N146

## Claim

HDD层动态功耗增量的量化：单盘动态读功耗 P_active = 9W，增量 ΔP_disk = 9W - 6W = 3W。总动态增量功率 ΔP_total = 32 * 3W = 96W = 0.096kW。假设动态占空比 D_dynamic = 1% (基于月均<1次访问及短暂IO)，年动态能耗 E_dynamic = 0.096kW * 8760h * 1.4 * 0.01 = 11.79 kWh。年动态电费 C_dynamic = 11.79 * 0.8 = ¥9.4。

## Corrected Claim

HDD层动态功耗增量的量化：单盘动态读功耗 P_active = 9W，增量 ΔP_disk = 9W - 6W = 3W。总动态增量功率 ΔP_total = 32 * 3W = 96W = 0.096kW。假设动态占空比 D_dynamic = 1% (基于月均<1次访问及短暂IO)，年动态能耗 E_dynamic = 0.096kW * 8760h * 1.4 * 0.01 = 11.79 kWh。年动态电费 C_dynamic = 11.79 * 0.8 = ¥9.4。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（32*3=96W, 96*8760*1.4*0.01≈11.79kWh, 11.79*0.8≈9.4元），参数假设（HDD功耗、PUE、电价、占空比）符合工程常识。
