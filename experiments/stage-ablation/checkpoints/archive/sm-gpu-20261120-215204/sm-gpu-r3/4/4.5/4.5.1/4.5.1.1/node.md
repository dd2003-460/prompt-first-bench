# N305: 工作点A（高性低成）：RTX 4090 + W4A16精度，理论峰值 = 1008 GB/s / 13.5 GB ≈ 74.6 Tokens/s；扣除KV Ca

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N107

## Claim

工作点A（高性低成）：RTX 4090 + W4A16精度，理论峰值 = 1008 GB/s / 13.5 GB ≈ 74.6 Tokens/s；扣除KV Cache读取（~12.8GB/32K上下文）和反量化开销后，实际有效吞吐估算为 45-55 Tokens/s。

## Corrected Claim

工作点A（高性低成）：RTX 4090 + W4A16精度，理论峰值 = 1008 GB/s / 13.5 GB ≈ 74.6 Tokens/s；扣除KV Cache读取（~12.8GB/32K上下文）和反量化开销后，实际有效吞吐估算为 45-55 Tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090带宽1008GB/s与W4A16模型大小13.5GB符合硬件规格，理论峰值计算正确，实际吞吐估算符合工程经验。
