# N80: A100 80GB SXM 显存带宽为 2039 GB/s，在 FP8 精度下运行 Qwen3-27B (25.2GB权重) 的理论最大解码吞吐量为 2039/

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21, N22, N23

## Claim

A100 80GB SXM 显存带宽为 2039 GB/s，在 FP8 精度下运行 Qwen3-27B (25.2GB权重) 的理论最大解码吞吐量为 2039/25.2 ≈ 80.9 tokens/s，相比 RTX 4090 (1008 GB/s, ~40 tokens/s) 提升约 2 倍，这是其高价格的核心性能依据。

## Corrected Claim

A100 80GB SXM 显存带宽为 2039 GB/s，在 FP8 精度下运行 Qwen3-27B (25.2GB权重) 的理论最大解码吞吐量为 2039/25.2 ≈ 80.9 tokens/s，相比 RTX 4090 (1008 GB/s, ~40 tokens/s) 提升约 2 倍，这是其高价格的核心性能依据。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB SXM 带宽 2039 GB/s 与 RTX 4090 带宽 1008 GB/s 均为公认硬件规格，2039/25.2 ≈ 80.9 及 1008/25.2 ≈ 40 计算正确，2倍提升结论符合算术逻辑。

## Search Query

A100 80GB SXM memory bandwidth GB/s FP8 inference benchmark Qwen 27B
