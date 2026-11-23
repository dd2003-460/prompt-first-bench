# N27: 显存带宽对 32K 上下文推理延迟的影响量化：在 Decode 阶段，推理延迟主要由显存带宽决定。计算公式为 Latency_ms ≈ (Model_Weigh

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

显存带宽对 32K 上下文推理延迟的影响量化：在 Decode 阶段，推理延迟主要由显存带宽决定。计算公式为 Latency_ms ≈ (Model_Weight_Size_GB + KV_Cache_Size_GB) / (Memory_Bandwidth_GBps) * 1000。例如，RTX 5090 (1.79 TB/s) 在 FP8 (27GB) 下理论极限约 15ms/token，而 H100 (3.35 TB/s) 约 8ms/token；此差异决定了在低并发场景下高端卡的溢价合理性。

## Corrected Claim

显存带宽对 32K 上下文推理延迟的影响量化：在 Decode 阶段，推理延迟主要由显存带宽决定。计算公式为 Latency_ms ≈ (Model_Weight_Size_GB + KV_Cache_Size_GB) / (Memory_Bandwidth_GBps) * 1000。例如，RTX 5090 (1.79 TB/s) 在 FP8 (27GB) 下理论极限约 15ms/token，而 H100 (3.35 TB/s) 约 8ms/token；此差异决定了在低并发场景下高端卡的溢价合理性。

## Evidence

检索失败: no sources from any channel (all 5 failed)
