# N637: 工作点B的机柜租金分摊逻辑：C_colocation = (Rack_Rent_Total / N_Servers_Per_Rack)，假设42U机柜月租¥3,

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N212

## Claim

工作点B的机柜租金分摊逻辑：C_colocation = (Rack_Rent_Total / N_Servers_Per_Rack)，假设42U机柜月租¥3,000（二线城市），每机柜部署6台标准密度服务器，则单台分摊¥500；若部署密度提升至8台/机柜，分摊降至¥375，但需验证散热和电力容量是否支持。

## Corrected Claim

工作点B的机柜租金分摊逻辑：C_colocation = (Rack_Rent_Total / N_Servers_Per_Rack)，假设42U机柜月租¥3,000（二线城市），每机柜部署6台标准密度服务器，则单台分摊¥500；若部署密度提升至8台/机柜，分摊降至¥375，但需验证散热和电力容量是否支持。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（3000/6=500, 3000/8=375），且42U机柜部署6-8台服务器符合标准密度服务器（通常2U-4U）的物理空间限制，散热与电力提示符合工程常识。

## Search Query

second tier city colocation rack cost standard server density
