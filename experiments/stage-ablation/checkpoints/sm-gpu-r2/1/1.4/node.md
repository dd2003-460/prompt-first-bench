# N10: 多卡方案（如 2×24GB 或 2×32GB）的通信开销与显存碎片化：PCIe 带宽限制导致多卡推理延迟增加，且 KV Cache 分片需额外显存用于同步，实际

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

多卡方案（如 2×24GB 或 2×32GB）的通信开销与显存碎片化：PCIe 带宽限制导致多卡推理延迟增加，且 KV Cache 分片需额外显存用于同步，实际可用显存效率约为单卡的 85-90%。

## Corrected Claim

多卡方案（如 2×24GB 或 2×32GB）的通信开销与显存碎片化：PCIe 带宽限制导致多卡推理延迟增加，且 KV Cache 分片需额外显存用于同步，实际可用显存效率约为单卡的 85-90%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

multi-gpu inference overhead PCIe bandwidth KV cache sharding efficiency
