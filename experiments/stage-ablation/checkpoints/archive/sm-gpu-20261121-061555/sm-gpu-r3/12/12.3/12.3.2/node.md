# N387: Qwen3-27B 在 TP=2 架构下，每层 Attention 的 All-Reduce 通信量约为 2 * batch_size * seq_len * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N136

## Claim

Qwen3-27B 在 TP=2 架构下，每层 Attention 的 All-Reduce 通信量约为 2 * batch_size * seq_len * hidden_size * bytes_per_element，对于 32K 上下文 BF16 权重，单次前向传播的总通信数据量需量化为 GB 单位以估算延迟。

## Corrected Claim

Qwen3-27B 在 TP=2 架构下，每层 Attention 的 All-Reduce 通信量约为 2 * batch_size * seq_len * hidden_size * bytes_per_element，对于 32K 上下文 BF16 权重，单次前向传播的总通信数据量需量化为 GB 单位以估算延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：TP=2下Attention层All-Reduce通信量公式符合张量并行原理，量纲与数值量级合理。
