# N62: 下游投影 2（广告收益项）：Data_value * N_users 项中，Data_value 具体化为每用户日均广告收入 ARPU_ad = eCPM * 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N12

## Claim

下游投影 2（广告收益项）：Data_value * N_users 项中，Data_value 具体化为每用户日均广告收入 ARPU_ad = eCPM * Impressions_per_user / 1000；高挂价商品占据列表页增加浏览深度 Time_on_site，从而增加 Impressions_per_user；量化关系为 ΔARPU_ad ≈ δ_ad * ΔTime_on_site，其中 δ_ad ≈ 0.5-1.0 元/商品/天，是平台维持高挂价均衡的直接财务动机。

## Corrected Claim

下游投影 2（广告收益项）：Data_value * N_users 项中，Data_value 具体化为每用户日均广告收入 ARPU_ad = eCPM * Impressions_per_user / 1000；高挂价商品可能通过增加列表页停留时间（Time_on_site）从而增加 Impressions_per_user，进而提升 ARPU_ad。具体的量化关系需结合平台实际 eCPM 和浏览深度弹性系数确定，δ_ad 的具体数值（0.5-1.0 元/商品/天）缺乏通用性，应视为特定场景下的估算值而非通用常数。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1（共享随机源定义）与子节点2（浏览深度与广告库存关系）存在严重内容重叠，均重复描述了 ARPU_ad 的公式及 Time_on_site 对 Impressions_per_user 的影响机制，未体现正交性；子节点1中“随机源”的定义在父节点中未明确涉及，且与子节点2的确定性传导路径逻辑不匹配。）

## Search Query

average revenue per user advertising eCPM impressions time on site platform revenue
