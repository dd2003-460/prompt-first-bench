# N143: 通信开销占比计算公式：Communication_Overhead = (Comm_Time / (Compute_Time + Comm_Time)) × 1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

通信开销占比计算公式：Communication_Overhead = (Comm_Time / (Compute_Time + Comm_Time)) × 100%，其中 Comm_Time = Comm_Volume / Bandwidth，Compute_Time = FLOPs / (TFLOPS × MFU)，需代入具体硬件参数计算

## Corrected Claim

通信开销占比计算公式：Communication_Overhead = (Comm_Time / (Compute_Time + Comm_Time)) × 100%，其中 Comm_Time = Comm_Volume / Bandwidth，Compute_Time = FLOPs / (TFLOPS × MFU)，需代入具体硬件参数计算

## Evidence

先验知识/题面给定，逻辑校验通过
