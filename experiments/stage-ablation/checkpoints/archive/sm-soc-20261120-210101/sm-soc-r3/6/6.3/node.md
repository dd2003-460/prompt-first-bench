# N105: E_drop 的'降价幅度' %ΔPrice_drop 定义为 (P_pre_drop - P_post_drop) / P_pre_drop，且必须控制降价后

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27, N28, N29

## Claim

E_drop 的'降价幅度' %ΔPrice_drop 定义为 (P_pre_drop - P_post_drop) / P_pre_drop，且必须控制降价后的'曝光重置'效应：若平台在降价后重置了推荐权重，则需引入修正项 W_reset ∈ [0.8, 1.2]，实际弹性 E_drop_adj = E_drop_raw / W_reset。

## Corrected Claim

E_drop 的'降价幅度' %ΔPrice_drop 定义为 (P_pre_drop - P_post_drop) / P_pre_drop，且必须控制降价后的'曝光重置'效应：若平台在降价后重置了推荐权重，则需引入修正项 W_reset ∈ [0.8, 1.2]，实际弹性 E_drop_adj = E_drop_raw / W_reset。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

price drop exposure weight reset recommendation algorithm
