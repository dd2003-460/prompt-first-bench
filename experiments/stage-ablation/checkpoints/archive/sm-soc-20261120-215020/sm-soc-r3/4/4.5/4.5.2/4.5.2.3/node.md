# N186: 高溢价卖家 GMV 贡献占比 $S_{high}$ 的估算公式：$S_{high} \approx S_{top5} \times p_{high|top} +

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N63

## Claim

高溢价卖家 GMV 贡献占比 $S_{high}$ 的估算公式：$S_{high} \approx S_{top5} \times p_{high|top} + (1 - S_{top5}) \times p_{high|longtail}$，其中 $p_{high|longtail}$ 为长尾卖家中高溢价比例（假设较低，如 0.1），用于量化 $S_{high}$ 是否低于 20%。

## Corrected Claim

高溢价卖家 GMV 贡献占比 $S_{high}$ 的估算公式：$S_{high} \approx S_{top5} \times p_{high|top} + (1 - S_{top5}) \times p_{high|longtail}$，其中 $p_{high|longtail}$ 为长尾卖家中高溢价比例（假设较低，如 0.1），用于量化 $S_{high}$ 是否低于 20%。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式基于全概率公式（Total Probability Theorem）对卖家群体进行Top5与长尾的二分法拆解，数学结构自洽，量纲正确（占比乘以比例等于占比），且作为估算模型逻辑合理。
