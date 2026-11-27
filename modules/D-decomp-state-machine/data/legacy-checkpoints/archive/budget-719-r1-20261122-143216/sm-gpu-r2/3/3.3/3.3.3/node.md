# N88: 2×RTX 4090 在 BF16 精度下的性价比指标 = 实际吞吐量 (取中值 17.5 tokens/s) / 3年TCO ($7346) ≈ 0.0023

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

2×RTX 4090 在 BF16 精度下的性价比指标 = 实际吞吐量 (取中值 17.5 tokens/s) / 3年TCO ($7346) ≈ 0.00238 tokens/s/$，该数值显著低于 RTX 5090 单卡的 BF16 性价比 (0.00505)，表明在 32K 上下文单用户场景下双卡方案并非性价比最优。

## Corrected Claim

2×RTX 4090 在 BF16 精度下的性价比指标 = 实际吞吐量 (取中值 17.5 tokens/s) / 3年TCO ($7346) ≈ 0.00238 tokens/s/$，该数值显著低于 RTX 5090 单卡的 BF16 性价比 (0.00505)，表明在 32K 上下文单用户场景下双卡方案并非性价比最优。

## Evidence

先验知识/题面给定，逻辑校验通过：17.5/7346 ≈ 0.00238，且 0.00238 < 0.00505，数值计算与比较逻辑自洽。
