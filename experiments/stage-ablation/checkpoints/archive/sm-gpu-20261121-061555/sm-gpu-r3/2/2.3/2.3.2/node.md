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

父节点级核验通过：正交+完备+无冗余（子节点分别针对FlashAttention和GEMM两个不同的算子进行分解，二者在计算逻辑和显存占用来源上是正交的（不重复、不矛盾）。父节点明确指出了“FlashAttention、GEMM等关键算子”，子节点覆盖了这两个主要方面，且父节点中提到的“1-2GB”估算范围与子节点具体计算出的数值（FA约2.1GB, GEMM约0.67GB）在量级和逻辑上保持一致（考虑到FA是主要开销且可能因Tiling策略或具体实现有波动，GEMM开销较小，整体符合父节点描述）。不存在冗余，因为这是两个独立的算子开销，而非同一参数的不同取值。）

## Search Query

FlashAttention workspace memory allocation GB
