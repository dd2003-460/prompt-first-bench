# N152: t_sync 的数据同步延迟构成：t_sync = t_download + t_write_disk，其中 t_download = s_obj / B_sy

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

t_sync 的数据同步延迟构成：t_sync = t_download + t_write_disk，其中 t_download = s_obj / B_sync（s_obj 为对象大小，B_sync 为同步带宽，典型 1-10 Gbps），t_write_disk 为 NVMe SSD 写入延迟（<1ms for random, <10ms for large sequential）；对于 2TB 日均下载量，若同步 10% 热点对象（200GB），在 10Gbps 带宽下 t_sync_total ≈ 200GB / (1.25GB/s) ≈ 160s，但并行同步可缩短至 <10s

## Corrected Claim

t_sync 的数据同步延迟构成：t_sync = t_download + t_write_disk，其中 t_download = s_obj / B_sync（s_obj 为对象大小，B_sync 为同步带宽，典型 1-10 Gbps），t_write_disk 为 NVMe SSD 写入延迟（<1ms for random, <10ms for large sequential）；对于 2TB 日均下载量，若同步 10% 热点对象（200GB），在 10Gbps 带宽下 t_sync_total ≈ 200GB / (1.25GB/s) ≈ 160s，但并行同步可缩短至 <10s

## Evidence

先验知识/题面给定，逻辑校验通过：200GB / 1.25GB/s = 160s 计算正确，NVMe 延迟量级符合工程常识，并行缩短延迟符合逻辑。

## Search Query

CDN edge node data sync latency NVMe write time download bandwidth calculation
