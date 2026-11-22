# N28: 电力成本（OpEx 主要项）：年电费 = TDP_watts * 24h * 365d * Electricity_Rate_per_kWh * Duty_Cy

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

电力成本（OpEx 主要项）：年电费 = TDP_watts * 24h * 365d * Electricity_Rate_per_kWh * Duty_Cycle，消费级 GPU TDP 通常 250-450W，数据中心 GPU TDP 可达 400-1000W，需结合当地电价（如中国 0.5-1.5 元/kWh）计算

## Corrected Claim

电力成本（OpEx 主要项）：年电费 = TDP_watts * 24h * 365d * Electricity_Rate_per_kWh * Duty_Cycle，消费级 GPU TDP 通常 250-450W，数据中心 GPU TDP 可达 400-1000W，需结合当地电价（如中国 0.5-1.5 元/kWh）计算

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（W * h * 1/kWh = kWh），消费级与数据中心GPU的TDP范围（250-450W vs 400-1000W）及中国电价范围（0.5-1.5元/kWh）符合当前工程常识与市场行情。

## Search Query

GPU power consumption annual electricity cost LLM inference server
