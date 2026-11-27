# N216: 4x RTX 4090 多卡系统的 PCIe 互联带宽瓶颈量化：若采用 PCIe 4.0 x16 链路，理论双向带宽 64 GB/s，实际有效带宽受协议开销限制

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

4x RTX 4090 多卡系统的 PCIe 互联带宽瓶颈量化：若采用 PCIe 4.0 x16 链路，理论双向带宽 64 GB/s，实际有效带宽受协议开销限制约 50 GB/s；对比单卡 HBM 带宽 1008 GB/s，跨卡通信延迟导致 BF16 模型 (54GB) 的 Decode 吞吐从理论 4.7 tokens/s 进一步降至 3.5-4.0 tokens/s (含 15-25% 通信开销)。

## Corrected Claim

4x RTX 4090 多卡系统的 PCIe 互联带宽瓶颈量化：若采用 PCIe 4.0 x16 链路，理论双向带宽 64 GB/s，实际有效带宽受协议开销限制约 50 GB/s；对比单卡 HBM 带宽 1008 GB/s，跨卡通信延迟导致 BF16 模型 (54GB) 的 Decode 吞吐从理论 4.7 tokens/s 进一步降至 3.5-4.0 tokens/s (含 15-25% 通信开销)。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（严重偏离父节点主题。父节点核心是'PCIe互联带宽瓶颈量化'及'通信开销对Decode吞吐的影响'，但8个子节点中前6个完全在讨论硬件采购成本(CapEx)，与带宽/性能无关；后2个仅覆盖了带宽参数，缺失了父节点中关于'通信延迟'、'BF16模型大小'、'吞吐下降具体机制'及'15-25%开销推导'的关键内容。此外，前6个成本节点内部存在大量冗余，属于同一主题的不同配置档位，不应作为独立正交节点存在。）

## Search Query

PCIe 4.0 x16 effective bandwidth GPU-to-GPU communication overhead
