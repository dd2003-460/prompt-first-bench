# N10: 硬件可行域下限：总显存 ≥ 54 GB (BF16) + 128 MB×N (KV) + 2 GB (Activations) + 2 GB (Framewor

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

硬件可行域下限：总显存 ≥ 54 GB (BF16) + 128 MB×N (KV) + 2 GB (Activations) + 2 GB (Framework/CUDA Context Overhead)，即 BF16 下至少需要 60 GB 显存才能支持单流 32K 上下文。

## Corrected Claim

硬件可行域下限：总显存 ≥ 54 GB (BF16) + 128 MB×N (KV) + 2 GB (Activations) + 2 GB (Framework/CUDA Context Overhead)，即 BF16 下至少需要 60 GB 显存才能支持单流 32K 上下文。

## Evidence

先验知识/题面给定，逻辑校验通过：54+0.128+2+2=58.128 GB，向上取整或考虑碎片开销后约60 GB，量级与算术逻辑自洽。
