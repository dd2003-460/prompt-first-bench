# N461: NCCL All-Reduce 在 2 卡 PCIe 4.0 互联下的通信延迟（Latency）：对于小消息（< 4KB），延迟通常在 10-20 μs 范围内

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N147

## Claim

NCCL All-Reduce 在 2 卡 PCIe 4.0 互联下的通信延迟（Latency）：对于小消息（< 4KB），延迟通常在 10-20 μs 范围内 [待核验]，这主要受 PCIe 事务处理开销影响，而非带宽限制

## Corrected Claim

NCCL All-Reduce 在 2 卡 PCIe 4.0 互联下，对于小消息（< 4KB），通信延迟通常受 PCIe 事务处理开销主导，典型量级在微秒级（约 10-20 μs），而非受带宽限制。

## Evidence

[质询]具体数值（10-20 μs）属于经验事实，受驱动版本、拓扑结构及具体实现影响较大，缺乏直接来源支持该特定区间，且不同环境下可能波动至 5-30 μs 范围。 | 经验事实，逻辑自洽（小消息通信确实受延迟主导而非带宽限制，PCIe 事务开销是主要瓶颈），但缺来源直接支持具体数值区间。

## Search Query

NCCL all-reduce small message latency microseconds PCIe
