# N75: 惩罚阈值 T_penalty 的博弈论基础：平台设置 T_penalty = 72h 是基于卖家平均决策周期 T_seller 的 3 倍标准差，即 T_pen

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

惩罚阈值 T_penalty 的博弈论基础：平台设置 T_penalty = 72h 是基于卖家平均决策周期 T_seller 的 3 倍标准差，即 T_penalty = 3 * σ_T_seller。若卖家在 72h 内未成交，算法判定为‘低效商品’并降低曝光，这一阈值设计使得卖家必须在 T_penalty 前维持高曝光以获取 W_boost，从而形成均衡。

## Corrected Claim

惩罚阈值 T_penalty 的博弈论基础：平台设置 T_penalty = 72h 是基于卖家平均决策周期 T_seller 的 3 倍标准差，即 T_penalty = 3 * σ_T_seller。若卖家在 72h 内未成交，算法判定为‘低效商品’并降低曝光，这一阈值设计使得卖家必须在 T_penalty 前维持高曝光以获取 W_boost，从而形成均衡。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

penalty threshold algorithm seller decision cycle standard deviation
