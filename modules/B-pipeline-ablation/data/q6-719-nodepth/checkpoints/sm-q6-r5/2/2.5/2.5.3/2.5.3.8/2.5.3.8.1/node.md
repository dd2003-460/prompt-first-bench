# N630: 工作点 2 的服务器数量 N_servers = 278 台是基于 10Gbps 单口带宽与 60% 利用率计算，该配置下单台服务器承载并发连接数受限，需验证 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N209

## Claim

工作点 2 的服务器数量 N_servers = 278 台是基于 10Gbps 单口带宽与 60% 利用率计算，该配置下单台服务器承载并发连接数受限，需验证 CPU 上下文切换开销是否成为瓶颈；若 CPU 利用率超过 80%，需引入更多核心或调整内核参数，否则 P99 抖动将超出容忍度。

## Corrected Claim

工作点 2 的服务器数量 N_servers = 278 台是基于 10Gbps 单口带宽与 60% 利用率计算，该配置下单台服务器承载并发连接数受限，需验证 CPU 上下文切换开销是否成为瓶颈；若 CPU 利用率超过 80%，需引入更多核心或调整内核参数，否则 P99 抖动将超出容忍度。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge server CPU bottleneck concurrent connections 10Gbps
