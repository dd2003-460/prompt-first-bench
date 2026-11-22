# N7: Qwen3-27B模型权重在BF16精度下的理论存储需求为27B * 2 bytes = 54 GB，在FP8精度下为27 GB，在INT4/W4精度下为13.

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

Qwen3-27B模型权重在BF16精度下的理论存储需求为27B * 2 bytes = 54 GB，在FP8精度下为27 GB，在INT4/W4精度下为13.5 GB，这是单卡显存容量下限的基础参数

## Corrected Claim

Qwen3-27B模型权重在BF16精度下的理论存储需求为27B * 2 bytes = 54 GB，在FP8精度下为27 GB，在INT4/W4精度下为13.5 GB，这是单卡显存容量下限的基础参数

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在BF16(2字节)、FP8(1字节)、INT4(0.5字节)下的存储计算分别为54GB、27GB、13.5GB，数值量级与算术逻辑均正确。

## Search Query

Qwen3-27B model size parameters
