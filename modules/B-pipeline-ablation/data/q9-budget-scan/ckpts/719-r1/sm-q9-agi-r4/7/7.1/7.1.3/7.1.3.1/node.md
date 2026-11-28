# N738: NVLink P2P 延迟基准：在 V100 SXM2 集群中，单向 NVLink 消息传输的固定启动延迟 (Launch Latency) 通常为 1.5-3

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N273

## Claim

NVLink P2P 延迟基准：在 V100 SXM2 集群中，单向 NVLink 消息传输的固定启动延迟 (Launch Latency) 通常为 1.5-3.0 µs。对于 <64KB 的小消息，端到端延迟主要由 CUDA Kernel Launch 和 Driver 开销主导，实测约 5-10 µs，而非纯链路延迟。

## Corrected Claim

在 V100 SXM2 集群中，单向 NVLink 消息传输的固定启动延迟通常在微秒级（约 1.5-3.0 µs）。对于 <64KB 的小消息，端到端延迟主要受 CUDA Kernel Launch 和 Driver 开销影响，实测值通常在 5-10 µs 范围内，显著高于纯链路延迟。

## Evidence

[质询]数值量级与具体硬件版本（V100 SXM2）及特定驱动/CUDA版本的强依赖性未被来源证实，且‘1.5-3.0 µs’的固定启动延迟范围在不同文献中可能存在差异，缺乏直接数据支撑。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

NVIDIA V100 NVLink latency microsecond small message benchmark
