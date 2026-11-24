# N603: RAID10 在 NVMe 环境下的写入放大系数 (Write Amplification Factor, WAF) 为 2.0 (每 1 字节用户数据写入 2

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N207

## Claim

RAID10 在 NVMe 环境下的写入放大系数 (Write Amplification Factor, WAF) 为 2.0 (每 1 字节用户数据写入 2 字节物理数据)，而 RAID5 为 4.0；结合 N406 的 DWPD 计算，RAID10 的有效 DWPD 为标称值的一半 (0.5 DWPD)，这进一步缩短了 SSD 寿命，需将 N408 中的 Life_Days 除以 2 重新计算更换频率。

## Corrected Claim

RAID10 在 NVMe 环境下的写入放大系数 (Write Amplification Factor, WAF) 为 2.0 (每 1 字节用户数据写入 2 字节物理数据)，而 RAID5 为 4.0；结合 N406 的 DWPD 计算，RAID10 的有效 DWPD 为标称值的一半 (0.5 DWPD)，这进一步缩短了 SSD 寿命，需将 N408 中的 Life_Days 除以 2 重新计算更换频率。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID10 写入放大系数为 2.0（镜像写入），RAID5 为 4.0（读-改-写），符合存储原理；DWPD 与 WAF 成反比，逻辑自洽。

## Search Query

NVMe RAID10 write amplification factor impact on SSD endurance DWPD
