# N83: FP8 精度下，若 KV Cache 保持 BF16 存储而仅权重为 FP8，则 KV Cache 占用仍为 4.096 GB，此时总显存需求为 31.096 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

FP8 精度下，若 KV Cache 保持 BF16 存储而仅权重为 FP8，则 KV Cache 占用仍为 4.096 GB，此时总显存需求为 31.096 GB + 开销，高于全 FP8 方案

## Corrected Claim

FP8 精度下，若 KV Cache 保持 BF16 存储而仅权重为 FP8，则 KV Cache 占用仍为 4.096 GB，此时总显存需求为 31.096 GB + 开销，高于全 FP8 方案

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 保持 BF16 意味着其显存占用不变（4.096 GB），总显存 = 权重(FP8) + KV(BF16) + 激活/开销，必然高于全 FP8 方案（权重+KV均为FP8），数值累加逻辑自洽。
