# N241: TP=2 下的同步开销时间 t_sync = (通信量 / 有效PCIe带宽) * 2 (往返)；以 INT8 为例，t_sync ≈ (0.5 MB / 15

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73, N74, N75

## Claim

TP=2 下的同步开销时间 t_sync = (通信量 / 有效PCIe带宽) * 2 (往返)；以 INT8 为例，t_sync ≈ (0.5 MB / 15.75 GB/s) * 2 ≈ 63.5 μs/step；若 Decode 阶段单步计算时间 t_compute ≈ 10-15 ms，则同步占比约为 0.4-0.6%，表明纯通信延迟不是主要瓶颈，主要瓶颈在于 PCIe 带宽限制了双卡并行计算的数据交换效率或驱动/框架的同步机制开销。

## Corrected Claim

TP=2 下的同步开销时间 t_sync = (通信量 / 有效PCIe带宽) * 2 (往返)；以 INT8 为例，t_sync ≈ (0.5 MB / 15.75 GB/s) * 2 ≈ 63.5 μs/step；若 Decode 阶段单步计算时间 t_compute ≈ 10-15 ms，则同步占比约为 0.4-0.6%，表明纯通信延迟不是主要瓶颈，主要瓶颈在于 PCIe 带宽限制了双卡并行计算的数据交换效率或驱动/框架的同步机制开销。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 有效带宽约 15.75 GB/s，0.5MB 数据往返延迟计算正确（~63.5μs），相对于 10-15ms 的计算时间占比约 0.4-0.6%，量级与逻辑自洽。

## Search Query

tensor parallelism allreduce latency PCIe bottleneck LLM inference
