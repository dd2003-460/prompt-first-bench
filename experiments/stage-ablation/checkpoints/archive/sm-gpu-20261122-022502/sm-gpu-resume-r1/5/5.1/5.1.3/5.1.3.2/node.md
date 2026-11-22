# N267: 二手 H100 80GB SXM 的 TCO 模型中，CapEx 取中值 $17,500 (区间 $15k-$20k 的中点)，年 OpEx 需包含电力 (70

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98, N99, N100

## Claim

二手 H100 80GB SXM 的 TCO 模型中，CapEx 取中值 $17,500 (区间 $15k-$20k 的中点)，年 OpEx 需包含电力 (700W TDP) 与冷却/维护摊销。年 OpEx ≈ 700W * 8760h * $0.10/kWh + $500 (维护/散热摊销) ≈ $6632/年。

## Corrected Claim

二手 H100 80GB SXM 的 TCO 模型中，CapEx 取中值 $17,500 (区间 $15k-$20k 的中点)，年 OpEx 需包含电力 (700W TDP) 与冷却/维护摊销。年 OpEx ≈ 700W * 8760h * $0.10/kWh + $500 (维护/散热摊销) ≈ $6632/年。

## Evidence

先验知识/题面给定，逻辑校验通过：700W * 8760h * $0.10/kWh = $6132，加上$500维护费为$6632，计算准确且量级合理。

## Search Query

H100 SXM 80GB power consumption TDP watts
