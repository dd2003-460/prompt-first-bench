# N165: RTX 5090 与 RTX 4090 的性价比量化对比：定义性价比指标为 (Throughput * Quality_Score) / Cost。假设 FP8

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N53

## Claim

RTX 5090 与 RTX 4090 的性价比量化对比：定义性价比指标为 (Throughput * Quality_Score) / Cost。假设 FP8 质量分数为 0.95，BF16 为 1.0。RTX 4090 (BF16, 24GB) 无法原生高效运行 FP8，需使用 INT8 或 BF16。RTX 5090 (FP8, 32GB) 理论 Decode 吞吐 = 1792 / 27 ≈ 66.4 tokens/s (FP8 权重)。RTX 4090 (INT8, 24GB) 理论 Decode 吞吐 = 1008 / 27 ≈ 37.3 tokens/s (INT8 权重，假设 INT8 计算效率与 BF16 相当)。

## Corrected Claim

RTX 5090 (FP8, 32GB) 理论 Decode 吞吐 ≈ 66.4 tokens/s；RTX 4090 (INT8, 24GB) 理论 Decode 吞吐 ≈ 74.6 tokens/s (假设 INT8 效率为 BF16 的 2 倍)。

## Evidence

[质询]RTX 4090 的 INT8 计算效率假设与 BF16 相当是不准确的，Ada Lovelace 架构的 INT8 吞吐量通常是 BF16 的 2 倍左右，因此 37.3 tokens/s 的理论值被低估，导致性价比对比偏差。 | 先验知识/题面给定，逻辑校验通过，但存在经验参数假设偏差
