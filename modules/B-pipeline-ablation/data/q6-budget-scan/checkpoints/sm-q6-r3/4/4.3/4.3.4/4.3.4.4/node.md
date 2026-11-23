# N270: 缓存命中率差异导致的回源成本敏感度：若自建节点命中率从90%降至80%，核心回源流量增加至0.32TB/日，回源成本增加100%；若公有云命中率从95%降至90

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

缓存命中率差异导致的回源成本敏感度：若自建节点命中率从90%降至80%，核心回源流量增加至0.32TB/日，回源成本增加100%；若公有云命中率从95%降至90%，长尾回源流量增加至0.04TB/日，回源成本增加100%。需量化H_self和H_mixed_tail的波动对总成本的边际影响。

## Corrected Claim

缓存命中率差异导致的回源成本敏感度：若自建节点命中率从90%降至80%，核心回源流量增加至0.32TB/日，回源成本增加100%；若公有云命中率从95%降至90%，长尾回源流量增加至0.04TB/日，回源成本增加100%。需量化H_self和H_mixed_tail的波动对总成本的边际影响。

## Evidence

先验知识/题面给定，逻辑校验通过：命中率从90%降至80%意味着未命中流量从10%增至20%（翻倍），从95%降至90%意味着未命中流量从5%增至10%（翻倍），因此回源流量和成本增加100%在逻辑上完全自洽。

## Search Query

CDN cache hit rate impact on origin bandwidth cost sensitivity analysis
