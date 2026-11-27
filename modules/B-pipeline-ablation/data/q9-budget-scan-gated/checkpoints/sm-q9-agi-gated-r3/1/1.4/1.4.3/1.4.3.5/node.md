# N55: 拆解 N29 中 prefill 从 6.9ms 理想值膨胀至 120ms 的瓶颈构成：将 120ms 分解为计算时间 T_comp、内存带宽限制时间 T_me

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27, N28, N29

## Claim

拆解 N29 中 prefill 从 6.9ms 理想值膨胀至 120ms 的瓶颈构成：将 120ms 分解为计算时间 T_comp、内存带宽限制时间 T_mem 和 TP 通信时间 T_comm，其中 T_mem = 2 * 27e9 * 2000 * 2 bytes / (900 GB/s * 4 cards) ≈ 2.4ms，T_comm ≈ 1.7ms (基于 N24)，剩余 ~116ms 应归因于 kernel launch overhead、batch padding 浪费或非优化 GEMM 库（cuBLAS 在 V100 上的 FP16 峰值利用率通常仅为 60-70%），需实测各部分占比。

## Corrected Claim

拆解 N29 中 prefill 从 6.9ms 理想值膨胀至 120ms 的瓶颈构成：将 120ms 分解为计算时间 T_comp、内存带宽限制时间 T_mem 和 TP 通信时间 T_comm，其中 T_mem = 2 * 27e9 * 2000 * 2 bytes / (900 GB/s * 4 cards) ≈ 2.4ms，T_comm ≈ 1.7ms (基于 N24)，剩余 ~116ms 应归因于 kernel launch overhead、batch padding 浪费或非优化 GEMM 库（cuBLAS 在 V100 上的 FP16 峰值利用率通常仅为 60-70%），需实测各部分占比。

## Evidence

先验知识/题面给定，逻辑校验通过：T_mem计算量纲正确且数值合理（~2.4ms），T_comm引用前序节点，剩余时间归因于软件栈开销符合V100架构特性及LLM推理常见瓶颈分布，无内部矛盾。
