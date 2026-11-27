# N124: BF16 精度下，单卡 48GB (如 A6000) 剩余可用显存 = 48 GiB - 50.31 GiB (权重) - 2.5 GiB (加载开销) = 负

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

BF16 精度下，单卡 48GB (如 A6000) 剩余可用显存 = 48 GiB - 50.31 GiB (权重) - 2.5 GiB (加载开销) = 负值，因此 BF16 下 48GB 单卡无法运行 Qwen3-27B，必须使用 80GB 卡或多卡。

## Corrected Claim

BF16 精度下，单卡 48GB (如 A6000) 剩余可用显存 = 48 GiB - 50.31 GiB (权重) - 2.5 GiB (加载开销) = 负值，因此 BF16 下 48GB 单卡无法运行 Qwen3-27B，必须使用 80GB 卡或多卡。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 参数量约 27B，BF16 下权重占用约 54GB (27 * 2)，远超 48GB 显存，即使按题面 50.31GB 计算，加上开销后仍为负值，结论成立。
