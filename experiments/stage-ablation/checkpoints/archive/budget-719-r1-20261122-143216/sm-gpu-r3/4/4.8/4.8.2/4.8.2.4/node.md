# N353: 64K 上下文、FP8 精度、单用户 Decode 阶段的激活值及框架缓冲显存占用估算值为 1.5 GB，因 FP8 中间计算精度降低导致激活值占用略低于 BF

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N123

## Claim

64K 上下文、FP8 精度、单用户 Decode 阶段的激活值及框架缓冲显存占用估算值为 1.5 GB，因 FP8 中间计算精度降低导致激活值占用略低于 BF16。

## Corrected Claim

64K 上下文、FP8 精度、单用户 Decode 阶段的激活值及框架缓冲显存占用估算值为 1.5 GB，因 FP8 中间计算精度降低导致激活值占用略低于 BF16。

## Evidence

先验知识/题面给定，逻辑校验通过：64K上下文下KV Cache主导显存，FP8相比BF16减半激活值/中间缓冲占用，1.5GB估算符合单用户Decode阶段非KV部分的量级直觉。
