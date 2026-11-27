# N185: Qwen3-27B W4 量化中嵌入层（Embedding）和输出层（LM Head）通常保持 BF16 精度的额外显存开销：假设 Embedding 维度为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

Qwen3-27B W4 量化中嵌入层（Embedding）和输出层（LM Head）通常保持 BF16 精度的额外显存开销：假设 Embedding 维度为 4096，词表大小 152K，则 Embedding 层大小 = 152e3 * 4096 * 2 bytes ≈ 1.24 GB；若输出层也保持 BF16，总额外开销约 1.2-2.5 GB，因此总显存占用 = 12.86 GB (W4) + 1.24 GB (Embed) ≈ 14.1 GB

## Corrected Claim

Qwen3-27B W4 量化中嵌入层（Embedding）和输出层（LM Head）通常保持 BF16 精度的额外显存开销：假设 Embedding 维度为 4096，词表大小 152K，则 Embedding 层大小 = 152e3 * 4096 * 2 bytes ≈ 1.24 GB；若输出层也保持 BF16，总额外开销约 1.2-2.5 GB，因此总显存占用 = 12.86 GB (W4) + 1.24 GB (Embed) ≈ 14.1 GB

## Evidence

先验知识/题面给定，逻辑校验通过：152,000 * 4,096 * 2 bytes ≈ 1.24 GB 计算正确，总显存估算符合量化模型常见工程实践。
