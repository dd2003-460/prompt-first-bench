# N9: 各精度下 Qwen3-27B 权重文件大小：BF16=54GB, FP8=27GB, INT8=27GB, NVFP4=13.5GB, W4A16=13.5GB

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

各精度下 Qwen3-27B 权重文件大小：BF16=54GB, FP8=27GB, INT8=27GB, NVFP4=13.5GB, W4A16=13.5GB, W8A8=27GB, W4A4=13.5GB（基于 27e9 参数 * 字节数 / 1e9）

## Corrected Claim

各精度下 Qwen3-27B 权重文件大小：BF16=54GB, FP8=27GB, INT8=27GB, NVFP4=13.5GB, W4A16=13.5GB, W8A8=27GB, W4A4=13.5GB（基于 27e9 参数 * 字节数 / 1e9）

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在BF16(2字节)下为54GB，FP8/INT8(1字节)下为27GB，4-bit精度(NVFP4/W4A16/W4A4)下为13.5GB，数值量级与计算逻辑完全自洽。
