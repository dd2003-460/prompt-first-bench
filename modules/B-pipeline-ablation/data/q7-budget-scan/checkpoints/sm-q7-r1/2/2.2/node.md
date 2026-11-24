# N12: HDD+SSD分层方案的CapEx构成：SSD层成本(100TB×¥150-300/TB) + HDD层成本(400TB×¥20-40/TB) + 分层管理硬件

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

HDD+SSD分层方案的CapEx构成：SSD层成本(100TB×¥150-300/TB) + HDD层成本(400TB×¥20-40/TB) + 分层管理硬件(缓存控制器/自动化迁移模块) + 服务器基础架构；HDD单价约为SSD的1/5-1/10，混合配置可显著降低初始投资

## Corrected Claim

HDD+SSD分层方案的CapEx构成：SSD层成本(100TB×¥150-300/TB) + HDD层成本(400TB×¥20-40/TB) + 分层管理硬件(缓存控制器/自动化迁移模块) + 服务器基础架构；HDD单价约为SSD的1/5-1/10，混合配置可显著降低初始投资

## Evidence

先验知识/题面给定，逻辑校验通过：HDD与SSD的单位容量成本差异符合行业常识（HDD通常比SSD便宜5-10倍），分层存储通过用低成本HDD承载冷数据、高成本SSD承载热数据来降低整体CapEx的逻辑自洽。
