# N255: 若要将 32K BF16 KV Cache (8.6 GB) 切分到 2 张 4090 上，每卡需 4.3 GB KV，加上 13.5 GB 权重和 0.5 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88, N89, N90

## Claim

若要将 32K BF16 KV Cache (8.6 GB) 切分到 2 张 4090 上，每卡需 4.3 GB KV，加上 13.5 GB 权重和 0.5 GB 开销，总占用 18.3 GB < 24 GB，理论可行；但需确认框架是否支持跨卡 KV Cache 分片及由此引入的 All-Gather 通信开销。

## Corrected Claim

若要将 32K BF16 KV Cache (8.6 GB) 切分到 2 张 4090 上，每卡需 4.3 GB KV，加上 13.5 GB 权重和 0.5 GB 开销，总占用 18.3 GB < 24 GB，理论可行；但需确认框架是否支持跨卡 KV Cache 分片及由此引入的 All-Gather 通信开销。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（4.3+13.5+0.5=18.3 < 24），且跨卡KV分片需All-Gather通信符合分布式推理基本原理。
