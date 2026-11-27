# N250: RTX 4090 (1008 GB/s) 在 Qwen3-27B INT8 量化下（权重 ~27GB，双卡 TP=2 后每卡负载 ~13.5GB + KV），单

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N114

## Claim

RTX 4090 (1008 GB/s) 在 Qwen3-27B INT8 量化下（权重 ~27GB，双卡 TP=2 后每卡负载 ~13.5GB + KV），单卡理论 Decode 吞吐上限为 1008 GB/s / (13.5 GB + 0.5 GB) ≈ 71.8 tokens/s；双卡并行有效吞吐受 PCIe 同步开销影响，预计实际值为理论值的 80-90%，即 57-65 tokens/s。

## Corrected Claim

RTX 4090 (1008 GB/s) 在 Qwen3-27B INT8 量化下，单卡理论 Decode 带宽上限约为 71.8 tokens/s；但受计算瓶颈及双卡 TP=2 同步开销影响，实际有效吞吐通常显著低于此理论值，预计实际值可能在 30-50 tokens/s 区间，具体取决于实现优化程度。

## Evidence

[质询]该陈述将复杂的LLM推理性能简化为单纯的内存带宽除法，忽略了计算瓶颈（Compute-bound）和架构效率。对于27B模型，即使INT8量化，单卡1008GB/s带宽在理想Roofline模型下确实能支撑约70+ tokens/s的算术上限，但实际Decode阶段受限于矩阵乘法的计算密度和GPU利用率，通常远低于纯带宽理论值；此外，'80-90%效率'对于跨卡TP=2的同步开销而言过于乐观，实际效率往往更低。 | 先验知识/题面给定，逻辑校验通过（量纲正确，数值量级在理论上限范围内），但缺乏外部来源支持具体效率系数，且理论模型过于简化，故降级。
