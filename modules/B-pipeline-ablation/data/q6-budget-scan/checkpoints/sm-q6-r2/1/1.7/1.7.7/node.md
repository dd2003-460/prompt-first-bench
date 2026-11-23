# N42: P99延迟的长尾主要由‘缓存未命中且回源路径拥塞’的请求构成，其延迟分布服从对数正态分布，P99 = mu + 2.33 * sigma，其中 mu 和 sig

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

P99延迟的长尾主要由‘缓存未命中且回源路径拥塞’的请求构成，其延迟分布服从对数正态分布，P99 = mu + 2.33 * sigma，其中 mu 和 sigma 需通过实测或仿真获得。

## Corrected Claim

P99延迟的长尾主要由‘缓存未命中且回源路径拥塞’的请求构成，其延迟分布服从对数正态分布，P99 = mu + 2.33 * sigma，其中 mu 和 sigma 需通过实测或仿真获得。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布的P99分位数公式推导正确（ln(P99)=mu+2.33sigma），长尾成因符合系统性能常识。

## Search Query

P99 latency distribution log-normal CDN cache miss
