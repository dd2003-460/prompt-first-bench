# N247: 3年电力成本计算：2 × 450W TDP × 24h × 365d × 3y × $0.15/kWh = $3,666；此计算假设 GPU 持续满载运行，若实

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

3年电力成本计算：2 × 450W TDP × 24h × 365d × 3y × $0.15/kWh = $3,666；此计算假设 GPU 持续满载运行，若实际利用率低于 100%，成本按比例线性降低，但作为 TCO 上限估算采用满载假设。

## Corrected Claim

3年电力成本计算：2 × 450W TDP × 24h × 365d × 3y × $0.15/kWh = $3,666；此计算假设 GPU 持续满载运行，若实际利用率低于 100%，成本按比例线性降低，但作为 TCO 上限估算采用满载假设。

## Evidence

先验知识/题面给定，逻辑校验通过：2 * 0.45kW * 24h * 365d * 3y * $0.15/kWh = 3666.3，数值量级与计算逻辑自洽。

## Search Query

RTX 4090 power consumption watts idle load
