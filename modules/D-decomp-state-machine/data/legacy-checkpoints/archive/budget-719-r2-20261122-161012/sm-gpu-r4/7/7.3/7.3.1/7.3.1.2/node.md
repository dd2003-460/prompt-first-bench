# N655: H100 SXM 单卡 BF16 的实际 Decode 吞吐修正：基于 N293 修正后的总显存占用 67.6 GB，理论上限 = 3350 GB/s / 67

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N270

## Claim

H100 SXM 单卡 BF16 的实际 Decode 吞吐修正：基于 N293 修正后的总显存占用 67.6 GB，理论上限 = 3350 GB/s / 67.6 GB ≈ 49.5 tokens/s；考虑 HBM3 实际带宽利用率 85%，实际吞吐 ≈ 49.5 * 0.85 ≈ 42.1 tokens/s，此值低于 N270 声称的 51-54 tokens/s，需以此修正值参与最终性价比计算。

## Corrected Claim

H100 SXM 单卡 BF16 的实际 Decode 吞吐修正：基于 N293 修正后的总显存占用 67.6 GB，理论上限 = 3350 GB/s / 67.6 GB ≈ 49.5 tokens/s；考虑 HBM3 实际带宽利用率 85%，实际吞吐 ≈ 49.5 * 0.85 ≈ 42.1 tokens/s，此值低于 N270 声称的 51-54 tokens/s，需以此修正值参与最终性价比计算。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（3350/67.6≈49.55, 49.55*0.85≈42.12），且符合H100 SXM带宽及LLM Decode带宽受限的物理直觉。
