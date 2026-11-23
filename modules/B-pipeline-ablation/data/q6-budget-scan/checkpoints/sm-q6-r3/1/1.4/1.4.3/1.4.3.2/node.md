# N206: 源站单实例服务速率 μ_origin 的基准值：对于静态对象回源，μ_origin ≈ 1 / T_service_origin，其中 T_service_or

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

源站单实例服务速率 μ_origin 的基准值：对于静态对象回源，μ_origin ≈ 1 / T_service_origin，其中 T_service_origin 包含磁盘 I/O 与网络传输，典型值 5-20 ms/req，故单实例 μ_origin ≈ 50-200 req/s；若使用 NVMe SSD 与内存缓存，μ_origin 可提升至 500-1000 req/s

## Corrected Claim

源站单实例服务速率 μ_origin 的基准值：对于静态对象回源，μ_origin ≈ 1 / T_service_origin，其中 T_service_origin 包含磁盘 I/O 与网络传输，典型值 5-20 ms/req，故单实例 μ_origin ≈ 50-200 req/s；若使用 NVMe SSD 与内存缓存，μ_origin 可提升至 500-1000 req/s

## Evidence

先验知识/题面给定，逻辑校验通过：5-20ms 对应 50-200 req/s，5-10ms (NVMe/缓存优化后) 对应 200-1000 req/s，量级与工程常识一致
