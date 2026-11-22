# N34: 多卡互联开销量化：2x RTX 4090 通过 PCIe 4.0 x16 互联，双向带宽约 64 GB/s，远低于单卡 HBM 带宽 (1 TB/s+)。在长上

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

多卡互联开销量化：2x RTX 4090 通过 PCIe 4.0 x16 互联，双向带宽约 64 GB/s，远低于单卡 HBM 带宽 (1 TB/s+)。在长上下文(32K)推理中，KV Cache 的跨卡传输或张量并行(Tensor Parallelism)通信开销可能导致有效吞吐量下降 10-30% [待核验]，抵消部分显存扩容优势。

## Corrected Claim

多卡互联开销量化：2x RTX 4090 通过 PCIe 4.0 x16 互联，双向带宽约 64 GB/s，远低于单卡 HBM 带宽 (1 TB/s+)。在长上下文(32K)推理中，KV Cache 的跨卡传输或张量并行(Tensor Parallelism)通信开销可能导致有效吞吐量下降 10-30% [待核验]，抵消部分显存扩容优势。

## Evidence

检索失败: no sources from any channel (all 5 failed)
