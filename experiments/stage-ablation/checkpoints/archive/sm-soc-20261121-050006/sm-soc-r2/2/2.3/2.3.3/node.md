# N62: 下游投影 2（广告收益项）：Data_value * N_users 项中，Data_value 具体化为每用户日均广告收入 ARPU_ad = eCPM * 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N12

## Claim

下游投影 2（广告收益项）：Data_value * N_users 项中，Data_value 具体化为每用户日均广告收入 ARPU_ad = eCPM * Impressions_per_user / 1000；高挂价商品占据列表页增加浏览深度 Time_on_site，从而增加 Impressions_per_user；量化关系为 ΔARPU_ad ≈ δ_ad * ΔTime_on_site，其中 δ_ad ≈ 0.5-1.0 元/商品/天，是平台维持高挂价均衡的直接财务动机。

## Corrected Claim

下游投影 2（广告收益项）：Data_value * N_users 项中，Data_value 具体化为每用户日均广告收入 ARPU_ad = eCPM * Impressions_per_user / 1000；高挂价商品可能通过增加列表页停留时间（Time_on_site）从而增加 Impressions_per_user，进而提升 ARPU_ad。具体的量化关系需结合平台实际 eCPM 和浏览深度弹性系数确定，δ_ad 的具体数值（0.5-1.0 元/商品/天）缺乏通用性，应视为特定场景下的估算值而非通用常数。

## Evidence

[质询]数值量级与逻辑推导存在严重矛盾：δ_ad 定义为 0.5-1.0 元/商品/天，但 ARPU_ad 的单位是 元/用户/天。若按公式 ΔARPU_ad ≈ δ_ad * ΔTime_on_site 计算，量纲不匹配（除非隐含了浏览商品数，但公式未体现）。更关键的是，若 δ_ad 代表每增加1天浏览时间带来的ARPU增量，0.5-1.0元/天的增量对于电商广告而言过于微小，无法构成“直接财务动机”去维持高挂价均衡（通常高挂价带来的广告收益增量远高于此，或该参数定义模糊，混淆了单次曝光收益与日均收益）。此外，将“高挂价商品”直接等同于“增加浏览深度”缺乏因果必然性，高挂价可能导致用户快速跳出，反而降低 Time_on_site。 | source=knowledge，但逻辑校验发现量纲/量级不合理及因果链条薄弱，且无外部来源支持该具体数值参数。

## Search Query

average revenue per user advertising eCPM impressions time on site platform revenue
