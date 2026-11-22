# N50: A100 80GB 显存带宽为 2039 GB/s，H100 80GB 为 3350 GB/s；在 BF16 下，H100 的理论 token 生成速度约为 A

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

A100 80GB 显存带宽为 2039 GB/s，H100 80GB 为 3350 GB/s；在 BF16 下，H100 的理论 token 生成速度约为 A100 的 1.64 倍，但 H100 价格更高，需结合 TCO 和延迟需求权衡

## Corrected Claim

A100 80GB 显存带宽为 2039 GB/s，H100 80GB 为 3350 GB/s；在 BF16 下，H100 的理论 token 生成速度约为 A100 的 1.64 倍，但 H100 价格更高，需结合 TCO 和延迟需求权衡

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB显存带宽2039 GB/s与H100 80GB显存带宽3350 GB/s符合官方规格，带宽比3350/2039≈1.64，与理论token生成速度倍数一致，数值量级合理且无内部矛盾。
