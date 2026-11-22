# N121: Activation 显存占用的 Batch Size 依赖性：N46 中固定 Activation 为 ~3GB，但该值仅在 Batch Size=1 且使用

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

Activation 显存占用的 Batch Size 依赖性：N46 中固定 Activation 为 ~3GB，但该值仅在 Batch Size=1 且使用 Flash Attention 时成立。若 Batch Size 增加至 4，Activation 占用将线性增加至 ~12GB，导致 INT8 方案总显存需求升至 ~48GB，从而排除 L40S (48GB) 作为高并发选项，仅适合低并发场景。

## Corrected Claim

Activation 显存占用的 Batch Size 依赖性：N46 中固定 Activation 为 ~3GB，但该值仅在 Batch Size=1 且使用 Flash Attention 时成立。若 Batch Size 增加至 4，Activation 占用将线性增加至 ~12GB，导致 INT8 方案总显存需求升至 ~48GB，从而排除 L40S (48GB) 作为高并发选项，仅适合低并发场景。

## Evidence

先验知识/题面给定，逻辑校验通过：Activation显存随Batch Size线性增长符合Transformer推理基本原理，数值量级（3GB*4=12GB）及总显存估算（12GB+模型权重等≈48GB）在工程上合理且自洽。
