# N319: Mac Studio M2 Ultra 运行 BF16 Qwen3-27B 时的实际 Decode 吞吐受统一内存带宽 (800 GB/s) 和访问延迟 (约 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N115

## Claim

Mac Studio M2 Ultra 运行 BF16 Qwen3-27B 时的实际 Decode 吞吐受统一内存带宽 (800 GB/s) 和访问延迟 (约 200-300 ns) 双重限制，实测值通常在 10-15 tokens/s 区间，低于理论带宽上限 (12.0 tokens/s) 的 20-50%，具体数值取决于内存控制器调度效率 [时效待核]。

## Corrected Claim

Mac Studio M2 Ultra 运行 BF16 Qwen3-27B 时的实际 Decode 吞吐受统一内存带宽 (800 GB/s) 限制，理论上限约为 14-15 tokens/s，实测值通常接近该理论上限（约 10-14 tokens/s），具体数值取决于内存控制器调度效率及模型量化精度。

## Evidence

[质询]陈述存在严重的内部逻辑矛盾和数值错误：声称实测值（10-15 tokens/s）低于理论带宽上限（12.0 tokens/s）的 20-50%，这在数学上是不可能的（10-15 远大于 12 的 20-50%，即 2.4-6.0）。此外，对于 27B 模型在 800GB/s 带宽下，理论 Decode 上限约为 800/54 ≈ 14.8 tokens/s，实测 10-15 tokens/s 接近或超过理论值，而非远低于。 | 陈述内部数值自相矛盾（实测值被描述为低于理论上限的 20-50%，但实际数值远高于该比例），且理论带宽计算与描述不符，构成硬逻辑错误。

## Search Query

Mac Studio M2 Ultra LLM inference throughput tokens per second real-world measurement
