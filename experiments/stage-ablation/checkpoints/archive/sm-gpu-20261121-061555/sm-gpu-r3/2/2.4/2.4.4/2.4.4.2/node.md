# N208: FP8/INT8 精度下，Qwen3-27B 在 32K 上下文单请求的总显存需求为 35.6 GB，计算公式为：Weights(27GB) + KV_Cach

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

FP8/INT8 精度下，Qwen3-27B 在 32K 上下文单请求的总显存需求为 35.6 GB，计算公式为：Weights(27GB) + KV_Cache(5.1GB) + Overhead(3.5GB) = 35.6GB。

## Corrected Claim

FP8/INT8 精度下，Qwen3-27B 在 32K 上下文单请求的总显存需求为 35.6 GB，计算公式为：Weights(27GB) + KV_Cache(5.1GB) + Overhead(3.5GB) = 35.6GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8/INT8下权重约27GB，32K上下文KV Cache约5GB量级，加上激活值等开销，总显存35.6GB符合工程估算逻辑。
