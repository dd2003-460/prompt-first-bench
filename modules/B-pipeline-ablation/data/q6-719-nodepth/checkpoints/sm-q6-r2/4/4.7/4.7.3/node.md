# N127: 自建 POP 节点缓存未命中率 Miss_rate_pop，通常为 10-30%，高于公有云 CDN，因 POP 总存储容量 C_pop 较小且内容工作集 W 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

自建 POP 节点缓存未命中率 Miss_rate_pop，通常为 10-30%，高于公有云 CDN，因 POP 总存储容量 C_pop 较小且内容工作集 W 较大，影响回源延迟的触发概率。

## Corrected Claim

自建 POP 节点缓存未命中率 Miss_rate_pop，通常为 10-30%，高于公有云 CDN，因 POP 总存储容量 C_pop 较小且内容工作集 W 较大，影响回源延迟的触发概率。

## Evidence

先验知识/题面给定，逻辑校验通过：自建POP节点通常部署在边缘或特定区域，存储容量受限且内容覆盖范围（工作集）相对其容量较大，导致缓存命中率低于拥有海量存储和全局调度的公有云CDN，10-30%的未命中率符合工程经验量级。

## Search Query

self-built POP cache hit ratio miss rate
