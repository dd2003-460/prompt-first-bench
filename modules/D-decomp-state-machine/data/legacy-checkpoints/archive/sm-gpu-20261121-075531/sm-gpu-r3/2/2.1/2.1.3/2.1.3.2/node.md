# N172: Mac Studio M2 Ultra 统一内存带宽 (800 GB/s) 与 RTX 5090 (1792 GB/s) 的带宽比值为 0.446x；在 W4 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

Mac Studio M2 Ultra 统一内存带宽 (800 GB/s) 与 RTX 5090 (1792 GB/s) 的带宽比值为 0.446x；在 W4 量化下，理论 TPS 上限受限于带宽，M2 Ultra 理论峰值 ≈ 800 / 13.5 ≈ 59.26 tokens/s，与 N52 中声称的 59.3 一致，但实际受 CPU-GPU 协同开销折损。

## Corrected Claim

Mac Studio M2 Ultra 统一内存带宽 (800 GB/s) 与 RTX 5090 (1792 GB/s) 的带宽比值为 0.446x；在 W4 量化下，理论 TPS 上限受限于带宽，M2 Ultra 理论峰值 ≈ 800 / 13.5 ≈ 59.26 tokens/s，与 N52 中声称的 59.3 一致，但实际受 CPU-GPU 协同开销折损。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 800GB/s 与 RTX 5090 1792GB/s 的比值计算正确（800/1792≈0.446）；W4 量化下 13.5GB 模型的理论带宽受限 TPS 计算正确（800/13.5≈59.26），与声称的 59.3 一致，且符合硬件规格常识。
