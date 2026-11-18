# N239: RTX 4090 运行 Qwen3-27B BF16 的总显存需求 = 54 GB (权重) + 2.0 GB (KV Cache) + 1.5 GB (激活值

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

RTX 4090 运行 Qwen3-27B BF16 的总显存需求 = 54 GB (权重) + 2.0 GB (KV Cache) + 1.5 GB (激活值) ≈ 57.5 GB，远超 24 GB 物理显存，因此单卡 RTX 4090 无法在 BF16 精度下完整加载 Qwen3-27B 模型，必须使用量化或 Offload。

## Corrected Claim

RTX 4090 运行 Qwen3-27B BF16 的总显存需求 = 54 GB (权重) + 2.0 GB (KV Cache) + 1.5 GB (激活值) ≈ 57.5 GB，远超 24 GB 物理显存，因此单卡 RTX 4090 无法在 BF16 精度下完整加载 Qwen3-27B 模型，必须使用量化或 Offload。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数BF16权重约54GB，加上KV Cache和激活值后总显存需求远超RTX 4090的24GB物理显存，结论符合硬件规格与模型规模的基本事实。
