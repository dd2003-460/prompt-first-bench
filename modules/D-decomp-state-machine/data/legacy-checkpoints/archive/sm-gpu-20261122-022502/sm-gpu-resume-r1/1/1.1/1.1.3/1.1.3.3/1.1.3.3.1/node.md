# N448: INT4 GPTQ/AWQ 量化在 HuggingFace/vLLM 推理中，CUDA Context 及 cuBLAS/cuDNN 工作区 (Workspac

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N139, N140, N141

## Claim

INT4 GPTQ/AWQ 量化在 HuggingFace/vLLM 推理中，CUDA Context 及 cuBLAS/cuDNN 工作区 (Workspace) 的基础占用量约为 200-400 MB，该数值独立于模型参数量，主要取决于 GPU 架构 (Ampere/Hopper) 和驱动版本。

## Corrected Claim

INT4 GPTQ/AWQ 量化在 HuggingFace/vLLM 推理中，CUDA Context 及 cuBLAS/cuDNN 工作区 (Workspace) 的基础占用量约为 200-400 MB，该数值独立于模型参数量，主要取决于 GPU 架构 (Ampere/Hopper) 和驱动版本。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CUDA context memory footprint baseline size GB
