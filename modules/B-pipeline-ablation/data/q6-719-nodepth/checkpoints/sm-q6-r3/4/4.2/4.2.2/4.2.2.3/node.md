# N277: 自建vs云托管监控的总成本对比：自建总成本 = Storage_Cost_Monthly + Maintenance_Labor_Monthly = 3,072

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

自建vs云托管监控的总成本对比：自建总成本 = Storage_Cost_Monthly + Maintenance_Labor_Monthly = 3,072 + 6,250 ≈ ¥9,322/月（一线SRE）或 3,072 + 4,500 ≈ ¥7,572/月（二线SRE）；云托管总成本 = ¥3,000/月。自建方案成本是云托管的2.5-3倍，但自建方案可提供更低延迟的数据查询（无网络传输开销），若数据查询延迟对故障恢复时间（MTTR）的影响显著，则自建方案的隐性收益需量化为 MTTR_reduction × Cost_Per_Min_Downtime。

## Corrected Claim

自建vs云托管监控的总成本对比：自建总成本 = Storage_Cost_Monthly + Maintenance_Labor_Monthly = 3,072 + 6,250 ≈ ¥9,322/月（一线SRE）或 3,072 + 4,500 ≈ ¥7,572/月（二线SRE）；云托管总成本 = ¥3,000/月。自建方案成本是云托管的2.5-3倍，但自建方案可提供更低延迟的数据查询（无网络传输开销），若数据查询延迟对故障恢复时间（MTTR）的影响显著，则自建方案的隐性收益需量化为 MTTR_reduction × Cost_Per_Min_Downtime。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（3072+6250=9322, 3072+4500=7572），倍数关系合理（9322/3000≈3.1, 7572/3000≈2.5），成本构成与MTTR量化逻辑符合工程常识。
