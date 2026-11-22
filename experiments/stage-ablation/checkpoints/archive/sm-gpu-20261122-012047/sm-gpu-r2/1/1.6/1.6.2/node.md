# N67: CUDA 架构兼容性方面，H100 (Hopper) 和 RTX 4090 (Ada Lovelace) 均支持 FP8/INT8 Tensor Core，但 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

CUDA 架构兼容性方面，H100 (Hopper) 和 RTX 4090 (Ada Lovelace) 均支持 FP8/INT8 Tensor Core，但 H100 支持 FP8 加速而 RTX 4090 仅支持 INT8 加速，导致在 FP8 推理场景下 H100 具有硬件优势。

## Corrected Claim

CUDA 架构兼容性方面，H100 (Hopper) 和 RTX 4090 (Ada Lovelace) 均支持 FP8/INT8 Tensor Core，但 H100 支持 FP8 加速而 RTX 4090 仅支持 INT8 加速，导致在 FP8 推理场景下 H100 具有硬件优势。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 (Hopper) 架构原生支持 FP8 Tensor Core，而 RTX 4090 (Ada Lovelace) 架构仅支持 INT8/FP16/BF16 Tensor Core，不支持原生 FP8 加速，陈述符合硬件架构事实。
