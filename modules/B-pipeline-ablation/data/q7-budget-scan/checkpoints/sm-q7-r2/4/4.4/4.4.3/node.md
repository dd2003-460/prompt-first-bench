# N85: 云对象存储 API 速率限制对恢复吞吐的影响：AWS S3 GET 请求限制为 3,500/秒/前缀，若平均对象大小为 1MB，最大有效吞吐 = 3500 re

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N24

## Claim

云对象存储 API 速率限制对恢复吞吐的影响：AWS S3 GET 请求限制为 3,500/秒/前缀，若平均对象大小为 1MB，最大有效吞吐 = 3500 req/s * 1MB = 3.5GB/s，远低于 1Gbps 网络带宽，需通过分片上传/下载优化

## Corrected Claim

AWS S3 在高并发场景下，单一前缀的请求速率可能受到限制（历史上常引用约 3,500 GET/秒或 3,500 PUT/秒），若平均对象大小为 1MB，单前缀最大有效吞吐约为 3.5GB/s，这可能低于高带宽网络需求，因此建议通过分散前缀或使用分片上传/下载来优化吞吐。

## Evidence

[质询]AWS S3 官方文档已不再强调固定的“3,500 GET/秒/前缀”硬性限制，而是指出 S3 会自动扩展以应对新请求速率，且高吞吐通常依赖于使用多个前缀或分片操作，单一前缀下的具体数值限制可能随账户历史和负载动态变化，直接断言固定为 3500 且导致 3.5GB/s 上限过于绝对。 | 来源 [1] 和 [3] 确认了 S3 性能优化和自动扩展机制，但未直接提供“3,500/秒/前缀”这一具体数值作为当前硬性标准，属于经验事实且缺乏直接来源支持，故降级。

## Search Query

AWS S3 API rate limit GET requests per second prefix throughput impact

## Retrieval Sources

- {'url': 'https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/userguide/optimizing-performance-design-patterns.html&rut=46207a1d09cca222e44a2e19fb3c1e3381fec82a5ae8abcc7a4f500b33d02f4c', 'type': 'ddg', 'title': 'Amazon S3 的性能设计规律 - Amazon Simple Storage Service'}
- {'url': 'https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/userguide/optimizing-performance.html&rut=b683b433446fff2d981494e8c89c00daaeb080acbc58a810a1e4c5f85130c65c', 'type': 'ddg', 'title': '最佳实践设计模式：优化 Amazon S3 性能 - Amazon Simple Storage Service'}
- {'url': 'https://docs.amazonaws.cn/AmazonS3/latest/userguide/optimizing-performance-guidelines.html&rut=385059c7d15e8f9fb2612088ed901a2369ec37ce5d7e8928e5f3a49f5516c47a', 'type': 'ddg', 'title': 'Amazon S3 的性能准则 - Amazon Simple Storage Service'}
