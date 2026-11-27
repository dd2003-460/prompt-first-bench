# N95: 双卡高性低成工作点：2× RTX 4090 24GB (48GB 总显存) 运行 Qwen3-27B BF16 (54GB 权重)，需 Tensor Paral

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28, N29, N30

## Claim

双卡高性低成工作点：2× RTX 4090 24GB (48GB 总显存) 运行 Qwen3-27B BF16 (54GB 权重)，需 Tensor Parallelism 分割权重，单卡负载 27GB > 24GB，不可行；若运行 FP8 (27GB 权重)，单卡 13.5GB 可行，理论吞吐 ≈ 27GB / (2*1008GB/s) ≈ 13.4ms/token (≈74 tok/s)，TCO_5yr ≈ 2*$1599 + 5 * (1300W * 8h * 365d * $0.15) ≈ $3198 + $2846 ≈ $6044

## Corrected Claim

双卡高性低成工作点：2× RTX 4090 24GB (48GB 总显存) 运行 Qwen3-27B BF16 (54GB 权重)，需 Tensor Parallelism 分割权重，单卡负载 27GB > 24GB，不可行；若运行 FP8 (27GB 权重)，单卡 13.5GB 可行，理论吞吐 ≈ 27GB / (2*1008GB/s) ≈ 13.4ms/token (≈74 tok/s)，TCO_5yr ≈ 2*$1599 + 5 * (1300W * 8h * 365d * $0.15) ≈ $3198 + $2846 ≈ $6044

## Evidence

先验知识/题面给定，逻辑校验通过：27B BF16权重约54GB，单卡24GB无法容纳，需TP分割；FP8权重约27GB，单卡13.5GB可行；带宽计算27GB/(2*1008GB/s)≈13.4ms/token合理；TCO计算符合基本算术逻辑。
