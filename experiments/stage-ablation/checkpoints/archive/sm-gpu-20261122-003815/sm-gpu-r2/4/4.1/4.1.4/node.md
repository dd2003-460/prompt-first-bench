# N120: BF16 总显存需求修正值：Total_VRAM_BF16 = 54 GB (Weights) + KV_Cache_N45 + Activation_N46。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22, N23, N24

## Claim

BF16 总显存需求修正值：Total_VRAM_BF16 = 54 GB (Weights) + KV_Cache_N45 + Activation_N46。若 KV Cache 实际为 10GB 且 Activation 为 3GB，则总需求为 67GB；若 KV Cache 为 20GB，则总需求为 77GB。此值决定最小可行硬件显存下限。

## Corrected Claim

BF16 总显存需求修正值：Total_VRAM_BF16 = 54 GB (Weights) + KV_Cache_N45 + Activation_N46。若 KV Cache 实际为 10GB 且 Activation 为 3GB，则总需求为 67GB；若 KV Cache 为 20GB，则总需求为 77GB。此值决定最小可行硬件显存下限。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（54+10+3=67, 54+20+3=77），且符合大模型推理显存构成的基本逻辑（权重+KV Cache+激活值）。
