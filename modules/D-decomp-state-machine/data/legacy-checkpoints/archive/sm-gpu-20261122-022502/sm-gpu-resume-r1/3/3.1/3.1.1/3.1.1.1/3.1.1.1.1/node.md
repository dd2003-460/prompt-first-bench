# N649: RTX 4090 24GB 显存容量限制：在 BF16 精度下，24GB 显存仅能容纳约 12B 参数模型（不含 KV Cache），对于 27B 模型必须使用

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N200

## Claim

RTX 4090 24GB 显存容量限制：在 BF16 精度下，24GB 显存仅能容纳约 12B 参数模型（不含 KV Cache），对于 27B 模型必须使用 4-bit 量化（W4A16 或 NVFP4）才能装入单卡，量化系数 q = 1/16，权重体积 = 27e9 * 0.5 bytes = 13.5GB，剩余 10.5GB 用于 KV Cache。

## Corrected Claim

RTX 4090 24GB 显存容量限制：在 BF16 精度下，24GB 显存仅能容纳约 12B 参数模型（不含 KV Cache），对于 27B 模型必须使用 4-bit 量化（W4A16 或 NVFP4）才能装入单卡，量化系数 q = 1/16，权重体积 = 27e9 * 0.5 bytes = 13.5GB，剩余 10.5GB 用于 KV Cache。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在4-bit量化下体积约为13.5GB，加上KV Cache后总显存占用在24GB范围内，符合RTX 4090硬件规格及量化原理。
