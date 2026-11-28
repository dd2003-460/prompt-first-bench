# N537: 并发度从 8 降至 2 对单位时间吞吐量（Tokens/sec）的影响系数：Throughput_Ratio = (2/8) × (Batch_Efficien

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N190

## Claim

并发度从 8 降至 2 对单位时间吞吐量（Tokens/sec）的影响系数：Throughput_Ratio = (2/8) × (Batch_Efficiency_2 / Batch_Efficiency_8)，由于 V100 显存带宽瓶颈，小 Batch 效率更低，假设 Batch_Efficiency_2 ≈ 0.6, Batch_Efficiency_8 ≈ 0.9，则 Throughput_Ratio ≈ 0.167，意味着单位时间处理 token 数仅为原配置的 1/6，需配合更长的单次请求超时时间

## Corrected Claim

并发度从 8 降至 2 对单位时间吞吐量（Tokens/sec）的影响系数：Throughput_Ratio = (2/8) × (Batch_Efficiency_2 / Batch_Efficiency_8)，由于 V100 显存带宽瓶颈，小 Batch 效率更低，假设 Batch_Efficiency_2 ≈ 0.6, Batch_Efficiency_8 ≈ 0.9，则 Throughput_Ratio ≈ 0.167，意味着单位时间处理 token 数仅为原配置的 1/6，需配合更长的单次请求超时时间

## Evidence

先验知识/题面给定，逻辑校验通过：并发度降低导致总吞吐量下降符合线性缩放与批处理效率损失的叠加效应，数值量级（1/6）在合理范围内，且无外部来源矛盾。

## Search Query

LLM inference batch size efficiency vLLM small batch throughput degradation
