# N399: 写 IOPS 与缓存失效开销：日均上传 200GB，峰值 4 小时，写速率 = 200GB/4h = 50GB/h ≈ 14MB/s。若平均对象 5MB，写 Q

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N140

## Claim

写 IOPS 与缓存失效开销：日均上传 200GB，峰值 4 小时，写速率 = 200GB/4h = 50GB/h ≈ 14MB/s。若平均对象 5MB，写 QPS ≈ 2.8 QPS。但 CDN 缓存失效（Eviction）产生的写操作（日志、元数据更新）可能放大写 IOPS。假设缓存命中率 80%，回源请求 20%，回源带宽 = 2TB × 20% = 400GB/天，需源站具备足够带宽支撑

## Corrected Claim

写 IOPS 与缓存失效开销：日均上传 200GB，峰值 4 小时，写速率 = 200GB/4h = 50GB/h ≈ 14MB/s。若平均对象 5MB，写 QPS ≈ 2.8 QPS。但 CDN 缓存失效（Eviction）产生的写操作（日志、元数据更新）可能放大写 IOPS。假设缓存命中率 80%，回源请求 20%，回源带宽 = 2TB × 20% = 400GB/天，需源站具备足够带宽支撑

## Evidence

先验知识/题面给定，逻辑校验通过：200GB/4h=50GB/h≈13.9MB/s，13.9/5≈2.78 QPS，2TB*20%=400GB，数值量级与计算逻辑均自洽。
