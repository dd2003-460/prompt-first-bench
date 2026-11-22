# N310: 电价敏感度临界值计算：设TCO_A = P_A + W_A * h * r * 3，∂TCO_A/∂r = W_A * h * 3；对于4090（W=450W,

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

电价敏感度临界值计算：设TCO_A = P_A + W_A * h * r * 3，∂TCO_A/∂r = W_A * h * 3；对于4090（W=450W, h=2000h/年），∂TCO_4090/∂r = $2,700；对于L40S（W=350W, h=2000h/年），∂TCO_L40S/∂r = $2,100；排名翻转临界电价Δr = |TCO_4090 - TCO_L40S| / (2700 - 2100) = |TCO_diff| / 600 $/kWh

## Corrected Claim

电价敏感度临界值计算：设TCO_A = P_A + W_A * h * r * 3，∂TCO_A/∂r = W_A * h * 3；对于4090（W=450W, h=2000h/年），∂TCO_4090/∂r = $2,700；对于L40S（W=350W, h=2000h/年），∂TCO_L40S/∂r = $2,100；排名翻转临界电价Δr = |TCO_4090 - TCO_L40S| / (2700 - 2100) = |TCO_diff| / 600 $/kWh

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，数值计算（450*2000*3=2700, 350*2000*3=2100, 差值600）准确，量纲一致。

## Search Query

electricity price sensitivity TCO ranking flip threshold
