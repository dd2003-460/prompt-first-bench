# N313: 2× RTX 4090 INT8 方案的理论 Decode 吞吐量上限 = (Total_Effective_Bandwidth / Bytes_per_tok

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N113

## Claim

2× RTX 4090 INT8 方案的理论 Decode 吞吐量上限 = (Total_Effective_Bandwidth / Bytes_per_token) * 1000 = ((2 * 856.8~907.2) / 27.1) * 1000 ≈ 63,200 - 67,000 tokens/s (理论峰值，未考虑内存访问效率系数 0.6-0.85，实际约 37,900 - 57,000 tokens/s)

## Corrected Claim

2× RTX 4090 INT8 方案的理论 Decode 吞吐量上限 = (Total_Effective_Bandwidth / Bytes_per_token) * 1000 = ((2 * 856.8~907.2) / 27.1) * 1000 ≈ 63,200 - 67,000 tokens/s (理论峰值，未考虑内存访问效率系数 0.6-0.85，实际约 37,900 - 57,000 tokens/s)

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽约 1008 GB/s，有效带宽取 856.8~907.2 GB/s 合理；INT8 下每 token 27.1 Bytes 符合典型大模型权重+KV Cache 估算；计算 (2*856.8/27.1)*1000 ≈ 63,200 及 (2*907.2/27.1)*1000 ≈ 67,000 数值准确，逻辑自洽。
