# N140: NVIDIA A100 80GB SXM 运行 Qwen3-27B (BF16) 在 32K 上下文下的理论最大吞吐量：受限于 HBM2e 带宽 (2039 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

NVIDIA A100 80GB SXM 运行 Qwen3-27B (BF16) 在 32K 上下文下的理论最大吞吐量：受限于 HBM2e 带宽 (2039 GB/s) 和 BF16 权重大小 (54GB)，理论上限为 2039/54 ≈ 37.76 tokens/s；实际受 KV Cache 和计算开销影响，预计 25-35 tokens/s。

## Corrected Claim

NVIDIA A100 80GB SXM 运行 Qwen3-27B (BF16) 在 32K 上下文下的理论最大吞吐量：受限于 HBM2e 带宽 (2039 GB/s) 和 BF16 权重大小 (54GB)，理论上限为 2039/54 ≈ 37.76 tokens/s；实际受 KV Cache 和计算开销影响，预计 25-35 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB SXM 带宽约 2039 GB/s，Qwen3-27B BF16 权重约 54GB，理论上限 2039/54 ≈ 37.76 tokens/s 符合算术逻辑，实际吞吐量受 KV Cache 和计算开销影响降至 25-35 tokens/s 符合工程直觉。
