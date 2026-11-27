# N136: 单token prefill成本c的硬件瓶颈分解：在V100 TP=4配置下，c受限于HBM带宽（权重读取）与Compute（GEMM）中的最大值，具体公式为 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

单token prefill成本c的硬件瓶颈分解：在V100 TP=4配置下，c受限于HBM带宽（权重读取）与Compute（GEMM）中的最大值，具体公式为 c = max(T_weight_read, T_compute)，其中T_weight_read = 3.375GB / 900GB/s = 3.75ms，T_compute需结合cuBLAS在V100上的实际TFLOPS利用率（约60-70%峰值）计算。

## Corrected Claim

单token prefill成本c的硬件瓶颈分解：在V100 TP=4配置下，c受限于HBM带宽（权重读取）与Compute（GEMM）中的最大值，具体公式为 c = max(T_weight_read, T_compute)，其中T_weight_read = 3.375GB / 900GB/s = 3.75ms，T_compute需结合cuBLAS在V100上的实际TFLOPS利用率（约60-70%峰值）计算。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 HBM带宽约900GB/s，3.375GB权重读取耗时3.75ms符合算术逻辑；Prefill阶段通常受计算或带宽限制，取max符合Roofline模型直觉；cuBLAS利用率60-70%为合理工程估计。
