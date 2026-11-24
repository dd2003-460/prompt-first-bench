# N441: RAID6 重建对 HDD 层业务带宽的挤占量化：业务可用带宽 B_biz_avail = B_total * (1 - f_bandwidth_rebuild

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N193

## Claim

RAID6 重建对 HDD 层业务带宽的挤占量化：业务可用带宽 B_biz_avail = B_total * (1 - f_bandwidth_rebuild)，其中 f_bandwidth_rebuild ≈ 40% (典型值)，若 B_total=14.5GB/s (145 disks * 100MB/s)，则 B_biz_avail ≈ 8.7GB/s，业务吞吐下降 40%

## Corrected Claim

RAID6 重建对 HDD 层业务带宽的挤占量化：业务可用带宽 B_biz_avail = B_total * (1 - f_bandwidth_rebuild)，其中 f_bandwidth_rebuild ≈ 40% (典型值)，若 B_total=14.5GB/s (145 disks * 100MB/s)，则 B_biz_avail ≈ 8.7GB/s，业务吞吐下降 40%

## Evidence

先验知识/题面给定，逻辑校验通过：RAID6重建期间HDD需同时处理数据读取和奇偶校验计算，通常消耗约30%-50%的I/O带宽，40%为典型工程估算值；算术运算 14.5 * (1 - 0.4) = 8.7 正确，量纲一致。
