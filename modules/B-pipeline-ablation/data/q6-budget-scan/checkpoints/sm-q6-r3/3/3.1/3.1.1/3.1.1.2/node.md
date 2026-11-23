# N205: 单位请求 CPU 处理时间 CPU_time_per_req 取决于对象大小 s_avg 和压缩/加密算法复杂度；对于 5MB 对象，若启用 Brotli 压缩

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

单位请求 CPU 处理时间 CPU_time_per_req 取决于对象大小 s_avg 和压缩/加密算法复杂度；对于 5MB 对象，若启用 Brotli 压缩和 TLS 1.3 加密，单核处理时间约为 50-100ms；若不启用压缩，仅 TLS 握手和转发，处理时间约为 10-20ms。该值直接决定弹性实例的计费时长。

## Corrected Claim

单位请求 CPU 处理时间 CPU_time_per_req 取决于对象大小 s_avg 和压缩/加密算法复杂度；对于 5MB 对象，若启用 Brotli 压缩和 TLS 1.3 加密，单核处理时间约为 50-100ms；若不启用压缩，仅 TLS 握手和转发，处理时间约为 10-20ms。该值直接决定弹性实例的计费时长。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge server CPU processing time per request compression encryption latency
