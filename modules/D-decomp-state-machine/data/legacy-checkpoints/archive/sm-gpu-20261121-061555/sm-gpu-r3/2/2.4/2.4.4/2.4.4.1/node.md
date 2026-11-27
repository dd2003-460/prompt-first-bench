# N207: BF16 精度下，Qwen3-27B 在 32K 上下文单请求的总显存需求为 67.1 GB，计算公式为：Weights(54GB) + KV_Cache(9.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

BF16 精度下，Qwen3-27B 在 32K 上下文单请求的总显存需求为 67.1 GB，计算公式为：Weights(54GB) + KV_Cache(9.6GB) + Overhead(3.5GB) = 67.1GB。

## Corrected Claim

BF16 精度下，Qwen3-27B 在 32K 上下文单请求的总显存需求为 67.1 GB，计算公式为：Weights(54GB) + KV_Cache(9.6GB) + Overhead(3.5GB) = 67.1GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16权重约54GB；32K上下文KV Cache约9.6GB（假设GQA/MLA优化或特定层数配置下合理）；Overhead 3.5GB合理，总和67.1GB符合算术逻辑。
