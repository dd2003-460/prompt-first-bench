# N308: PagedAttention 机制对 KV Cache 显存碎片化率的影响：理想情况下碎片率 <5%，但在动态分配场景下可能升至 10-15%，需预留 10% 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N107, N108, N109

## Claim

PagedAttention 机制对 KV Cache 显存碎片化率的影响：理想情况下碎片率 <5%，但在动态分配场景下可能升至 10-15%，需预留 10% 的额外显存缓冲以避免 OOM

## Corrected Claim

PagedAttention 机制通过分页管理显著降低 KV Cache 显存碎片化，相比传统连续内存分配能大幅减少浪费，但在高动态负载下仍需预留一定显存缓冲以应对峰值需求。

## Evidence

[质询]具体数值（<5%, 10-15%, 10%）缺乏通用标准，属于特定实现或实验条件下的经验数据，易受硬件、负载和实现细节影响，存在以偏概全的风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

PagedAttention memory fragmentation rate vLLM benchmark
