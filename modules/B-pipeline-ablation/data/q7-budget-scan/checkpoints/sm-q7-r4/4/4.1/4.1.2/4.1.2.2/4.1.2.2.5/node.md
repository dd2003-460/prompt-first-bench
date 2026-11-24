# N785: API 限流对恢复耗时的影响：S3 默认速率限制为每秒 3,500 PUT/POST/LIST 请求和 5,500 DELETE 请求，GET 请求无硬限制但受

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N288, N289, N290

## Claim

API 限流对恢复耗时的影响：S3 默认速率限制为每秒 3,500 PUT/POST/LIST 请求和 5,500 DELETE 请求，GET 请求无硬限制但受账户级吞吐量限制（初始 5,500 请求/秒，可申请提升）；4.1e9 次 GET 请求在 5,500 req/s 下限速下耗时 ≈ 745,455 秒 ≈ 207 小时，需申请提升至 50,000 req/s 才能将耗时降至 20.7 小时

## Corrected Claim

S3 默认速率限制为每秒 3,500 PUT/POST/DELETE 请求和 5,500 GET 请求；若发生 4.1e9 次 GET 请求，在 5,500 req/s 下限速下理论耗时约为 207 小时，需申请提升限额以缩短时间。

## Evidence

[质询]陈述中关于“4.1e9 次 GET 请求”的具体数值及由此推导出的耗时（207小时/20.7小时）属于特定场景下的经验数据或假设前提，参考来源仅提供了通用的速率限制阈值（5,500 req/s），并未包含该特定请求量级的数据，因此无法从现有来源直接验证该具体计算场景的真实性。 | 来源 [1] 和 [3] 直接支持了 S3 的默认速率限制数值（PUT/POST/DELETE 3,500/s, GET 5,500/s），但来源未覆盖“4.1e9 次请求”这一具体业务场景及其对应的耗时计算，属于经验事实缺来源支持。

## Search Query

AWS S3 API rate limit GET requests per second default limit

## Retrieval Sources

- {'url': 'https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html&rut=bbed961742686e1d92a9c7af3944ac3abd5b4b5d89819eba792e9c0991d45564', 'type': 'ddg', 'title': 'Best practices design patterns: optimizing Amazon S3 performance'}
- {'url': 'https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/userguide/optimizing-performance.html&rut=b683b433446fff2d981494e8c89c00daaeb080acbc58a810a1e4c5f85130c65c', 'type': 'ddg', 'title': '最佳实践设计模式：优化 Amazon S3 性能 - Amazon Simple Storage Service'}
- {'url': 'https://stackharbor.com/en/knowledge-base/awsfix-s3-503-slowdown-request-rate/&rut=0fda2812375923afa69dd14a71bd997d4ce572673185c5e12f6d23e90dc9bfb5', 'type': 'ddg', 'title': 'S3 503 Slowdown: request-rate limits and prefix design'}
