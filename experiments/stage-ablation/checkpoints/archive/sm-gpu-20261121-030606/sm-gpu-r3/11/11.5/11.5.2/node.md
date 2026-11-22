# N401: 修正N165中总显存占用与吞吐计算：若权重=27.0GB，KV Cache=1.99GB，激活值=2.5GB，则总显存占用为31.49GB。RTX 5090带宽

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N165

## Claim

修正N165中总显存占用与吞吐计算：若权重=27.0GB，KV Cache=1.99GB，激活值=2.5GB，则总显存占用为31.49GB。RTX 5090带宽=1792 GB/s，理论吞吐上限 = 1792 / 31.49 ≈ 56.9 tokens/s。

## Corrected Claim

修正N165中总显存占用与吞吐计算：若权重=27.0GB，KV Cache=1.99GB，激活值=2.5GB，则总显存占用为31.49GB。RTX 5090带宽=1792 GB/s，理论吞吐上限 = 1792 / 31.49 ≈ 56.9 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：显存加和 27.0+1.99+2.5=31.49GB 正确；吞吐计算 1792/31.49≈56.9 tokens/s 符合算术逻辑；RTX 5090 带宽 1792 GB/s 符合其 GDDR7 规格常识。
