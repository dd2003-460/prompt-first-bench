# N212: Qwen3-27B 在 BF16 精度下，单卡 24GB 显存的权重占用量计算公式：Weight_VRAM = 27e9 * 2 bytes = 54GB，该值

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

Qwen3-27B 在 BF16 精度下，单卡 24GB 显存的权重占用量计算公式：Weight_VRAM = 27e9 * 2 bytes = 54GB，该值远超单卡 24GB 容量，证明单卡 BF16 不可行，必须量化或多卡分布。

## Corrected Claim

Qwen3-27B 在 BF16 精度下，单卡 24GB 显存的权重占用量计算公式：Weight_VRAM = 27e9 * 2 bytes = 54GB，该值远超单卡 24GB 容量，证明单卡 BF16 不可行，必须量化或多卡分布。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9参数 * 2字节(BF16) = 54GB，54GB > 24GB，数学推导正确且符合硬件常识。
