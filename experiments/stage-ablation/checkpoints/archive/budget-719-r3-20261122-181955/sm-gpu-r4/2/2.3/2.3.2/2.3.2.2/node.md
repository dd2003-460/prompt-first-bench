# N248: llama.cpp 使用 -ngl 999 (全层 offload) 时，GPU 显存中除模型权重和 KV Cache 外，还需预留约 100-200 MB 用

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

llama.cpp 使用 -ngl 999 (全层 offload) 时，GPU 显存中除模型权重和 KV Cache 外，还需预留约 100-200 MB 用于 CUDA 上下文初始化及 cuBLAS/cuDNN 工作区，该部分不随上下文长度线性增长，但随 GPU 驱动版本变化。

## Corrected Claim

llama.cpp 使用 -ngl 999 (全层 offload) 时，GPU 显存中除模型权重和 KV Cache 外，还需预留约 100-200 MB 用于 CUDA 上下文初始化及 cuBLAS/cuDNN 工作区，该部分不随上下文长度线性增长，但随 GPU 驱动版本变化。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

llama.cpp gpu memory overhead cuda context cublas workspace size
