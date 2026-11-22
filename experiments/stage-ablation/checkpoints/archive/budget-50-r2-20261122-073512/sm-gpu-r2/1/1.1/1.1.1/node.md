# N39: Qwen3-27B 的静态权重显存需求在不同量化精度下的具体数值：BF16=54 GB, FP8=27 GB, INT8=27 GB, NVFP4/W4=13.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Qwen3-27B 的静态权重显存需求在不同量化精度下的具体数值：BF16=54 GB, FP8=27 GB, INT8=27 GB, NVFP4/W4=13.5 GB, W8A8=27 GB

## Corrected Claim

Qwen3-27B 的静态权重显存需求在不同量化精度下的具体数值：BF16=54 GB, FP8=27 GB, INT8=27 GB, NVFP4/W4=13.5 GB, W8A8=27 GB

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数模型在BF16下约为54GB，FP8/INT8减半为27GB，4bit量化约为13.5GB，数值量级与计算逻辑完全自洽。
