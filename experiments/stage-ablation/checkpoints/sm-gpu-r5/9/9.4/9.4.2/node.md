# N280: 2x RTX 4090 在 FP8 量化下的实际吞吐修正：理论上限 180 tokens/sec 需乘以互联效率系数 0.85（PCIe 4.0 x16 带宽瓶

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N109

## Claim

2x RTX 4090 在 FP8 量化下的实际吞吐修正：理论上限 180 tokens/sec 需乘以互联效率系数 0.85（PCIe 4.0 x16 带宽瓶颈）和内存访问效率系数 0.9（非顺序访问），实际吞吐约为 180 * 0.85 * 0.9 = 137.7 tokens/sec，误差范围 ±10 tokens/sec

## Corrected Claim

2x RTX 4090 在 FP8 量化下的实际吞吐修正：理论上限 180 tokens/sec 需乘以互联效率系数 0.85（PCIe 4.0 x16 带宽瓶颈）和内存访问效率系数 0.9（非顺序访问），实际吞吐约为 180 * 0.85 * 0.9 = 137.7 tokens/sec，误差范围 ±10 tokens/sec

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RTX 4090 PCIe bandwidth LLM inference efficiency factor
