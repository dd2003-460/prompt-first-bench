# N170: 约束条件1：显存下限 VRAM_min = Weight_Size + KV_Cache_32K + Activation_Buffer。若要求 BF16 精度

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

约束条件1：显存下限 VRAM_min = Weight_Size + KV_Cache_32K + Activation_Buffer。若要求 BF16 精度，VRAM_min >= 71.2 GB (基于 N22)；若允许 FP8，VRAM_min >= 35.6 GB (基于 N23)。

## Corrected Claim

约束条件1：显存下限 VRAM_min = Weight_Size + KV_Cache_32K + Activation_Buffer。若要求 BF16 精度，VRAM_min >= 71.2 GB (基于 N22)；若允许 FP8，VRAM_min >= 35.6 GB (基于 N23)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

minimum VRAM requirement Qwen3 27B BF16 FP8
