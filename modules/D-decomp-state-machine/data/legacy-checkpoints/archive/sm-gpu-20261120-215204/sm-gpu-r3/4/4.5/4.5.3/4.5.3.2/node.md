# N310: 工作点B（中性价比最优）：A100 80GB + BF16精度，理论峰值 = 2039 GB/s / 54 GB ≈ 37.8 Tokens/s；BF16精度下

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

工作点B（中性价比最优）：A100 80GB + BF16精度，理论峰值 = 2039 GB/s / 54 GB ≈ 37.8 Tokens/s；BF16精度下无需反量化，实际有效吞吐估算为 30-35 Tokens/s，显存占用约60-62GB，接近80GB上限但可行。

## Corrected Claim

工作点B（中性价比最优）：A100 80GB + BF16精度，理论峰值 = 2039 GB/s / 54 GB ≈ 37.8 Tokens/s；BF16精度下无需反量化，实际有效吞吐估算为 30-35 Tokens/s，显存占用约60-62GB，接近80GB上限但可行。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB HBM2e带宽约2039GB/s，54GB模型在BF16下理论吞吐37.8 Tokens/s符合算术推导，实际30-35 Tokens/s及60-62GB显存占用符合工程经验与物理约束。
