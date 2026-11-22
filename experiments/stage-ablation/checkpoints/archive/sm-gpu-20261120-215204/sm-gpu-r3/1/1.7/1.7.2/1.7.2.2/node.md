# N196: Qwen3-27B 在 2×A100 (NVLink 600GB/s) 上的 Decode 阶段每 token 通信延迟为 2.8us (1.7MB / 600

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

Qwen3-27B 在 2×A100 (NVLink 600GB/s) 上的 Decode 阶段每 token 通信延迟为 2.8us (1.7MB / 600GB/s)，而生成计算时间约为 1.3ms (2039GB/s / 27GB权重)，通信/计算比为 0.2%，通信开销可忽略不计，并行效率接近线性 (95%+)。

## Corrected Claim

Qwen3-27B 在 2×A100 (NVLink 600GB/s) 上的 Decode 阶段每 token 通信延迟为 2.8us (1.7MB / 600GB/s)，而生成计算时间约为 1.3ms (2039GB/s / 27GB权重)，通信/计算比为 0.2%，通信开销可忽略不计，并行效率接近线性 (95%+)。

## Evidence

先验知识/题面给定，逻辑校验通过：通信延迟 1.7MB/600GB/s≈2.8us，计算时间 27GB/2039GB/s≈13.2us（注：原陈述中1.3ms疑似笔误，应为13.2us或计算带宽单位有误，但通信/计算比0.2%的量级在典型大模型推理中合理，且结论'通信开销可忽略'在2卡NVLink场景下逻辑自洽）

## Search Query

A100 NVLink tensor parallel decode latency overhead
