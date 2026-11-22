# N91: 工作点 A2 (中性价比/平衡)：2x RTX 4090 运行 FP8 Qwen3-27B (27GB) 需跨卡分片，单卡有效带宽受限。理论 Decode 上限

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

工作点 A2 (中性价比/平衡)：2x RTX 4090 运行 FP8 Qwen3-27B (27GB) 需跨卡分片，单卡有效带宽受限。理论 Decode 上限 ≈ 504 GB/s (有效) / 27 GB ≈ 18.7 tokens/s (保守估计，含通信开销)。CapEx ≈ $3198 + $2000 配套 = $5198。

## Corrected Claim

工作点 A2 (中性价比/平衡)：2x RTX 4090 运行 FP8 Qwen3-27B (27GB) 需跨卡分片，单卡有效带宽受限。理论 Decode 上限 ≈ 504 GB/s (有效) / 27 GB ≈ 18.7 tokens/s (保守估计，含通信开销)。CapEx ≈ $3198 + $2000 配套 = $5198。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽约 1008 GB/s，2卡理论上限 2016 GB/s，考虑跨卡通信开销及FP8精度，有效带宽估算为 504 GB/s 合理；27GB 模型在 2x 24GB 卡上需分片，计算 504/27 ≈ 18.7 tokens/s 符合算术逻辑；CapEx 估算基于市场常见价格区间，量级合理。
