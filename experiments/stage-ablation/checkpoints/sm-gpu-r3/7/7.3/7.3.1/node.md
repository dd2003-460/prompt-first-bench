# N270: 在 BF16 精度下，H100 SXM 单卡 (80GB) 方案权重 55GB + 32K KV Cache 1GB，总占用 56GB < 80GB，可行；理论

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121

## Claim

在 BF16 精度下，H100 SXM 单卡 (80GB) 方案权重 55GB + 32K KV Cache 1GB，总占用 56GB < 80GB，可行；理论 Decode 吞吐上限 = 3350 GB/s / 56 GB ≈ 59.8 tokens/s，受 HBM3 实际带宽利用率 (通常 85-90%) 影响，实际吞吐约 51-54 tokens/s。

## Corrected Claim

在 BF16 精度下，H100 SXM 单卡 (80GB) 方案权重 55GB + 32K KV Cache 1GB，总占用 56GB < 80GB，可行；理论 Decode 吞吐上限 = 3350 GB/s / 56 GB ≈ 59.8 tokens/s，受 HBM3 实际带宽利用率 (通常 85-90%) 影响，实际吞吐约 51-54 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM HBM3带宽约3.35TB/s，56GB权重+KV占用在80GB显存内，算术推导59.8 tokens/s及85-90%利用率下的51-54 tokens/s符合物理直觉与工程常识。
