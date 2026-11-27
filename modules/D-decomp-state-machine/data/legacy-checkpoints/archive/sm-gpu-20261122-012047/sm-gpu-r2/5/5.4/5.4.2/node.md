# N148: 监控与日志复杂度：单卡方案仅需监控 1 个 GPU 的利用率、温度和显存使用，日志量较小；双卡方案需监控 2 个 GPU 及 PCIe 链路状态，日志量增加约 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

监控与日志复杂度：单卡方案仅需监控 1 个 GPU 的利用率、温度和显存使用，日志量较小；双卡方案需监控 2 个 GPU 及 PCIe 链路状态，日志量增加约 50-100%，且需额外处理多卡间通信错误日志；Apple Silicon 方案需监控 CPU/GPU/NPU 协同状态，日志格式与 Linux 标准不同，增加解析复杂度。

## Corrected Claim

监控与日志复杂度：单卡方案仅需监控 1 个 GPU 的利用率、温度和显存使用，日志量较小；双卡方案需监控 2 个 GPU 及 PCIe 链路状态，日志量增加约 50-100%，且需额外处理多卡间通信错误日志；Apple Silicon 方案需监控 CPU/GPU/NPU 协同状态，日志格式与 Linux 标准不同，增加解析复杂度。

## Evidence

先验知识/题面给定，逻辑校验通过
