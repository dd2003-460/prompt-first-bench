# N182: 在覆盖半径 R=50km 的基准工作点下，光纤单程传播延迟 L_prop = 50km / 200,000km/s = 0.25ms，往返基础延迟 RTT_ba

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

在覆盖半径 R=50km 的基准工作点下，光纤单程传播延迟 L_prop = 50km / 200,000km/s = 0.25ms，往返基础延迟 RTT_base = 2 * 0.25ms + 2.5ms (L_switching中值) = 3.0ms。

## Corrected Claim

在覆盖半径 R=50km 的基准工作点下，光纤单程传播延迟 L_prop = 50km / 200,000km/s = 0.25ms，往返基础延迟 RTT_base = 2 * 0.25ms + 2.5ms (L_switching中值) = 3.0ms。

## Evidence

先验知识/题面给定，逻辑校验通过：光速在光纤中约为200,000km/s，50km/200,000km/s=0.25ms，2*0.25ms+2.5ms=3.0ms，计算无误。

## Search Query

fiber optic propagation delay calculation 200km/s
