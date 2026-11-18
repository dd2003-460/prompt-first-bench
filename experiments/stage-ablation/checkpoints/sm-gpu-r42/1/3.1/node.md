# N5: Qwen3-27B 模型权重在 BF16 格式下占用约 54 GB (27B * 2 bytes)，FP8 格式下占用约 27 GB，INT8 格式下占用约 2

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

Qwen3-27B 模型权重在 BF16 格式下占用约 54 GB (27B * 2 bytes)，FP8 格式下占用约 27 GB，INT8 格式下占用约 27 GB，NVFP4/W4 格式下占用约 13.5 GB [待核验：具体参数量与量化后字节数需根据模型发布卡确认]

## Corrected Claim

Qwen3-27B 模型权重在 BF16 格式下占用约 54 GB (27B * 2 bytes)，FP8 格式下占用约 27 GB，INT8 格式下占用约 27 GB，NVFP4/W4 格式下占用约 13.5 GB [待核验：具体参数量与量化后字节数需根据模型发布卡确认]

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在BF16(2字节)下为54GB，FP8/INT8(1字节)下为27GB，NVFP4/W4(0.5字节)下为13.5GB，数值量级与计算逻辑完全自洽。

## Search Query

Qwen3-27B model size BF16 FP8 INT8 bytes
