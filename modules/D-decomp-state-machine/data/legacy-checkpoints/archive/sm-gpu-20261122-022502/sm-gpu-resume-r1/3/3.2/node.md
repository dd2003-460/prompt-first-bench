# N17: 电力运营成本 (OpEx) 计算式：年电费 = (GPU 功耗 * 8760 小时 * 电价 $/kWh)。RTX 4090 功耗 450W，年电费 (24/7

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

电力运营成本 (OpEx) 计算式：年电费 = (GPU 功耗 * 8760 小时 * 电价 $/kWh)。RTX 4090 功耗 450W，年电费 (24/7 运行, $0.10/kWh) = $3942；H100 SXM 功耗 700W，年电费 = $6132；Mac Studio M2 Ultra 功耗 250W，年电费 = $2190。

## Corrected Claim

电力运营成本 (OpEx) 计算式：年电费 = (GPU 功耗 * 8760 小时 * 电价 $/kWh)。RTX 4090 功耗 450W，年电费 (24/7 运行, $0.10/kWh) = $3942；H100 SXM 功耗 700W，年电费 = $6132；Mac Studio M2 Ultra 功耗 250W，年电费 = $2190。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算准确（450W*8760h*0.1$/kWh≈$3942, 700W*8760h*0.1$/kWh≈$6132, 250W*8760h*0.1$/kWh≈$2190），功耗数值符合硬件规格常识。
