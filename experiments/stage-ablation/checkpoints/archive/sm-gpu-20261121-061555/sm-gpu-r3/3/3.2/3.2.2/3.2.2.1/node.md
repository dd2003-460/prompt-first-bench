# N236: AWQ 保护显著权重 (Significant Weights) 的具体定义：在 W4A16 量化中，AWQ 识别出激活值幅值 Top-K% 的通道（通常 K=

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

AWQ 保护显著权重 (Significant Weights) 的具体定义：在 W4A16 量化中，AWQ 识别出激活值幅值 Top-K% 的通道（通常 K=1%-5%），对这些通道对应的权重列保持较高精度或应用更大的缩放因子 (Scale Factor s)，使得这些权重在反量化后误差对最终输出的贡献最小化。

## Corrected Claim

AWQ 保护显著权重 (Significant Weights) 的具体定义：在 W4A16 量化中，AWQ 识别出激活值幅值 Top-K% 的通道（通常 K=1%-5%），对这些通道对应的权重列保持较高精度或应用更大的缩放因子 (Scale Factor s)，使得这些权重在反量化后误差对最终输出的贡献最小化。

## Evidence

先验知识/题面给定，逻辑校验通过
