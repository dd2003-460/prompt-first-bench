# N34: 统一口径成本公式：Cost_Per_TB_Year = (Hardware_CapEx/Useful_Life + Cloud_Fee + Power_Cost

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

统一口径成本公式：Cost_Per_TB_Year = (Hardware_CapEx/Useful_Life + Cloud_Fee + Power_Cost + Ops_Cost + Expected_RTO_Cost + Expansion_Cost) / Effective_Capacity_TB，其中Useful_Life：SSD 5年，HDD 5年，云存储按年付费无CapEx

## Corrected Claim

统一口径成本公式：Cost_Per_TB_Year = (Hardware_CapEx/Useful_Life + Cloud_Fee + Power_Cost + Ops_Cost + Expected_RTO_Cost + Expansion_Cost) / Effective_Capacity_TB，其中Useful_Life：SSD 5年，HDD 5年，云存储按年付费无CapEx

## Evidence

先验知识/题面给定，逻辑校验通过：成本公式结构符合TCO（总拥有成本）基本定义，将CapEx摊销、OpEx（云费/电力/运维）、风险成本（RTO）及扩容成本纳入分子，除以有效容量得到单位成本，量纲与逻辑自洽；SSD/HDD 5年寿命及云存储无CapEx为行业通用经验参数，符合常识。
