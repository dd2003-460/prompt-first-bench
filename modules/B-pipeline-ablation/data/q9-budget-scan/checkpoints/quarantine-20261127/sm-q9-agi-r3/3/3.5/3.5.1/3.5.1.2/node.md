# N171: 常驻 vLLM 服务的月度 Idle 电费成本（按 720h/月，0.5 CNY/kWh 计算）：若 Idle_Power=220W，则 Monthly_Cos

- **status**: verified
- **level**: L4
- **source**: derived
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

常驻 vLLM 服务的月度 Idle 电费成本（按 720h/月，0.5 CNY/kWh 计算）：若 Idle_Power=220W，则 Monthly_Cost_Idle_Resident = 220 * 720 / 1000 * 0.5 ≈ 79.2 CNY/月；若采用冷启动模式（用时加载，闲时休眠），Idle_Power≈160W，成本降至 ≈ 57.6 CNY/月，但引入每次启动 30-60s 的冷启动延迟成本。

## Corrected Claim

常驻 vLLM 服务的月度 Idle 电费成本（按 720h/月，0.5 CNY/kWh 计算）：若 Idle_Power=220W，则 Monthly_Cost_Idle_Resident = 220 * 720 / 1000 * 0.5 ≈ 79.2 CNY/月；若采用冷启动模式（用时加载，闲时休眠），Idle_Power≈160W，成本降至 ≈ 57.6 CNY/月，但引入每次启动 30-60s 的冷启动延迟成本。

## Evidence

逻辑推导成立，来源未直接覆盖
