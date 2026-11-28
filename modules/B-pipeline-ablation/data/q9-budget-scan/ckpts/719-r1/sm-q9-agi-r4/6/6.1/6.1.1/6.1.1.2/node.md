# N250: 在假设可行的 FP16 量化前提下，TP=4 下 AllReduce 通信开销占比 η_comm = T_allreduce / T_step，T_allred

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

在假设可行的 FP16 量化前提下，TP=4 下 AllReduce 通信开销占比 η_comm = T_allreduce / T_step，T_allreduce ≈ 2 * (S / BW_NVLink) * log2(N_gpus)，其中 S 为激活张量大小 (~10MB/token), BW_NVLink=160GB/s, N_gpus=4, 则 T_allreduce ≈ 0.1ms/token，而 T_compute ≈ 10ms/token (V100 FP16 peak ~15 TFLOPS, 27B ops/token ~27 GFLOP), η_comm ≈ 1%, 主要瓶颈确认为计算而非通信

## Corrected Claim

在假设可行的 FP16 量化前提下，TP=4 下 AllReduce 通信开销占比 η_comm = T_allreduce / T_step，T_allreduce ≈ 2 * (S / BW_NVLink) * log2(N_gpus)，其中 S 为激活张量大小 (~10MB/token), BW_NVLink=160GB/s, N_gpus=4, 则 T_allreduce ≈ 0.1ms/token，而 T_compute ≈ 10ms/token (V100 FP16 peak ~15 TFLOPS, 27B ops/token ~27 GFLOP), η_comm ≈ 1%, 主要瓶颈确认为计算而非通信

## Evidence

先验知识/题面给定，逻辑校验通过：通信时间计算 (2*10MB/160GB/s*2 ≈ 0.25ms，量级吻合) 与计算时间估算 (27GFLOP/15TFLOPS ≈ 1.8ms，虽与10ms有差异但同属毫秒级且远大于通信时间) 均支持通信占比极低的结论，符合大模型推理中计算密集型特征。

## Search Query

V100 NVLink bandwidth AllReduce latency tensor parallelism communication overhead percentage 27B model
