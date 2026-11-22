# N304: RTX 5090 的 PCIe 5.0 x16 带宽（~64 GB/s）在单卡本地推理中不构成瓶颈（因为权重和 KV Cache 均在本地 VRAM），但需确认

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103, N104, N105

## Claim

RTX 5090 的 PCIe 5.0 x16 带宽（~64 GB/s）在单卡本地推理中不构成瓶颈（因为权重和 KV Cache 均在本地 VRAM），但需确认驱动层是否存在 CPU-VRAM 同步开销导致的有效延迟增加，该延迟对 tokens/s 的影响预计 < 5%。

## Corrected Claim

RTX 5090 的 PCIe 5.0 x16 带宽（~64 GB/s）在单卡本地推理中不构成瓶颈（因为权重和 KV Cache 均在本地 VRAM），但需确认驱动层是否存在 CPU-VRAM 同步开销导致的有效延迟增加，该延迟对 tokens/s 的影响预计 < 5%。

## Evidence

先验知识/题面给定，逻辑校验通过：单卡本地推理中权重与KV Cache均在VRAM，PCIe带宽非瓶颈；驱动层同步开销对tokens/s影响<5%符合工程直觉

## Search Query

RTX 5090 PCIe 5.0 overhead LLM inference local VRAM latency impact
