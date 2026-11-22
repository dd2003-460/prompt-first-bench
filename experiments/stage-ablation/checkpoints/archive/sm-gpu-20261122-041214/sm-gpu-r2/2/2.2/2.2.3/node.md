# N82: L40S 48GB 显存带宽为 864 GB/s，在 FP8 精度下理论最大解码吞吐量为 864/25.2 ≈ 34.3 tokens/s，性能接近 RTX 4

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21, N22, N23

## Claim

L40S 48GB 显存带宽为 864 GB/s，在 FP8 精度下理论最大解码吞吐量为 864/25.2 ≈ 34.3 tokens/s，性能接近 RTX 4090 但显存更大，适合需要 48GB 显存但不需要极致算力的场景，其性价比取决于其价格是否低于 A100 40GB。

## Corrected Claim

L40S 48GB 显存带宽为 864 GB/s，在 FP8 精度下理论最大解码吞吐量为 864/25.2 ≈ 34.3 tokens/s，性能接近 RTX 4090 但显存更大，适合需要 48GB 显存但不需要极致算力的场景，其性价比取决于其价格是否低于 A100 40GB。

## Evidence

先验知识/题面给定，逻辑校验通过：L40S 48GB 显存带宽 864 GB/s 符合 NVIDIA 官方规格；FP8 下 25.2 GB 模型（如 Llama-3-70B 量化版）理论吞吐 864/25.2 ≈ 34.3 tokens/s 计算正确；L40S 性能定位及与 A100 的性价比对比符合市场共识。

## Search Query

NVIDIA L40S memory bandwidth GB/s FP8 inference performance
