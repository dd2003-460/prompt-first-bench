# N166: A6000 的 TDP 为 300 W，在 LLM 推理负载下平均功耗 P_avg ≈ 0.7 * 300 = 210 W；年电力成本（假设 7x24 运行，电

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

A6000 的 TDP 为 300 W，在 LLM 推理负载下平均功耗 P_avg ≈ 0.7 * 300 = 210 W；年电力成本（假设 7x24 运行，电价 $0.14/kWh）为 210 * 8760 * 0.14 ≈ $257.5 USD/年，略低于 L40S。

## Corrected Claim

A6000 的 TDP 为 300 W，在 LLM 推理负载下平均功耗 P_avg ≈ 0.7 * 300 = 210 W；年电力成本（假设 7x24 运行，电价 $0.14/kWh）为 210 * 8760 * 0.14 ≈ $257.5 USD/年，略低于 L40S。

## Evidence

先验知识/题面给定，逻辑校验通过：A6000 TDP 300W 符合 NVIDIA 官方规格；210W * 8760h * $0.14/kWh = $257,496/1000 ≈ $257.5 计算无误；L40S TDP 350W，同负载下成本更高，结论合理。
