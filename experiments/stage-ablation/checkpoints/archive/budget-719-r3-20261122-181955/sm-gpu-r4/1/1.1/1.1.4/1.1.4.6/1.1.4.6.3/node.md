# N438: RTX 4090 在 FP8 量化下的能效比计算：FP8 权重约 27GB，KV Cache (BF16) 8GB，总内存 35GB。理论 Decode 上限 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N147

## Claim

RTX 4090 在 FP8 量化下的能效比计算：FP8 权重约 27GB，KV Cache (BF16) 8GB，总内存 35GB。理论 Decode 上限 = 1008 GB/s / 35 GB ≈ 28.8 tokens/s (假设 4090 带宽与 3090 Ti 相近，实际 4090 为 1008 GB/s)。实测效率系数 0.7，实际吞吐量 ≈ 20.2 tokens/s。P_avg 315W，能效比 = 20.2 / 315 ≈ 0.064 tokens/s/W。

## Corrected Claim

RTX 4090 在 FP8 量化下的能效比计算：FP8 权重约 27GB，KV Cache (BF16) 8GB，总内存 35GB。理论 Decode 上限 = 1008 GB/s / 35 GB ≈ 28.8 tokens/s (假设 4090 带宽与 3090 Ti 相近，实际 4090 为 1008 GB/s)。实测效率系数 0.7，实际吞吐量 ≈ 20.2 tokens/s。P_avg 315W，能效比 = 20.2 / 315 ≈ 0.064 tokens/s/W。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 带宽 1008 GB/s 符合规格，内存占用估算（27GB+8GB=35GB）及能效比计算（20.2/315≈0.064）在数学和物理逻辑上自洽。
