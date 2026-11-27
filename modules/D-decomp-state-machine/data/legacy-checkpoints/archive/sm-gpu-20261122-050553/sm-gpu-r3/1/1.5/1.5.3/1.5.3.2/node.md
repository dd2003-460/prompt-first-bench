# N170: 2x RTX 4090 张量并行 (TP=2) 在 PCIe 4.0 环境下的有效吞吐折损系数：由于 PCIe 4.0 x16 带宽 (~32 GB/s) 远低

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

2x RTX 4090 张量并行 (TP=2) 在 PCIe 4.0 环境下的有效吞吐折损系数：由于 PCIe 4.0 x16 带宽 (~32 GB/s) 远低于 NVLink，每层 Transformer 的 All-Reduce 通信延迟主导；对于 Qwen3-27B (64 层)，理论通信开销占比 = (2 * Layers * Activation_Size) / (Compute_Time + Comm_Time)；实测数据显示，在 PCIe 连接下，TP=2 的推理吞吐量相比理想 NVLink 环境下降 30%-50%，即有效 Tokens/s 需乘以 0.5-0.7 的折损因子，这直接抵消了双卡带来的显存容量优势，使得单卡 W4 方案在延迟敏感场景下可能优于双卡 TP 方案。

## Corrected Claim

2x RTX 4090 张量并行 (TP=2) 在 PCIe 4.0 环境下，由于带宽远低于 NVLink，All-Reduce 通信延迟显著增加，导致推理吞吐量相比理想 NVLink 环境有明显下降（具体折损比例取决于模型结构与负载，通常显著高于 NVLink 方案），这使得单卡 W4 方案在延迟敏感场景下可能优于双卡 TP 方案。

## Evidence

[质询]该陈述包含具体的经验性数值（30%-50% 吞吐下降、0.5-0.7 折损因子），属于硬件性能与系统调优的经验事实，无法从第一性原理严格推导；且缺乏实测数据支持，不同模型结构、Batch Size 及具体 PCIe 拓扑下该比例波动极大，直接断言固定区间存在过度概括风险。 | 经验事实，逻辑自洽（PCIe 带宽瓶颈导致 TP 通信开销大是公认原理），但缺来源支持具体数值区间，故降级。

## Search Query

tensor parallelism PCIe vs NVLink throughput degradation LLM inference RTX 4090
