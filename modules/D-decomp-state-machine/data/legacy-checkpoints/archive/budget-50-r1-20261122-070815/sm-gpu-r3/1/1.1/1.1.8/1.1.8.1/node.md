# N175: CUDA 上下文 (CUDA Context) 在 NVIDIA GPU 上的固定显存开销约为 200-500 MB，该部分不随模型大小变化，是运行时碎片的主要

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

CUDA 上下文 (CUDA Context) 在 NVIDIA GPU 上的固定显存开销约为 200-500 MB，该部分不随模型大小变化，是运行时碎片的主要固定来源。

## Corrected Claim

CUDA 上下文 (CUDA Context) 在 NVIDIA GPU 上的固定显存开销约为 200-500 MB，该部分不随模型大小变化，是运行时碎片的主要固定来源。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CUDA context memory overhead size MB
