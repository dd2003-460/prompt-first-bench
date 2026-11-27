# N175: A100 80GB SXM4 在 BF16 精度下运行 Qwen3-27B 的 Decode 理论吞吐量上限为 2039 GB/s / 54.6 GB ≈ 37

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

A100 80GB SXM4 在 BF16 精度下运行 Qwen3-27B 的 Decode 理论吞吐量上限为 2039 GB/s / 54.6 GB ≈ 37.3 tokens/s，相比 40GB 版本提升约 31%，主要归因于带宽差异而非显存容量。

## Corrected Claim

A100 80GB SXM4 在 BF16 精度下运行 Qwen3-27B 的 Decode 理论吞吐量上限为 2039 GB/s / 54.6 GB ≈ 37.3 tokens/s，相比 40GB 版本提升约 31%，主要归因于带宽差异而非显存容量。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 SXM4 带宽 2039 GB/s 与 Qwen3-27B BF16 权重约 54.6 GB 符合工程常识，计算 2039/54.6 ≈ 37.3 tokens/s 正确，且 Decode 阶段受带宽限制而非显存容量，逻辑自洽。
