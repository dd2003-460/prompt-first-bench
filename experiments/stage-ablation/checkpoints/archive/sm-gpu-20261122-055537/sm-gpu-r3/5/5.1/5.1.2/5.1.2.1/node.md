# N266: T_throughput 定义的工作点 1 (短上下文/高吞吐)：Seq_len = 4K。在此长度下，KV Cache 占用小 (约 1-2GB)，RTX 4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

T_throughput 定义的工作点 1 (短上下文/高吞吐)：Seq_len = 4K。在此长度下，KV Cache 占用小 (约 1-2GB)，RTX 4090 INT4 的解码速度接近理论带宽上限 (70-80 tokens/s)。此时瓶颈纯为 Memory-Bound，计算单元利用率低。

## Corrected Claim

T_throughput 定义的工作点 1 (短上下文/高吞吐)：Seq_len = 4K。在此长度下，KV Cache 占用小 (约 1-2GB)，RTX 4090 INT4 的解码速度接近理论带宽上限 (70-80 tokens/s)。此时瓶颈纯为 Memory-Bound，计算单元利用率低。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存带宽约1TB/s，INT4下4K序列KV Cache占用约1-2GB，解码速度70-80 tokens/s符合Memory-Bound特征
