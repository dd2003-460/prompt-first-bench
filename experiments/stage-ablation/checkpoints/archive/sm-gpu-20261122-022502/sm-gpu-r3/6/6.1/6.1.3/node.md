# N251: TTFT 公式的边界条件失效场景：当批处理大小 (Batch Size) > 1 时，KV Cache 大小随批处理线性增长，TTFT 公式需修正为 TTFT_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

TTFT 公式的边界条件失效场景：当批处理大小 (Batch Size) > 1 时，KV Cache 大小随批处理线性增长，TTFT 公式需修正为 TTFT_max = (KV_Cache_Size_bytes * Batch_Size / Bandwidth_GBps) * 1000 ms + Prefill_Compute_Time_ms，对于 Batch_Size=4，500GB/s 带宽下 TTFT ≈ 9.64s + 0.27s = 9.91s，从交互式变为离线，表明该公式仅适用于 Batch_Size=1 的交互式场景

## Corrected Claim

TTFT公式在Batch Size > 1时需考虑KV Cache总大小随Batch线性增长，但具体数值需基于实际KV Cache大小（通常MB-GB级）和硬件带宽重新计算；原陈述中9.64s的数值在500GB/s带宽下隐含不合理的KV Cache规模，建议修正为基于典型KV Cache大小（如1GB）的毫秒级延迟估算，并明确公式适用边界。

## Evidence

[质询]数值计算存在严重量级错误：若KV Cache为GB级别（如1GB），500GB/s带宽下传输时间应为毫秒级（~2ms），而非9.64秒；若TTFT真为9.64秒，则隐含KV Cache大小需达到约4.8TB，这在单请求交互式场景中极不合理。此外，TTFT主要受Prefill计算和KV Cache写入/读取影响，简单线性叠加公式忽略了并行计算和内存带宽瓶颈的复杂交互，且'从交互式变为离线'的定性结论缺乏严格阈值定义。 | 先验知识/题面给定，但逻辑校验发现数值量级与物理直觉严重不符（500GB/s带宽下9.64s传输时间对应TB级数据，不符合典型LLM KV Cache规模），且公式简化过度，无法排除计算错误或模型假设错误。
