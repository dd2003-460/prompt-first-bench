# N15: 精度对 KV Cache 大小的影响：INT8/W4 权重下，KV Cache 是否支持低精度存储（如 FP8/INT8 KV Cache）及其对显存占用的缩减

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

精度对 KV Cache 大小的影响：INT8/W4 权重下，KV Cache 是否支持低精度存储（如 FP8/INT8 KV Cache）及其对显存占用的缩减比例。

## Corrected Claim

精度对 KV Cache 大小的影响：INT8/W4 权重下，KV Cache 是否支持低精度存储（如 FP8/INT8 KV Cache）及其对显存占用的缩减比例。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8/FP8 KV Cache 相比 FP16/BF16 可将显存占用减半（50%缩减），W4 权重量化与 KV Cache 精度选择相互独立但共同降低总显存需求，符合硬件存储位宽与数据压缩的基本原理。

## Search Query

low precision KV cache FP8 INT8 memory reduction LLM inference
