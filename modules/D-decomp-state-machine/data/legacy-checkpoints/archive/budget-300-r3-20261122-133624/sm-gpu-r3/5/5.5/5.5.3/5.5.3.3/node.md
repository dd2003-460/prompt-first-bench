# N404: vLLM 自动重连机制的实际中断时间 T_downtime 量化：在 PCIe 5.0 环境下，vLLM 检测到 Worker 崩溃并重启加载 27B INT8

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N157

## Claim

vLLM 自动重连机制的实际中断时间 T_downtime 量化：在 PCIe 5.0 环境下，vLLM 检测到 Worker 崩溃并重启加载 27B INT8 权重的时间约为 45-60 秒（含 CUDA context 重建），而非 N157 声称的 5 分钟；若使用 Warm Standby 机制，中断时间可降至 <5 秒，但需额外 10% 显存开销。

## Corrected Claim

在 PCIe 5.0 环境下，vLLM 检测到 Worker 崩溃并重启加载 27B INT8 权重的时间通常在数十秒量级（具体取决于硬件与配置），而非固定的 5 分钟；若使用 Warm Standby 机制，中断时间可显著降低，但需额外显存开销。

## Evidence

[质询]具体数值（45-60秒、<5秒、10%显存）属于高度依赖硬件配置、模型分片策略及vLLM具体版本实现的经验事实，缺乏通用性，且‘自动重连’通常指网络层，此处混淆了Worker进程崩溃重启与网络重连的概念，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值量级）

## Search Query

vLLM worker crash recovery time benchmark 27B model PCIe
