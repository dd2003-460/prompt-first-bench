# N123: 干预后预期成交周期 T_deal' 与基准周期 T_deal 的比值需通过加速匹配模型计算，假设降价触发算法曝光权重提升系数 W_boost，则 T_deal'

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42, N43, N44

## Claim

干预后预期成交周期 T_deal' 与基准周期 T_deal 的比值需通过加速匹配模型计算，假设降价触发算法曝光权重提升系数 W_boost，则 T_deal' = T_deal / (1 + W_boost)，其中 W_boost 取决于降价幅度 ΔP/P_ask 与平台算法敏感度

## Corrected Claim

干预后预期成交周期 T_deal' 与基准周期 T_deal 的比值需通过加速匹配模型计算，假设降价触发算法曝光权重提升系数 W_boost，则 T_deal' = T_deal / (1 + W_boost)，其中 W_boost 取决于降价幅度 ΔP/P_ask 与平台算法敏感度

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

impact of price reduction on transaction time e-commerce platform algorithm
