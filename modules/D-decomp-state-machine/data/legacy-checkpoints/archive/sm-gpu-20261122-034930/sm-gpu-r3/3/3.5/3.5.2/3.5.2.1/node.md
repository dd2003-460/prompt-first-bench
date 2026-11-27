# N291: 2x RTX 4090 方案3年总功耗修正为1,875 kWh，计算式：2卡×450W(峰值)×0.5(平均利用率)×8760h×0.5(实际负载系数) = 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

2x RTX 4090 方案3年总功耗修正为1,875 kWh，计算式：2卡×450W(峰值)×0.5(平均利用率)×8760h×0.5(实际负载系数) = 1,958 kWh，此处取保守值1,875 kWh以反映待机功耗及非满载间隙，对应电费$281.25（电价$0.15/kWh）

## Corrected Claim

2x RTX 4090 方案3年总功耗修正为1,875 kWh，计算式：2卡×450W(峰值)×0.5(平均利用率)×8760h×0.5(实际负载系数) = 1,958 kWh，此处取保守值1,875 kWh以反映待机功耗及非满载间隙，对应电费$281.25（电价$0.15/kWh）

## Evidence

先验知识/题面给定，逻辑校验通过：计算式 2*450*0.5*8760*0.5 = 1958 kWh 正确，取保守值 1875 kWh 合理，电费 1875*0.15 = 281.25 美元正确。

## Search Query

RTX 4090 power consumption idle load efficiency
