# N97: CUDA Context 及运行时开销：PyTorch/vLLM 框架本身及 CUDA Context 占用约 0.5-1.5 GB 显存，这部分不随模型精度变

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

CUDA Context 及运行时开销：PyTorch/vLLM 框架本身及 CUDA Context 占用约 0.5-1.5 GB 显存，这部分不随模型精度变化，但必须计入总显存需求。总需求修正公式：Total_VRAM = Weight + KV_Cache + Activation + Runtime_Overhead (1 GB)。

## Corrected Claim

CUDA Context 及运行时开销：PyTorch/vLLM 框架本身及 CUDA Context 占用约 0.5-1.5 GB 显存，这部分不随模型精度变化，但必须计入总显存需求。总需求修正公式：Total_VRAM = Weight + KV_Cache + Activation + Runtime_Overhead (1 GB)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

PyTorch CUDA context memory overhead GPU inference
