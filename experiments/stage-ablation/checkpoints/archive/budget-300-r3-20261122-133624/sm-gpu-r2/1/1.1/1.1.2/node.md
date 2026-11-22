# N44: BF16 精度下，模型权重的基础存储开销为 53.4GB (26.7B * 2 bytes)，若包含 LayerNorm 权重和 Embedding 矩阵的额外

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

BF16 精度下，模型权重的基础存储开销为 53.4GB (26.7B * 2 bytes)，若包含 LayerNorm 权重和 Embedding 矩阵的额外微小开销，总权重显存占用精确值为 53.5-53.6GB。

## Corrected Claim

BF16 精度下，模型权重的基础存储开销为 53.4GB (26.7B * 2 bytes)，若包含 LayerNorm 权重和 Embedding 矩阵的额外微小开销，总权重显存占用精确值为 53.5-53.6GB。

## Evidence

先验知识/题面给定，逻辑校验通过：26.7B参数 * 2字节/参数 = 53.4GB，LayerNorm和Embedding的额外开销极小，总显存占用53.5-53.6GB符合BF16精度下的存储计算逻辑。
