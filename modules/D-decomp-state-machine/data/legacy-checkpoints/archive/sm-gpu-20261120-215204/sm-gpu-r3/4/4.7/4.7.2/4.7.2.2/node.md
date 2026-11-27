# N326: 多卡同步的固定延迟 (Latency) 部分：PCIe 4.0 的 AllReduce 启动延迟通常在 10-20 μs 每跳，而 NVLink 3.0 的启动

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N115

## Claim

多卡同步的固定延迟 (Latency) 部分：PCIe 4.0 的 AllReduce 启动延迟通常在 10-20 μs 每跳，而 NVLink 3.0 的启动延迟通常在 5-10 μs 每跳；对于小数据包 (如 <1MB)，延迟主导；对于大数据包 (如 >100MB)，带宽主导。

## Corrected Claim

多卡同步中，PCIe 4.0 的 AllReduce 启动延迟通常高于 NVLink 3.0；对于小数据包（如 <1MB），延迟主导；对于大数据包（如 >100MB），带宽主导。

## Evidence

[质询]具体数值（10-20 μs vs 5-10 μs）属于经验事实，且不同硬件实现、驱动版本及拓扑结构下波动较大，缺乏统一标准；此外，NVLink 3.0 通常指 A100 架构，其 AllReduce 启动延迟受软件栈（如 NCCL 版本）影响显著，固定区间表述可能过于绝对。 | 经验事实，逻辑自洽（延迟主导小数据、带宽主导大数据符合通信原理），但本轮检索无可用来源支持具体数值区间，无法排除其他可能性。

## Search Query

NVLink 3.0 vs PCIe 4.0 AllReduce latency microseconds small message benchmark
