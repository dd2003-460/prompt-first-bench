# N102: 条件分支1 (高电价/高负载) 的量化触发条件：E_price > $0.15/kWh 且 T_hours > 6000h/year。此时 L4 方案因电力节省

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

条件分支1 (高电价/高负载) 的量化触发条件：E_price > $0.15/kWh 且 T_hours > 6000h/year。此时 L4 方案因电力节省 ($561+/year) 在 3 年 TCO 内可抵消其较高的初始采购溢价 (假设 L4 ~$3000 vs 4090 ~$1600, 溢价 $1400, 需 ~2.5 年回本)。

## Corrected Claim

条件分支1 (高电价/高负载) 的量化触发条件：E_price > $0.15/kWh 且 T_hours > 6000h/year。此时 L4 方案因电力节省 ($561+/year) 在 3 年 TCO 内可抵消其较高的初始采购溢价 (假设 L4 ~$3000 vs 4090 ~$1600, 溢价 $1400, 需 ~2.5 年回本)。

## Evidence

先验知识/题面给定，逻辑校验通过：计算显示 $561/年节省在约2.5年内可覆盖 $1400 溢价，与3年TCO周期兼容，数值量级合理。
