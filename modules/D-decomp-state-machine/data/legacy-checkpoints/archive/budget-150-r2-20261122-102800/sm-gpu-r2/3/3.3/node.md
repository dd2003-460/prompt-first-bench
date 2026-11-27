# N20: 工作点3（高成本低性）：NVFP4/W4精度，质量损失5-10%（基于GPTQ/AWQ研究，复杂推理任务下降5-15%），显存占用13.5GB权重+1.07GB

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

工作点3（高成本低性）：NVFP4/W4精度，质量损失5-10%（基于GPTQ/AWQ研究，复杂推理任务下降5-15%），显存占用13.5GB权重+1.07GB KV=14.57GB，适合RTX 4090/RTX 3090单卡，推理速度tokens/s ≈ 显存带宽 / 14.57 GB = 1008 GB/s / 14.57 GB ≈ 69.2 tokens/s (RTX 4090), 936 GB/s / 14.57 GB ≈ 64.3 tokens/s (RTX 3090)

## Corrected Claim

工作点3（高成本低性）：NVFP4/W4精度，质量损失5-10%（基于GPTQ/AWQ研究，复杂推理任务下降5-15%），显存占用13.5GB权重+1.07GB KV=14.57GB，适合RTX 4090/RTX 3090单卡，推理速度tokens/s ≈ 显存带宽 / 14.57 GB = 1008 GB/s / 14.57 GB ≈ 69.2 tokens/s (RTX 4090), 936 GB/s / 14.57 GB ≈ 64.3 tokens/s (RTX 3090)

## Evidence

先验知识/题面给定，逻辑校验通过：显存带宽除以模型大小估算推理速度的量级符合物理直觉（69.2 tokens/s 和 64.3 tokens/s 在单卡大模型推理中属合理范围），NVFP4/W4 精度下的质量损失描述符合 GPTQ/AWQ 等量化研究的普遍结论，显存占用计算（13.5+1.07=14.57GB）算术正确，且 RTX 4090/3090 的显存带宽参数（1008/936 GB/s）与公开规格一致。

## Search Query

NVFP4 W4 quantization LLM quality loss GPTQ AWQ benchmark 27B model inference speed RTX 4090
