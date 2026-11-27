# N292: NVLink 4.0 互联在 TP=2 架构下，AllReduce 操作的固定启动延迟具体数值（通常低于 PCIe，约 2-5 µs），用于与 PCIe 方案进

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N108

## Claim

NVLink 4.0 互联在 TP=2 架构下，AllReduce 操作的固定启动延迟具体数值（通常低于 PCIe，约 2-5 µs），用于与 PCIe 方案进行同口径的延迟开销对比，修正 10%-15% 吞吐损失估算中的常数项偏差。

## Corrected Claim

NVLink 4.0 互联在 TP=2 架构下，AllReduce 操作的固定启动延迟通常低于 PCIe 方案，具体数值需参考特定硬件实测数据，用于修正吞吐损失估算中的常数项偏差。

## Evidence

[质询]具体数值（2-5 µs）属于经验事实，缺乏来源支持，且不同硬件代际和具体实现下延迟可能波动，无法仅凭逻辑推导确定精确区间。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

NVLink 4.0 AllReduce launch latency microseconds H100 TP2
