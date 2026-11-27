# N526: NVLink 4.0 的通信延迟 (Latency) 约为 1-2 微秒，而 PCIe 4.0 的通信延迟约为 10-20 微秒，对于 8KB 的小消息 All

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N216

## Claim

NVLink 4.0 的通信延迟 (Latency) 约为 1-2 微秒，而 PCIe 4.0 的通信延迟约为 10-20 微秒，对于 8KB 的小消息 All-Reduce，延迟 (Latency) 而非带宽 (Bandwidth) 是主要瓶颈，NVLink 的延迟优势使其在 TP=2 配置下通信开销可忽略不计。

## Corrected Claim

NVLink 4.0 的通信延迟 (Latency) 约为 1-2 微秒，而 PCIe 4.0 的通信延迟约为 10-20 微秒，对于 8KB 的小消息 All-Reduce，延迟 (Latency) 而非带宽 (Bandwidth) 是主要瓶颈，NVLink 的延迟优势使其在 TP=2 配置下通信开销可忽略不计。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVLink 4.0 vs PCIe 4.0 latency small message All-Reduce
