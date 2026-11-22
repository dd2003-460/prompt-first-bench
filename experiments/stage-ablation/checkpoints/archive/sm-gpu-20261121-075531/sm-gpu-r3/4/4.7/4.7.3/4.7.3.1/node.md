# N312: AMD RX 7900 XTX 运行 Qwen3-27B INT8 在 32K 上下文下的理论 Decode TPS 上限 = 960 GB/s (GDDR6 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N102

## Claim

AMD RX 7900 XTX 运行 Qwen3-27B INT8 在 32K 上下文下的理论 Decode TPS 上限 = 960 GB/s (GDDR6 带宽) / (27GB 权重 + 1.93GB KV + 1GB 开销) ≈ 33.6 tokens/s，实际效率系数 η_rocm 通常为 0.5-0.7 (ROCm 后端优化低于 CUDA)，故预期实测 TPS 为 16.8-23.5 tokens/s [待核验]。

## Corrected Claim

AMD RX 7900 XTX 运行 Qwen3-27B INT8 在 32K 上下文下的理论带宽限制 Decode TPS 上限约为 33.6 tokens/s。考虑到 ROCm 后端优化效率及计算开销，实际实测 TPS 预计显著低于此理论值，具体数值需依赖实际基准测试，通常效率系数在 0.5-0.7 之间仅为经验估计。

## Evidence

[质询]该陈述将复杂的LLM推理性能简化为纯内存带宽瓶颈计算，忽略了计算延迟（Compute-bound）和ROCm后端的具体实现效率。虽然对于大模型Decode阶段，带宽确实是主要瓶颈，但'理论上限'通常指硬件极限，而实际效率系数η_rocm=0.5-0.7是一个经验估计值，缺乏针对Qwen3-27B在RX 7900 XTX上的具体基准测试支持，且INT8量化下的实际内存访问模式可能因算子融合程度不同而有较大波动。 | 先验知识/题面给定，逻辑校验通过。计算过程：960 / (27 + 1.93 + 1) ≈ 33.6，数值量级合理。但作为经验事实（具体硬件+模型+量化下的性能预测），缺乏直接来源支持，且效率系数为估计值，故降级。

## Search Query

RX 7900 XTX Qwen3-27B INT8 32k context decode tokens per second ROCm benchmark
