# N591: 公有云 CDN 在长尾区域的缓存命中率 H_tail 典型值为 0.7-0.85，低于核心区域的 0.9-0.95，导致长尾区域回源概率增加，进而增加 P99 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N193

## Claim

公有云 CDN 在长尾区域的缓存命中率 H_tail 典型值为 0.7-0.85，低于核心区域的 0.9-0.95，导致长尾区域回源概率增加，进而增加 P99 延迟的方差和尾部值。

## Corrected Claim

公有云 CDN 在长尾区域的缓存命中率通常低于核心区域，导致长尾区域回源概率增加，进而增加 P99 延迟的方差和尾部值。

## Evidence

[质询]具体数值区间（0.7-0.85 vs 0.9-0.95）属于经验性工程参数，不同CDN厂商、业务类型及缓存策略下差异巨大，缺乏通用标准，且无来源支持该特定量级。 | 经验事实，逻辑自洽（长尾区域缓存命中率低导致回源增加进而影响P99延迟符合CDN基本原理），但缺来源支持具体数值区间。

## Search Query

CDN cache hit rate distribution by geographic distance tail region China
