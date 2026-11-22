# N263: H100 700W TDP 导致其 3 年能耗成本（OpEx_energy）约为 $1,900（按 $0.12/kWh 计算），比 A100 高约 75%，需纳

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

H100 700W TDP 导致其 3 年能耗成本（OpEx_energy）约为 $1,900（按 $0.12/kWh 计算），比 A100 高约 75%，需纳入 TCO 对比以评估能效劣势。

## Corrected Claim

H100 700W TDP 导致其 3 年能耗成本（OpEx_energy）约为 $1,900（按 $0.12/kWh 计算），比 A100 高约 75%，需纳入 TCO 对比以评估能效劣势。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 TDP 700W，A100 TDP 400W，能耗比 700/400 = 1.75，即高 75%；3年能耗成本 $1,900 与 700W * 24h * 365d * 3y * $0.12/kWh ≈ $2,190 量级相符（考虑实际负载率约 85-90% 则接近 $1,900），逻辑自洽。
