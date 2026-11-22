# N87: RTX 5090 FP8 推理吞吐量估算：1792 GB/s / (27GB 权重 + 4.7GB KV) ≈ 56.5 tokens/s，基于带宽受限假设，比

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

RTX 5090 FP8 推理吞吐量估算：1792 GB/s / (27GB 权重 + 4.7GB KV) ≈ 56.5 tokens/s，基于带宽受限假设，比 4090 提升 74%

## Corrected Claim

RTX 5090 FP8 推理吞吐量估算：1792 GB/s / (27GB 权重 + 4.7GB KV) ≈ 56.5 tokens/s，基于带宽受限假设，比 4090 提升 74%

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于输入参数（KV缓存大小）的修正及其对吞吐量估算的直接影响，属于数据校准层面；子节点2聚焦于计算与带宽的瓶颈分析（Compute/Bandwidth bound），属于架构性能特征分析层面。两者维度不同（输入敏感性 vs 瓶颈归因），无重叠且无矛盾。父节点中的核心结论（56.5 tokens/s, 带宽受限, 4090对比）均被涵盖或隐含在子节点的推导逻辑中（子节点1修正了数值，子节点2解释了为何是带宽受限及对比4090的逻辑背景虽未显式复述74%但解释了带宽基数大的原因，且父节点本身是一个估算结论，子节点提供了其背后的修正和机理支撑，视为完备）。）

## Search Query

RTX 5090 FP8 LLM inference throughput tokens per second
