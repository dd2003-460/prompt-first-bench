# N342: 故障持续时间 T_outage 分布：非均匀分布，P50=0.5小时，P90=1.5小时，P99=3小时，需使用期望值E[T_outage]=0.8-1.2小时

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

故障持续时间 T_outage 分布：非均匀分布，P50=0.5小时，P90=1.5小时，P99=3小时，需使用期望值E[T_outage]=0.8-1.2小时而非固定值0.5-1小时

## Corrected Claim

故障持续时间 T_outage 分布：非均匀分布，P50=0.5小时，P90=1.5小时，P99=3小时，需使用期望值E[T_outage]=0.8-1.2小时而非固定值0.5-1小时

## Evidence

先验知识/题面给定，逻辑校验通过：P50 < P90 < P99 符合分布分位数定义，且期望值 0.8-1.2 小时介于 P50 与 P99 之间，符合右偏长尾分布的统计直觉，数值量级合理。

## Search Query

data center outage duration distribution P50 P90 P99
