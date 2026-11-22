# N468: H100 SXM5 的 TDP 为 700W，在 LLM 推理负载下平均功耗估算为 0.7 * 700W = 490W，年电力成本（7x24 运行, $0.15

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N158

## Claim

H100 SXM5 的 TDP 为 700W，在 LLM 推理负载下平均功耗估算为 0.7 * 700W = 490W，年电力成本（7x24 运行, $0.15/kWh）约为 490W * 8760h * $0.15/kWh ≈ $644 USD/年

## Corrected Claim

H100 SXM5 的 TDP 为 700W，在 LLM 推理负载下平均功耗估算为 0.7 * 700W = 490W，年电力成本（7x24 运行, $0.15/kWh）约为 490W * 8760h * $0.15/kWh ≈ $644 USD/年

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 TDP 700W 为公开规格，0.7 负载系数及电价计算符合算术逻辑，无来源矛盾。
