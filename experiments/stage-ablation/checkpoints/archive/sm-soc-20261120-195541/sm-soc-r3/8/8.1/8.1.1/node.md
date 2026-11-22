# N190: k1 的校准方法：通过对比降价前 7 天与降价后 48 小时的曝光量差异，k1 = (Impressions_pre - Impressions_post) /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

k1 的校准方法：通过对比降价前 7 天与降价后 48 小时的曝光量差异，k1 = (Impressions_pre - Impressions_post) / (ΔP / P_market)，需排除季节性波动（使用同比数据），若 k1 > 0.5 则支持强惩罚假设，否则需调整模型。

## Corrected Claim

k1 的校准方法：通过对比降价前 7 天与降价后 48 小时的曝光量差异，k1 = (Impressions_pre - Impressions_post) / (ΔP / P_market)，需排除季节性波动（使用同比数据），若 k1 > 0.5 则支持强惩罚假设，否则需调整模型。

## Evidence

先验知识/题面给定，逻辑校验通过
