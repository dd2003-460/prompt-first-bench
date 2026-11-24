# N288: 云厂商单位存储价格的电力成本分摊公式：C_elec_cloud_per_TB = (P_base_per_TB * k_power * T_hours * E_

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N134

## Claim

云厂商单位存储价格的电力成本分摊公式：C_elec_cloud_per_TB = (P_base_per_TB * k_power * T_hours * E_price) / C_storage_price，其中 P_base_per_TB ≈ 0.05 W/TB（冷数据），E_price ≈ ¥0.6/kWh，若 C_storage_price = ¥120/TB/月，则电力分摊占比约为 (0.05*3.5*7200*0.6)/(120*30) ≈ 0.5%，表明云价中电力占比极低，主要成本是硬件折旧与运营。

## Corrected Claim

云厂商单位存储价格的电力成本分摊公式：C_elec_cloud_per_TB = (P_base_per_TB * k_power * T_hours * E_price) / C_storage_price，其中 P_base_per_TB ≈ 0.05 W/TB（冷数据），E_price ≈ ¥0.6/kWh，若 C_storage_price = ¥120/TB/月，则电力分摊占比约为 (0.05*3.5*7200*0.6)/(120*30) ≈ 0.5%，表明云价中电力占比极低，主要成本是硬件折旧与运营。

## Evidence

父节点级核验未通过：不完备（子节点分别针对公式中的三个核心变量（功率 P、电价 E、存储单价 C）进行独立修正和细化，彼此之间逻辑正交，无重复或矛盾。然而，父节点结论指出“主要成本是硬件折旧与运营”，但子节点仅讨论了电力成本的敏感性分析，未涵盖“硬件折旧”和“运营成本”这两个被父节点强调的关键成本构成要素，因此覆盖不全。）

## Search Query

cloud storage price breakdown electricity cost percentage
