# N101: 在 4x V100 TP=4 架构下，Decode 阶段的理论单 token 延迟下限 T_decode_min 受限于 HBM 带宽与 AllReduce 通

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 4x V100 TP=4 架构下，Decode 阶段的理论单 token 延迟下限 T_decode_min 受限于 HBM 带宽与 AllReduce 通信的并行瓶颈；公式为 T_decode_min = Max(T_memory_access, T_comm_sync)；其中 T_memory_access = Weight_Size_Bytes / (HBM_Bandwidth_per_GPU * TP)，T_comm_sync 约为 2 * Layer_Count * T_allreduce_layer；对于 27B 模型，若 T_allreduce_layer ≈ 0.5ms (NVLink 3.0 优化后)，则通信总开销 ≈ 16ms/layer * 32 layers ≈ 512ms 的理论上限需通过流水线并行(Pipeline Parallelism)或重叠计算与通信来掩盖，否则实际吞吐将低于 2 tokens/s。

## Corrected Claim

在 4x V100 TP=4 架构下，Decode 阶段的理论单 token 延迟下限 T_decode_min 受限于 HBM 带宽与 AllReduce 通信的并行瓶颈；公式为 T_decode_min = Max(T_memory_access, T_comm_sync)；其中 T_memory_access = Weight_Size_Bytes / (HBM_Bandwidth_per_GPU * TP)，T_comm_sync 约为 2 * Layer_Count * T_allreduce_layer；对于 27B 模型，若 T_allreduce_layer ≈ 0.5ms (NVLink 3.0 优化后)，则通信总开销 ≈ 16ms/layer * 32 layers ≈ 512ms 的理论上限需通过流水线并行(Pipeline Parallelism)或重叠计算与通信来掩盖，否则实际吞吐将低于 2 tokens/s。

## Evidence

检索失败: no sources from any channel (all 5 failed)
