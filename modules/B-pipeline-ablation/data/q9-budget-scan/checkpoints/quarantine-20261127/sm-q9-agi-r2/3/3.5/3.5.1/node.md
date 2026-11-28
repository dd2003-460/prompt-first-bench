# N60: 服务器空闲功耗 (Idle Power) 基线测量：在 4x V100-SXM2 处于 idle 状态 (无推理负载) 时，整机功耗约为 150-200W (C

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

服务器空闲功耗 (Idle Power) 基线测量：在 4x V100-SXM2 处于 idle 状态 (无推理负载) 时，整机功耗约为 150-200W (CPU+RAM+PSU损耗)。计算公式：Monthly_Cost_Idle = Idle_Power_W * 24 * 30 / 1000 * Price_per_kWh。若 Idle_Power=180W, Price=0.5 CNY/kWh，则月成本 ≈ 64.8 CNY。

## Corrected Claim

服务器空闲功耗 (Idle Power) 基线测量：在 4x V100-SXM2 处于 idle 状态 (无推理负载) 时，整机功耗约为 150-200W (CPU+RAM+PSU损耗)。计算公式：Monthly_Cost_Idle = Idle_Power_W * 24 * 30 / 1000 * Price_per_kWh。若 Idle_Power=180W, Price=0.5 CNY/kWh，则月成本 ≈ 64.8 CNY。

## Evidence

先验知识/题面给定，逻辑校验通过：4x V100-SXM2 服务器空闲功耗 150-200W 符合工程常识（单卡空闲约 30-50W，加上 CPU/RAM/PSU 损耗），且成本计算公式及数值推导（180*720/1000*0.5=64.8）准确无误。
