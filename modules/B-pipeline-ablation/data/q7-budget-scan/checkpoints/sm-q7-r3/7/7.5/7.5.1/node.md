# N348: 多连接并行下载对API QPS的压力增量：若使用50个并发连接达到50Gbps总带宽，每个连接需维持1Gbps吞吐；S3 GET请求速率限制为3500 req/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N119

## Claim

多连接并行下载对API QPS的压力增量：若使用50个并发连接达到50Gbps总带宽，每个连接需维持1Gbps吞吐；S3 GET请求速率限制为3500 req/s（账户级），50个连接共享此限额，单连接最大QPS = 3500/50 = 70 req/s；若对象大小为128MB，单连接70 req/s对应带宽 = 70 * 128MB/s = 8.96GB/s >> 1Gbps，故QPS非瓶颈，瓶颈仍在单连接带宽或TCP窗口，需确认多连接是否真正突破10Gbps总带宽限制。

## Corrected Claim

多连接并行下载对API QPS的压力增量：若使用50个并发连接达到50Gbps总带宽，每个连接需维持1Gbps吞吐；S3 GET请求速率限制为3500 req/s（账户级），50个连接共享此限额，单连接最大QPS = 3500/50 = 70 req/s；若对象大小为128MB，单连接70 req/s对应带宽 = 70 * 128MB/s = 8.96GB/s >> 1Gbps，故QPS非瓶颈，瓶颈仍在单连接带宽或TCP窗口，需确认多连接是否真正突破10Gbps总带宽限制。

## Evidence

先验知识/题面给定，逻辑校验通过：单位换算正确（70 req/s * 128MB ≈ 8.96GB/s ≈ 71.68Gbps > 1Gbps），S3账户级限流逻辑符合AWS文档常识，推导链条自洽。
