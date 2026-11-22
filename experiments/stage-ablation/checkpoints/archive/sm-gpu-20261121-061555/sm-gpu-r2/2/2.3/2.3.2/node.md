# N63: 算子工作区（Workspace）开销：FlashAttention、GEMM（如cuBLAS）等关键算子在执行时需要临时分配显存，峰值占用通常为最大激活张量的2

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

算子工作区（Workspace）开销：FlashAttention、GEMM（如cuBLAS）等关键算子在执行时需要临时分配显存，峰值占用通常为最大激活张量的2-3倍，对于27B模型在Batch=1、Seq=32K时，估算约为1-2GB，具体取决于算子实现（如是否使用FP8/INT8加速路径）。

## Corrected Claim

算子工作区（Workspace）开销：FlashAttention、GEMM（如cuBLAS）等关键算子在执行时需要临时分配显存，峰值占用通常为最大激活张量的2-3倍，对于27B模型在Batch=1、Seq=32K时，估算约为1-2GB，具体取决于算子实现（如是否使用FP8/INT8加速路径）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

FlashAttention workspace memory allocation GB
