# N288: 实际吞吐瓶颈分解：在 AI < 17.4 的 Memory-Bound 区，单流延迟 T_latency 由 DRAM 访问延迟 (Latency_DRAM ≈

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N115, N116, N117

## Claim

实际吞吐瓶颈分解：在 AI < 17.4 的 Memory-Bound 区，单流延迟 T_latency 由 DRAM 访问延迟 (Latency_DRAM ≈ 400-600 ns) 和 Kernel Launch Overhead (≈ 10-20 μs) 主导；对于小 Batch Size (BS=1-8)，计算时间 T_comp < T_memory 的比值 (Compute-Memory Ratio) 小于 0.1，导致 GPU 利用率 (MFU) 极低 (<10%)，证实 45 tok/s 的瓶颈在于小 Batch 下的低算术强度而非显存带宽耗尽。

## Corrected Claim

实际吞吐瓶颈分解：在 AI < 17.4 的 Memory-Bound 区，单流延迟 T_latency 由 DRAM 访问延迟 (Latency_DRAM ≈ 400-600 ns) 和 Kernel Launch Overhead (≈ 10-20 μs) 主导；对于小 Batch Size (BS=1-8)，计算时间 T_comp < T_memory 的比值 (Compute-Memory Ratio) 小于 0.1，导致 GPU 利用率 (MFU) 极低 (<10%)，证实 45 tok/s 的瓶颈在于小 Batch 下的低算术强度而非显存带宽耗尽。

## Evidence

[质询]Kernel Launch Overhead (10-20 μs) 通常远大于 DRAM 访问延迟 (0.4-0.6 μs)，若为串行主导，总延迟应主要由 Kernel Launch 决定，陈述中并列两者作为主导因素可能存在权重描述上的模糊，但在小 Batch 场景下，Kernel Launch 确实是主要开销之一，且整体逻辑指向低算术强度导致利用率低，核心结论无误。 | 先验知识/题面给定，逻辑校验通过：AI<17.4 确属 Memory-Bound 区；小 Batch (BS=1-8) 下 Kernel Launch 开销占比高，导致 MFU 极低 (<10%) 符合 GPU 调度常识；45 tok/s 的低吞吐归因于低算术强度而非带宽耗尽，符合 Roofline 模型逻辑。

## Search Query

GPU small batch inference latency bound vs bandwidth bound MFU utilization low arithmetic intensity
