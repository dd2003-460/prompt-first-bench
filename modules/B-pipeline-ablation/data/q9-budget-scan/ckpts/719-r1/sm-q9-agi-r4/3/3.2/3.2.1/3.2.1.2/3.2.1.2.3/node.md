# N509: 工作点2 下 4×V100 TP=4 的有效吞吐量 Tokens/s 衰减因子：由于长序列导致 Attention 计算复杂度 O(L²) 增加，有效 Thro

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N182

## Claim

工作点2 下 4×V100 TP=4 的有效吞吐量 Tokens/s 衰减因子：由于长序列导致 Attention 计算复杂度 O(L²) 增加，有效 Throughput ≈ Base_Throughput × (1 - Attention_Overhead)，其中 Attention_Overhead 随 L 线性增长

## Corrected Claim

工作点2 下 4×V100 TP=4 的有效吞吐量 Tokens/s 衰减因子：由于长序列导致 Attention 计算复杂度 O(L²) 增加，有效 Throughput ≈ Base_Throughput × (1 - Attention_Overhead)，其中 Attention_Overhead 随 L 的增加而显著上升（具体增长趋势取决于 Overhead 的定义及与其他计算部分的相对比例）。

## Evidence

[质询]Attention 计算复杂度为 O(L²)，但陈述中称 Attention_Overhead 随 L 线性增长，这与二次方复杂度的直觉不符，除非 Overhead 被定义为相对于总时间的占比且受其他线性项主导，否则量级描述存在逻辑瑕疵。 | 先验知识/题面给定，逻辑校验发现复杂度 O(L²) 与 Overhead 线性增长的描述存在潜在矛盾，缺乏外部来源支持以澄清具体定义。
