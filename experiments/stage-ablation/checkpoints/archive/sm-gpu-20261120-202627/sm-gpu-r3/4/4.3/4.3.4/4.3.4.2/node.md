# N358: 空调负荷增加导致的 OpEx 增量：每增加 1kW 持续散热负载，在标准办公空调效率（COP=3.0）下，额外电力消耗为 1kW/3.0 = 0.333kW，3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

空调负荷增加导致的 OpEx 增量：每增加 1kW 持续散热负载，在标准办公空调效率（COP=3.0）下，额外电力消耗为 1kW/3.0 = 0.333kW，3 年 OpEx 增量 = 0.333kW × 24h × 365d × 3y × $0.12/kWh ≈ $1050；若使用数据中心级精密空调（COP=4.0），则 OpEx 增量降至约 $780。

## Corrected Claim

空调负荷增加导致的 OpEx 增量：每增加 1kW 持续散热负载，在标准办公空调效率（COP=3.0）下，额外电力消耗为 1kW/3.0 = 0.333kW，3 年 OpEx 增量 = 0.333kW × 24h × 365d × 3y × $0.12/kWh ≈ $1050；若使用数据中心级精密空调（COP=4.0），则 OpEx 增量降至约 $780。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 0.333kW * 24h * 365d * 3y * $0.12/kWh ≈ $1050 及 COP=4.0 时的 $780 均符合物理定义与算术逻辑。
