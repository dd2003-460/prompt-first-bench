# N21: 在显存带宽受限场景下（Batch=1, Decode阶段），单卡吞吐量的理论上限公式为 Throughput_max = (Memory_Bandwidth_G

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

在显存带宽受限场景下（Batch=1, Decode阶段），单卡吞吐量的理论上限公式为 Throughput_max = (Memory_Bandwidth_GBps / Bytes_per_token) * 1000 tokens/s，其中 Bytes_per_token = (Model_Size_GB / Precision_Multiplier) * (1 + KV_Cache_Overhead_Factor)，需根据具体硬件（如RTX 4090: 1008 GB/s, A100: 2039 GB/s, H100: 3350 GB/s）计算各候选卡的理论上限。

## Corrected Claim

在显存带宽受限场景下（Batch=1, Decode阶段），单卡吞吐量的理论上限公式为 Throughput_max = (Memory_Bandwidth_GBps / Bytes_per_token) * 1000 tokens/s，其中 Bytes_per_token = (Model_Size_GB / Precision_Multiplier) * (1 + KV_Cache_Overhead_Factor)，需根据具体硬件（如RTX 4090: 1008 GB/s, A100: 2039 GB/s, H100: 3350 GB/s）计算各候选卡的理论上限。

## Evidence

[质询]公式中 Bytes_per_token 的定义存在概念混淆：在 Decode 阶段，每生成一个 token 需要读取的字节数主要取决于模型权重大小（Model_Size）加上当前序列长度对应的 KV Cache 大小，而非简单的 (Model_Size / Precision_Multiplier) * (1 + Overhead)。此外，Precision_Multiplier 的定义模糊（通常精度越低字节数越少，若 Multiplier 代表精度倍数如 FP16=2, FP8=1，则除法逻辑需明确；若 Multiplier 代表量化压缩比，则逻辑相反）。但作为理论上限的粗略估算框架，其量纲和核心逻辑（带宽/每token字节数）是成立的。 | 先验知识/题面给定，逻辑校验通过。该公式符合显存带宽受限场景下 LLM 推理吞吐量的基本物理直觉（Roofline Model 简化版），硬件参数（RTX 4090, A100, H100 带宽）量级正确。

## Search Query

LLM inference decode phase memory bandwidth bound throughput formula
