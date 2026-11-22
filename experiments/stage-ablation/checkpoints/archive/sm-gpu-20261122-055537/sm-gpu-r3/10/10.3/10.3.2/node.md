# N370: NVIDIA L4 在 24/7 运行场景下的年度电力成本 C_power_L4 = 0.122 kW * 8760 h * $0.15/kWh = $160.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N116

## Claim

NVIDIA L4 在 24/7 运行场景下的年度电力成本 C_power_L4 = 0.122 kW * 8760 h * $0.15/kWh = $160.3/year，基于 N97 估算的整机功耗 122W（GPU 72W + 系统 50W）。

## Corrected Claim

NVIDIA L4 在 24/7 运行场景下的年度电力成本 C_power_L4 = 0.122 kW * 8760 h * $0.15/kWh = $160.3/year，基于 N97 估算的整机功耗 122W（GPU 72W + 系统 50W）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 0.122 * 8760 * 0.15 = 160.308 正确，功耗构成（GPU+系统）符合常识，无内部矛盾。
