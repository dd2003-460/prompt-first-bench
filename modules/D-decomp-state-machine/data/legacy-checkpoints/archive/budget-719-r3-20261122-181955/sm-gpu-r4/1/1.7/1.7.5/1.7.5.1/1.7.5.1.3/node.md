# N657: L40S 的 TDP 为 350W，在 LLM 推理负载下平均功耗约为 0.7 * 350W = 245W；基于 $0.14/kWh 电价，年电力成本 = 24

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N233

## Claim

L40S 的 TDP 为 350W，在 LLM 推理负载下平均功耗约为 0.7 * 350W = 245W；基于 $0.14/kWh 电价，年电力成本 = 245W * 8760h * $0.14/kWh ≈ $300 USD/年；3 年 TCO 中电力项为 $900 USD，需与硬件成本（$2,000-$3,000）相加以计算总 TCO。

## Corrected Claim

L40S 的 TDP 为 350W，在 LLM 推理负载下平均功耗约为 0.7 * 350W = 245W；基于 $0.14/kWh 电价，年电力成本 = 245W * 8760h * $0.14/kWh ≈ $300 USD/年；3 年 TCO 中电力项为 $900 USD，需与硬件成本（$2,000-$3,000）相加以计算总 TCO。

## Evidence

先验知识/题面给定，逻辑校验通过：245W * 8760h * 0.14 USD/kWh ≈ 300.3 USD/年，3年约900 USD，计算无误且量级合理。
