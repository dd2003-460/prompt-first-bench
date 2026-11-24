# N634: 工作点A的机柜租金分摊逻辑：C_colocation = (Rack_Rent_Total / N_Servers_Per_Rack)，假设42U机柜月租¥5,

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N211

## Claim

工作点A的机柜租金分摊逻辑：C_colocation = (Rack_Rent_Total / N_Servers_Per_Rack)，假设42U机柜月租¥5,000，每机柜部署4台高密度服务器，则单台分摊¥1,250；若部署密度提升至6台/机柜，分摊降至¥833，但需验证散热和电力容量是否支持。

## Corrected Claim

工作点A的机柜租金分摊逻辑：C_colocation = (Rack_Rent_Total / N_Servers_Per_Rack)，假设42U机柜月租¥5,000，每机柜部署4台高密度服务器，则单台分摊¥1,250；若部署密度提升至6台/机柜，分摊降至¥833，但需验证散热和电力容量是否支持。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（5000/4=1250, 5000/6≈833.33），且关于高密度部署需验证散热和电力容量的工程约束符合物理直觉。

## Search Query

colocation rack density cost per server high performance edge node
