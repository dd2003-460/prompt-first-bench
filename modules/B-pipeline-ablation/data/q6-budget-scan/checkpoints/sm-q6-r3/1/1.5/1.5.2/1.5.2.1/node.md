# N210: 缓存命中路径的平均服务时间 T_service_hit 的微观构成：T_service_hit = T_lookup + T_read + T_write_ba

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N64

## Claim

缓存命中路径的平均服务时间 T_service_hit 的微观构成：T_service_hit = T_lookup + T_read + T_write_back，其中 T_lookup (内存哈希查找) < 0.1ms, T_read (SSD/NVMe 读取) ≈ 0.1-1ms, T_write_back (若存在持久化) 0ms (异步)，故 T_service_hit ≈ 0.2-1.1 ms，对应 μ_hit ≈ 900-5000 req/s

## Corrected Claim

缓存命中路径的平均服务时间 T_service_hit 的微观构成：T_service_hit = T_lookup + T_read + T_write_back，其中 T_lookup (内存哈希查找) < 0.1ms, T_read (SSD/NVMe 读取) ≈ 0.1-1ms, T_write_back (若存在持久化) 0ms (异步)，故 T_service_hit ≈ 0.2-1.1 ms，对应 μ_hit ≈ 900-5000 req/s

## Evidence

先验知识/题面给定，逻辑校验通过：各组件耗时量级符合硬件常识（内存<0.1ms, SSD 0.1-1ms），求和范围0.2-1.1ms与倒数推导出的吞吐量900-5000 req/s在数学上自洽。
