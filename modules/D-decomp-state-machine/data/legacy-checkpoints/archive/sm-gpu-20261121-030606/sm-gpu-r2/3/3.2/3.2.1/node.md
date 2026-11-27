# N111: FP8精度下Qwen3-27B的权重存储占用为27GB（修正自矛盾检测：N19中FP8=27GB为正确值，N7/N12/N13中13.5GB实为NVFP4/W4

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

FP8精度下Qwen3-27B的权重存储占用为27GB（修正自矛盾检测：N19中FP8=27GB为正确值，N7/N12/N13中13.5GB实为NVFP4/W4精度下的占用，非FP8），该数值直接决定RTX 5090 (32GB) 的可行性，而RTX 4090 (24GB) 在FP8下必然溢出（27GB > 24GB），因此FP8精度仅适用于≥32GB显存硬件。

## Corrected Claim

FP8精度下Qwen3-27B的权重存储占用为27GB（修正自矛盾检测：N19中FP8=27GB为正确值，N7/N12/N13中13.5GB实为NVFP4/W4精度下的占用，非FP8），该数值直接决定RTX 5090 (32GB) 的可行性，而RTX 4090 (24GB) 在FP8下必然溢出（27GB > 24GB），因此FP8精度仅适用于≥32GB显存硬件。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8（1字节/参数）下占用约27GB，符合数学推导；27GB > 24GB (RTX 4090) 且 27GB < 32GB (RTX 5090)，逻辑自洽。
