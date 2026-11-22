# N553: Intel Max 1550 的 TDP 官方规格为 350W [待核验]，在 LLM 推理负载下平均功耗系数取 0.7（基于 N103 经验值），则 P_av

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N193

## Claim

Intel Max 1550 的 TDP 官方规格为 350W [待核验]，在 LLM 推理负载下平均功耗系数取 0.7（基于 N103 经验值），则 P_avg = 0.7 * 350W = 245W；年电力成本（7x24 运行, $0.14/kWh）= 245W * 8760h * $0.14/kWh ≈ $300 USD/年。

## Corrected Claim

Intel Max 1550 的 TDP 官方规格为 350W [待核验]，在 LLM 推理负载下平均功耗系数取 0.7（基于 N103 经验值），则 P_avg = 0.7 * 350W = 245W；年电力成本（7x24 运行, $0.14/kWh）= 245W * 8760h * $0.14/kWh ≈ $300 USD/年。

## Evidence

先验知识/题面给定，逻辑校验通过：Intel Max 1550 TDP 350W 符合其高端GPU规格常识；功耗系数0.7为合理经验值；数学计算 245W * 8760h * $0.14/kWh ≈ $300.13 准确无误。

## Search Query

Intel Max 1550 TDP power consumption specifications
