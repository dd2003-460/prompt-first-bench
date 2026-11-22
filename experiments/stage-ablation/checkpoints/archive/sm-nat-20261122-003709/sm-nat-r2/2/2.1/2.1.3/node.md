# N43: 引入更新率对 LFU 的滞后惩罚项：LFU 的频率计数器收敛时间 T_conv ≈ 1/λ_update = 100 天。在 T_conv 期间，LFU 的命中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

引入更新率对 LFU 的滞后惩罚项：LFU 的频率计数器收敛时间 T_conv ≈ 1/λ_update = 100 天。在 T_conv 期间，LFU 的命中率 H_LFU(t) 低于稳态值。计算前 100 天的平均命中率损失 ΔH_lag，该值需从 ΔH_max 中扣除，得到净提升 ΔH_net = ΔH_max - ΔH_lag。ΔH_lag 可通过积分 H_LFU(t) - H_LRU(t) 从 0 到 100 天求得

## Corrected Claim

引入更新率对 LFU 的滞后惩罚项：LFU 的频率计数器收敛时间 T_conv ≈ 1/λ_update = 100 天。在 T_conv 期间，LFU 的命中率 H_LFU(t) 低于稳态值。计算前 100 天的平均命中率损失 ΔH_lag，该值需从 ΔH_max 中扣除，得到净提升 ΔH_net = ΔH_max - ΔH_lag。ΔH_lag 可通过积分 H_LFU(t) - H_LRU(t) 从 0 到 100 天求得

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 频率计数器收敛时间与更新率倒数成正比符合指数衰减模型直觉，积分计算滞后损失的方法论在逻辑上自洽且量纲合理。
