# N170: Qwen3-27B 在 INT8 精度下的理论最大吞吐量（Throughput_max）计算公式为：Bandwidth (GB/s) / (2 × 27e9 ×

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

Qwen3-27B 在 INT8 精度下的理论最大吞吐量（Throughput_max）计算公式为：Bandwidth (GB/s) / (2 × 27e9 × 1 byte)，其中 1 byte 为 INT8 精度；例如 RTX 4090 (1008 GB/s) 的理论上限为 1008 / (2 × 27e9 × 1) ≈ 37.3 tokens/s，但实际受计算瓶颈限制，通常仅为理论值的 60-80%。

## Corrected Claim

Qwen3-27B 在 INT8 精度下的理论最大吞吐量（Throughput_max）计算公式为：Bandwidth (GB/s) / (2 × 27e9 × 1 byte)，其中 1 byte 为 INT8 精度；例如 RTX 4090 (1008 GB/s) 的理论上限为 1008 / (2 × 27e9 × 1) ≈ 37.3 tokens/s，但实际受计算瓶颈限制，通常仅为理论值的 60-80%。
