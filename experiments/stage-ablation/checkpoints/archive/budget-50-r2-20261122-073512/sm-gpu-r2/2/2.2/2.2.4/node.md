# N84: NVIDIA A100 80GB 单卡运行 Qwen3-27B (BF16) 的 OPEX 电力成本：P_gpu = 400W, P_auxiliary ≈ 1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

NVIDIA A100 80GB 单卡运行 Qwen3-27B (BF16) 的 OPEX 电力成本：P_gpu = 400W, P_auxiliary ≈ 100W, P_total = 500W = 0.5 kW; T_hours = 8760h; E_unit_price = $0.10/kWh; OPEX_power = 0.5 * 8760 * 0.10 ≈ $438.00/年。

## Corrected Claim

NVIDIA A100 80GB 单卡运行 Qwen3-27B (BF16) 的 OPEX 电力成本：P_gpu = 400W, P_auxiliary ≈ 100W, P_total = 500W = 0.5 kW; T_hours = 8760h; E_unit_price = $0.10/kWh; OPEX_power = 0.5 * 8760 * 0.10 ≈ $438.00/年。

## Evidence

先验知识/题面给定，逻辑校验通过：功率500W=0.5kW，年运行8760小时，电价$0.10/kWh，计算0.5*8760*0.10=438，数值与逻辑均正确。
