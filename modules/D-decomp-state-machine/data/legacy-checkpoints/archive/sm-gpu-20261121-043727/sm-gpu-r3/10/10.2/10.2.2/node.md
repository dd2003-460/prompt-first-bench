# N275: 计算 2x H100 (BF16, NVLink) 的 T_decode 理论下限：总带宽 = 2 * 3.35 TB/s = 6.7 TB/s。但需考虑 NV

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

计算 2x H100 (BF16, NVLink) 的 T_decode 理论下限：总带宽 = 2 * 3.35 TB/s = 6.7 TB/s。但需考虑 NVLink 通信开销。在 Tensor Parallelism 下，每层 AllReduce 通信量 ≈ 1MB (N75)。NVLink 带宽 900GB/s，通信耗时 ≈ 1.1us。计算耗时 ≈ 87GB / 6.7TB/s ≈ 13us。总 T_decode ≈ max(13, 1.1) + 通信开销 ≈ 14.1 us/token。注意：实际中由于同步延迟，可能略高于理论值，假设为 15 us/token。

## Corrected Claim

计算 2x H100 (BF16, NVLink) 的 T_decode 理论下限：总带宽 = 2 * 3.35 TB/s = 6.7 TB/s。但需考虑 NVLink 通信开销。在 Tensor Parallelism 下，每层 AllReduce 通信量 ≈ 1MB (N75)。NVLink 带宽 900GB/s，通信耗时 ≈ 1.1us。计算耗时 ≈ 87GB / 6.7TB/s ≈ 13us。总 T_decode ≈ max(13, 1.1) + 通信开销 ≈ 14.1 us/token。注意：实际中由于同步延迟，可能略高于理论值，假设为 15 us/token。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 HBM3带宽约3.35TB/s，NVLink4带宽900GB/s，计算耗时13us与通信耗时1.1us量级合理，总耗时15us符合理论下限推导。

## Search Query

H100 NVLink tensor parallelism latency overhead LLM inference
