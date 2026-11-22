# N798: PagedAttention 对 OOM 风险的缓解机制量化：PagedAttention 将 KV Cache 分为固定大小的 Block (如 16 tok

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N248, N249, N250

## Claim

PagedAttention 对 OOM 风险的缓解机制量化：PagedAttention 将 KV Cache 分为固定大小的 Block (如 16 tokens/block)，允许非连续内存分配。它不减少总显存占用，但消除了内存碎片导致的可用显存浪费。在 24GB 显存限制下，若静态预分配失败，PagedAttention 可通过动态扩缩容将可用显存利用率从 ~85% 提升至 ~98%，从而将安全余量从 0.71GB 提升至 ~2.5GB。

## Corrected Claim

PagedAttention 将 KV Cache 分为固定大小的 Block，允许非连续内存分配。它不减少总显存占用，但通过消除内存碎片显著提升了可用显存利用率，从而在相同显存限制下增加了安全余量。

## Evidence

[质询]具体数值（85%、98%、0.71GB、2.5GB）缺乏通用理论支持，属于特定场景下的经验估算或虚构数据，且‘动态扩缩容’表述不够严谨（PagedAttention核心是分页管理而非传统意义的动态扩缩容算法）。 | 先验知识/题面给定，逻辑校验通过：PagedAttention确实通过分页消除碎片，提升显存利用率，但具体百分比和GB数值为经验性估算，非普适物理常数，故降级为定性表述。

## Search Query

PagedAttention vLLM memory fragmentation reduction efficiency
