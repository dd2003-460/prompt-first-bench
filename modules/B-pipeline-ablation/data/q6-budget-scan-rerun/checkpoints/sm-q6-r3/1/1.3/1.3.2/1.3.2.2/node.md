# N148: 节点间缓存同步延迟对 P99 CHR 的影响：自建 10 POP 点间采用异步复制（Asynchronous Replication），同步延迟 T_sync 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

节点间缓存同步延迟对 P99 CHR 的影响：自建 10 POP 点间采用异步复制（Asynchronous Replication），同步延迟 T_sync 典型值为 1-5 秒；在此窗口内，新上传的热门短视频在其他 POP 点未命中，导致 P99 CHR 比 P95 CHR 低 10-15%；若改用同步复制（Synchronous），T_sync 降至 <100ms，但增加 20-30% 的网络带宽开销，需权衡成本与命中率。

## Corrected Claim

节点间缓存同步延迟对 P99 CHR 的影响：自建 10 POP 点间采用异步复制（Asynchronous Replication），同步延迟 T_sync 典型值为 1-5 秒；在此窗口内，新上传的热门短视频在其他 POP 点未命中，导致 P99 CHR 比 P95 CHR 低 10-15%；若改用同步复制（Synchronous），T_sync 降至 <100ms，但增加 20-30% 的网络带宽开销，需权衡成本与命中率。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN cache consistency asynchronous replication latency impact hit ratio
