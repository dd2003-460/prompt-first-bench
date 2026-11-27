# N262: 修正 N85 中的电力成本计算：基于 E_A100 = 7884 kWh，当 E_price = $0.05/kWh 时，C_power_A100 = 7884

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

修正 N85 中的电力成本计算：基于 E_A100 = 7884 kWh，当 E_price = $0.05/kWh 时，C_power_A100 = 7884 × $0.05 = $394.2；当 E_price = $0.15/kWh 时，C_power_A100 = 7884 × $0.15 = $1182.6。

## Corrected Claim

修正 N85 中的电力成本计算：基于 E_A100 = 7884 kWh，当 E_price = $0.05/kWh 时，C_power_A100 = 7884 × $0.05 = $394.2；当 E_price = $0.15/kWh 时，C_power_A100 = 7884 × $0.15 = $1182.6。

## Evidence

先验知识/题面给定，逻辑校验通过：7884 × 0.05 = 394.2 且 7884 × 0.15 = 1182.6，算术正确，量纲一致。
