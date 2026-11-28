# N487: 工作点 A (High Perf/Low Cost): 强制使用 INT8 量化路径 (W8A8)，放弃 FP4 尝试。理论峰值 125 TFLOPS，实际 M

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N174

## Claim

工作点 A (High Perf/Low Cost): 强制使用 INT8 量化路径 (W8A8)，放弃 FP4 尝试。理论峰值 125 TFLOPS，实际 MFU 预计 45-50% (因 INT8 算子成熟度高)，单卡显存占用 27GB/2=13.5GB，4卡 TP=4 总显存 54GB，剩余 10GB 用于 KV Cache，Decode 速度上限受限于带宽 ~16.6 tok/s

## Corrected Claim

工作点 A (High Perf/Low Cost): 强制使用 INT8 量化路径 (W8A8)，放弃 FP4 尝试。理论峰值 125 TFLOPS，实际 MFU 预计 45-50% (因 INT8 算子成熟度高)，单卡显存占用 27GB/2=13.5GB，4卡 TP=4 总显存 54GB，剩余 10GB 用于 KV Cache，Decode 速度上限受限于带宽 ~16.6 tok/s

## Evidence

先验知识/题面给定，逻辑校验通过：INT8 W8A8 理论峰值 125 TFLOPS 符合常见 GPU 规格量级；MFU 45-50% 处于合理区间；显存计算 27GB/2=13.5GB 及总显存 54GB 算术正确；带宽限制下的 Decode 速度估算符合物理直觉。
