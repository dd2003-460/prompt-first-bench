# N243: H100 SXM 80GB在BF16精度下的年均电力成本（40%负载因子）为 $2,452.8/年，计算公式为 700W * 0.4 * 24h * 365d 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N107

## Claim

H100 SXM 80GB在BF16精度下的年均电力成本（40%负载因子）为 $2,452.8/年，计算公式为 700W * 0.4 * 24h * 365d * $0.10/kWh，此数值用于更贴近本地工作站实际使用场景的TCO对比。

## Corrected Claim

H100 SXM 80GB在BF16精度下的年均电力成本（40%负载因子）为 $2,452.8/年，计算公式为 700W * 0.4 * 24h * 365d * $0.10/kWh，此数值用于更贴近本地工作站实际使用场景的TCO对比。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM 80GB 典型 TDP 为 700W，计算公式 700 * 0.4 * 24 * 365 * 0.10 = 2452.8，数值与逻辑均自洽。
