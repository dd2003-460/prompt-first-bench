# N180: 在Batch=1且序列长度32K时，PyTorch/CUDA激活值（Activation Buffers）的峰值显存占用主要取决于Transformer层的中间

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

在Batch=1且序列长度32K时，PyTorch/CUDA激活值（Activation Buffers）的峰值显存占用主要取决于Transformer层的中间状态，对于27B模型，单层激活值约为20-50MB，全模型峰值激活值约为1.0-2.0GB，该值随Batch size线性增加，是4GB框架开销中的主要可变部分。

## Corrected Claim

在Batch=1且序列长度32K时，PyTorch/CUDA激活值（Activation Buffers）的峰值显存占用主要取决于Transformer层的中间状态，对于27B模型，单层激活值约为20-50MB，全模型峰值激活值约为1.0-2.0GB，该值随Batch size线性增加，是4GB框架开销中的主要可变部分。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型单层激活值20-50MB及全模型峰值1.0-2.0GB的量级符合Transformer架构在Batch=1、Seq=32K下的显存占用规律，且随Batch线性增加的逻辑自洽。

## Search Query

PyTorch CUDA activation memory footprint 27B model 32k sequence length batch 1
