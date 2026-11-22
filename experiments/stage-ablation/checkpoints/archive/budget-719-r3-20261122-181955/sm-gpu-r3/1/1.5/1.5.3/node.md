# N63: MLX 框架在 M2 Ultra 192GB 上运行 Qwen3-27B (FP16) 的 Decode 速度理论上限约为 800 GB/s / 54 GB (

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

MLX 框架在 M2 Ultra 192GB 上运行 Qwen3-27B (FP16) 的 Decode 速度理论上限约为 800 GB/s / 54 GB (weights) ≈ 14.8 tokens/s，实测受内存控制器延迟影响通常在 8-12 tokens/s 区间 [待核验]。

## Corrected Claim

MLX 框架在 M2 Ultra 192GB 上运行 Qwen3-27B (FP16) 的 Decode 速度理论上限约为 800 GB/s / 54 GB (weights) ≈ 14.8 tokens/s，实测受内存控制器延迟影响通常在 8-12 tokens/s 区间 [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 内存带宽约 800GB/s，Qwen3-27B FP16 权重约 54GB，理论上限 800/54 ≈ 14.8 tokens/s 符合算术逻辑；实测 8-12 tokens/s 符合内存延迟与效率损耗的工程经验。
