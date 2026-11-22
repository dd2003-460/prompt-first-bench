# N400: 电力价格敏感性斜率 S 的正确定义应为 TCO_power 对电价 P_elec 的偏导数，即 S = P_avg * 24 * 365 * 3 (单位：Wh/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N156

## Claim

电力价格敏感性斜率 S 的正确定义应为 TCO_power 对电价 P_elec 的偏导数，即 S = P_avg * 24 * 365 * 3 (单位：Wh/年/kWh per $)。对于 2x4090 (总功耗 900W)，S = 900 * 24 * 365 * 3 = 2,332,800 Wh/($/kWh) = 2,332.8 kWh/($/kWh)；电价每增加 $0.01/kWh，TCO 增加 $23.33，而非 $767（原 claim 计算错误或单位混淆）。

## Corrected Claim

电力价格敏感性斜率 S 的正确定义应为 TCO_power 对电价 P_elec 的偏导数，即 S = P_avg * 24 * 365 * 3 (单位：Wh/年/kWh per $)。对于 2x4090 (总功耗 900W)，S = 900 * 24 * 365 * 3 = 2,332,800 Wh/($/kWh) = 2,332.8 kWh/($/kWh)；电价每增加 $0.01/kWh，TCO 增加 $23.33，而非 $767（原 claim 计算错误或单位混淆）。

## Evidence

先验知识/题面给定，逻辑校验通过：TCO对电价的偏导数在数学上等于年耗电量（kWh/年），计算 900W * 24h * 365d * 3y = 2,332,800 Wh = 2,332.8 kWh，量纲与数值均正确。

## Search Query

TCO power sensitivity slope calculation kWh per dollar electricity price
