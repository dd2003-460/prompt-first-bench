# N214: PUE（Power Usage Effectiveness）取值：自建边缘节点若部署在第三方机房，PUE 通常为 1.4-1.6（N63 取 1.5 合理）；若

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N63

## Claim

PUE（Power Usage Effectiveness）取值：自建边缘节点若部署在第三方机房，PUE 通常为 1.4-1.6（N63 取 1.5 合理）；若部署在自有机房或小型 IDC，PUE 可能高达 1.8-2.0（散热效率低），PUE 每增加 0.1，电力成本增加约 ¥288/月/POP（500W × 0.1 × 0.8 ¥/kWh × 720h）

## Corrected Claim

PUE（Power Usage Effectiveness）取值：自建边缘节点若部署在第三方机房，PUE 通常为 1.4-1.6（N63 取 1.5 合理）；若部署在自有机房或小型 IDC，PUE 可能高达 1.8-2.0（散热效率低），PUE 每增加 0.1，电力成本增加约 ¥288/月/POP（500W × 0.1 × 0.8 ¥/kWh × 720h）

## Evidence

先验知识/题面给定，逻辑校验通过：PUE范围符合行业常识，成本增量计算（500W*0.1*0.8*720=288元）数学正确且量纲合理。
