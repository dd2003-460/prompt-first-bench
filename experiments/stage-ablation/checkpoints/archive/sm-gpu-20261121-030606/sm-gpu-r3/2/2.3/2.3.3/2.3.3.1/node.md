# N242: H100 SXM 80GB在BF16精度下的年均电力成本（满载）为 $6,132/年，计算公式为 700W * 24h * 365d * $0.10/kWh，此

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N107

## Claim

H100 SXM 80GB在BF16精度下的年均电力成本（满载）为 $6,132/年，计算公式为 700W * 24h * 365d * $0.10/kWh，此数值用于TCO长期持有成本对比，修正了N26中基于部分负载的低估。

## Corrected Claim

H100 SXM 80GB在BF16精度下的年均电力成本（满载）为 $6,132/年，计算公式为 700W * 24h * 365d * $0.10/kWh，此数值用于TCO长期持有成本对比，修正了N26中基于部分负载的低估。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM 80GB TDP 为 700W，计算公式 700 * 24 * 365 * 0.1 = 6132 正确，符合满载年均电力成本定义。
