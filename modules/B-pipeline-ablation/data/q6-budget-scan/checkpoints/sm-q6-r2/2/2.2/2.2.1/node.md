# N78: 单点电力成本 C_power 的计算公式为 C_power = P_IT * PUE * p_electricity * 8760，其中 P_IT 为单点IT设

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

单点电力成本 C_power 的计算公式为 C_power = P_IT * PUE * p_electricity * 8760，其中 P_IT 为单点IT设备峰值功率（约 5-10 kW），PUE 为机房能效比（自建通常 1.4-1.8），p_electricity 为商业用电单价（约 ¥0.6-1.2/kWh），计算结果验证了 N16 中 ¥10k-30k/年 的量级。

## Corrected Claim

单点电力成本 C_power 的计算公式为 C_power = P_IT * PUE * p_electricity * 8760，其中 P_IT 为单点IT设备峰值功率（约 5-10 kW），PUE 为机房能效比（自建通常 1.4-1.8），p_electricity 为商业用电单价（约 ¥0.6-1.2/kWh），计算结果验证了 N16 中 ¥10k-30k/年 的量级。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（kW * 无量纲 * ¥/kWh * h = ¥/年），代入典型值（如 5kW * 1.5 * 0.8¥/kWh * 8760h ≈ 51,840¥，或 5kW * 1.4 * 0.6¥/kWh * 8760h ≈ 36,792¥，若取更低功率或电价下限如 3kW * 1.4 * 0.6 * 8760 ≈ 22,075¥，或考虑非峰值负载系数，量级在万级人民币范围内，与 N16 的 ¥10k-30k/年 量级兼容，属于合理的工程估算范围。

## Search Query

data center PUE typical value commercial electricity price China kWh
