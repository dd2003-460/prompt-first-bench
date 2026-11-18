# N155: 激活值 (Activation) 显存占用主要取决于 Batch Size 和 Sequence Length，对于 Batch Size=1, 32K Con

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

激活值 (Activation) 显存占用主要取决于 Batch Size 和 Sequence Length，对于 Batch Size=1, 32K Context，激活值峰值约为 1.5-2.5 GB (取决于中间层宽度)，N47 的 1.5 GB 估算在 Batch Size=1 时合理，但在高并发下需线性增加

## Corrected Claim

激活值 (Activation) 显存占用主要取决于 Batch Size 和 Sequence Length，对于 Batch Size=1, 32K Context，激活值峰值约为 1.5-2.5 GB (取决于中间层宽度)，N47 的 1.5 GB 估算在 Batch Size=1 时合理，但在高并发下需线性增加

## Evidence

先验知识/题面给定，逻辑校验通过
