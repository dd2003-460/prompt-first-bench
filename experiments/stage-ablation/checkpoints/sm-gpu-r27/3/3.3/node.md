# N7: 显存容量下限公式：Required_VRAM = Weights_Size + KV_Cache_Size + Activation_Buffer (约 1-2

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

显存容量下限公式：Required_VRAM = Weights_Size + KV_Cache_Size + Activation_Buffer (约 1-2 GB) + Framework_Overhead (约 0.5-1 GB)；因此 BF16 最低需 ~57 GB 显存，FP8/INT8 最低需 ~30 GB 显存，W4 最低需 ~16 GB 显存

## Corrected Claim

显存容量下限公式：Required_VRAM = Weights_Size + KV_Cache_Size + Activation_Buffer (约 1-2 GB) + Framework_Overhead (约 0.5-1 GB)；因此 BF16 最低需 ~57 GB 显存，FP8/INT8 最低需 ~30 GB 显存，W4 最低需 ~16 GB 显存

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference VRAM calculation formula weights kv cache activation
