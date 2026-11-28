# N349: MMLU-Pro 完整评测 (14k samples) 的总耗时 T_total 受 AllReduce 通信开销影响，在 TP=4 配置下，每层 Transf

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N110

## Claim

MMLU-Pro 完整评测 (14k samples) 的总耗时 T_total 受 AllReduce 通信开销影响，在 TP=4 配置下，每层 Transformer 的 AllReduce 延迟约为 0.5-1ms，若 Qwen3-27B 有 64 层，则单次前向传播的通信开销约为 32-64ms，占 0.8s 总耗时的 4-8%，需确认 AllReduce 是否确为瓶颈或 Prefill 计算才是主要耗时。

## Corrected Claim

MMLU-Pro 完整评测 (14k samples) 的总耗时 T_total 受 AllReduce 通信开销影响，在 TP=4 配置下，每层 Transformer 的 AllReduce 延迟通常在亚毫秒至毫秒级别，若 Qwen3-27B 有 64 层，则单次前向传播的通信开销可能在数十毫秒量级，需确认 AllReduce 是否确为瓶颈或 Prefill 计算才是主要耗时。

## Evidence

[质询]AllReduce 延迟 0.5-1ms 及总耗时占比 4-8% 属于高度依赖硬件环境（如 NVLink 带宽、PCIe 版本）和具体实现细节的经验数据，无法从第一性原理严格推导，且缺乏来源支持其具体数值量级。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Tensor Parallelism AllReduce latency V100 Qwen3-27B inference bottleneck
