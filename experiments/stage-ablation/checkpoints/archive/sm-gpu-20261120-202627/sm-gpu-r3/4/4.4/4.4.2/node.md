# N114: PCIe 带宽瓶颈对多卡推理吞吐量的具体影响量化：在 Qwen3-27B 张量并行 (TP=2) 场景下，PCIe 4.0 x16 (约 32 GB/s) 相比

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

PCIe 带宽瓶颈对多卡推理吞吐量的具体影响量化：在 Qwen3-27B 张量并行 (TP=2) 场景下，PCIe 4.0 x16 (约 32 GB/s) 相比 NVLink (约 900 GB/s) 的带宽差异，导致 All-Reduce 通信时间增加，实测吞吐量下降通常在 5%-15% 之间（取决于 Batch Size 和序列长度） [search]

## Corrected Claim

在 Qwen3-27B 张量并行 (TP=2) 场景下，PCIe 4.0 x16 相比 NVLink 的带宽差异会导致 All-Reduce 通信时间增加，从而引起吞吐量下降，具体幅度取决于 Batch Size 和序列长度。

## Evidence

[质询]该陈述包含具体的经验性数值（5%-15%的吞吐量下降范围），属于硬件性能与系统调优的经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

multi-GPU inference throughput loss PCIe vs NVLink tensor parallelism LLM
