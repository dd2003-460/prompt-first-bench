# N8: Qwen3-27B 在 4-bit 量化 (W4A8/W4A16) 下的权重显存占用约为 13.5-17 GB (取决于量化组大小和校准数据)，加上 32K 上

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B 在 4-bit 量化 (W4A8/W4A16) 下的权重显存占用约为 13.5-17 GB (取决于量化组大小和校准数据)，加上 32K 上下文 KV Cache 开销约 6-8 GB，总硬性显存需求约为 20-25 GB。

## Corrected Claim

Qwen3-27B 在 4-bit 量化 (W4A8/W4A16) 下的权重显存占用约为 13.5-17 GB (取决于量化组大小和校准数据)，加上 32K 上下文 KV Cache 开销约 6-8 GB，总硬性显存需求约为 20-25 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在4-bit量化下权重约13.5GB，32K上下文KV Cache约6-8GB，总显存20-25GB符合工程估算逻辑。
