# N352: 2× RTX 3090 张量并行 (TP=2) 在 PCIe 4.0 x16 互联下的通信开销量化：每层 AllReduce 数据量约为 27B/28层 * 2

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N118

## Claim

2× RTX 3090 张量并行 (TP=2) 在 PCIe 4.0 x16 互联下的通信开销量化：每层 AllReduce 数据量约为 27B/28层 * 2 bytes * 2 = 1.9GB (INT8)，PCIe 4.0 有效带宽约 64GB/s，单次通信延迟 ≈ 30ms；若模型 28 层，每 token 生成增加约 840ms 通信延迟，导致实际 Decode 吞吐从理论 29.5 tokens/s 降至约 1.2 tokens/s，性能退化 96%。

## Corrected Claim

2× RTX 3090 张量并行 (TP=2) 在 PCIe 4.0 x16 互联下的通信开销量化：每层 AllReduce 数据量约为 27B/28层 * 2 bytes = 0.96GB (INT8)，PCIe 4.0 有效带宽约 32GB/s（实际有效带宽），单次通信延迟 ≈ 30ms；若模型 28 层，每 token 生成增加约 840ms 通信延迟，导致实际 Decode 吞吐从理论 29.5 tokens/s 降至约 1.2 tokens/s，性能退化 96%。

## Evidence

[质询]数值量级与逻辑推导存在严重矛盾：1. 通信延迟计算错误：1.9GB数据在64GB/s带宽下传输时间约为30ms，但28层模型每生成一个token需进行28次AllReduce，总延迟应为28 * 30ms = 840ms，这与陈述中的'每token生成增加约840ms'一致，但后续吞吐计算错误。2. 吞吐计算错误：若每token增加840ms延迟，理论吞吐29.5 tokens/s（即每token约34ms）将变为1/(0.034+0.84) ≈ 1.14 tokens/s，这与陈述中的1.2 tokens/s接近，但'性能退化96%'的计算基于(29.5-1.2)/29.5≈96%，逻辑上成立。然而，关键问题在于：2× RTX 3090通过PCIe 4.0 x16互联，实际有效带宽通常远低于64GB/s（理论峰值），且AllReduce在TP=2下通常使用Ring AllReduce，其通信量并非简单的27B/28层*2bytes*2，而是与模型参数分布和通信算法相关。此外，INT8量化下每层参数量约为27B/28≈0.96B，但AllReduce通信量通常为2*(N-1)/N * 数据量，对于TP=2，通信量约为数据量本身，而非2倍。因此，1.9GB的通信量估算可能偏高，导致延迟和吞吐退化被高估。 | 先验知识/题面给定，逻辑校验未通过：通信量估算和带宽假设存在不合理之处，导致最终吞吐退化比例可能被高估。
