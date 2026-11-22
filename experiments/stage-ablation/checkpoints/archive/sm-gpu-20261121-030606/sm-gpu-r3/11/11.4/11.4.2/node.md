# N398: 修正N164中总显存占用与吞吐计算：若权重=27.0GB，KV Cache=1.99GB，激活值=2.5GB，则总显存占用为31.49GB。双RTX 4090有

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N164

## Claim

修正N164中总显存占用与吞吐计算：若权重=27.0GB，KV Cache=1.99GB，激活值=2.5GB，则总显存占用为31.49GB。双RTX 4090有效带宽=2×1008×0.65=1310.4 GB/s，理论吞吐上限 = 1310.4 / 31.49 ≈ 41.6 tokens/s。

## Corrected Claim

修正N164中总显存占用与吞吐计算：若权重=27.0GB，KV Cache=1.99GB，激活值=2.5GB，则总显存占用为31.49GB。双RTX 4090有效带宽=2×1008×0.65=1310.4 GB/s，理论吞吐上限 = 1310.4 / 31.49 ≈ 41.6 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：显存加和 27.0+1.99+2.5=31.49GB 正确；带宽计算 2*1008*0.65=1310.4 GB/s 正确；吞吐估算 1310.4/31.49≈41.6 tokens/s 符合算术逻辑。
