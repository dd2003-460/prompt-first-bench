# N340: 受影响用户数估算：N_affected_users = DAU * (1/10) * k_geo_overlap，其中k_geo_overlap为故障POP覆盖

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

受影响用户数估算：N_affected_users = DAU * (1/10) * k_geo_overlap，其中k_geo_overlap为故障POP覆盖用户与活跃用户重叠系数（约0.8-0.9），单次故障影响约40-45万用户

## Corrected Claim

受影响用户数估算：N_affected_users = DAU * (1/10) * k_geo_overlap，其中k_geo_overlap为故障POP覆盖用户与活跃用户重叠系数（约0.8-0.9），单次故障影响约40-45万用户

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构合理，k_geo_overlap取值0.8-0.9符合地理重叠系数的常见量级，最终估算值40-45万与输入参数在数量级上自洽。

## Search Query

CDN node failure affected user estimation geographic coverage
