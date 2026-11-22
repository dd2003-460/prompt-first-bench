# N181: 共享随机源定义：卖家异质性偏好噪声 ε_seller 服从截断正态分布 N(0, σ_seller²)，其中 σ_seller = 0.15 * P_media

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

共享随机源定义：卖家异质性偏好噪声 ε_seller 服从截断正态分布 N(0, σ_seller²)，其中 σ_seller = 0.15 * P_median（基于 N29 中 σ_pref 的对称假设），截断范围为 [-0.25*P_median, 0.25*P_median]，确保 P_ask 波动在 15-25% 区间内。

## Corrected Claim

共享随机源定义：卖家异质性偏好噪声 ε_seller 服从截断正态分布 N(0, σ_seller²)，其中 σ_seller = 0.15 * P_median（基于 N29 中 σ_pref 的对称假设），截断范围为 [-0.25*P_median, 0.25*P_median]，确保 P_ask 波动在 15-25% 区间内。

## Evidence

先验知识/题面给定，逻辑校验通过：截断正态分布参数设定符合经济学模型中噪声项的常规量级（标准差0.15倍中位数，截断范围±0.25倍中位数），且内部逻辑自洽（截断范围大于标准差，确保分布有效），无来源矛盾。
