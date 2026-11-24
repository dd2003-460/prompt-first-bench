# N563: 阿里云 OSS IA 层 GET 请求的官方 SLA 延迟分布：P99 延迟通常高于 Standard 层，具体数值需查阅阿里云文档，一般认为 IA 层存在毫秒

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N186

## Claim

阿里云 OSS IA 层 GET 请求的官方 SLA 延迟分布：P99 延迟通常高于 Standard 层，具体数值需查阅阿里云文档，一般认为 IA 层存在毫秒级额外寻址/调度延迟，且在高并发下尾延迟显著增加。

## Corrected Claim

阿里云 OSS IA 层 GET 请求的延迟通常高于 Standard 层，具体 P99 数值需查阅阿里云最新文档，其延迟特性受访问频率和并发情况影响。

## Evidence

[质询]陈述中关于“IA层存在毫秒级额外寻址/调度延迟”及“高并发下尾延迟显著增加”的具体机制和量级描述属于经验性推测，缺乏阿里云官方文档的直接数据支持，且不同存储层级间的延迟差异受多种因素影响，不能简单归因为固定的毫秒级寻址开销。 | 来源[1]涉及OSS加速器性能但未直接对比Standard与IA层的P99延迟具体数值；来源[2][3]为通用延迟概念解释，与阿里云OSS特定层级无关。该事实为经验性技术细节，逻辑上合理（低频访问通常伴随更高延迟）但缺乏直接来源支持，故降级。

## Search Query

Alibaba Cloud OSS IA storage GET request latency P99 SLA

## Retrieval Sources

- {'url': 'https://www.alibabacloud.com/help/en/oss/user-guide/performance-index&rut=2fe6a7d9d3c7762452e833f4ecd5d9400bdcd9556d4e04226381c86b651889fc', 'type': 'ddg', 'title': 'Performance metrics of OSS accelerator - Alibaba Cloud'}
- {'url': 'https://redis.io/blog/p99-latency/&rut=74aa5f076eaaf0a34695c953a15a6b67e7d838ea46cafd251813ebe50d66a453', 'type': 'ddg', 'title': 'P99 Latency: What It Means & How to Fix It - Redis'}
- {'url': 'https://www.alibabacloud.com/help/en/pts/performance-test-pts-3-0/product-overview/test-metrics&rut=7fd8a3267c8efddd22fca118a3e12b533852fef575edc5d875e7be480527f442', 'type': 'ddg', 'title': 'Performance Testing:Test metrics - Alibaba Cloud'}
