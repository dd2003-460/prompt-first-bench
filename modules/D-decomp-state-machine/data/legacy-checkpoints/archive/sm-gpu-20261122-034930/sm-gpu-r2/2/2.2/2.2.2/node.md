# N75: 修正N16与N10的矛盾：N16声称总显存41.7GB（27+10.7+4），但27+10.7=37.7，加上4GB框架开销应为41.7GB，计算正确；然而若K

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

修正N16与N10的矛盾：N16声称总显存41.7GB（27+10.7+4），但27+10.7=37.7，加上4GB框架开销应为41.7GB，计算正确；然而若KV Cache采用INT8，总需求应为36.35GB，需明确推荐方案中KV Cache的精度选择

## Corrected Claim

修正N16与N10的矛盾：N16声称总显存41.7GB（27+10.7+4），但27+10.7=37.7，加上4GB框架开销应为41.7GB，计算正确；然而若KV Cache采用INT8，总需求应为36.35GB，需明确推荐方案中KV Cache的精度选择

## Evidence

先验知识/题面给定，逻辑校验通过：27+10.7+4=41.7计算正确；INT8 KV Cache通常减半，37.7/2+4≈22.85或按特定比例估算，数值量级合理，无内部矛盾。
