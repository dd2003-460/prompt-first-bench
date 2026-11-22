# N201: Qwen3-27B 在 NVFP4 (W4A16) 精度下的权重显存占用精确值为 6.875 GB（基于 27.5B 参数量 × 0.25 bytes/para

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N48

## Claim

Qwen3-27B 在 NVFP4 (W4A16) 精度下的权重显存占用精确值为 6.875 GB（基于 27.5B 参数量 × 0.25 bytes/param + 量化 scale 开销），需确认 NVFP4 是否包含额外的 scale 因子显存占用（通常增加 5-10%）

## Corrected Claim

Qwen3-27B 在 NVFP4 (W4A16) 精度下的基础权重显存占用约为 6.875 GB（基于 27.5B 参数量 × 0.25 bytes/param）。实际总显存占用需额外加上量化 scale 因子的开销（通常估计为 5-10%，具体取决于 block size 和 scale 精度），因此总占用预计略高于 6.875 GB。

## Evidence

[质询]数值计算存在内部矛盾：27.5B 参数 × 0.25 bytes/param 的理论基础值为 6.875 GB，但陈述声称该值已包含 5-10% 的量化 scale 开销，这在数学上是不成立的（若含开销，总显存应大于 6.875 GB，或基础参数量需小于 27.5B）。此外，NVFP4 的具体 scale 存储机制（如 block size 和 scale 精度）未明确，导致 5-10% 的开销估算缺乏依据。 | 经验事实，逻辑校验发现数值与描述矛盾（基础值与含开销值混淆），且无外部来源支持 NVFP4 的具体 scale 开销比例。

## Search Query

NVFP4 quantization memory overhead scale factors Qwen3-27B
