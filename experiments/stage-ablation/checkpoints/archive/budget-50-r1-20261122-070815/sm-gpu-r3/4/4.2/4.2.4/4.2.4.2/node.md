# N312: Mac Studio M2 Ultra 的能效比 E_eff (tokens/W) 计算公式为 Throughput_tokens_per_s / P_avg_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

Mac Studio M2 Ultra 的能效比 E_eff (tokens/W) 计算公式为 Throughput_tokens_per_s / P_avg_W，由于 M2 Ultra 内存带宽 (800 GB/s) 低于 RTX 4090 (1008 GB/s) 且无专用 Tensor Core 加速，其 E_eff 通常低于同代 NVIDIA 消费级显卡，具体比值需对比 RTX 4090 在相同模型下的实测能效数据。

## Corrected Claim

Mac Studio M2 Ultra 的能效比 E_eff (tokens/W) 计算公式为 Throughput_tokens_per_s / P_avg_W，由于 M2 Ultra 内存带宽 (800 GB/s) 低于 RTX 4090 (1008 GB/s) 且无专用 Tensor Core 加速，其 E_eff 通常低于同代 NVIDIA 消费级显卡，具体比值需对比 RTX 4090 在相同模型下的实测能效数据。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 内存带宽 (800 GB/s) 确实低于 RTX 4090 (1008 GB/s)，且 Apple Silicon 缺乏 NVIDIA 专用的 Tensor Core 架构，在 LLM 推理等内存带宽受限场景下，其能效比通常低于同代高端 NVIDIA 消费级显卡，符合硬件性能与能效的基本物理直觉。
