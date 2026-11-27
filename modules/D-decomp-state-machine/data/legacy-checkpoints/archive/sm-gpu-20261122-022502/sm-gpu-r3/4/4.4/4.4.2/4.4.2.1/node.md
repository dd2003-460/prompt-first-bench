# N216: 2×RTX 4090 方案在 PCIe 4.0 x16 双槽位下，张量并行（TP=2）的通信开销占推理总时间的比例约为 15-20%，若主机仅支持 PCIe 3

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70, N71, N72

## Claim

2×RTX 4090 方案在 PCIe 4.0 x16 双槽位下，张量并行（TP=2）的通信开销占推理总时间的比例约为 15-20%，若主机仅支持 PCIe 3.0 或带宽受限，该比例将上升至 25-30%，导致有效吞吐量下降 10-15%，进而使 TCO/Throughput 恶化约 10-20%。

## Corrected Claim

2×RTX 4090 方案在 PCIe 4.0 x16 双槽位下，张量并行（TP=2）的通信开销通常占推理总时间的 15-20% 左右（具体取决于模型和负载）；若主机仅支持 PCIe 3.0，由于带宽减半，该比例可能上升至 25-30%，导致有效吞吐量下降约 10-15%，进而使 TCO/Throughput 恶化约 10-20%。

## Evidence

[质询]数值过于精确且缺乏通用性：TP=2的通信开销比例高度依赖于模型架构（如Transformer层数、FFN大小）、序列长度、Batch Size以及具体的推理引擎优化（如AllReduce实现、通信重叠），15-20%并非一个固定的物理常数，而是特定场景下的经验估算值，直接断言为固定比例存在以偏概全的风险。 | 先验知识/题面给定，逻辑校验通过：PCIe 4.0带宽约为3.0的两倍，带宽减半确实会导致通信时间占比上升，进而影响吞吐量和TCO，量级关系符合直觉；但具体百分比（15-20% vs 25-30%）属于经验事实，缺乏通用来源支持，故降级。

## Search Query

RTX 4090 tensor parallel PCIe 4.0 vs 3.0 communication overhead inference latency
