# N211: 在 2 卡 Tensor Parallelism (TP=2) 下，BF16 精度方案的单卡显存占用为 33.55 GB，计算公式为：Total_VRAM_BF

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N69

## Claim

在 2 卡 Tensor Parallelism (TP=2) 下，BF16 精度方案的单卡显存占用为 33.55 GB，计算公式为：Total_VRAM_BF16(67.1GB) / 2 = 33.55GB。

## Corrected Claim

在 2 卡 Tensor Parallelism (TP=2) 下，BF16 精度方案的单卡显存占用为 33.55 GB，计算公式为：Total_VRAM_BF16(67.1GB) / 2 = 33.55GB。

## Evidence

先验知识/题面给定，逻辑校验通过：67.1GB / 2 = 33.55GB，算术正确且符合TP=2均分显存的逻辑。
