# N586: 工作点 B（标准基线/中性价比）：标准 Nginx/OpenResty 配置下，单请求服务时间 E[S] 受限于磁盘 I/O 及 SSL 握手，平均耗时为 1.

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N192

## Claim

工作点 B（标准基线/中性价比）：标准 Nginx/OpenResty 配置下，单请求服务时间 E[S] 受限于磁盘 I/O 及 SSL 握手，平均耗时为 1.0 ms（假设 90% 内存命中，10% 磁盘读取，NVMe 平均延迟 500μs），单核服务率 μ_core = 1,000 req/s，16 核节点总服务率 μ_node = 16,000 req/s。

## Corrected Claim

工作点 B（标准基线/中性价比）：标准 Nginx/OpenResty 配置下，单请求服务时间 E[S] 受限于磁盘 I/O 及 SSL 握手，平均耗时为 1.0 ms（假设 90% 内存命中，10% 磁盘读取，NVMe 平均延迟 500μs），单核服务率 μ_core = 1,000 req/s，16 核节点总服务率 μ_node = 16,000 req/s。

## Evidence

先验知识/题面给定，逻辑校验通过：1.0ms 平均耗时与 1000 req/s 单核服务率数值自洽（1/0.001s = 1000），16核线性扩展至 16,000 req/s 符合常规假设，无逻辑矛盾。

## Search Query

Nginx average request processing time benchmark 1ms
