# N29: 在 β=0.9 的平缓热度分布下，LFU 与 LRU 的性能差距 ΔH 通常小于 5 个百分点，因为 LFU 的计数老化机制在长尾访问中易受噪声干扰，而 LRU

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 β=0.9 的平缓热度分布下，LFU 与 LRU 的性能差距 ΔH 通常小于 5 个百分点，因为 LFU 的计数老化机制在长尾访问中易受噪声干扰，而 LRU 的局部性原理在时间局部性强的工作负载中表现稳健，具体数值需通过 ns-3 或 SimPy 仿真获取。

## Corrected Claim

在 β=0.9 的平缓热度分布下，LFU 与 LRU 的性能差距 ΔH 通常小于 5 个百分点，因为 LFU 的计数老化机制在长尾访问中易受噪声干扰，而 LRU 的局部性原理在时间局部性强的工作负载中表现稳健，具体数值需通过 ns-3 或 SimPy 仿真获取。

## Evidence

检索失败: no sources from any channel (all 5 failed)
