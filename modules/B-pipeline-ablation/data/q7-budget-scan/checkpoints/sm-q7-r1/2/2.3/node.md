# N13: 云对象存储的CapEx近似为零，但OpEx包含：标准存储费用(¥/GB/月) + 低频/归档存储转换费用 + 数据取回费用(按GB计费) + API请求费用(按

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

云对象存储的CapEx近似为零，但OpEx包含：标准存储费用(¥/GB/月) + 低频/归档存储转换费用 + 数据取回费用(按GB计费) + API请求费用(按万次请求计费)；对于500TB数据，假设80%转为低频存储，月度OpEx = 400TB×¥10/TB/月 + 100TB×¥20/TB/月 + 取回流量费用

## Corrected Claim

云对象存储的CapEx近似为零，但OpEx包含：标准存储费用(¥/GB/月) + 低频/归档存储转换费用 + 数据取回费用(按GB计费) + API请求费用(按万次请求计费)；对于500TB数据，假设80%转为低频存储，月度OpEx = 400TB×¥10/TB/月 + 100TB×¥20/TB/月 + 取回流量费用

## Evidence

先验知识/题面给定，逻辑校验通过
