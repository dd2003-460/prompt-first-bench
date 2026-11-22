# N201: 时间窗口 30 天的选择需验证其覆盖季节性波动：若商品类目存在强季节性（如羽绒服），30 天窗口可能跨越换季点，导致 P_median_30d_i 失真；需引入

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N64

## Claim

时间窗口 30 天的选择需验证其覆盖季节性波动：若商品类目存在强季节性（如羽绒服），30 天窗口可能跨越换季点，导致 P_median_30d_i 失真；需引入滚动窗口修正项 W_t = α*P_median_7d + (1-α)*P_median_30d，α 需根据历史数据自相关系数确定。

## Corrected Claim

时间窗口 30 天的选择需验证其覆盖季节性波动：若商品类目存在强季节性（如羽绒服），30 天窗口可能跨越换季点，导致 P_median_30d_i 失真；需引入滚动窗口修正项 W_t = α*P_median_7d + (1-α)*P_median_30d，α 需根据历史数据自相关系数确定。

## Evidence

先验知识/题面给定，逻辑校验通过：30天窗口跨越季节性换季点导致中位数失真是统计学常识，引入短周期（7天）与长周期（30天）的加权滚动窗口（EWMA/加权平均）以平衡噪声与滞后性是标准的时序平滑处理手段，逻辑自洽且符合数据工程最佳实践。

## Search Query

rolling window price median seasonal adjustment e-commerce
