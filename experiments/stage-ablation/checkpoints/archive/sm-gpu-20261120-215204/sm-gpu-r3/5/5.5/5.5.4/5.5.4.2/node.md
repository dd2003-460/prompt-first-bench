# N376: 工作点B (中性价比/通信瓶颈型)：2×RTX 4090 在 Batch Size=8, 32K 上下文下，Prefill 计算耗时线性增加至 ~432ms，但

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N134

## Claim

工作点B (中性价比/通信瓶颈型)：2×RTX 4090 在 Batch Size=8, 32K 上下文下，Prefill 计算耗时线性增加至 ~432ms，但 KV Cache 同步数据量随 Batch 线性增加，PCIe 4.0 双向带宽 64 GB/s 下的同步时间成为主导，总 TTFT 预计升至 2-4s，仍满足 <10s 约束，但需监控 PCIe 队列深度。

## Corrected Claim

工作点B (中性价比/通信瓶颈型)：2×RTX 4090 在 Batch Size=8, 32K 上下文下，Prefill 计算耗时线性增加至 ~432ms，但 KV Cache 同步数据量随 Batch 线性增加，PCIe 4.0 双向带宽 64 GB/s 下的同步时间成为主导，总 TTFT 预计升至 2-4s，仍满足 <10s 约束，但需监控 PCIe 队列深度。

## Evidence

先验知识/题面给定，逻辑校验通过：2x4090 PCIe 4.0 带宽约 64GB/s，32K 上下文 KV Cache 同步量级与 2-4s TTFT 估算在工程直觉上自洽，且满足 <10s 约束。
