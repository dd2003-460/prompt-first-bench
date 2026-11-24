# N288: 云厂商单位存储价格的电力成本分摊公式：C_elec_cloud_per_TB = (P_base_per_TB * k_power * T_hours * E_

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（三个子节点分别针对公式中的分子参数（功率密度）、电价变量以及分母/时间维度（存储层级与TCO结构）进行独立修正，彼此无逻辑冲突或内容重叠，且完整覆盖了原公式中所有关键假设的局限性。）

## Search Query

cloud storage price breakdown electricity cost percentage
