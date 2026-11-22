# N434: Qwen3-27B模型中非线性层（如LayerNorm的weight/bias）在FP8量化中是否保持FP16/BF16精度，导致额外显存占用：需统计模型中La

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N140

## Claim

Qwen3-27B模型中非线性层（如LayerNorm的weight/bias）在FP8量化中是否保持FP16/BF16精度，导致额外显存占用：需统计模型中LayerNorm参数总量（约32层 * (2 * hidden_size) * 2 bytes），计算该部分未量化部分的显存占比

## Corrected Claim

Qwen3-27B模型中非线性层（如LayerNorm的weight/bias）在FP8量化中是否保持FP16/BF16精度，导致额外显存占用：需统计模型中LayerNorm参数总量（约32层 * (2 * hidden_size) * 2 bytes），计算该部分未量化部分的显存占比

## Evidence

先验知识/题面给定，逻辑校验通过：LayerNorm参数通常保持高精度（FP16/BF16）是量化标准实践，且32层Transformer的参数量级估算符合基本数学逻辑。

## Search Query

Qwen3-27B LayerNorm parameters FP16 memory overhead quantization
