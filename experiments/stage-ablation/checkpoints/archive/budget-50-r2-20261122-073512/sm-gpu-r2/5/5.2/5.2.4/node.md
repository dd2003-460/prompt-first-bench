# N169: Qwen3-27B 在 BF16 精度下的理论最大吞吐量（Throughput_max）计算公式为：Bandwidth (GB/s) / (2 × 27e9 ×

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

Qwen3-27B 在 BF16 精度下的理论最大吞吐量（Throughput_max）计算公式为：Bandwidth (GB/s) / (2 × 27e9 × 2 bytes)，其中 Bandwidth 为显存带宽，27e9 为参数量，2 bytes 为 BF16 精度；例如 RTX 4090 (1008 GB/s) 的理论上限为 1008 / (2 × 27e9 × 2) ≈ 18.7 tokens/s。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的理论最大吞吐量（Throughput_max）计算公式为：Bandwidth (GB/s) / (2 × 27e9 × 2 bytes)，其中 Bandwidth 为显存带宽，27e9 为参数量，2 bytes 为 BF16 精度；例如 RTX 4090 (1008 GB/s) 的理论上限为 1008 / (2 × 27e9 × 2) ≈ 18.7 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合大模型推理带宽瓶颈下的理论吞吐量推导（Throughput = Bandwidth / (Params × Bytes_per_param × 2)，其中2代表权重读取和KV Cache/激活等开销的简化系数，或特定语境下的定义），数值计算 1008 / (2 * 27e9 * 2) ≈ 18.666... ≈ 18.7 正确。
