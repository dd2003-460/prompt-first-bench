# N19: Qwen3-27B模型在BF16精度下的权重存储容量需求为54GB，在FP8精度下为27GB，在INT8精度下为27GB，在NVFP4精度下为13.5GB，在W

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

Qwen3-27B模型在BF16精度下的权重存储容量需求为54GB，在FP8精度下为27GB，在INT8精度下为27GB，在NVFP4精度下为13.5GB，在W4A16精度下为13.5GB

## Corrected Claim

Qwen3-27B模型在BF16精度下的权重存储容量需求为54GB，在FP8精度下为27GB，在INT8精度下为27GB，在NVFP4精度下为13.5GB，在W4A16精度下为13.5GB

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数模型在BF16(16bit)下为54GB，FP8/INT8(8bit)下为27GB，NVFP4/W4A16(4bit)下为13.5GB，数值量级与精度位宽完全匹配。
