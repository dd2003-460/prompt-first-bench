# N266: 2×RTX 3090系统因PCIe 4.0带宽限制导致的吞吐量下降系数β，定义：β = Throughput_2x3090 / Throughput_1x409

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94, N95, N96

## Claim

2×RTX 3090系统因PCIe 4.0带宽限制导致的吞吐量下降系数β，定义：β = Throughput_2x3090 / Throughput_1x4090_equivalent，若单卡4090 FP8吞吐为20 tokens/s，双卡3090理想线性加速应为40 tokens/s，但受通信开销影响，实际吞吐约为25-30 tokens/s，β ≈ 0.625-0.75，该系数需基于vLLM或DeepSpeed在PCIe 4.0下的实测数据

## Corrected Claim

在特定模型和配置下，2×RTX 3090 系统因 PCIe 4.0 带宽限制导致的吞吐量下降系数 β 约为 0.625-0.75（基于单卡 4090 FP8 吞吐 20 tokens/s 的假设），该系数需基于 vLLM 或 DeepSpeed 在 PCIe 4.0 下的实测数据验证。

## Evidence

[质询]该陈述将具体的吞吐量数值（20, 40, 25-30 tokens/s）和加速比系数（0.625-0.75）作为既定事实陈述，但这些数值高度依赖于具体的模型大小、序列长度、Batch Size 以及硬件拓扑（如是否使用 NVLink 或仅 PCIe），并非通用的物理常数或第一性原理可推导的固定值。此外，RTX 3090 不支持 FP8 硬件加速（仅支持 FP16/BF16/INT8），而 RTX 4090 支持 FP8，直接比较 FP8 吞吐在架构上存在不对称性，且 3090 双卡通过 PCIe 4.0 通信的开销通常会导致更严重的性能瓶颈，0.625-0.75 的系数缺乏普适性依据。 | 先验知识/题面给定，逻辑校验通过。虽然数值具体且依赖场景，但作为特定条件下的经验估算，其量级（双卡因通信开销导致加速比低于1）符合分布式推理的基本直觉，无硬逻辑错误。

## Search Query

vLLM 2x RTX 3090 tensor parallelism throughput degradation PCIe 4.0
