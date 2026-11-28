# N56: NVIDIA H100 SXM 的 BF16 理论峰值算力为 989 TFLOPS，HBM3 带宽 3350 GB/s，显存 80GB，其 Prefill 速度

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

NVIDIA H100 SXM 的 BF16 理论峰值算力为 989 TFLOPS，HBM3 带宽 3350 GB/s，显存 80GB，其 Prefill 速度比 A100 快约 3.16 倍 (989/312)，Decode 速度快约 1.64 倍 (3350/2039)，适合对首字延迟敏感的高并发场景。

## Corrected Claim

NVIDIA H100 SXM 的 BF16 理论峰值算力为 989 TFLOPS，HBM3 带宽 3350 GB/s，显存 80GB，其 Prefill 速度比 A100 快约 3.16 倍 (989/312)，Decode 速度快约 1.64 倍 (3350/2039)，适合对首字延迟敏感的高并发场景。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM BF16 峰值算力 989 TFLOPS、HBM3 带宽 3.35 TB/s、显存 80GB 均为标准公开规格；A100 SXM BF16 峰值 312 TFLOPS、HBM2e 带宽 2.039 TB/s 亦符合事实；Prefill 受算力限制，比值 989/312≈3.17（文中取3.16，误差极小）；Decode 受带宽限制，比值 3350/2039≈1.64，逻辑与数值均自洽。
