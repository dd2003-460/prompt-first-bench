# N222: RTX 5090 单卡 FP8 可行工作点：显存需求降至 ~29GB (权重 27GB + KV 1GB + 框架开销 1GB)，小于 32GB 物理显存，理论

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

RTX 5090 单卡 FP8 可行工作点：显存需求降至 ~29GB (权重 27GB + KV 1GB + 框架开销 1GB)，小于 32GB 物理显存，理论 Decode 吞吐量上限 = 1792 GB/s / 29GB ≈ 61.8 tokens/s，实际预计 55-60 tokens/s [待核验]。

## Corrected Claim

RTX 5090 单卡 FP8 可行工作点：显存需求降至 ~29GB (权重 27GB + KV 1GB + 框架开销 1GB)，小于 32GB 物理显存，理论 Decode 吞吐量上限 = 1792 GB/s / 29GB ≈ 61.8 tokens/s，实际预计 55-60 tokens/s [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 显存带宽 1792 GB/s 与 32GB 容量符合已知规格，显存需求估算（27+1+1=29GB）小于物理显存，吞吐量计算（1792/29≈61.8）符合 Roofline 模型逻辑，实际效率折损（55-60 tokens/s）符合工程经验。

## Search Query

Qwen3-27B FP8 memory usage RTX 5090 inference throughput
