# N123: FP8 总显存需求修正值：Total_VRAM_FP8 = Weight_FP8 (N48) + KV_Cache_FP8/BF16 (N45/N49) + A

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22, N23, N24

## Claim

FP8 总显存需求修正值：Total_VRAM_FP8 = Weight_FP8 (N48) + KV_Cache_FP8/BF16 (N45/N49) + Activation (N46)。例如：27.2 + 8.6 (FP8 KV) + 3.0 = 38.8 GB。此值用于判断 48GB 卡（如 L40S/A6000）是否足以运行 FP8。

## Corrected Claim

FP8 总显存需求修正值：Total_VRAM_FP8 = Weight_FP8 (N48) + KV_Cache_FP8/BF16 (N45/N49) + Activation (N46)。例如：27.2 + 8.6 (FP8 KV) + 3.0 = 38.8 GB。此值用于判断 48GB 卡（如 L40S/A6000）是否足以运行 FP8。

## Evidence

先验知识/题面给定，逻辑校验通过：显存需求由权重、KV缓存和激活值组成，算术运算 27.2 + 8.6 + 3.0 = 38.8 正确，且 38.8GB < 48GB 符合逻辑。
