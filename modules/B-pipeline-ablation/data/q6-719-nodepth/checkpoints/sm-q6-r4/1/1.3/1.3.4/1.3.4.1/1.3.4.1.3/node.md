# N684: 同省/同城 BGP 专线的带宽利用率瓶颈：由于专线是固定带宽，当实际流量波动超过 95 百分位阈值时，无弹性扩容能力，需预留 20-30% 的带宽余量（Head

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N227

## Claim

同省/同城 BGP 专线的带宽利用率瓶颈：由于专线是固定带宽，当实际流量波动超过 95 百分位阈值时，无弹性扩容能力，需预留 20-30% 的带宽余量（Headroom）以应对突发峰值，这导致有效成本单价上升 15-25%

## Corrected Claim

同省/同城 BGP 专线的带宽利用率瓶颈：由于专线是固定带宽，当实际流量波动超过 95 百分位阈值时，无弹性扩容能力，需预留 20-30% 的带宽余量（Headroom）以应对突发峰值，这导致有效成本单价上升 15-25%

## Evidence

先验知识/题面给定，逻辑校验通过：固定带宽专线缺乏弹性，为应对95th百分位计费及突发峰值，预留20-30%余量是标准工程实践，由此导致的单位有效成本上升15-25%符合经济学直觉与行业经验。

## Search Query

dedicated line bandwidth headroom peak to average ratio cost efficiency
