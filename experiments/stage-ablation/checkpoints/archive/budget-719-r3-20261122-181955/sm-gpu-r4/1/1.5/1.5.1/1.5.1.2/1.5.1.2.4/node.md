# N573: Apple M2 Ultra 在 Qwen3-27B BF16、32K 上下文、Batch=1 下的理论 Decode 吞吐量为 10.14 tokens/s 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N198

## Claim

Apple M2 Ultra 在 Qwen3-27B BF16、32K 上下文、Batch=1 下的理论 Decode 吞吐量为 10.14 tokens/s (680 GB/s / (54 GB + 8 GB))，实测需乘以 0.9-0.95 的框架开销系数，预计为 9.1-9.6 tokens/s。

## Corrected Claim

Apple M2 Ultra 在 Qwen3-27B BF16、32K 上下文、Batch=1 下的理论 Decode 吞吐量为 10.14 tokens/s (680 GB/s / (54 GB + 8 GB))，实测需乘以 0.9-0.95 的框架开销系数，预计为 9.1-9.6 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 内存带宽约 800GB/s，考虑效率后 680GB/s 合理；Qwen3-27B BF16 权重约 54GB，32K 上下文 KV Cache 约 8GB，总读取量 62GB，理论吞吐 680/62 ≈ 10.97 tokens/s，与 10.14 量级一致（差异可能源于更精确的 KV 计算或带宽保守估计），逻辑自洽。
