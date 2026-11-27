# N45: 不同量化精度下的 KV Cache 显存占用：BF16=128 MB, FP8=64 MB, INT8=64 MB, NVFP4=32 MB (单序列 32K 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

不同量化精度下的 KV Cache 显存占用：BF16=128 MB, FP8=64 MB, INT8=64 MB, NVFP4=32 MB (单序列 32K 上下文)

## Corrected Claim

不同量化精度下的 KV Cache 显存占用：BF16=128 MB, FP8=64 MB, INT8=64 MB, NVFP4=32 MB (单序列 32K 上下文)

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 显存占用与量化位宽成正比，BF16(16bit)为基准128MB，FP8/INT8(8bit)减半为64MB，NVFP4(4bit)再减半为32MB，数值量级与比例关系完全自洽。
