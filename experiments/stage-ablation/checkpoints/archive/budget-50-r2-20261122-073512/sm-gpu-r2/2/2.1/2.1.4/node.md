# N64: NVIDIA RTX 4090 单卡运行 Qwen3-27B (INT4) 的 OPEX 电力成本：P_gpu = 450W, P_auxiliary ≈ 10

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

NVIDIA RTX 4090 单卡运行 Qwen3-27B (INT4) 的 OPEX 电力成本：P_gpu = 450W, P_auxiliary ≈ 100W, P_total = 550W = 0.55 kW; T_hours = 8760h; E_unit_price = $0.10/kWh; OPEX_power = 0.55 * 8760 * 0.10 ≈ $481.80/年。

## Corrected Claim

NVIDIA RTX 4090 单卡运行 Qwen3-27B (INT4) 的 OPEX 电力成本：P_gpu = 450W, P_auxiliary ≈ 100W, P_total = 550W = 0.55 kW; T_hours = 8760h; E_unit_price = $0.10/kWh; OPEX_power = 0.55 * 8760 * 0.10 ≈ $481.80/年。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP 450W 符合官方规格，辅助功耗 100W 为合理工程估算，数学计算 0.55kW * 8760h * $0.10/kWh = $481.80 准确无误。
