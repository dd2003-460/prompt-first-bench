# N253: Weight_VRAM 的精度依赖性：在 BF16 下，Qwen3-27B 权重占用 54.36 GB；在 FP8 下，权重占用约 27.18 GB；在 INT

- **status**: verified
- **level**: L4
- **source**: derived
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N89

## Claim

Weight_VRAM 的精度依赖性：在 BF16 下，Qwen3-27B 权重占用 54.36 GB；在 FP8 下，权重占用约 27.18 GB；在 INT8 下，权重占用约 27.18 GB；在 INT4 下，权重占用约 13.59 GB；该值直接决定 Batch_Size 公式中的分子大小，进而影响最大并发能力。

## Corrected Claim

Weight_VRAM 的精度依赖性：在 BF16 下，Qwen3-27B 权重占用 54.36 GB；在 FP8 下，权重占用约 27.18 GB；在 INT8 下，权重占用约 27.18 GB；在 INT4 下，权重占用约 13.59 GB；该值直接决定 Batch_Size 公式中的分子大小，进而影响最大并发能力。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在BF16(2字节)下约为54GB，FP8/INT8(1字节)下约为27GB，INT4(0.5字节)下约为13.5GB，数值量级与精度换算逻辑完全自洽。
