# N189: 工作点C（低敏感度/极弱信任冲击）：假设 β_perception = 0.1（用户群体对平台策略不敏感，如高粘性B端卖家），ΔTrustShock = 0.0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

工作点C（低敏感度/极弱信任冲击）：假设 β_perception = 0.1（用户群体对平台策略不敏感，如高粘性B端卖家），ΔTrustShock = 0.05（基于细微算法权重调整，几乎无感知）。则 ΔChurnRate = 0.1 * 0.05 = 0.005，即用户流失率上升0.5个百分点，可忽略不计。

## Corrected Claim

工作点C（低敏感度/极弱信任冲击）：假设 β_perception = 0.1（用户群体对平台策略不敏感，如高粘性B端卖家），ΔTrustShock = 0.05（基于细微算法权重调整，几乎无感知）。则 ΔChurnRate = 0.1 * 0.05 = 0.005，即用户流失率上升0.5个百分点，可忽略不计。

## Evidence

先验知识/题面给定，逻辑校验通过：乘法运算 0.1 * 0.05 = 0.005 正确，0.005 对应 0.5 个百分点的表述准确，符合线性模型假设下的计算逻辑。

## Search Query

low churn rate insensitive users minor algorithm adjustment
