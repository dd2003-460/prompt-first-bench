# N34: FP8 精度在 Hopper 架构 (H100/H200) 上原生支持，但在 Ampere (A100) 和 Ada (RTX 4090) 上需通过软件模拟或转

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

FP8 精度在 Hopper 架构 (H100/H200) 上原生支持，但在 Ampere (A100) 和 Ada (RTX 4090) 上需通过软件模拟或转换，可能导致 10-20% 的吞吐量损失；若在 RTX 4090 上运行 FP8 模型，实际收益可能低于预期，建议优先使用 INT8 (GPTQ/AWQ) 或 BF16

## Corrected Claim

FP8 精度在 Hopper 架构 (H100/H200) 上原生支持，但在 Ampere (A100) 和 Ada (RTX 4090) 上需通过软件模拟或转换，可能导致显著的吞吐量损失；若在 RTX 4090 上运行 FP8 模型，实际收益可能低于预期，建议优先使用 INT8 (GPTQ/AWQ) 或 BF16

## Evidence

[质询]陈述中关于Ampere/Ada架构上FP8需软件模拟且导致10-20%吞吐量损失的具体数值缺乏来源支持，且RTX 4090（Ada架构）实际上通过TensorRT-LLM等软件栈支持FP8推理，并非完全无法运行或必然导致该特定幅度的损失，具体性能表现高度依赖模型结构和软件优化程度，该具体百分比属于经验事实且缺乏直接证据。 | 来源[1]和[2]直接支持Hopper架构原生支持FP8，但未提供Ampere/Ada架构上FP8模拟的具体性能损失数据（10-20%），该部分为经验事实且缺来源支持，故降级。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_26854475/article/details/164413905&rut=7d174d175c700294c182a84500b486b17e9b569fae8ddeb4a6b5a3d4a5d8aff1', 'type': 'ddg', 'title': 'NVIDIA H100 Hopper架构深度解读：从Tensor Core到FP8与大模型训练-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29051149/article/details/170172769&rut=53007fededc6f0652a7472bcecaafb554ac0f0cb985bfc172b1e0c6cc15aa42a', 'type': 'ddg', 'title': 'Hopper GPU上的FP8 FlashAttention加速原理与实操指南 - CSDN博客'}
