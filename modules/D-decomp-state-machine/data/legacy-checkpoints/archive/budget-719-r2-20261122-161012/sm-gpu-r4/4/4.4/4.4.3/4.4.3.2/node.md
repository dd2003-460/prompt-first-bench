# N227: 2x RTX 4090 FP8 可行工作点：总显存需求 ~58GB (2*27GB 权重 + 2GB KV) 仍超出 48GB 物理显存，因此 FP8 下 2x

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

2x RTX 4090 FP8 可行工作点：总显存需求 ~58GB (2*27GB 权重 + 2GB KV) 仍超出 48GB 物理显存，因此 FP8 下 2x 4090 依然不可行，除非使用 INT4 (总需求 ~30GB < 48GB) 或启用 Offload，修正 N107 中 'FP8 可行' 的错误结论。

## Corrected Claim

2x RTX 4090 FP8 可行工作点：总显存需求 ~58GB (2*27GB 权重 + 2GB KV) 仍超出 48GB 物理显存，因此 FP8 下 2x 4090 依然不可行，除非使用 INT4 (总需求 ~30GB < 48GB) 或启用 Offload，修正 N107 中 'FP8 可行' 的错误结论。

## Evidence

先验知识/题面给定，逻辑校验通过：2x RTX 4090 物理显存为 48GB (2*24GB)，FP8 下总需求 ~58GB 确实超出物理限制，结论自洽。

## Search Query

Qwen3-27B FP8 dual GPU memory requirement 48GB limit
