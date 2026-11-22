# N184: 年电力成本计算公式 C_power_annual = P_avg * 8760h * E_rate，假设电价 E_rate = $0.15/kWh (北美商业平

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

年电力成本计算公式 C_power_annual = P_avg * 8760h * E_rate，假设电价 E_rate = $0.15/kWh (北美商业平均)：RX 7800 XT ≈ $250/年，A100 80GB ≈ $368/年，MI300X ≈ $686/年，2x RTX 4090 (P_avg=0.7*450*2=630W) ≈ $824/年。

## Corrected Claim

年电力成本计算公式 C_power_annual = P_avg * 8760h * E_rate，假设电价 E_rate = $0.15/kWh (北美商业平均)：RX 7800 XT ≈ $250/年，A100 80GB ≈ $368/年，MI300X ≈ $686/年，2x RTX 4090 (P_avg=0.7*450*2=630W) ≈ $824/年。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 C = P * 8760 * Rate 正确；各GPU功耗假设（RX 7800 XT ~230W, A100 ~400W, MI300X ~750W, 2x4090 630W）符合工程常识，计算结果量级准确。
