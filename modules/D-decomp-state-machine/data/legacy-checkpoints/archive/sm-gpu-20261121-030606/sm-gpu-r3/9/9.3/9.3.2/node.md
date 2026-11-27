# N373: 双卡4090方案KV Cache同步延迟监控需部署nvidia-smi + p2pBandwidthLatencyTest脚本，单次执行耗时2.5s，需每5分钟

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N157

## Claim

双卡4090方案KV Cache同步延迟监控需部署nvidia-smi + p2pBandwidthLatencyTest脚本，单次执行耗时2.5s，需每5分钟执行一次，日均CPU占用率为0.4%

## Corrected Claim

双卡4090方案KV Cache同步延迟监控需部署nvidia-smi + p2pBandwidthLatencyTest脚本，单次执行耗时约2.5s，建议每5分钟执行一次，日均CPU占用率较低（约0.4%量级）。

## Evidence

[质询]具体数值（2.5s耗时、0.4% CPU占用）缺乏通用基准支持，可能因驱动版本、系统负载或具体脚本实现差异而波动，属于特定环境下的经验观测值而非固定物理常数。 | 先验知识/题面给定，逻辑校验通过：nvidia-smi和p2pBandwidthLatencyTest是标准工具，5分钟间隔下2.5s任务占比约0.83%时间，0.4% CPU占用在量级上合理（取决于脚本是否阻塞或并行），无逻辑矛盾，但具体数值为经验事实，无外部来源直接支持。
