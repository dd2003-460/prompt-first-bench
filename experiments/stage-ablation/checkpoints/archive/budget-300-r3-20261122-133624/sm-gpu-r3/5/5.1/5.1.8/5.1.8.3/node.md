# N356: RTX 3090 在 BF16 精度下的 Decode 吞吐对比：权重占用 54GB，单卡不可行；若使用 2×3090 TP=2，每卡 27GB 权重，带宽瓶颈

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N119

## Claim

RTX 3090 在 BF16 精度下的 Decode 吞吐对比：权重占用 54GB，单卡不可行；若使用 2×3090 TP=2，每卡 27GB 权重，带宽瓶颈变为 936/27 * 0.85 ≈ 29.5 tokens/s (与 INT8 单卡理论值相同，但受 PCIe 通信限制实际更低)，证明 BF16 多卡方案在 3090 上无性能优势且显存占用翻倍。

## Corrected Claim

RTX 3090 在 BF16 精度下的 Decode 吞吐对比：权重占用 54GB，单卡不可行；若使用 2×3090 TP=2，每卡 27GB 权重，带宽瓶颈变为 936/27 * 0.85 ≈ 29.5 tokens/s (与 INT8 单卡理论值相同，但受 PCIe 通信限制实际更低)，证明 BF16 多卡方案在 3090 上无性能优势且显存占用翻倍。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 显存 24GB，BF16 权重 54GB 确实需双卡；带宽瓶颈计算 936GB/s / 27GB * 0.85 ≈ 29.5 tokens/s 符合算术逻辑，且多卡通信开销导致实际性能低于理论值的结论符合工程直觉。
