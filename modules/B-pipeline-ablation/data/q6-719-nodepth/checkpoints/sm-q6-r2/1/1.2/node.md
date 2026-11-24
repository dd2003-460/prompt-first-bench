# N8: 公有云 CDN 策略下，单请求端到端延迟分布的 P99 值（单位：ms），需基于其全球节点密度与回源架构估算。

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N1

## Claim

公有云 CDN 策略下，单请求端到端延迟分布的 P99 值（单位：ms），需基于其全球节点密度与回源架构估算。

## Corrected Claim

公有云 CDN 策略下，单请求端到端延迟分布的 P99 值通常在几十毫秒到几百毫秒之间（取决于具体厂商、节点距离及回源情况），需基于具体服务商的监控数据或公开基准测试估算，而非单一固定值。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上正交，分别对应公式中的不同项（RTT、处理、传输、回源）。但存在两处关键缺陷：1. 完备性缺失：公式中包含 T_transfer_edge_to_client（数据传输时间），但四个子节点中没有任何一个专门估算该项，导致无法计算最终 P99；2. 统计错误：子节点1使用了错误的延迟叠加公式。P99(A+B) 不等于 P99(A)+P99(B)，这种直接相加会严重高估 P99 值，应使用卷积或蒙特卡洛模拟，或至少指出这是上界估计。）

## Search Query

Alibaba Cloud CDN P99 latency global distribution 2024

## Retrieval Sources

- {'url': 'https://blog.csdn.net/2600_94959998/article/details/157125128&rut=358e43b59793c09407c94409edead8bfb627400604ddc58a38e2000d2d2bc761', 'type': 'ddg', 'title': '深入解析p99延迟：从概念到优化的实战指南 - Csdn博客'}
- {'url': 'https://blog.csdn.net/2600_94959702/article/details/157227534&rut=a28c2f5bd23d334a04ff6730c0a9e0c83ed080cd03abe672ef0626105d712d55', 'type': 'ddg', 'title': '深入解析p99延迟：原理、测量与优化实战 - Csdn博客'}
- {'url': 'https://blog.openresty.com/cn/p99-latency/&rut=233dd5c3a18a3791af688572afb0f24354b8415ef888957190725cafc9e9c8eb', 'type': 'ddg', 'title': 'P99 延迟：为什么平均值会骗人，以及如何诊断最慢的 1% - OpenResty 官方博客'}
