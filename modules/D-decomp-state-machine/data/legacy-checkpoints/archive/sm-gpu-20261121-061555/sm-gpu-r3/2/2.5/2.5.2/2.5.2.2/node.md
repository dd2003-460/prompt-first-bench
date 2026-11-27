# N213: 2卡 PP 方案下，每卡需承载的权重显存占比：Weight_VRAM_per_GPU = (27e9 * 2 bytes) / 2 = 27GB，该值仍超过 R

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

2卡 PP 方案下，每卡需承载的权重显存占比：Weight_VRAM_per_GPU = (27e9 * 2 bytes) / 2 = 27GB，该值仍超过 RTX 4090 的 24GB 物理显存，导致 2卡 PP 在 BF16 下不可行，除非采用 FP8/INT8 量化或增加卡数。

## Corrected Claim

2卡 PP 方案下，每卡需承载的权重显存占比：Weight_VRAM_per_GPU = (27e9 * 2 bytes) / 2 = 27GB，该值仍超过 RTX 4090 的 24GB 物理显存，导致 2卡 PP 在 BF16 下不可行，除非采用 FP8/INT8 量化或增加卡数。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数模型在BF16下权重占用54GB，2卡均分后每卡27GB，确实超过RTX 4090的24GB显存，结论成立。
