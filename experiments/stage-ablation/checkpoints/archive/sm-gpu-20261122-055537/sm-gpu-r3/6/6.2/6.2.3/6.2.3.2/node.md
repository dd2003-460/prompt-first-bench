# N316: 电力成本差异的敏感性斜率系数：∂(ΔC_power_year)/∂(E_price) = 428Wh * T_hours / 1000，用于计算电价每波动 $0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N98

## Claim

电力成本差异的敏感性斜率系数：∂(ΔC_power_year)/∂(E_price) = 428Wh * T_hours / 1000，用于计算电价每波动 $0.01/kWh 对年度 TCO 的具体影响金额，例如在 T_hours=8760 时，斜率为 $3.75/($0.01/kWh)。

## Corrected Claim

电力成本差异的敏感性斜率系数：∂(ΔC_power_year)/∂(E_price) = 428Wh * T_hours / 1000，用于计算电价每波动 $0.01/kWh 对年度 TCO 的具体影响金额，例如在 T_hours=8760 时，斜率为 $3.75/($0.01/kWh)。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

sensitivity analysis electricity price impact on TCO formula
