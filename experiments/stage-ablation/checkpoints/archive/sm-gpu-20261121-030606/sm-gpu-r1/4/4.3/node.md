# N21: Qwen3-27B模型在BF16精度下的总显存需求（权重+激活值+KV Cache）在32K上下文长度下约为65GB，FP8/INT8精度下约为40GB，NVF

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

Qwen3-27B模型在BF16精度下的总显存需求（权重+激活值+KV Cache）在32K上下文长度下约为65GB，FP8/INT8精度下约为40GB，NVFP4/W4精度下约为25GB

## Corrected Claim

Qwen3-27B模型在BF16精度下的总显存需求（权重+激活值+KV Cache）在32K上下文长度下约为65GB，FP8/INT8精度下约为40GB，NVFP4/W4精度下约为25GB

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在BF16下权重约54GB，加上32K上下文下的KV Cache和激活值，总显存需求约65GB符合工程估算；FP8/INT8权重减半至约27GB，总需求约40GB合理；NVFP4/W4权重进一步压缩至约13.5GB，总需求约25GB符合低精度量化后的显存节省规律。
