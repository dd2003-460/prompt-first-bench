# N181: CUDA Context的固定显存开销约为0.5-1.0GB，该值不随模型大小或序列长度变化，但在多GPU环境（如2x RTX 4090）中，每个GPU上下文独

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

CUDA Context的固定显存开销约为0.5-1.0GB，该值不随模型大小或序列长度变化，但在多GPU环境（如2x RTX 4090）中，每个GPU上下文独立占用，导致总框架开销在双卡场景下翻倍，需分别计算每卡的可用显存。

## Corrected Claim

CUDA Context的固定显存开销约为0.5-1.0GB，该值不随模型大小或序列长度变化，但在多GPU环境（如2x RTX 4090）中，每个GPU上下文独立占用，导致总框架开销在双卡场景下翻倍，需分别计算每卡的可用显存。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CUDA context memory overhead per GPU multi-GPU inference
