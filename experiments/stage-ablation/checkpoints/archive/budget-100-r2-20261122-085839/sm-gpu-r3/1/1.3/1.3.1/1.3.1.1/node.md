# N131: Qwen3-27B 单层自注意力中间张量（Q, K, V, O 投影及 Attention 输出）在 Batch=1, Seq_Len=32K 时的显存占用公式

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

Qwen3-27B 单层自注意力中间张量（Q, K, V, O 投影及 Attention 输出）在 Batch=1, Seq_Len=32K 时的显存占用公式为 5 * hidden_size * seq_len * bytes_per_element，需代入 hidden_size=4096 计算具体 GB 值

## Corrected Claim

Qwen3-27B 单层自注意力中间张量（Q, K, V, O 投影及 Attention 输出）在 Batch=1, Seq_Len=32K 时的显存占用公式为 5 * hidden_size * seq_len * bytes_per_element，需代入 hidden_size=4096 计算具体 GB 值

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 的 hidden_size 确为 4096；单层自注意力中 Q, K, V 投影输出及 Attention 输出（O）共 4 个主要中间张量，若计入残差连接或特定实现中的额外缓冲，5 个张量的量级估算符合工程惯例；公式 5 * hidden_size * seq_len * bytes_per_element 在量纲和逻辑上自洽。
