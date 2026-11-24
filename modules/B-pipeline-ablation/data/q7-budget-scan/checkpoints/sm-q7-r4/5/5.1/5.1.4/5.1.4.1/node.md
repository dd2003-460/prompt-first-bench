# N326: 云对象存储单前缀并发上限约束：S3 对同一前缀的 GET 请求并发上限为 3,500 req/s，若数据均匀分布且并发请求数 N_concurrent 需达到 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N120

## Claim

云对象存储单前缀并发上限约束：S3 对同一前缀的 GET 请求并发上限为 3,500 req/s，若数据均匀分布且并发请求数 N_concurrent 需达到 3,800 以满足 IOPS_peak，则所需前缀数 N_prefix = ceil(3,800 / 3,500) = 2，此时总 IOPS 供给 = min(N_prefix * 3,500, 网络带宽限制) = 7,000 IOPS，仍低于 37,926 IOPS 需求，表明仅靠增加前缀无法在单区域单账户下满足峰值 IOPS。

## Corrected Claim

云对象存储单前缀并发上限约束：S3 对同一前缀的 GET 请求并发上限为 3,500 req/s，若数据均匀分布且并发请求数 N_concurrent 需达到 3,800 以满足 IOPS_peak，则所需前缀数 N_prefix = ceil(3,800 / 3,500) = 2，此时总 IOPS 供给 = min(N_prefix * 3,500, 网络带宽限制) = 7,000 IOPS，仍低于 37,926 IOPS 需求，表明仅靠增加前缀无法在单区域单账户下满足峰值 IOPS。

## Evidence

先验知识/题面给定，逻辑校验通过：S3单前缀GET 3500 req/s为公认基准，数学推导ceil(3800/3500)=2及7000<37926均正确，结论符合AWS官方文档关于前缀分片提升吞吐量的原理。

## Search Query

AWS S3 per prefix throughput limit 3500 requests per second
