# N472: L40S 的 TDP 为 350W，在 LLM 推理负载下平均功耗估算为 0.7 * 350W = 245W，年电力成本（7x24 运行, $0.15/kWh）

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N159

## Claim

L40S 的 TDP 为 350W，在 LLM 推理负载下平均功耗估算为 0.7 * 350W = 245W，年电力成本（7x24 运行, $0.15/kWh）约为 245W * 8760h * $0.15/kWh ≈ $321 USD/年

## Corrected Claim

L40S 的 TDP 为 350W，在 LLM 推理负载下平均功耗估算为 0.7 * 350W = 245W，年电力成本（7x24 运行, $0.15/kWh）约为 245W * 8760h * $0.15/kWh ≈ $321 USD/年

## Evidence

先验知识/题面给定，逻辑校验通过：L40S TDP 350W 符合 NVIDIA 官方规格；0.7 负载系数为合理工程估算；数学计算 245 * 8760 * 0.15 = 321,339 Wh * $0.15/kWh = $321.33，数值准确。
