# N528: 2x RTX 4090 采用 Pipeline Parallelism (PP=2) 时，每步通信量仅为最终输出 (268 MB)，总通信延迟约为 64 层 *

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N163

## Claim

2x RTX 4090 采用 Pipeline Parallelism (PP=2) 时，每步通信量仅为最终输出 (268 MB)，总通信延迟约为 64 层 * 10.5 ms / 2 = 336 ms/step，通信开销占比降至约 86%。

## Corrected Claim

2x RTX 4090 采用 Pipeline Parallelism (PP=2) 时，每步通信量为最终输出 (268 MB)。在 NVLink 连接下，通信延迟极低（毫秒级），通信开销占比取决于计算时间，通常远低于 86%。

## Evidence

[质询]数值逻辑严重矛盾：总通信延迟计算为 336 ms/step，而单步输出仅 268 MB。若按此延迟计算，隐含带宽仅为 ~0.8 Gbps，远低于 NVLink 或 PCIe 的实际带宽（TB/s 或 GB/s 级别）。此外，'通信开销占比降至约 86%' 与 '仅为' 的表述在语境上通常暗示开销低，但 86% 是极高开销，且 336ms 的延迟对于 268MB 数据在双卡间传输是不合理的（实际应在毫秒级或亚毫秒级）。 | 逻辑校验失败：336ms 延迟对应 268MB 数据的带宽极低，违背硬件物理直觉；且 86% 的通信占比通常被视为高开销而非优化后的低开销，表述自相矛盾。
