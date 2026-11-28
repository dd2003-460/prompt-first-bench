# N115: Memory-Bound 极限吞吐工作点：在 AI < 17.4 的条件下，最大理论吞吐量 Throughput_max = Bandwidth / Bytes

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N44

## Claim

Memory-Bound 极限吞吐工作点：在 AI < 17.4 的条件下，最大理论吞吐量 Throughput_max = Bandwidth / Bytes_per_token。对于 27B 模型，Bytes_per_token 主要由 KV Cache 大小决定，若每 token 读取 1KB KV 数据，则 Throughput_max ≈ 900 GB/s / 1 KB ≈ 900,000 tokens/s (理论上限)，但受限于 DRAM 访问延迟和 TP 通信，实际可达上限约为 50-70 tok/s (单流)，与 N62 中的 45 tok/s 一致。

## Corrected Claim

Memory-Bound 极限吞吐工作点：在低算术强度（AI）条件下，最大理论吞吐量 Throughput_max = Bandwidth / Bytes_per_token。对于 27B 模型，若每 token 读取 1KB KV 数据，理论上限约为 900,000 tokens/s。然而，受限于 DRAM 访问延迟、TP 通信开销及内存带宽利用率（通常远低于峰值），实际单流可达上限通常在数百至数千 tokens/s 量级，具体取决于硬件配置和批处理策略，而非仅 50-70 tok/s（除非存在极端的串行化瓶颈或极低效实现）。

## Evidence

[质询]数值量级严重失真：900,000 tokens/s 的理论上限与 50-70 tok/s 的实际上限之间相差约 10,000 倍，这在任何硬件架构下都是不可能的性能差距（通常 Memory-Bound 场景下实际效率为理论峰值的 10%-50%，即差距应在 2-10 倍左右）。此外，'AI < 17.4' 这一具体阈值缺乏上下文定义，且 27B 模型每 token 读取 1KB KV 数据的假设过于简化，未考虑权重加载或激活值影响。 | 逻辑校验发现理论值与实际值量级矛盾（4个数量级差异违背基本硬件性能直觉），且 source=knowledge 节点虽免外部核验，但存在硬逻辑错误（量级不合理），故降级。
