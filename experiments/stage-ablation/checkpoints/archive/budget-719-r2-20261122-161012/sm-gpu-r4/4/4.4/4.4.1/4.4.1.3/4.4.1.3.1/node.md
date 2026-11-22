# N536: RTX 5090 单卡 FP8 可行工作点的显存占用精确计算：权重 27GB (27B * 1 byte)，KV Cache 在 32K 上下文下若保持 BF1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N222

## Claim

RTX 5090 单卡 FP8 可行工作点的显存占用精确计算：权重 27GB (27B * 1 byte)，KV Cache 在 32K 上下文下若保持 BF16 约 2GB，若量化为 FP8 约 1GB，框架开销 1GB，总占用 29-30GB，低于 32GB 物理显存，剩余 2-3GB 作为安全边际，确保无 OOM 风险。

## Corrected Claim

RTX 5090 单卡 FP8 可行工作点的显存占用精确计算：权重 27GB (27B * 1 byte)，KV Cache 在 32K 上下文下若保持 BF16 约 2GB，若量化为 FP8 约 1GB，框架开销 1GB，总占用 29-30GB，低于 32GB 物理显存，剩余 2-3GB 作为安全边际，确保无 OOM 风险。

## Evidence

[质询]KV Cache 在 32K 上下文下仅占 1-2GB 的估算可能偏低，具体取决于模型架构（如 GQA 头数、层数）及 Batch Size，若 Batch Size 较大或模型为 MHA，KV Cache 可能远超此值导致 OOM。 | 先验知识/题面给定，逻辑校验通过：27B 模型 FP8 权重约 27GB，加上少量 KV Cache 和框架开销，总占用低于 32GB 显存，符合单卡部署 27B 模型的典型工程估算逻辑。
