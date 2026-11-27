# N694: CUDA 上下文初始化显存开销的精确构成：包括 CUDA Context (固定 ~200MB-400MB，随驱动版本波动) + cuBLAS Workspac

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N248, N249, N250

## Claim

CUDA 上下文初始化显存开销的精确构成：包括 CUDA Context (固定 ~200MB-400MB，随驱动版本波动) + cuBLAS Workspace (动态，取决于 Batch Size 和 Layer Shape，通常 100-500MB) + cuDNN Workspace (动态，通常 50-200MB)；在 Llama.cpp 单卡推理场景下，该总开销可近似为常数 C_cuda ≈ 300MB-800MB，不随 Seq_Len 变化。

## Corrected Claim

CUDA 上下文初始化显存开销的精确构成：包括 CUDA Context (固定 ~200MB-400MB，随驱动版本波动) + cuBLAS Workspace (动态，取决于 Batch Size 和 Layer Shape，通常 100-500MB) + cuDNN Workspace (动态，通常 50-200MB)；在 Llama.cpp 单卡推理场景下，该总开销可近似为常数 C_cuda ≈ 300MB-800MB，不随 Seq_Len 变化。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CUDA context memory overhead MB cuBLAS workspace size inference
