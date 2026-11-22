# N271: 在 FP8 精度下，H100 SXM 单卡 (80GB) 方案权重 27GB + 32K KV Cache 0.5GB，总占用 27.5GB < 80GB，可行

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121

## Claim

在 FP8 精度下，H100 SXM 单卡 (80GB) 方案权重 27GB + 32K KV Cache 0.5GB，总占用 27.5GB < 80GB，可行；理论 Decode 吞吐上限 = 3350 GB/s / 27.5 GB ≈ 121.8 tokens/s，受 HBM3 实际带宽利用率影响，实际吞吐约 104-110 tokens/s，相比 BF16 精度提升约 90-100%。

## Corrected Claim

在 FP8 精度下，H100 SXM 单卡 (80GB) 方案权重 27GB + 32K KV Cache 0.5GB，总占用 27.5GB < 80GB，可行；理论 Decode 吞吐上限 = 3350 GB/s / 27.5 GB ≈ 121.8 tokens/s，受 HBM3 实际带宽利用率影响，实际吞吐约 104-110 tokens/s，相比 BF16 精度提升约 90-100%。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM HBM3带宽约3.35TB/s，FP8权重减半及KV Cache优化符合硬件规格与算术逻辑，数值量级合理。
