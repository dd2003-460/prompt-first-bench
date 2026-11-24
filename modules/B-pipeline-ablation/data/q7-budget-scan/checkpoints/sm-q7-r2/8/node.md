# N45: 数据丢失风险期望损失(EL) = ALE * 概率。本地HDD RAID6在双盘故障下的数据丢失概率约为0.05% (基于MTBF和重建时间窗口)，云存储S3为

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

数据丢失风险期望损失(EL) = ALE * 概率。本地HDD RAID6在双盘故障下的数据丢失概率约为0.05% (基于MTBF和重建时间窗口)，云存储S3为1e-11。若数据价值为¥100/TB，500TB总价值¥50,000,000，本地方案年期望损失≈¥25,000，云方案≈¥0.0005。

## Corrected Claim

数据丢失风险期望损失(EL) = ALE * 概率。本地HDD RAID6在双盘故障下的数据丢失概率需根据具体硬盘MTBF和重建时间计算（典型值可能在0.01%-1%区间，0.05%为一种估算），云存储S3持久性为11个9（1e-11）。若数据价值为¥100/TB，500TB总价值¥50,000,000，基于0.05%概率的本地方案年期望损失≈¥25,000，云方案≈¥0.0005。

## Evidence

[质询]RAID6双盘故障导致数据丢失的概率并非固定值，而是高度依赖于硬盘容量、MTBF、重建时间窗口及URE率等具体参数，0.05%这一数值缺乏特定硬件配置的支撑，属于经验估算而非通用事实；此外，S3的1e-11通常指对象持久性（11个9），直接等同于“数据丢失概率”在口径上存在细微差异（虽在量级上兼容，但严格来说持久性≠单次访问丢失概率，尽管在EL计算中常混用）。 | 来源[1][2][3]仅讨论RAID6重建机制和URE风险定性，未提供具体的0.05%概率数值或S3的1e-11具体数值支持；该事实为经验性工程估算，逻辑自洽但缺乏直接来源支持具体数值。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_31236101/article/details/161966249&rut=1ed4d47e1426e87710be553fd7a0c39dc2002e5a0479eccfa7aba85ba0ef7ede', 'type': 'ddg', 'title': 'Raid5重建失败数据全丢？从硬盘容量翻倍的时代，重新审视raid6的必要性-csdn博客'}
- {'url': 'https://www.v2ex.com/t/659670&rut=deee5fbbca75956b9de38b758eea9d6310f6ced3bec0b7a20b725cc1130811dc', 'type': 'ddg', 'title': 'Raid6 的重建失败概率是怎么计算的？ - V2ex'}
- {'url': 'https://www.sosit.com.cn/2025/de_yjxw_0120/16958.html&rut=2d15d0fd20c0c5ccca154c92f1ce91dcc95ad743a1d55ed029bfcce5e73bf7e0', 'type': 'ddg', 'title': 'raid6重建 机制，raid6重建失败概率计算_恢复教程_恢复资讯_技王数据恢复'}
