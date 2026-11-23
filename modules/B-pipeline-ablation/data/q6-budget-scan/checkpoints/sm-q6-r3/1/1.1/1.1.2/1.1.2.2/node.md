# N180: 边缘节点单请求服务时间 T_service 的分解：T_service = T_tls + T_http + T_cache_lookup + T_io_rea

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

边缘节点单请求服务时间 T_service 的分解：T_service = T_tls + T_http + T_cache_lookup + T_io_read，其中 T_cache_lookup ≈ 0.1-0.5ms（Redis/Memcached 本地内存访问），T_io_read ≈ 1-5ms（NVMe SSD 随机读，取决于 4K 块对齐与页缓存命中率），总 T_service 典型值 2-10ms，直接决定 M/M/K 模型中的 μ。

## Corrected Claim

边缘节点单请求服务时间 T_service 的分解：T_service = T_tls + T_http + T_cache_lookup + T_io_read，其中 T_cache_lookup ≈ 0.1-0.5ms（Redis/Memcached 本地内存访问），T_io_read ≈ 1-5ms（NVMe SSD 随机读，取决于 4K 块对齐与页缓存命中率），总 T_service 典型值 2-10ms，直接决定 M/M/K 模型中的 μ。

## Evidence

先验知识/题面给定，逻辑校验通过：各组件延迟量级（TLS/HTTP握手、内存缓存、NVMe IO）符合工程常识，总和2-10ms合理，且直接决定M/M/K模型服务率μ的逻辑关系正确。

## Search Query

CDN edge node request service time breakdown NVMe SSD latency cache lookup
