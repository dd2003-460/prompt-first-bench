# N178: A6000 48GB PCIe 在 BF16 精度下运行 Qwen3-27B 的 Decode 理论吞吐量上限为 768 GB/s / 54.6 GB ≈ 14

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

A6000 48GB PCIe 在 BF16 精度下运行 Qwen3-27B 的 Decode 理论吞吐量上限为 768 GB/s / 54.6 GB ≈ 14.1 tokens/s，是候选集中带宽最低的单卡方案，仅适用于对延迟不敏感且预算极低的场景。

## Corrected Claim

A6000 48GB PCIe 在 BF16 精度下运行 Qwen3-27B 的 Decode 理论吞吐量上限为 768 GB/s / 54.6 GB ≈ 14.1 tokens/s，是候选集中带宽最低的单卡方案，仅适用于对延迟不敏感且预算极低的场景。

## Evidence

先验知识/题面给定，逻辑校验通过：A6000 48GB PCIe 带宽约 768 GB/s，Qwen3-27B BF16 权重约 54.6 GB，计算 768/54.6 ≈ 14.1 tokens/s 符合内存带宽瓶颈下的理论吞吐量公式，且该数值在候选集中确属较低水平，逻辑自洽。
