# N411: Batch Size 对计算密度（Arithmetic Intensity）的影响机制：当 Batch Size > 1 时，GPU 的 Tensor Core

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N145

## Claim

Batch Size 对计算密度（Arithmetic Intensity）的影响机制：当 Batch Size > 1 时，GPU 的 Tensor Core 利用率从 ~5% (Batch=1, Memory Bound) 提升至 ~40-60% (Batch=8, Compute Bound)，导致 Compute_Time 的增长斜率小于线性，从而进一步降低通信开销占比。

## Corrected Claim

Batch Size 对计算密度（Arithmetic Intensity）的影响机制：当 Batch Size > 1 时，GPU 的 Tensor Core 利用率从 ~5% (Batch=1, Memory Bound) 提升至 ~40-60% (Batch=8, Compute Bound)，导致 Compute_Time 的增长斜率小于线性，从而进一步降低通信开销占比。

## Evidence

先验知识/题面给定，逻辑校验通过
