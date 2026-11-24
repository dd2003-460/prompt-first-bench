# N669: 纯 NVMe SSD 方案总功耗 P_total_NVMe_Final 校准：500TB 数据需 500/7.68 ≈ 65 块 SSD，RAID6 后需 ce

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N277

## Claim

纯 NVMe SSD 方案总功耗 P_total_NVMe_Final 校准：500TB 数据需 500/7.68 ≈ 65 块 SSD，RAID6 后需 ceil(65*1.25)=82 块。单盘平均功耗 8.1W (同 N248)。P_drives = 82 * 8.1 = 664.2W。基础设施 P_infra_NVMe = 控制器(50W) + 背板(8%*664=53W) + 风扇(20W) ≈ 123W。P_total_NVMe = 664 + 123 = 787W。N277 原引用的 '2000W+' 严重高估，可能混淆了峰值功耗或包含了未优化的老旧设备。

## Corrected Claim

纯 NVMe SSD 方案总功耗 P_total_NVMe_Final 校准：500TB 数据需 500/7.68 ≈ 65 块 SSD，RAID6 后需 ceil(65*1.25)=82 块。单盘平均功耗 8.1W (同 N248)。P_drives = 82 * 8.1 = 664.2W。基础设施 P_infra_NVMe = 控制器(50W) + 背板(8%*664=53W) + 风扇(20W) ≈ 123W。P_total_NVMe = 664 + 123 = 787W。N277 原引用的 '2000W+' 严重高估，可能混淆了峰值功耗或包含了未优化的老旧设备。

## Evidence

[质询]RAID6 的冗余开销通常由数据盘和校验盘共同承担，简单的 1.25 倍系数（即 25% 开销）在某些 RAID 级别或配置下可能偏高或偏低，但作为工程估算的近似值在逻辑上是可接受的；此外，'2000W+' 的高估归因于峰值或老旧设备属于推测，但核心计算逻辑自洽。 | 先验知识/题面给定，逻辑校验通过：500TB/7.68TB≈65.1，取整65；65*1.25=81.25，向上取整82；82*8.1W=664.2W；基础设施估算合理；总和787W符合物理直觉。
