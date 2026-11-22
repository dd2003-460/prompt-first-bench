# N92: 工作点 A3 (高成本低性/冗余)：4x RTX 4090 运行 BF16 Qwen3-27B (54GB) + BF16 KV Cache (12.58GB)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

工作点 A3 (高成本低性/冗余)：4x RTX 4090 运行 BF16 Qwen3-27B (54GB) + BF16 KV Cache (12.58GB) = 66.58GB < 96GB。理论 Decode 上限 ≈ 252 GB/s (有效) / 54 GB ≈ 4.7 tokens/s (严重受限于多卡通信)。CapEx ≈ $6396 + $3500 配套 = $9896。

## Corrected Claim

工作点 A3 (高成本低性/冗余)：4x RTX 4090 运行 BF16 Qwen3-27B (54GB) + BF16 KV Cache (12.58GB) = 66.58GB < 96GB。理论 Decode 上限 ≈ 252 GB/s (有效) / 54 GB ≈ 4.7 tokens/s (严重受限于多卡通信)。CapEx ≈ $6396 + $3500 配套 = $9896。

## Evidence

先验知识/题面给定，逻辑校验通过：4x RTX 4090 显存总量 96GB 大于模型+KV Cache 需求 66.58GB，显存约束满足；Decode 速度估算基于显存带宽瓶颈（252GB/s / 54GB ≈ 4.67 tokens/s），量级合理；CapEx 计算符合硬件市场大致价格区间。
